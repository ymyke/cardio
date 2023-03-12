import pytest
from cardio import Grid, Card, GridPos


def get_test_grid() -> Grid:
    g = Grid(width=4)
    g[2][3] = Card("X", 1, 1, 1)
    g[1][3] = Card("Y", 1, 1, 1)
    g[2][2] = Card("Z", 1, 1, 1)
    return g


def test_init():
    g = Grid(width=2)
    assert g.lines == [[None, None], [None, None], [None, None]]
    assert g.width == 2


def test_is_empty():
    g = Grid()
    assert g.is_empty()


def test_access_grid():
    g = Grid(width=4)
    testcard = Card("X", 1, 1, 1)
    # Direct access:
    g[2][3] = testcard
    assert g[2][3] is testcard
    assert g.lines == [[None] * 4, [None] * 4, [None] * 3 + [testcard]]
    # Access via set_card and get_card:
    assert g.get_card(GridPos(2, 3)) is testcard
    g.set_card(GridPos(0, 0), testcard)
    assert g[0][0] is testcard


def test_invalid_access_to_grid():
    g = Grid(width=2)
    with pytest.raises(IndexError):
        g[3][0]
    with pytest.raises(IndexError):
        g[1][2]


def test_find_card():
    g = get_test_grid()
    pos = g.find_card(g[2][3])
    assert pos == GridPos(2, 3)


def test_find_nongrid_card():
    assert get_test_grid().find_card(Card("X", 1, 1, 1)) is None


def test_get_opposing_card():
    g = get_test_grid()
    c = g[2][3]
    assert g.get_opposing_card(g.get_opposing_card(c)) is c


def test_get_nongrid_opposing_card():
    g = get_test_grid()
    assert g.get_opposing_card(g[2][2]) is None


def test_remove_card():
    g = get_test_grid()
    g.remove_card(g[2][2])
    assert g[2][2] is None


def test_move_card():
    g = get_test_grid()
    c = g[2][2]
    g.move_card(c, GridPos(0, 1))
    assert g[0][1] is c
    assert g[2][2] is None


def test_activate_line(mocker):
    spy = mocker.patch("cardio.card.Card.activate")
    g = get_test_grid()
    g.activate_line(1)
    assert spy.call_count == 1
    g.activate_line(2)
    assert spy.call_count == 3


def test_prepare_line(mocker):
    spy = mocker.patch("cardio.card.Card.prepare")
    g = get_test_grid()
    g[0][0] = Card("X", 1, 1, 1)
    g.prepare_line()
    assert spy.call_count == 1
