import logging
from typing import Optional
from . import Card, gg
from . import skills as sk

# This module should contain all functions that are related to cards and fighting.
# Hence, the module could eventually be turned into a `FightingCard` class.

# QQ: Could use self.vnc etc. instead of gg everywhere if this was part of the FightVnC
# class


def sacrifice_card(card: Card) -> None:
    card.health = 0
    gg.grid.remove_card(card)


def card_died(card: Card) -> None:
    pos = card.get_grid_pos()
    if card.is_human():  # TODO Can this be tested differently?
        gg.humanplayer.spirits += card.has_spirits
        gg.vnc.decks.used.add_card(card)
    gg.grid.remove_card(card)
    gg.vnc.card_died(card, pos)


def take_damage(card: Card, howmuch: int) -> int:
    """Returns how much damage is still left to be consumed. Damage can be left when
    a card died w/o consuming all damage. Keep in mind that damage can be consumed
    by shields an other skills too.
    """
    assert howmuch >= 0
    if howmuch == 0:
        return 0
    damage_left = howmuch

    if sk.Shield in card.skills:
        damage_left -= card.skills.get(sk.Shield).absorbed_damage(
            damage_left, gg.vnc.round_num
        )

    damage_left = card.reduce_health(damage_left)
    if card.is_dead():
        card_died(card)
    else:
        gg.vnc.card_lost_health(card)

    return damage_left


def attack(attacker: Card, target: Optional[Card] = None) -> None:
    assert gg.grid.find_card(attacker) is not None
    assert gg.grid.find_card(attacker).line != 0
    attacker_is_human = attacker.is_human()

    # ----- No power? -> Return immediately -----

    if attacker.power == 0:
        logging.debug("%s would attack but has 0 power, so doesn't", attacker.name)
        return

    # FIXME Log all cases
    # logging.debug(
    #     "%s:%s%s attacks %s %s",
    #     attacking_agent,
    #     attacker.name,
    #     "".join(s.symbol for s in attacker.skills),
    #     target.name,
    #     "".join(s.symbol for s in target.skills),
    # )  # FIXME Add some `name_with_skills` or `xname` method to Card?

    # ----- Activate & prepare -----

    gg.vnc.card_activate(attacker)

    # TODO Call pre-attack on all skills that have it -- Should this happen outside of
    # this routine before any of the attacks happen?
    for skill in attacker.skills:  # TODO Add this as a method to SkillSet
        skill.pre_attack()
    # TODO Need the same for targets and prepcards too?

    # ----- Early special cases -----

    # Will the card die before it can attack due to an unlucky LuckyStrike?
    if (
        sk.LuckyStrike in attacker.skills
        and not attacker.skills.get(sk.LuckyStrike).is_lucky()  # type: ignore
    ):
        attacker.die()
        logging.debug("%s gets unlucky with Lucky Strike", attacker.name)
        return
    # Post-condition: If attacker has LuckyStrike, it is lucky this attack.

    # ----- Attack the agent behind directly -----

    attacker_touches_target = target is not None and (
        sk.Soaring not in attacker.skills or sk.Airdefense in target.skills
    )
    attacks_agent_directly = target is None or not attacker_touches_target

    if attacks_agent_directly:
        power = attacker.power
        if sk.LuckyStrike in attacker.skills:
            power = attacker.skills.get(sk.LuckyStrike).power_up_against_agent(power)  # type: ignore
        gg.vnc.handle_agent_damage(attacker_is_human, power)
        return

    # ----- Otherwise: Attack the opposing card -----

    assert target is not None
    gg.vnc.card_getting_attacked(target, attacker)

    # ----- Opposing card dies instantly -----

    target_dies_instanly = attacker_touches_target and (
        sk.InstantDeath in attacker.skills
        or (
            sk.LuckyStrike in attacker.skills
            and attacker.skills.get(sk.LuckyStrike).is_lucky()  # type: ignore
        )
    )
    if target_dies_instanly:
        target.die()
        logging.debug("%s dies from InstantDeath or LuckyStrike", target.name)
        return

    # ----- Otherwise: Normal attack -----
    #
    # Note that we collect all power and health loss here and apply it afterwards. This
    # also means that a card can _theoretically_ die here, but will still apply all its
    # damage before dying later.
    attacker_power = attacker.power
    attacker_to_lose = 0

    if sk.Spines in target.skills:
        logging.debug("%s -> %s: 1D (Spines)", target.name, attacker.name)
        # attacker.lose_health(1)
        attacker_to_lose += 1

    if sk.Underdog in attacker.skills and attacker_power < target.power:
        logging.debug("%s: +1 P (Underdog)", attacker.name)
        attacker_power += 1
        # cf [1]

    # ----- Deal damage -----

    # Damage to target:
    target_damage_left = take_damage(target, attacker_power)
    if target_damage_left > 0:
        gg.vnc.handle_agent_damage(attacker_is_human, target_damage_left)

    # Damage to attacker: (e.g., due to Spines)
    attacker_damage_left = take_damage(attacker, attacker_to_lose)
    # Note that due to the call to `take_damage`, the attacker can also die here, and it
    # can also make use of shields and other skills.
    if attacker_damage_left > 0:
        gg.vnc.handle_agent_damage(not attacker_is_human, attacker_damage_left)

    # ----- Cleanup -----

    for skill in attacker.skills:  # TODO Add this as a method to SkillSet
        skill.post_attack()
    # TODO Need the same for targets and prepcards too?

    # gg.vnc.pos_card_deactivate(pos)   # TODO turn this into pos_card_deactivate(attacker)


# Notes:
#
# [1] Underdog:
# Note/QQ: The way this is currently implemented, some interdependencies might get
# missed with future skills. E.g., if there is a skill that gives a buff if a card has a
# certain power, it will not be triggered by Underdog as it is currently implemented. If
# we ever have such skills and interdependencies, we might need to implement Underdog an
# similar skills with temporary attributes or attribute modifiers in the card. OR: Each
# such dependent skill has to check if there are any other skills in play that might
# affect it.


def prepare(card: Card) -> bool:
    """Prepare a card for attack by moving it from the prepline to the computer line.
    Returns True if the card was prepared, False if it couldn't be prepared.
    """
    pos = card.get_grid_pos()
    assert pos is not None and pos.line == 0
    to_pos = pos._replace(line=1)
    prep_to = gg.grid.get_card(to_pos)
    if prep_to is not None:
        logging.debug(
            "Preparing %s but the prep-to space is occupied by %s",
            card.name,
            prep_to.name,
        )
        return False

    logging.debug("Preparing %s, moving to computer line", card.name)
    gg.vnc.card_prepare(card)
    gg.grid.move_card(card, to_pos=to_pos)
    return True
