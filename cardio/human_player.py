from dataclasses import dataclass, field
from cardio import session
from cardio.card import CardList
from .deck import Deck


@dataclass
class HumanPlayer:
    name: str
    lives: int = 1  # 💓
    gems: int = 0  # 💎
    spirits: int = 0  # 👻 (or droplets/essence? 💧)
    deck: Deck = field(default_factory=lambda: Deck("main"))

    def get_all_human_cards(self) -> CardList:
        cards = []

        # During fights I: Add fight decks
        try:
            cards.extend(session.vnc.decks.get_all_cards())
        except AttributeError:
            pass

        # During fights II: Add cards on the grid in the human player's line
        # (Adding this as a separate try-except clause bc it makes tests easier without
        # having to mock up the entire decks in FightVnC.)
        try:
            cards.extend([c for c in session.grid.lines[2] if c is not None])
        except AttributeError:
            pass

        # Outside fights: Add human player's deck
        # (Note that tis test does not suffice during a fight bc new cards could be
        # created (e.g., via fertility) during a fight which are added to one of the
        # fight decks but not yet to a player's deck (which gets recreated only after a
        # fight).)
        cards.extend(self.deck.cards)

        return cards
