from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict, List
from . import FightCard, Grid, GridPosAndCard

if TYPE_CHECKING:
    from . import FightVnC


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
    def cards_to_be_played(self, round_number: int) -> List[GridPosAndCard]:
        pass

    def play_cards(self, round_number: int, vnc: FightVnC) -> None:
        # FIXME I don't think it's very nice that we pass vnc here. We need it to create
        # the FightCards. We could also inline the play_cards method into FightVnC but
        # then we'd lose the flexibility of having more realistic placement strategies
        # also for the computer.
        for (line, slot), card in self.cards_to_be_played(round_number):
            if card and not isinstance(card, FightCard):
                card = FightCard.from_card(card, vnc, self.grid)
            self.grid.lines[line][slot] = card


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


class PredefinedStrategy(ComputerStrategy):
    """Simply plays predefined cards in specific rounds of a fight. Does not perform any
    checks whether the grid is empty or not where a card should be played.
    # FIXME Add that check and test it too.
    """

    def __init__(
        self, cards_per_round: Dict[int, List[GridPosAndCard]], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.cards_per_round = cards_per_round

    def cards_to_be_played(self, round_number: int) -> List[GridPosAndCard]:
        return self.cards_per_round.get(round_number, [])


# TODO watch out! After the first round, computer strategy should place cards only in
# the prep line, not in line 1 directly.
