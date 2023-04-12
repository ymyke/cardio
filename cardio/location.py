from abc import ABC, abstractmethod
from typing import List
import random
from cardio import Grid, GridPos, gg
from cardio.computer_strategies import ComputerStrategy, Round0OnlyStrategy
from cardio.card_blueprints import _BLUEPRINTS, create_cards_from_blueprints
from cardio.tui import tui


class Location(ABC):
    marker = "   "

    def __init__(self, base_seed: str, rung: int, index: int, paths: List[int]) -> None:
        self.id = f"{self.__class__.__name__[0]}{rung}_{index}"
        self.seed = f"L{rung}_{index}_{base_seed}"
        self.rung = rung  # Steps from start
        self.index = index  # Index position at current rung
        self.paths = paths  # Paths to next locations
        self.generate()

    @abstractmethod
    def generate(self) -> None:
        random.seed(self.seed)
        pass

    @abstractmethod
    def handle(self) -> bool:
        """Returns `True` if the game is is still on, `False` if game is over."""
        pass


# ----- Factory -----


def create_random_location(
    base_seed: str, rung: int, index: int, paths: List[int]
) -> Location:
    known_locations = [  # 1 = "base" frequency
        (NoLocation, 5),
        (FightLocation, 5),
    ]
    random.seed(f"L{rung}_{index}_{base_seed}_locationfactory")
    exploded_locations = [loc for loc, count in known_locations for _ in range(count)]
    location_class = random.choice(exploded_locations)
    return location_class(base_seed, rung, index, paths)


# ----- Specific locations -----


class NoLocation(Location):
    marker = "···"

    def generate(self) -> None:
        pass

    def handle(self) -> bool:
        return True


class FightLocation(Location):
    marker = "FFF"
    grid: Grid
    computerstrategy: ComputerStrategy

    def generate(self) -> None:
        super().generate()
        self.grid = Grid(4)
        nofcards = random.randint(1, 4)
        cardnames = [random.choice(_BLUEPRINTS).name for _ in range(nofcards)]
        cards = create_cards_from_blueprints(cardnames)
        positions = [
            GridPos(line, slot) for line in (0, 1) for slot in range(self.grid.width)
        ]
        random.shuffle(positions)
        posncards = list(zip(positions, cards))
        self.computerstrategy = Round0OnlyStrategy(grid=self.grid, cards=posncards)

        # FIXME Use some other computer strategy later
        # FIXME Use rung to somehow increase difficulty as more distance is traveled
        # (e.g., more cards every x steps)

    def handle(self) -> bool:
        vnc = tui.TUIFightVnC(
            computerstrategy=self.computerstrategy, grid=self.grid, debug=True
        )
        gg.vnc = vnc  # Stick information into the globals
        gg.grid = self.grid
        vnc.handle_fight()
        vnc.close()
        return vnc._has_human_won()
