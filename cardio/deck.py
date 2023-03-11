from typing import Optional, List
from dataclasses import dataclass, fields, field
import logging
import random
from . import Card, CardList


class Deck:
    def __init__(self, name: str, cards: Optional[CardList] = None) -> None:
        assert isinstance(name, str)
        self.name = name
        if cards is None:
            self.cards = []
        else:
            assert all(isinstance(c, Card) for c in cards)
            self.cards = cards

    def size(self) -> int:
        return len(self.cards)

    def is_empty(self) -> bool:
        return self.size() == 0

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def add_card(self, card: Card) -> None:
        """Add `card` to the right/end."""
        assert isinstance(card, Card)
        self.cards.append(card)

    def draw_cards(self, howmany: int) -> CardList:
        """Draw `howmany` cards from the left/beginning. Drawn cards are removed from
        the deck.
        """
        assert howmany > 0
        drawncards = self.cards[:howmany]
        del self.cards[:howmany]
        return drawncards

    def draw_card(self) -> Card:
        """Draw exactly 1 card."""
        return self.draw_cards(1).pop()

    def pick_card(self, i: int) -> Card:
        """Pick sepcific card at position `i`, remove it from the deck and return it."""
        assert i >= 0 and i < len(self.cards)
        card = self.cards[i]
        del self.cards[i]
        return card

    def reset_cards(self) -> None:
        """Reset all cards in deck."""
        for card in self.cards:
            card.reset()


@dataclass
class FightDecks:
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

    def get_all_cards(self) -> CardList:
        return [card for deck in self.get_decks() for card in deck.cards]
