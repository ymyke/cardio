from abc import ABC, abstractmethod
from typing import List, Optional
from . import Grid, Deck, GridPos, GridPosAndCard


# FIXME This is maybe ComputerAgentStrategy bc it only applies to the computer agent,
# who can directly influence the grid.
class AgentStrategy(ABC):
    @abstractmethod
    def play_cards(self, grid: Grid, turn_number: int) -> None:
        # FIXME Should `grid` be set in the initalizer? Same as in HumanAgentStrategy?
        pass


class HumanAgentStrategy(ABC):
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    def add_decks(
        self, fightdeck: Deck, hamsterdeck: Deck, handdeck: Deck, useddeck: Deck
    ) -> None:
        # FIXME Ugly! Should get rid of this once we have something like CardCollection
        # which can be set up in the strategy outside of the handle_fight function.
        self.fightdeck = fightdeck
        self.hamsterdeck = hamsterdeck
        self.handdeck = handdeck
        self.useddeck = useddeck

    @abstractmethod
    def deck_to_draw_from(self, turn_number: int) -> Deck:
        pass

    @abstractmethod
    def card_to_play_from_hand(self, turn_number: int) -> Optional[GridPosAndCard]:
        # FIXME Needs a different name, e.g., play_card(s)
        """The card that is returned is expected to be removed from the handdeck
        already. Returns `None` if no card to be played.
        """
        pass
        # FIXME Should this be unified with computer's AgentStrategy bc this is
        # essentially the same as play_cards with the difference that this here returns
        # the position and card while the other places the card directly. But we'll need
        # the former mechanism anyway bc the view needs to get updated with the newly
        # placed card(s).


class SimpleHumanStrategy(HumanAgentStrategy):
    def deck_to_draw_from(self, turn_number: int) -> Deck:
        if self.hamsterdeck.is_empty():
            return self.fightdeck
        if self.fightdeck.is_empty():
            return self.hamsterdeck
        if turn_number % 2 == 0:
            return self.hamsterdeck
        return self.fightdeck

    def card_to_play_from_hand(self, turn_number: int) -> Optional[GridPosAndCard]:
        if self.handdeck.is_empty():
            return None
        for sloti in range(self.grid.width):
            if self.grid[2][sloti] is None:
                return (GridPos(2, sloti), self.handdeck.draw_card())
        return None


class Turn0OnlyStrategy(AgentStrategy):
    """Doesn't perform any checks whether there are cards on the grid in the spots where
    new cards should be placed since this strategy is only concerned with turn 0
    placements.
    """

    def __init__(self, cards: List[GridPosAndCard]) -> None:
        super().__init__()
        self.cards = cards

    def play_cards(self, grid: Grid, turn_number: int) -> None:
        if turn_number == 0:
            for (linei, sloti), card in self.cards:
                grid.lines[linei][sloti] = card
