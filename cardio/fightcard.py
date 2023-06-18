from __future__ import annotations
import logging
from typing import TYPE_CHECKING, ClassVar, List, Optional
from . import Card
from . import skills as sk

if TYPE_CHECKING:
    from . import FightVnC, Grid, GridPos


# QQ: What use cases for `vnc` are there in this class? And how could those be untangled
# further? (E.g., information access (round number), pure view calls, controller calls,
# things that should be controller calls(deck updates)?, ...?)


class FightCard(Card):
    """A card that is currently fighting. It knows about the FightVnC and the grid. And
    it knows the original card itself, which will be left untouched. Thus, `FightCard`s
    are like throwaway cards that add the necessary functionality during fights.
    """

    vnc: ClassVar[FightVnC]
    grid: ClassVar[Grid]
    _orig: Card

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Initializer disabled. Use `from_card()` instead.")

    def to_card(self) -> Card:
        """Return the original card. Usually unnecessary as long as a reference to the
        original is kept elsewhere.
        """
        return self._orig

    @classmethod
    def init_fight(cls, vnc: FightVnC, grid: Grid) -> None:
        """Set the `FightVnC` and the `Grid` for this class. Do this at the beginning of
        a fight, before creating any `FightCard`s.
        """
        cls.vnc = vnc
        cls.grid = grid

    @classmethod
    def from_card(cls, card: Card) -> FightCard:
        """Create a `FightCard` from a `Card`."""
        assert cls.vnc and cls.grid, "Call `init_fight` first."
        assert isinstance(card, Card)
        fc = card.copy()
        fc.__class__ = cls
        assert isinstance(fc, FightCard)
        fc._orig = card
        fc._orig._fc = fc  # Just to have access to this in tests, e.g., in test_skills
        return fc

    @classmethod
    def from_cards(cls, cards: list[Card]) -> List[FightCard]:
        return [cls.from_card(c) for c in cards]

    def is_human(self) -> bool:
        """Whether this card belongs to the human player or not. (Note that there is no
        `is_human` method in the `Card` class, because it is not straightforward to
        implement there and it is also not needed there.)
        """
        return self in self.vnc.decks.get_all_cards() + self.grid.lines[2]

    def copy(self) -> FightCard:
        """Copy the card. Use case: temporary copies of cards during a fight. E.g., for
        fertility.
        """
        cp = super().copy()
        assert isinstance(cp, FightCard)
        return cp

    def get_grid_pos(self) -> GridPos:
        pos = self.grid.find_card(self)
        assert pos is not None, "Cards calling `get_grid_pos` must be on the grid"
        return pos

    def get_prep_card(self) -> Optional[FightCard]:
        """Get the card from the prepline of this card's slot."""
        return self.grid.get_card(self.get_grid_pos()._replace(line=0))

    def sacrifice(self) -> int:
        """Sacrifice this card and return the amount of fire it had. Note that
        sacrificing does not produce any spirits.
        """
        self.health = 0
        if self.is_human():  # QQ: Can this be done differently?
            self.vnc.decks.used.add_card(self)
        self.grid.remove_card(self)
        logging.debug("%s sacrificed.", self.name)
        return self.has_fire

    def die(self) -> None:
        self.health = 0
        pos = self.get_grid_pos()
        if self.is_human():  # QQ: Can this be done differently?
            self.vnc.humanplayer.spirits += self.has_spirits
            self.vnc.decks.used.add_card(self)
        self.grid.remove_card(self)
        self.vnc.card_died(self, pos)
        logging.debug("%s died.", self.name)

    def take_damage(self, howmuch: int) -> int:
        """Returns how much damage is still left to be consumed. Damage can be left when
        a card died w/o consuming all damage. Keep in mind that damage can be consumed
        by shields an other skills too.
        """
        assert howmuch >= 0
        if howmuch == 0:
            return 0
        damage_left = howmuch

        if sk.Shield in self.skills:
            damage_left -= self.skills.get(sk.Shield).absorbed_damage(
                damage_left, self.vnc.round_num
            )

        if damage_left >= self.health:
            damage_left -= self.health
            self.die()
        else:
            self.health -= damage_left
            damage_left = 0
            self.vnc.card_lost_health(self)

        logging.debug(
            "%s: -%sH (now at %sH)", self.name, howmuch - damage_left, self.health
        )
        return damage_left

    def prepare(self) -> bool:
        """Prepare a card for attack by moving it from the prepline to the computer line.
        Returns `True` if the card was prepared, `False` if it couldn't be prepared.
        """
        pos = self.get_grid_pos()
        assert pos is not None and pos.line == 0
        to_pos = pos._replace(line=1)
        prep_to = self.grid.get_card(to_pos)
        if prep_to is not None:
            logging.debug(
                "Preparing %s but %s occupied by %s", self.name, to_pos, prep_to.name
            )
            return False

        logging.debug("Preparing %s", self.name)
        self.vnc.card_prepare(self)
        self.grid.move_card(self, to_pos=to_pos)
        return True

    def attack(self, target: Optional[FightCard] = None) -> None:
        assert self.grid.find_card(self) is not None
        assert self.grid.find_card(self).line != 0
        attacker_player, target_player = (
            ("human", "computer") if self.is_human() else ("computer", "human")
        )

        # ----- No power? -> Return immediately -----

        if self.power == 0:
            logging.debug("%s would attack but has 0 power, so doesn't", self.name)
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

        self.vnc.card_activate(self)

        self.skills.call("pre_attack")

        # ----- Early special cases -----

        # Will the card die before it can attack due to an unlucky LuckyStrike?
        if (
            sk.LuckyStrike in self.skills
            and not self.skills.get(sk.LuckyStrike).is_lucky()  # type: ignore
        ):
            self.die()
            logging.debug("%s gets unlucky with Lucky Strike", self.name)
            return
        # Post-condition: If attacker has LuckyStrike, it is lucky this attack.

        # ----- Attack the agent behind directly -----

        attacker_touches_target = target is not None and (
            sk.Soaring not in self.skills or sk.Airdefense in target.skills
        )
        attacks_agent_directly = target is None or not attacker_touches_target

        if attacks_agent_directly:
            power = self.power
            if sk.LuckyStrike in self.skills:
                power = self.skills.get(sk.LuckyStrike).power_up_against_agent(power)  # type: ignore
            self.vnc.handle_agent_damage(target_player, power)
            return

        # ----- Otherwise: Attack the opposing card -----

        assert target is not None
        self.vnc.card_getting_attacked(target, self)

        # ----- Opposing card dies instantly -----

        target_dies_instanly = attacker_touches_target and (
            sk.InstantDeath in self.skills
            or (
                sk.LuckyStrike in self.skills
                and self.skills.get(sk.LuckyStrike).is_lucky()  # type: ignore
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
        attacker_power = self.power
        attacker_to_lose = 0

        if sk.Spines in target.skills:
            logging.debug("%s -> %s: 1D (Spines)", target.name, self.name)
            # attacker.lose_health(1)
            attacker_to_lose += 1

        if sk.Underdog in self.skills and attacker_power < target.power:
            logging.debug("%s: +1 P (Underdog)", self.name)
            attacker_power += 1
            # cf [1]

        # ----- Deal damage -----

        # Damage to target:
        target_damage_left = target.take_damage(attacker_power)
        if target_damage_left > 0:
            self.vnc.handle_agent_damage(target_player, target_damage_left)

        # Damage to attacker: (e.g., due to Spines)
        attacker_damage_left = self.take_damage(attacker_to_lose)
        # Note that due to the call to `take_damage`, the attacker can also die here, and it
        # can also make use of shields and other skills.
        if attacker_damage_left > 0:
            self.vnc.handle_agent_damage(attacker_player, attacker_damage_left)

        # ----- Cleanup -----

        self.skills.call("post_attack")

        self.vnc.card_deactivate(self)

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
