from __future__ import annotations
import logging
from dataclasses import dataclass
from typing import Optional
from . import session
from . import events


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

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        self.health = 0
        session.add_event(events.CardDies(self))
        session.grid.remove_card(self)

    def lose_health(self, howmuch: int) -> int:
        if howmuch >= self.health:
            howmuch = self.health
            self.die()
        else:
            self.health -= howmuch
            logging.debug("%s new health: %s", self.name, self.health)
        return howmuch
        # FIXME Handle overflow damage to creature behind. Does that always happen? No
        # matter how the health got lost in the first place?

    def get_attacked(self, opponent: Card) -> None:
        logging.debug("%s gets attacked by %s", self.name, opponent.name)
        sloti = self.get_sloti()
        howmuch = self.lose_health(opponent.power)
        if opponent.power > howmuch:
            session.add_event(
                events.OverflowDamage(damage=opponent.power - howmuch, sloti=sloti)
            )

    def attack(self, opponent: Card) -> None:
        logging.debug("%s attacks %s", self.name, opponent.name)
        session.add_event(events.CardGetsAttacked(attacker=self, target=opponent))

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.find_opponent(self)
        if opponent is not None:
            self.attack(opponent)
