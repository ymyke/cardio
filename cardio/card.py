from __future__ import annotations
from dataclasses import dataclass
from . import session
import logging


@dataclass
class Card:
    name: str
    power: int
    health: int

    def loose_health(self, howmuch: int) -> None:
        if howmuch >= self.health:
            self.health = 0
            # dies FIXME
            logging.debug("%s dies.", self.name)
            return
        self.health -= howmuch
        logging.debug("%s new health: %s", self.name, self.health)
        # FIXME Handle overflow damage to creature behind. Does that always happen? No
        # matter how the health got lost in the first place?

    def attack(self, opponent: Card) -> None:
        logging.debug("%s attacks %s", self.name, opponent.name)
        opponent.loose_health(self.power)

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.find_opponent(self)
        if opponent is not None:
            self.attack(opponent)
