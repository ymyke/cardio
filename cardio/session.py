from typing import Optional
from .events import Event

grid = None
view = None
events = []


def add_event(event: Event) -> None:
    events.append(event)


def bootstrap(prefill: bool = False) -> None:

    from .grid import Grid
    from .gridview import SimpleView
    from .card import Card

    global grid
    global view

    grid = Grid(4)
    view = SimpleView(grid)

    if prefill:
        # Add some stuff:
        grid[0][1] = Card("Steed", 2, 10)
        grid[2][0] = Card("Cat", 1, 3)
        grid[1][0] = Card("Dog", 2, 5)
