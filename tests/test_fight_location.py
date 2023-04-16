from cardio import Grid, GridPos
from cardio.locations.location import FightLocation
from cardio.computer_strategies import Round0OnlyStrategy


def test_generate():
    l = FightLocation("0", 0, 0, [0])
    assert isinstance(l.grid, Grid)
    assert isinstance(l.computerstrategy, Round0OnlyStrategy)
    assert [(loc, card.name) for loc, card in l.computerstrategy.cards] == [
        (GridPos(line=0, slot=1), "Weasel"),
        (GridPos(line=0, slot=2), "Koala"),
    ]

    # Try different seed:
    l = FightLocation("0", 10, 1, [0])
    assert [(loc, card.name) for loc, card in l.computerstrategy.cards] == [
        (GridPos(line=1, slot=1), "Church Mouse"),
        (GridPos(line=0, slot=2), "Koala"),
    ]
