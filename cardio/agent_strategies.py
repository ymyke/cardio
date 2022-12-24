from abc import ABC
from typing import Tuple, List
from . import Grid, Card

Position = Tuple[int, int]
PositionAndCard = Tuple[Position, Card]


class AgentStrategy(ABC):
    def play_cards(self, grid: Grid, turn_number: int) -> None:
        pass


class Turn0OnlyStrategy(AgentStrategy):
    """Doesn't perform any checks whether there are cards on the grid in the spots where
    new cards should be placed since this strategy is only concerned with turn 0
    placements.
    """

    def __init__(self, cards: List[PositionAndCard]) -> None:
        super().__init__()
        self.cards = cards

    def play_cards(self, grid: Grid, turn_number: int) -> None:
        if turn_number == 0:
            for (linei, sloti), card in self.cards:
                grid.lines[linei][sloti] = card
