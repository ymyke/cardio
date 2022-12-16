from dataclasses import dataclass
from .card import Card


class Event:
    pass


@dataclass
class CardGetsAttacked(Event):
    attacker: Card
    target: Card


@dataclass
class OverflowDamage(Event):
    damage: int
    sloti: int


@dataclass
class CardDies(Event):
    target: Card


# FIXME These cards will all point to objects that can still change and don't reflect
# the state at which the event was generated. Does that make sense???
