"""Tests for both `PlacementManager` and `FightVnC._place_card`."""

import pytest
from cardio import Grid, Card, GridPos, session, Deck
from cardio.fightvnc import FightVnC
from cardio.placement_manager import PlacementManager
from cardio.tui.decks import Decks


# ----- PlacementManager tests -----


def test_placement_manager():
    g = Grid(width=4)
    g[2][0] = Card("X", 1, 1, 1)
    g[2][1] = Card("Y", 1, 1, 1)
    g[2][2] = Card("Z", 1, 1, 1)

    # Initial state:
    p = PlacementManager(g, 0, Card("T", 1, 1, 2))
    assert not p.is_marked(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 3))
    assert not p.ready_to_pick()
    assert not p.ready_to_place()

    # Mark a position:
    p.mark_unmark_or_pick(GridPos(2, 0))
    assert p.get_marked_positions() == [GridPos(2, 0)]
    assert not p.can_mark(GridPos(2, 0))
    assert not p.ready_to_pick()  # Need 2 fire, so not ready yet
    assert not p.ready_to_place()

    # Unmark that position:
    p.mark_unmark_or_pick(GridPos(2, 0))
    assert p.get_marked_positions() == []

    # Mark 2 positions:
    p.mark_unmark_or_pick(GridPos(2, 0))
    p.mark_unmark_or_pick(GridPos(2, 1))
    assert p.get_marked_positions() == [GridPos(2, 0), GridPos(2, 1)]
    assert p.ready_to_pick()  # Now ready to pick
    assert not p.ready_to_place()  # But not ready to place yet

    # Can no longer mark now:
    p.mark_unmark_or_pick(GridPos(2, 2))
    assert p.get_marked_positions() == [GridPos(2, 0), GridPos(2, 1)]
    assert p.ready_to_pick()
    assert not p.ready_to_place()

    # Pick:
    p.mark_unmark_or_pick(GridPos(2, 3))
    assert p.get_marked_positions() == [GridPos(2, 0), GridPos(2, 1)]
    assert p.ready_to_place()
    assert p.get_placement_position() == GridPos(2, 3)

    # Try to pick again:
    with pytest.raises(AssertionError):
        p.mark_unmark_or_pick(GridPos(2, 3))


def test_can_mark():
    g = Grid(width=4)
    g[2][0] = Card("X", 1, 1, 1)
    p = PlacementManager(g, 0, Card("T", 1, 1, 1))

    assert not p.can_mark(GridPos(1, 0))
    assert not p.can_mark(GridPos(0, 0))
    p.mark_pos(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 0))
    p.unmark_pos(GridPos(2, 0))

    p.target_card.costs_fire = 0
    assert not p.can_mark(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 1))

    p.target_card.costs_fire = 1
    assert not p.can_mark(GridPos(2, 1))
    assert p.can_mark(GridPos(2, 0))

    # Cannot mark a card wich has 0 fire:
    g.get_card(GridPos(2, 0)).has_fire = 0  # type:ignore
    assert not p.can_mark(GridPos(2, 0))

    p.target_card.costs_fire = 0
    p.target_card.costs_spirits = 1
    assert not p.can_mark(GridPos(2, 0))
    assert not p.can_mark(GridPos(2, 1))


def test_never_ready_without_marked_positions():
    p = PlacementManager(Grid(width=4), 0, Card("T", 1, 1, 0))
    assert not p.ready_to_place()


def test_is_placeable():
    g = Grid(width=4)
    g[2][0] = Card("X", 1, 1, 1)
    g[2][1] = Card("X", 1, 1, 1)
    g[2][2] = Card("X", 1, 1, 1)
    g[2][3] = Card("X", 1, 1, 1)
    p = PlacementManager(g, 0, Card("T", 1, 1, 1))
    # Fire:
    assert p.is_placeable()
    p.target_card.costs_fire = 0
    assert not p.is_placeable()
    g[2][3] = None
    assert p.is_placeable()
    p.target_card.costs_fire = 3
    assert p.is_placeable()
    p.target_card.costs_fire = 4
    assert not p.is_placeable()
    # Spirits:
    p.target_card.costs_fire = 0
    p.target_card.costs_spirits = 1
    assert not p.is_placeable()
    p.available_spirits = 1
    assert p.is_placeable()


# ----- FightVnC._place_card tests -----


def test_place_card_with_fire_sacrifice():
    target_card = Card("T", 1, 1, 1)
    target_pos = GridPos(2, 3)
    sacrifice_card = Card("S", 1, 1, 1)
    sacrifice_pos = GridPos(2, 0)

    g = Grid(width=4)
    g.set_card(sacrifice_pos, sacrifice_card)

    session.setup()
    session.grid = g

    p = PlacementManager(g, 0, target_card)
    p.marked_positions = {sacrifice_pos}
    p.placement_position = target_pos

    vnc = FightVnC(g)
    session.view = vnc
    vnc.decks = Decks(Deck(), Deck(), Deck([target_card]), Deck())
    vnc._place_card(p, 0)

    assert g.get_card(target_pos) == target_card
    assert g.get_card(sacrifice_pos) is None
    assert vnc.decks.handdeck.is_empty()
    assert vnc.decks.useddeck.cards == [sacrifice_card]


def test_place_card_with_spirits_sacrifice():
    target_card = Card("T", 1, 1, costs_fire=0, costs_spirits=3)
    target_pos = GridPos(2, 3)

    g = Grid(width=4)

    session.setup()
    session.grid = g

    p = PlacementManager(g, 0, target_card)
    p.placement_position = target_pos

    spirits_before = session.humanplayer.spirits
    vnc = FightVnC(g)
    vnc.decks = Decks(Deck(), Deck(), Deck([target_card]), Deck())
    vnc._place_card(p, 0)

    assert g.get_card(target_pos) == target_card
    assert vnc.decks.handdeck.is_empty()
    assert vnc.decks.useddeck.cards == []
    assert session.humanplayer.spirits == spirits_before - 3
