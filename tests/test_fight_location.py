from cardio import Grid
from cardio.locations.fight_location import FightLocation
from cardio.computer_strategies import SimpleRungBasedStrategy


def test_generate():
    l = FightLocation("0", 0, 0, [0])
    assert isinstance(l.grid, Grid)
    assert isinstance(l.computerstrategy, SimpleRungBasedStrategy)
