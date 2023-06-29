from abc import ABC, abstractmethod
import logging
from typing import Dict, List
from ordered_set import OrderedSet
from . import FightCard, Grid, GridPosAndCard


class ComputerStrategy(ABC):
    """Abstract base class for computer strategies.

    A computer strategy defines when the computer brings which cards (or maybe in the
    future also other things, such as items) into play.

    A strategy can take some input parameters (initial deck, current grid, turn number,
    ...) and return which cards will be played to which slots.

    Note that this base strategy implements a waitlist mechanism, see `play_cards`.
    """

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self._waitlist: List[GridPosAndCard] = []

    @abstractmethod
    def cards_to_be_played(self, round_number: int) -> List[GridPosAndCard]:
        pass

    def play_cards(self, round_number: int) -> None:
        """Play cards to the grid. Will use `cards_to_be_played` to determine which
        cards to play. Implements the waitlist mechanism that makes sure cards that
        can't be played yet are played as soon as the respective slot becomes available.
        """
        # Using OrderedSet to make sure each card is only added once. (Cards can be
        # added multiple times if they remain in the waitlist for multiple rounds.)
        new_waitlist = OrderedSet([])
        for pos, card in self._waitlist + self.cards_to_be_played(round_number):
            if round_number > 0 and pos.line != 0:
                logging.warning(
                    "Computer is supposed to only place in prepline in later rounds. "
                    "Ignoring card %s.",
                    card.name,
                )
                continue
            if card and not isinstance(card, FightCard):
                card = FightCard.from_card(card)
            if self.grid.get_card(pos):
                new_waitlist.append(GridPosAndCard(pos, card))
            else:
                self.grid.set_card(pos, card)
        self._waitlist = list(new_waitlist)


class PredefinedStrategy(ComputerStrategy):
    """Simply plays predefined cards in specific rounds of a fight."""

    def __init__(
        self, cards_per_round: Dict[int, List[GridPosAndCard]], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.cards_per_round: Dict[int, List[GridPosAndCard]] = cards_per_round

    def cards_to_be_played(self, round_number: int) -> List[GridPosAndCard]:
        return self.cards_per_round.get(round_number, [])


class Round0OnlyStrategy(PredefinedStrategy):
    """Plays predefined cards only in round 0 of a fight."""

    def __init__(self, cards: List[GridPosAndCard], *args, **kwargs) -> None:
        self.cards = cards
        super().__init__({0: cards}, *args, **kwargs)
