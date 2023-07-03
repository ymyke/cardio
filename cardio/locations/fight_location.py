from typing import Protocol, Type
from cardio import Grid
from cardio.computer_strategies import ComputerStrategy, SimpleRungBasedStrategy
from cardio.human_player import HumanPlayer
from .location import Location
from .baseview import BaseLocationView


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
        self.computerstrategy = SimpleRungBasedStrategy(grid=self.grid, rung=self.rung)

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
