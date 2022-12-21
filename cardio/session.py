import os

grid = None
view = None
humanagent = None
computeragent = None
events = []

# QQ: Should this rather be Game instead of session? Or should there be a Game class?


def setup() -> None:
    from . import Grid, SimpleView, Agent

    global grid, view, humanagent, computeragent
    grid = Grid(4)  # QQ: What if the grid size changes in the game?
    view = SimpleView(grid)
    humanagent = Agent(name="Schnuzgi", health=5, initial_health=5, lives=1)
    computeragent = Agent(name="Yshl", health=5, initial_health=5, lives=1)
    os.system("cls")
