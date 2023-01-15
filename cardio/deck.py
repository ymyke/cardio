from typing import Optional
import random
from . import Card, CardList


class Deck:
    cards: CardList

    def __init__(self, cards: Optional[CardList] = None) -> None:
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
