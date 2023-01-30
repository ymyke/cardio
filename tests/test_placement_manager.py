from cardio import Grid, Card, GridPos
from cardio.tui.placement_manager import PlacementManager


def test_placement_manager():
    g = Grid(width=4)
    g[2][0] = Card("X", 1, 1, 1)
    g[2][1] = Card("Y", 1, 1, 1)

    p = PlacementManager(g, Card("T", 1, 1, 1))
    assert not p.is_marked(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 2))
    assert p.can_mark(GridPos(2, 0))
    p.mark_pos(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 0))
    assert p.get_all_pos() == [GridPos(2, 0)]
    p.unmark_pos(GridPos(2, 0))
    assert p.get_all_pos() == []
    assert not p.ready_to_place()
    p.mark_pos(GridPos(2, 1))
    p.mark_pos(GridPos(2, 0))
    assert len(p.get_all_pos()) == 2
    assert p.get_last_pos() == GridPos(2, 0)
    assert p.ready_to_place()
    p.unmark_pos(GridPos(2, 0))
    assert p.get_last_pos() == GridPos(2, 1)
    assert p.ready_to_place()
    p.mark_pos(GridPos(2, 0))
    p.do_place()
    assert g.get_card(GridPos(2, 0)).name == "T"  # type: ignore
    assert g.get_card(GridPos(2, 1)) is None


def test_can_mark():
    g = Grid(width=4)
    g[2][0] = Card("X", 1, 1, 1)
    p = PlacementManager(g, Card("T", 1, 1, 1))

    assert not p.can_mark(GridPos(1, 0))
    assert not p.can_mark(GridPos(0, 0))
    p.mark_pos(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 0))
    p.unmark_pos(GridPos(2, 0))

    p.target_card.costs_fire = 0
    assert not p.can_mark(GridPos(2, 0))
    assert p.can_mark(GridPos(2, 1))

    p.target_card.costs_fire = 1
    assert not p.can_mark(GridPos(2, 1))
    assert p.can_mark(GridPos(2, 0))
    g.get_card(GridPos(2, 0)).has_fire = 0  # type:ignore
    assert not p.can_mark(GridPos(2, 0))


def test_never_ready_without_marked_positions():
    p = PlacementManager(Grid(width=4), Card("T", 1, 1, 0))
    assert not p.ready_to_place()
