from abc import ABC, abstractmethod
import logging
import numpy as np
import random
from typing import Dict, List, Tuple
from ordered_set import OrderedSet
from . import FightCard, Grid, GridPosAndCard, GridPos

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


def biased_number(x: int, y: int, z: float) -> int:
    """Generates a single integer with a normal distribution biased towards z,
    with values ranging from x to y (inclusive). (z is a `float` in order to fine-tune
    the bias.)
    """
    assert x <= z <= y, "z should be within the interval [x, y]"
    # The standard deviation is set so 99.7% of values will be within the range [x, y]
    mu, sigma = z, (y - x) / 6
    s = np.random.normal(mu, sigma, 1)
    s = np.clip(s, x, y)
    s = np.rint(s)
    return int(s[0])


class SimpleRungBasedStrategy(PredefinedStrategy):
    """Plays cards based on the player's rung."""

    def _determine_difficulty(self, rung: int) -> Tuple[int, int, float]:
        """Return the difficulty settings of the game based on the player's rung.

        The difficulty is determined by the following dimensions, which are returned as
        a tuple:
        - `nofcards`: Number of cards overall
        - `density`: Number of cards per round
        - `max_potency`: potency of cards
        """
        # Number of cards overall:
        mincards = random.randint(1, 2)
        nofcards = rung // 3
        jitter = random.randint(-nofcards // 5, nofcards // 5)
        nofcards = max(mincards, nofcards + jitter)

        # Potency:
        max_potency = max(rung // 5, 5)

        # Sometimes decrease potency but bring more cards into play:
        while random.random() < 0.1 and max_potency > 1:
            morecards = max(nofcards // 5, 1)
            nofcards += morecards
            max_potency -= 1
        # TODO Same the other way round?

        # Density:
        density = min(max(rung / 150, 1), self.grid.width)

        # Sometimes decrease potency to increase density:
        while random.random() < 0.1 and density < self.grid.width and max_potency > 1:
            density = min(density + 0.5, self.grid.width)
            max_potency -= 1
        # TODO Same the other way round?

        logging.debug(
            "Difficulty settings: %s cards, %s max potency, %s density",
            nofcards,
            max_potency,
            density,
        )
        self.nofcards, self.max_potency, self.density = nofcards, max_potency, density
        return nofcards, max_potency, density

    def __init__(self, rung: int, *args, **kwargs) -> None:
        super().__init__(cards_per_round={}, *args, **kwargs)
        self._determine_difficulty(rung)

        # Get blueprints:
        from cardio.blueprints import thecatalog, BlueprintList  # prevent crclr import

        blueprint_candidates = thecatalog.find_by_potency(
            -100, self.max_potency, which="computer"
        )
        # Shift potencies because there can be negative potencies:
        potencies = [
            blueprint._original.potency("computer")
            for blueprint in blueprint_candidates
        ]
        min_potency = min(potencies)
        shifted_potencies = [potency - min_potency + 1 for potency in potencies]
        # Use shifted_potencies as weights to bias selection towards higher potentices:
        blueprints = random.choices(
            blueprint_candidates, weights=shifted_potencies, k=self.nofcards
        )

        # Build cards per round:
        cards = BlueprintList(blueprints).instantiate()
        cardsperround = {}
        i, j = 0, -1
        while i < len(cards):
            piece_length = biased_number(0, self.grid.width, self.density)
            if piece_length > 0:
                piece = cards[i : i + piece_length]
                slots = random.sample(range(self.grid.width), piece_length)
                cardsperround[j] = [
                    GridPosAndCard(GridPos(0, slot), card)
                    for slot, card in zip(slots, piece)
                ]
                i += piece_length
            j += 1

        if -1 in cardsperround:
            # Map cards to slot 1 instead of slot 0:
            line1 = [
                GridPosAndCard(GridPos(1, x.pos.slot), x.card)
                for x in cardsperround[-1]
            ]
            cardsperround[0] = line1 + cardsperround.get(0, [])
            cardsperround.pop(-1, None)

        self.cards_per_round = cardsperround
