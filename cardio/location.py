from abc import ABC, abstractmethod
import random
from cardio import Grid, GridPos
from cardio.computer_strategies import ComputerStrategy, Round0OnlyStrategy
from cardio.card_blueprints import _BLUEPRINTS, create_cards_from_blueprints


class Location(ABC):
    seed: int
    distance: int

    def __init__(self, seed: int, distance: int) -> None:
        self.seed = seed
        self.distance = distance
        self.generate()

    @abstractmethod
    def generate(self) -> None:
        pass


class FightLocation(Location):
    grid: Grid
    computerstrategy: ComputerStrategy

    def generate(self) -> None:
        random.seed(self.seed)
        self.grid = Grid(4)
        nofcards = random.randint(1, 4)
        cardnames = [random.choice(_BLUEPRINTS).name for _ in range(nofcards)]
        cards = create_cards_from_blueprints(cardnames)
        cards.extend([None] * (2 * self.grid.width - nofcards))
        positions = [
            GridPos(line, slot) for line in (0, 1) for slot in range(self.grid.width)
        ]
        posncards = list(zip(positions, cards))
        random.shuffle(posncards)
        self.computerstrategy = Round0OnlyStrategy(grid=self.grid, cards=posncards)

        # FIXME Use some other computer strategy later
        # FIXME Use distance to somehow increase difficulty as more distance is traveled
        # (e.g., more cards every x steps)
