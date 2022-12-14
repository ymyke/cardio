from __future__ import annotations
from dataclasses import dataclass
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
        # FIXME Handle overflow damage to creature behind.

    def attack(self, opponent: Card) -> None:
        logging.debug("%s attacks %s", self.name, opponent.name)
        opponent.loose_health(self.power)
