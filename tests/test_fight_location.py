from cardio import Grid, GridPos
from cardio.location import FightLocation
from cardio.computer_strategies import Round0OnlyStrategy


def test_generate():
    l = FightLocation(0, 0, 0)
    assert isinstance(l.grid, Grid)
    assert isinstance(l.computerstrategy, Round0OnlyStrategy)
    assert [(loc, card.name) for loc, card in l.computerstrategy.cards] == [
        (GridPos(line=0, slot=1), "Lynx"),
        (GridPos(line=0, slot=0), "Hamster"),
        (GridPos(line=1, slot=0), "Porcupine"),
        (GridPos(line=1, slot=1), "Weasel"),
    ]

    # Try different seed:
    l = FightLocation(0, 10, 1)
    assert [(loc, card.name) for loc, card in l.computerstrategy.cards] == [
        (GridPos(line=0, slot=3), "Weasel"),
        (GridPos(line=1, slot=2), "Porcupine"),
    ]
