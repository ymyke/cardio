from abc import ABC, abstractmethod
from typing import List
import random
from cardio import Grid, GridPos, gg
from cardio.computer_strategies import ComputerStrategy, Round0OnlyStrategy
from cardio.card_blueprints import _BLUEPRINTS, create_cards_from_blueprints
from cardio.tui import tui


class Location(ABC):
    def __init__(
        self, base_seed: str, distance: int, index: int, paths: List[int]
    ) -> None:
        self.name = f"L{distance}_{index}"
        self.seed = f"L{distance}_{index}_{base_seed}"
        self.distance = distance  # Distance from start
        self.index = index  # Index position at current distance
        self.paths = paths  # Paths to next locations
        self.generate()

    @abstractmethod
    def generate(self) -> None:
        pass

    @abstractmethod
    def handle(self) -> bool:
        """Returns `True` if the game is is still on, `False` if game is over."""
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
        positions = [
            GridPos(line, slot) for line in (0, 1) for slot in range(self.grid.width)
        ]
        random.shuffle(positions)
        posncards = list(zip(positions, cards))
        self.computerstrategy = Round0OnlyStrategy(grid=self.grid, cards=posncards)

        # FIXME Use some other computer strategy later
        # FIXME Use distance to somehow increase difficulty as more distance is traveled
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
