import pytest
from cardio import Grid, Card


testcard = Card("X", 1, 1)


def test_init():
    g = Grid(width=2)
    assert g.lines == [[None, None], [None, None], [None, None]]
    assert g.width == 2


def test_is_empty():
    g = Grid()
    assert g.is_empty()


def test_access_grid():
    g = Grid(width=4)
    g[2][3] = testcard
    assert g[2][3] is testcard
    assert g.lines == [[None] * 4, [None] * 4, [None] * 3 + [testcard]]


def test_invalid_access_to_grid():
    g = Grid(width=2)
    with pytest.raises(IndexError):
        g[3][0]
    with pytest.raises(IndexError):
        g[1][2]
