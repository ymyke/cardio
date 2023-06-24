from cardio import Grid, GridPos
from cardio.locations.fight_location import FightLocation
from cardio.computer_strategies import Round0OnlyStrategy


def test_generate():
    l = FightLocation("0", 0, 0, [0])
    assert isinstance(l.grid, Grid)
    assert isinstance(l.computerstrategy, Round0OnlyStrategy)
    assert [(loc, card.name) for loc, card in l.computerstrategy.cards] == [
        (GridPos(line=0, slot=1), "Hammerling"),
        (GridPos(line=0, slot=2), "Shattershell"),
    ]

    # Try different seed and higher rung:
    l = FightLocation("2", 30, 1, [0])
    assert [(loc, card.name) for loc, card in l.computerstrategy.cards] == [
        (GridPos(line=0, slot=0), "Seedar"),
        (GridPos(line=1, slot=3), "Emberling"),
        (GridPos(line=1, slot=0), "Ghostowl"),
        (GridPos(line=0, slot=2), "Hoardling"),
    ]
