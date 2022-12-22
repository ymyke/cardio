"""
- Real deck: I have my deck, where all cards are in normal/initial state (with some
  excpetions maybe such as the Ouroboros).
- Fight deck & squirrel deck: At the beginning of a fight, a squirell deck is created
  and a copy of the above deck is created. The fight deck (?).
- Hand: Then, the top x cards from the fight deck and the top 1 card from the squirrel
  deck are drawn to form my hand (deck).
- Once the fight is over, the fight deck gets deleted. (After some changes have been
  propagated to my real deck, if necessary.) (-- OR: The fight deck has a state or two
  different lists or something, but maybe not.)
"""

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

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def add_card(self, card: Card) -> None:
        """Add `card` to the right/end."""
        assert isinstance(card, Card)
        self.cards.append(card)

    def draw_cards(self, howmany: int) -> Optional[CardList]:
        """Draw `howmany` cards from the left/beginning. Drawn cards are removed from
        the deck.
        """
        assert howmany > 0
        drawncards = self.cards[:howmany]
        del self.cards[:howmany]
        return drawncards

    def pick_card(self, i: int) -> Card:
        """Pick sepcific card at position `i`, remove it from the deck and return it."""
        assert i >= 0 and i < len(self.cards)
        card = self.cards[i]
        del self.cards[i]
        return card
