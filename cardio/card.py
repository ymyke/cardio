from __future__ import annotations
import logging
import copy
from typing import Optional, List, TYPE_CHECKING
from .skills import Skill, SkillList
from . import gg

if TYPE_CHECKING:
    from . import GridPos


# QQ: This class in its current implementation is geared fully on being used during
# fights: accessing the grid, updating humanplayer, ... -- What will be necessary in the
# future when cards are also used outside of fights? -- Maybe it's ok since fights are
# at the very center of the game and everything else is surrounding stuff.


class Card:
    """Card class

    Principles for `has_*` and `costs_*`:
    - `costs_fire` & `costs_spirits`:
        - Exactly one is > 0.
    - `has_fire` & `has_spirits`:
        - Typically both are == 1.
        - Max one is > 1.
        - Neither is == 0, "0-ness" is indicated via some skill such as bloodless or
          inert or so. (A card with bloodless should always have both `has_*` == 1.)
        - The preceding two bullets are design decisions to keep things simple(r) so a
          player can rely on default information even if not all information is always
          displayed.
        - (QQ: Possible variant: `has_spirits` is always == 1; this would simplify
          things further. But the current philosophy could easily be adapted to such a
          rule.)

    QQ: Turn `has_*` and `costs_*` into properties to enforce the above rules?
    """

    MAX_ATTR = 10  # Max value per attribute (power, health, ...)
    MAX_SKILLS = 6  # Max number of skills a card can have
    # FIXME ^ These are not enforced yet. Should be. Not only in the initializer but
    # whenever something changes to affect these values.

    def __init__(
        self,
        # Mandatory:
        name: str,
        initial_power: int,  # 💪
        initial_health: int,  # 💓
        costs_fire: int,  # How much fire 🔥 needed
        # Optional:
        skills: Optional[SkillList] = None,
        costs_spirits: int = 0,  # How many spirits 👻 needed
        has_spirits: int = 1,  # How many spirits this card generates upon death 👻
        has_fire: int = 1,  # How much fire this card is worth when sacrificed 🔥
        power: int = 0,
        health: int = 0,
    ) -> None:
        self.name = name
        self.initial_power = initial_power
        self.initial_health = initial_health
        self.costs_fire = costs_fire
        self.skills = skills or []
        self.costs_spirits = costs_spirits
        self.has_spirits = has_spirits
        self.has_fire = has_fire

        self.is_temporary: bool = False  # Whether this is only used in a single fight

        if power * health == 0:  # Normal behavior
            self.reset()
        else:  # Used by tests to explicitly set values
            self.power = power
            self.health = health

        # Sanity checks:
        assert all(
            getattr(self, a) >= 0 for a in dir(self) if isinstance(a, int)
        ), "No negative numbers please"
        assert costs_fire * costs_spirits == 0, (
            "Either fire or spirit costs must be 0. "
            "Hybrids are not supported at this time."
            # (Will we ever have cards that can have both cost_fire and cost_spirits? If
            # so, would that be AND or OR? Note that such hybrids would add considerable
            # complexity to the UI, since the player would have to be able to choose how
            # much of either to use (unless specified algorithmically).)
        )

    def reset(self) -> None:
        self.power = self.initial_power
        self.health = self.initial_health

    def is_human(self) -> bool:
        return self in gg.humanplayer.get_all_human_cards()

    def is_skilled(self) -> bool:
        return len(self.skills) > 0

    @property
    def potency(self) -> int:
        """Return the potency of this card. Simply add a number of attributes, where
        power and health are weighted more heavily. Add a bonus for cards with no costs.
        """
        strengths = (
            self.initial_power * 2
            + self.initial_health * 2
            + self.has_fire
            + self.has_spirits
            + sum(s.value.potency for s in self.skills)
        )
        costs = self.costs_fire + self.costs_spirits
        costs_bonus = 10 if costs == 0 else 0  # Bonus for cards with no costs at all
        return strengths - costs + costs_bonus

    def get_grid_pos(self) -> GridPos:
        pos = gg.grid.find_card(self)
        assert pos is not None, "Cards calling `get_grid_pos` must be on the grid"
        return pos

    def clone(self) -> Card:
        """Return a real clone of this card."""
        return copy.deepcopy(self)

    def make_temp_copy(self) -> Card:
        """Return a temporary copy of card."""
        copy = self.clone()
        copy.is_temporary = True
        return copy

    def get_prep_card(self) -> Optional[Card]:
        """Get the card from the prepline of this cards slot."""
        return gg.grid.get_card(self.get_grid_pos()._replace(line=0))

    def _die_silently(self) -> None:
        self.health = 0
        if self.is_human():
            gg.humanplayer.spirits += self.has_spirits
            gg.vnc.decks.used.add_card(self)
        gg.grid.remove_card(self)
        # (Must happen after the `is_human` test, otherwise that test produces wrong
        # results bc one test is whether the card is on the grid or not.)

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        pos = self.get_grid_pos()
        self._die_silently()
        gg.vnc.card_died(self, pos)

    def sacrifice(self) -> None:
        self._die_silently()

    def lose_health(self, howmuch: int) -> int:
        assert howmuch > 0
        if howmuch >= self.health:
            howmuch = self.health
            self.die()
        else:
            self.health -= howmuch
            gg.vnc.card_lost_health(self)
            logging.debug("%s new health: %s", self.name, self.health)
        return howmuch

    def get_attacked(self, opponent: Card) -> None:
        logging.debug("%s gets attacked by %s", self.name, opponent.name)

        if Skill.SPINES in self.skills:
            # FIXME Should maybe be moved further down once we have an animation in
            # place for this because otherwise the animations will happen in the wrong
            # order.
            logging.debug(
                "%s causes 1 damage on %s with Spines", self.name, opponent.name
            )
            opponent.lose_health(1)

        prepcard = self.get_prep_card() if self.get_grid_pos().line == 1 else None
        # (Prep cards only relevant if computer is being attacked.)
        gg.vnc.card_getting_attacked(self, opponent)
        # (Needs to happen before the call to `lose_health` below, bc the card could
        # die/vanish during that call, leading to a `None` reference on the grid and an
        # error in the view update call.)
        howmuch = self.lose_health(opponent.power)
        if opponent.power > howmuch and prepcard is not None:
            logging.debug(
                "%s gets overflow damage of %s", prepcard.name, opponent.power - howmuch
            )
            prepcard.lose_health(opponent.power - howmuch)

    # QQ: Fight logic is distributed between Card and FightVNC. Can this be streamlined?
    # (One could argue that all the places where the card module needs to call a view
    # method should rather belong somewhere else?)

    def attack(self, opponent: Optional[Card]) -> None:
        if self.power == 0:
            logging.debug("%s would attack but has 0 power, so doesn't", self.name)
            return

        if opponent is None:
            gg.vnc.handle_player_damage(self.power, self)
            return

        logging.debug(
            "%s%s attacks %s %s",
            self.name,
            "".join(s.value.symbol for s in self.skills),
            opponent.name,
            "".join(s.value.symbol for s in opponent.skills),
        )

        if Skill.SOARING in self.skills:
            if Skill.AIRDEFENSE in opponent.skills:
                if Skill.INSTANTDEATH in self.skills:
                    opponent.die()
                else:
                    opponent.get_attacked(self)
            else:
                gg.vnc.handle_player_damage(self.power, self)
            return

        if Skill.INSTANTDEATH in self.skills:
            opponent.die()
            return

        opponent.get_attacked(self)

    def activate(self) -> None:
        if self.power == 0:
            logging.debug("%s become active but has 0 power, so doesn't", self.name)
            return
        logging.debug("%s becomes active", self.name)
        opponent = gg.grid.get_opposing_card(self)
        pos = self.get_grid_pos()
        gg.vnc.card_activate(self)
        self.attack(opponent)
        gg.vnc.pos_card_deactivate(pos)

    def prepare(self) -> None:
        pos = self.get_grid_pos()
        assert pos is not None and pos.line == 0
        to_pos = pos._replace(line=1)
        prep_to = gg.grid.get_card(to_pos)
        if prep_to is not None:
            logging.debug(
                "Preparing %s but the prep-to space is occupied by %s",
                self.name,
                prep_to.name,
            )
            return
        logging.debug("Preparing %s, moving to computer line", self.name)
        gg.vnc.card_prepare(self)
        gg.grid.move_card(self, to_pos=to_pos)
        self.activate()


# ----- Types -----

CardList = List[Card]
