import logging
from dataclasses import dataclass, field
from .deck import Deck


@dataclass
class Agent:
    name: str
    health: int
    initial_health: int
    lives: int
    # FIXME: Score? Money? ...?
    deck: Deck = field(default_factory=lambda: Deck())
    # QQ: Maybe ComputerAgent is a subclass of Agent which will ignore the deck but
    # offer some strategy instead or in addition?

    def lose_health(self, howmuch: int) -> None:
        """Agent's health can go below zero, the number below zero denoting overflow
        damage.
        """
        assert howmuch > 0
        self.health -= howmuch
        logging.debug(
            "Player %s loses %s health, new health %s", self.name, howmuch, self.health
        )

    def has_lost_life(self) -> bool:
        return self.health <= 0

    def update_lives_and_health_after_death(self) -> int:
        assert self.has_lost_life()
        overflow = abs(self.health)
        self.health = self.initial_health
        self.lives -= 1
        assert self.lives >= 0
        logging.debug(
            "Player %s loses 1 life, %s life/lives left, %s overflow damage",
            self.name,
            self.lives,
            overflow,
        )
        return overflow
