import random
from typing import Protocol, Type
from cardio import Grid, GridPos, gg
from cardio.card_blueprints import _BLUEPRINTS, create_cards_from_blueprints
from cardio.computer_strategies import ComputerStrategy, Round0OnlyStrategy
from .location import Location
from .baseview import BaseLocationView


class FightView(BaseLocationView, Protocol):
    def __init__(
        self, computerstrategy: ComputerStrategy, grid: Grid, debug=True
    ) -> None:
        ...

    def handle_fight(self) -> None:
        ...

    def _has_human_won(self) -> bool:
        # FIXME Make this method non-private
        ...


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

    def handle(self, view_class: Type[FightView]) -> bool:
        vnc = view_class(
            computerstrategy=self.computerstrategy, grid=self.grid, debug=True
        )
        gg.vnc = vnc  # Stick information into the globals
        gg.grid = self.grid
        vnc.handle_fight()
        vnc.close()
        return vnc._has_human_won()