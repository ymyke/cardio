from abc import ABC, abstractmethod
from typing import Dict, List
from . import Grid, GridPosAndCard


class ComputerStrategy(ABC):
    """Abstract base class for computer strategies.
    
    A computer strategy defines when the computer brings which cards (or maybe in the
    future also other things, such as items) into play. 

    A strategy can take some input parameters (initial deck, current grid, turn number,
    ...) and return which cards will be played to which slots. 
  
    It is conceivable that a strategy is as constrained or free as necessary: a)
    strategy adheres to no rules at all, b) strategy needs to work within all the rules
    (e.g., placement rules such as fire/spirit costs etc.), c) strategy needs to work
    with an initial deck.
    """
    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    @abstractmethod
    def cards_to_be_played(self, turn_number: int) -> List[GridPosAndCard]:
        pass

    @abstractmethod
    def play_cards(self, turn_number: int) -> None:
        pass


class Round0OnlyStrategy(ComputerStrategy):
    """Doesn't perform any checks whether there are cards on the grid in the spots where
    new cards should be placed since this strategy is only concerned with round 0
    placements.
    """

    def __init__(self, cards: List[GridPosAndCard], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cards = cards

    def cards_to_be_played(self, round_number: int) -> List[GridPosAndCard]:
        if round_number == 0:
            return self.cards
        return []

    def play_cards(self, round_number: int) -> None:
        for (line, slot), card in self.cards_to_be_played(round_number):
            self.grid.lines[line][slot] = card

class PredefinedStrategy(ComputerStrategy):
    """Simply plays predefined cards in specific rounds of a fight. Does not perform any
    checks whether the grid is empty or not where a card should be played. 
    # FIXME Add that check and test it too.
    """

    def __init__(self, cards_per_round: Dict[int, List[GridPosAndCard]], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cards_per_round = cards_per_round

    def cards_to_be_played(self, round_number: int) -> List[GridPosAndCard]:
        return self.cards_per_round.get(round_number, [])

    def play_cards(self, round_number: int) -> None:
        for (line, slot), card in self.cards_to_be_played(round_number):
            self.grid.lines[line][slot] = card
