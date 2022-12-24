from __future__ import annotations
import logging
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from .sigils import Sigil, SigilList
from . import session

if TYPE_CHECKING:
    # To prevent circular imports. Should maybe be fixed somehow at some point.
    from . import Agent


@dataclass
class Card:
    name: str
    initial_power: int
    initial_health: int
    # FIXME How much blood needed?
    # FIXME Bones...

    # Derived attributes:
    power: int = 0
    health: int = 0
    sigils: SigilList = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.power == 0 or self.health == 0:
            # (This test allows to explicitly set power and health, e.g., for tests.)
            self.reset()

    def reset(self) -> None:
        self.power = self.initial_power
        self.health = self.initial_health

    def get_sloti(self) -> int:
        sloti = session.grid.find_card_position(self)[1]
        if sloti is None:
            raise RuntimeError("Trying to get sloti for card that is not on the grid.")
        return sloti

    def get_linei(self) -> int:
        linei = session.grid.find_card_position(self)[0]
        if linei is None:
            raise RuntimeError("Trying to get linei for card that is not on the grid.")
        return linei

    def get_prep_card(self) -> Optional[Card]:
        """Get the card from the prepline of this cards slot."""
        return session.grid.prepline[self.get_sloti()]

    def get_opposing_agent(self) -> Agent:
        return session.computeragent if self.get_linei() == 2 else session.humanagent
        # QQ: Use enums or something instead of 0, 1, 2 for the lines?
        # QQ: Should this be a grid function? (Also some of the other methods?)

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        self.health = 0
        session.grid.remove_card(self)
        # FIXME Card must also be moved to a different deck?

    def lose_health(self, howmuch: int) -> int:
        assert howmuch > 0
        if howmuch >= self.health:
            howmuch = self.health
            self.die()
        else:
            self.health -= howmuch
            logging.debug("%s new health: %s", self.name, self.health)
        return howmuch

    def get_attacked(self, opponent: Card) -> None:
        logging.debug("%s gets attacked by %s", self.name, opponent.name)

        if Sigil.SPINES in self.sigils:
            logging.debug(
                "%s causes 1 damage on %s with Spines", self.name, opponent.name
            )
            opponent.lose_health(1)

        prep = self.get_prep_card()
        howmuch = self.lose_health(opponent.power)
        session.view.get_attacked(self, opponent)
        if opponent.power > howmuch and prep is not None:
            logging.debug(
                "%s gets overflow damage of %s", prep.name, opponent.power - howmuch
            )
            prep.lose_health(opponent.power - howmuch)

    def attack(self, opponent: Card) -> None:
        if self.power == 0:
            logging.debug("%s would attack but has 0 power, so doesn't", self.name)
            return

        logging.debug(
            "%s%s attacks %s %s",
            self.name,
            "".join(s.value.symbol for s in self.sigils),
            opponent.name,
            "".join(s.value.symbol for s in opponent.sigils),
        )

        if Sigil.SOARING in self.sigils:
            if Sigil.AIRDEFENSE in opponent.sigils:
                if Sigil.INSTANTDEATH in self.sigils:
                    opponent.die()
                else:
                    opponent.get_attacked(self)
            else:
                self.get_opposing_agent().lose_health(self.power)
            return

        if Sigil.INSTANTDEATH in self.sigils:
            opponent.die()
            return

        opponent.get_attacked(self)

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.get_opposing_card(self)
        session.view.activate_card(self)
        if opponent is not None:
            self.attack(opponent)
        elif self.power > 0:
            self.get_opposing_agent().lose_health(self.power)
            # ^ FIXME should this be in attack after all?

    def prepare(self) -> None:
        linei, sloti = session.grid.find_card_position(self)
        assert linei == 0 and sloti is not None
        prep_to_card = session.grid[1][sloti]
        # ^ QQ: Should this be a method like get_card() or something?
        if prep_to_card is not None:
            logging.debug(
                "Preparing %s but the prep-to space is occupied by %s",
                self.name,
                prep_to_card.name,
            )
            return
        logging.debug("Preparing %s, moving to computer line", self.name)
        session.grid.move_card(self, to_linei=1, to_sloti=sloti)
        self.activate()


# ----- Types -----

CardList = List[Card]
