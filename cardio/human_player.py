from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from .deck import Deck

# from cardio.blueprints import thecatalog # Imported below to avoid circular imports

if TYPE_CHECKING:
    from .blueprints import Blueprint


@dataclass
class HumanPlayer:
    name: str
    lives: int = 1  # 💓
    gems: int = 0  # 💎
    spirits: int = 0  # 👻 (or droplets/essence? 💧)
    deck: Deck = field(default_factory=lambda: Deck("main"))
    collection: Deck = field(default_factory=lambda: Deck("collection"))
    hamster_blueprint: Blueprint = None  # type: ignore

    def __post_init__(self):
        from cardio.blueprints import thecatalog

        if not self.hamster_blueprint:
            self.hamster_blueprint = thecatalog.get("Hamster")

    @classmethod
    def create_new(cls, name: str) -> HumanPlayer:
        from cardio.blueprints import thecatalog

        p = cls(name=name, lives=1, gems=0, spirits=3)
        start_cards = thecatalog.find_by_potency(0, 5, core=False).instantiate()
        start_cards = [
            c
            for c in start_cards
            if c.costs_fire + c.costs_spirits <= 2 and c.has_fire + c.has_spirits <= 2
        ]
        p.collection.cards = start_cards
        return p
