from dataclasses import dataclass, field
from cardio import gg
from cardio.card import CardList
from .deck import Deck


@dataclass
class HumanPlayer:
    name: str
    lives: int = 1  # 💓
    gems: int = 0  # 💎
    spirits: int = 0  # 👻 (or droplets/essence? 💧)
    deck: Deck = field(default_factory=lambda: Deck("main"))
    collection: Deck = field(default_factory=lambda: Deck("collection"))
