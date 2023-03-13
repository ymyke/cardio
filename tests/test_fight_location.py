from cardio import Grid
from cardio.location import FightLocation
from cardio.computer_strategies import Round0OnlyStrategy


def test_generate():
    l = FightLocation(0, 0)
    assert isinstance(l.grid, Grid)
    assert isinstance(l.computerstrategy, Round0OnlyStrategy)
    assert [c and c.name for _, c in l.computerstrategy.cards] == [
        "Hamster",
        "Lynx",
        None,
        None,
        None,
        "Porcupine",
        "Weasel",
        None,
    ]

    # Try different seed:
    l = FightLocation(1, 0)
    assert [c and c.name for _, c in l.computerstrategy.cards] == [
        None,
        "Hamster",
        None,
        None,
        None,
        None,
        "Weasel",
        None,
    ]
