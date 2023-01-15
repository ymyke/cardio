from abc import ABC, abstractmethod
from typing import List
from . import Grid, GridPosAndCard


class ComputerStrategy(ABC):
    @abstractmethod
    def cards_to_be_played(self, grid: Grid, turn_number: int) -> List[GridPosAndCard]:
        # FIXME Should `grid` be set in the initalizer? Same as in HumanAgentStrategy?
        pass

    @abstractmethod
    def play_cards(self, grid: Grid, turn_number: int) -> None:
        # FIXME Should `grid` be set in the initalizer? Same as in HumanAgentStrategy?
        pass


class Round0OnlyStrategy(ComputerStrategy):
    """Doesn't perform any checks whether there are cards on the grid in the spots where
    new cards should be placed since this strategy is only concerned with round 0
    placements.
    """

    def __init__(self, cards: List[GridPosAndCard]) -> None:
        super().__init__()
        self.cards = cards

    def cards_to_be_played(self, grid: Grid, turn_number: int) -> List[GridPosAndCard]:
        if turn_number == 0:
            return self.cards
        return []

    def play_cards(self, grid: Grid, turn_number: int) -> None:
        for (linei, sloti), card in self.cards_to_be_played(grid, turn_number):
            grid.lines[linei][sloti] = card
