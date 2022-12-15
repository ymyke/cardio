from dataclasses import dataclass
from .card import Card


class Event:
    pass


@dataclass
class CardAttacked(Event):
    attacker: Card
    target: Card
    damage: int


@dataclass
class CardDied(Event):
    target: Card
