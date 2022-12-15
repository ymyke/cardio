from __future__ import annotations
import logging
from dataclasses import dataclass
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
        self.reset()

    def reset(self) -> None:
        self.power = self.initial_power
        self.health = self.initial_health

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        self.health = 0
        session.add_event(events.CardDied(self))
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

    def attack(self, opponent: Card) -> None:
        logging.debug("%s attacks %s", self.name, opponent.name)
        e = events.CardAttacked(attacker=self, target=opponent, damage=0)
        session.add_event(e)
        howmuch = opponent.lose_health(self.power)
        e.damage = howmuch

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.find_opponent(self)
        if opponent is not None:
            self.attack(opponent)
