import logging
from typing import Literal, Optional
from . import Card, gg
from . import skills as sk

# QQ: Could use self.vnc etc. instead of gg everywhere if this was part of the FightVnC
# class


def attack(attacker: Card, target: Optional[Card] = None) -> None:
    assert gg.grid.find_card(attacker).line != 0

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
        gg.vnc.handle_player_damage(power, attacker)
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

    if sk.Spines in target.skills:
        logging.debug(
            "%s causes 1 damage on %s with Spines", target.name, attacker.name
        )
        attacker.lose_health(1)

    attacker_power = attacker.power
    if sk.Underdog in attacker.skills and attacker_power < target.power:
        logging.debug("%s has Underdog and gets +1 power", attacker.name)
        attacker_power += 1
        # cf [1]

    # ----- Deal damage -----

    # TODO Only track losing health above and apply it here?

    # TODO Move some code from the lose_health method in the card here. Esp. the Shield
    # code?

    damage_left = target.lose_health(attacker_power)
    if damage_left > 0:
        logging.debug("Agent gets overflow damage of %s", damage_left)
        gg.vnc.handle_player_damage(damage_left, attacker)

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
