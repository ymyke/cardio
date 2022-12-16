grid = None
view = None
events = []

# QQ: Should this rather be Game instead of session? Or should there be a Game class?


def bootstrap(prefill: bool = False) -> None:

    from .grid import Grid
    from .gridview import SimpleView
    from .card import Card

    global grid
    global view

    grid = Grid(4)  # QQ: What if the grid size changes in the game?
    view = SimpleView(grid)

    if prefill:
        # Add some stuff:
        grid[0][1] = Card(name="Steed", initial_power=2, initial_health=10)
        grid[2][0] = Card(name="Cat", initial_power=1, initial_health=3)
        grid[1][0] = Card(name="Dog", initial_power=2, initial_health=5)
