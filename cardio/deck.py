from typing import Generic, Optional, List, TypeVar
from dataclasses import dataclass, fields, field
import logging
import random


T = TypeVar("T")


class Deck(Generic[T]):
    def __init__(self, name: str, cards: Optional[List[T]] = None) -> None:
        assert isinstance(name, str)
        self.name = name
        if cards is None:
            self.cards = []
        else:
            assert all(isinstance(c, type(cards[0])) for c in cards)
            self.cards = cards

    def size(self) -> int:
        return len(self.cards)

    def is_empty(self) -> bool:
        return self.size() == 0

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def add_card(self, card: T) -> None:
        """Add `card` to the right/end."""
        assert self.is_empty() or isinstance(card, type(self.cards[0]))
        self.cards.append(card)

    def remove_card(self, card: T) -> None:
        self.cards.remove(card)

    def draw_cards(self, howmany: int) -> List[T]:
        """Draw `howmany` cards from the left/beginning. Drawn cards are removed from
        the deck.
        """
        assert howmany > 0
        drawncards = self.cards[:howmany]
        del self.cards[:howmany]
        return drawncards

    def draw_card(self) -> T:
        """Draw exactly 1 card."""
        return self.draw_cards(1).pop()

    def pick_card(self, i: int) -> T:
        """Pick sepcific card at position `i`, remove it from the deck and return it."""
        assert i >= 0 and i < len(self.cards)
        card = self.cards[i]
        del self.cards[i]
        return card


@dataclass
class FightDecks(Generic[T]):
    hand: Deck = field(default_factory=lambda: Deck("Hand"))
    used: Deck = field(default_factory=lambda: Deck("Used"))
    draw: Deck = field(default_factory=lambda: Deck("Draw"))
    hamster: Deck = field(default_factory=lambda: Deck("Hamster"))

    def get_decks(self) -> List[Deck]:
        return [getattr(self, f.name) for f in fields(self) if f.type == Deck]

    def log(self):
        for deck in self.get_decks():
            cardnames = ",".join([c.name for c in deck.cards])
            logging.debug("%sdeck size: %s (%s)", deck.name, len(deck.cards), cardnames)

    def get_all_cards(self) -> List[T]:
        return [card for deck in self.get_decks() for card in deck.cards]
