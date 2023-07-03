from cardio import GridPos, GridPosAndCard
from cardio.computer_strategies import (
    PredefinedStrategy,
    Round0OnlyStrategy,
    SimpleRungBasedStrategy,
)

# ----- Waitlist mechanism -----


def test_waitlist_cards_get_played(tt_setup):
    _, grid, _, ff = tt_setup
    cards_per_round = {
        0: [GridPosAndCard(GridPos(0, 0), ff("0", 1, 1, 1))],
        1: [GridPosAndCard(GridPos(0, 0), ff("1", 1, 1, 1))],
    }
    s = PredefinedStrategy(grid=grid, cards_per_round=cards_per_round)
    s.play_cards(0)
    assert s._waitlist == []
    assert grid.get_card(GridPos(0, 0)).name == "0"
    s.play_cards(1)
    assert s._waitlist == cards_per_round[1]
    assert grid.get_card(GridPos(0, 0)).name == "0"
    grid.clear_position(GridPos(0, 0))
    s.play_cards(200)  # No card here anymore, but waitlist should be played
    assert s._waitlist == []
    assert grid.get_card(GridPos(0, 0)).name == "1"


def test_waitlist_cards_get_played_first(tt_setup):
    _, grid, _, ff = tt_setup
    cards_per_round = {
        0: [GridPosAndCard(GridPos(0, 0), ff("0", 1, 1, 1))],
        1: [GridPosAndCard(GridPos(0, 0), ff("1", 1, 1, 1))],
        2: [GridPosAndCard(GridPos(0, 0), ff("2", 1, 1, 1))],
    }
    s = PredefinedStrategy(grid=grid, cards_per_round=cards_per_round)
    s.play_cards(0)
    assert s._waitlist == []
    s.play_cards(1)
    assert s._waitlist == cards_per_round[1]
    s.play_cards(2)
    assert s._waitlist == cards_per_round[1] + cards_per_round[2]
    grid.clear_position(GridPos(0, 0))
    s.play_cards(200)
    assert s._waitlist == cards_per_round[2]
    assert grid.get_card(GridPos(0, 0)).name == "1"
    grid.clear_position(GridPos(0, 0))
    s.play_cards(999)
    assert s._waitlist == []
    assert grid.get_card(GridPos(0, 0)).name == "2"


def test_waitlist_adds_same_card_only_once(tt_setup):
    _, grid, _, ff = tt_setup
    cards_per_round = {
        0: [GridPosAndCard(GridPos(0, 0), ff("0", 1, 1, 1))],
        1: [GridPosAndCard(GridPos(0, 0), ff("1", 1, 1, 1))],
    }
    s = PredefinedStrategy(grid=grid, cards_per_round=cards_per_round)
    s.play_cards(0)
    assert s._waitlist == []
    for i in range(1, 100):
        s.play_cards(i)
        assert s._waitlist == cards_per_round[1]


# ----- Concrete strategies -----


def test_predefined_strategy(tt_setup):
    _, grid, _, ff = tt_setup
    cards_per_round = {
        0: [GridPosAndCard(GridPos(0, 0), ff("0", 1, 1, 1))],
        1: [GridPosAndCard(GridPos(0, 1), ff("1", 1, 1, 1))],
        2: [
            GridPosAndCard(GridPos(0, 2), ff("2", 1, 1, 1)),
            GridPosAndCard(GridPos(0, 3), ff("3", 1, 1, 1)),
        ],
    }
    s = PredefinedStrategy(grid=grid, cards_per_round=cards_per_round)

    # Test cards_to_be_played:
    for i in [0, 1, 2]:
        assert s.cards_to_be_played(i) == cards_per_round[i]
    for i in range(3, 100):
        assert s.cards_to_be_played(i) == []

    # Test play_cards:
    for i in [0, 1]:
        s.play_cards(i)
        assert grid.get_card(cards_per_round[i][0].pos) == cards_per_round[i][0].card
    s.play_cards(2)
    for card in cards_per_round[2]:
        assert grid.get_card(card.pos) == card.card
    oldgrid = str(grid)
    for i in range(3, 100):
        s.play_cards(i)
    assert str(grid) == oldgrid


def test_round0only_strategy(tt_setup):
    _, grid, _, ff = tt_setup
    cards = [
        GridPosAndCard(GridPos(0, 0), ff("0", 1, 1, 1)),
        GridPosAndCard(GridPos(0, 1), ff("1", 1, 1, 1)),
    ]
    s = Round0OnlyStrategy(grid=grid, cards=cards)

    # Test cards_to_be_played:
    assert s.cards_to_be_played(0) == cards
    for i in range(1, 100):
        assert s.cards_to_be_played(i) == []

    # Test play_cards:
    s.play_cards(0)
    for card in cards:
        assert grid.get_card(card.pos) == card.card
    oldgrid = str(grid)
    for i in range(1, 100):
        s.play_cards(i)
    assert str(grid) == oldgrid


def test_rungbased_strategy(tt_setup):
    _, grid, _, ff = tt_setup
    for rung in range(0, 1000, 10):
        s = SimpleRungBasedStrategy(grid=grid, rung=rung)
        lengths = [len(s.cards_to_be_played(round)) for round in range(100)]
        assert lengths[0] <= 2 * grid.width
        assert all(l <= grid.width for l in lengths[1:])
        assert sum(lengths) > 0 and sum(lengths) <= s.nofcards
        s.play_cards(rung)

