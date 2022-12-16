import cardio.session as session
from cardio.card import Card
from cardio.grid import Grid
import cardio.events as events
import cardio.commands as commands
import cardio.handlers as handlers


def setup_grid(grid: Grid) -> None:
    grid[0][1] = Card(name="Steed", initial_power=2, initial_health=10)
    grid[2][0] = Card(name="Cat", initial_power=1, initial_health=3)
    grid[1][0] = Card(name="Dog", initial_power=2, initial_health=5)


def test_the_game():
    session.bootstrap()
    targetgrid = [[None for _ in range(4)] for _ in range(3)]

    targetgrid[0][1] = Card(
        name="Steed", initial_power=2, initial_health=10, power=2, health=10
    )
    targetgrid[1][0] = Card(
        name="Dog", initial_power=2, initial_health=5, power=2, health=3
    )

    setup_grid(session.grid)
    handlers.handle_turn(commands.HandleTurn())
    handlers.handle_turn(commands.HandleTurn())

    assert [[c for c in session.grid[row]] for row in range(3)] == targetgrid
    assert [type(e) for e in session.events] == [events.CardGetsAttacked] * 4 + [
        events.CardDies
    ]
    assert [getattr(e, "damage", None) for e in session.events] == [1, 2, 1, 1, None]
