import random
from typing import Protocol, Type
from cardio import Grid, GridPos
from cardio.computer_strategies import ComputerStrategy, Round0OnlyStrategy
from cardio.human_player import HumanPlayer
from .location import Location
from .baseview import BaseLocationView
from cardio.blueprints import thecatalog, BlueprintList


class FightView(BaseLocationView, Protocol):
    def __init__(
        self,
        computerstrategy: ComputerStrategy,
        grid: Grid,
        humanplayer: HumanPlayer,
        debug: bool = False,
        *args,
        **kwargs
    ) -> None:
        ...

    def handle_fight(self) -> None:
        ...


class FightLocation(Location):
    marker = "FFF"
    grid: Grid
    computerstrategy: ComputerStrategy

    def generate(self) -> None:
        super().generate()
        self.grid = Grid(4)
        nofcards = random.randint(1, 4)
        max_potency = max(self.rung // 3, 5)
        blueprint_candidates = thecatalog.find_by_potency(
            -100, max_potency, which="computer"
        )
        blueprints = random.choices(blueprint_candidates, k=nofcards)
        # FIXME ^ This random choice should maybe have bias for higher potency
        cards = BlueprintList(blueprints).instantiate()
        positions = [
            GridPos(line, slot) for line in (0, 1) for slot in range(self.grid.width)
        ]
        random.shuffle(positions)
        posncards = list(zip(positions, cards))
        self.computerstrategy = Round0OnlyStrategy(grid=self.grid, cards=posncards)

        # FIXME Use some other computer strategy later
        # FIXME Use rung to somehow increase difficulty as more distance is traveled
        # (e.g., more cards every x steps)

    def handle(self, view_class: Type[FightView], humanplayer: HumanPlayer) -> bool:
        vnc = view_class(
            computerstrategy=self.computerstrategy,
            grid=self.grid,
            humanplayer=humanplayer,
            debug=False,
            description="FIGHT!",
        )
        vnc.handle_fight()
        vnc.close()
        return humanplayer.lives > 0
