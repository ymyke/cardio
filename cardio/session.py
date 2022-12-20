import os

grid = None
view = None
humanagent = None
computeragent = None
events = []

# QQ: Should this rather be Game instead of session? Or should there be a Game class?


def setup(prefill: bool = False) -> None:

    os.system("cls")

    from .grid import Grid
    from .gridview import SimpleView
    from .card import Card
    from .agent import Agent
    from .sigils import Sigil

    global grid, view, humanagent, computeragent

    grid = Grid(4)  # QQ: What if the grid size changes in the game?
    view = SimpleView(grid)

    if prefill:
        # Add some stuff:
        grid[0][1] = Card(name="Steed", initial_power=2, initial_health=10)
        grid[2][0] = Card(
            name="Cat",
            initial_power=1,
            initial_health=3,
            sigils=[Sigil.INSTANTDEATH, Sigil.SOARING],
        )
        grid[1][0] = Card(name="Dog", initial_power=2, initial_health=5)

    humanagent = Agent(name="Schnuzgi", health=5, initial_health=5, lives=1)
    computeragent = Agent(name="Leshy", health=5, initial_health=5, lives=1)
