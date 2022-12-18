from __future__ import annotations
import logging
from dataclasses import dataclass
from typing import Optional
from .agent import Agent
from . import session


@dataclass
class Card:
    name: str
    initial_power: int
    initial_health: int

    # Derived attributes:
    power: int = 0
    health: int = 0

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

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        self.health = 0
        session.grid.remove_card(self)

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
        logging.debug("%s attacks %s", self.name, opponent.name)
        opponent.get_attacked(self)

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.find_opponent(self)
        session.view.activate_card(self)
        if opponent is not None:
            self.attack(opponent)
        elif self.power > 0:
            self.get_opposing_agent().lose_health(self.power)
