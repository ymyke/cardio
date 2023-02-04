import pytest
from cardio import Card, GridPos, session


@pytest.fixture
def common_setup(mocker) -> object:
    session.setup()
    session.grid[0][3] = Card("Z", 1, 1, 1)
    session.grid[1][3] = Card("Y", 1, 1, 1)
    session.grid[2][3] = Card("X", 1, 1, 1)
    mocked_view = mocker.patch("cardio.card.session.view")
    return mocked_view


def test_init():
    c = Card("X", 1, 2, 3)
    # explicit init:
    assert c.initial_power == 1
    assert c.initial_health == 2
    assert c.costs_fire == 3
    # post_init:
    assert c.power == 1
    assert c.health == 2
    # defaults:
    assert c.skills == []
    assert c.costs_spirits == 0
    assert c.has_spirits == 1
    assert c.has_fire == 1


def test_init_with_both_fire_and_spirit_should_fail():
    with pytest.raises(AssertionError):
        Card("X", 1, 1, costs_fire=1, costs_spirits=1)


def test_reset():
    c = Card("X", 1, 2, 3)
    c.health = c.power = 0
    c.reset()
    assert c.power == 1
    assert c.health == 2


def test_duplicate():
    c = Card("X", 1, 2, 3)
    d = c.duplicate()
    assert c == d
    assert c is not d


def test_get_grid_pos(common_setup):
    assert session.grid[2][3].get_grid_pos() == GridPos(2, 3)


def test_get_prep_card(common_setup):
    assert session.grid[2][3].get_prep_card() == session.grid[0][3]


def test_die(common_setup):
    mocked_view = common_setup
    c = session.grid[2][3]
    assert c.health == 1
    c.die()
    assert c.health == 0
    mocked_view.card_died.assert_called_once()


def test_lose_health(common_setup):
    mocked_view = common_setup
    c = session.grid[2][3]
    c.health = 10
    actual_loss = c.lose_health(3)
    assert actual_loss == 3
    assert c.health == 7
    mocked_view.card_lost_health.assert_called_once()
    mocked_view.card_died.assert_not_called()


def test_lose_health_and_die(common_setup):
    mocked_view = common_setup
    c = session.grid[2][3]
    actual_loss = c.lose_health(100)
    assert actual_loss == 1
    assert c.health == 0
    mocked_view.card_died.assert_called_once()


def test_get_attacked_targeting_humancard(common_setup):
    mocked_view = common_setup
    target = session.grid[2][3]
    attacker = Card("A", 10, 1, 1)
    target.get_attacked(attacker)
    assert target.health == 0
    assert session.grid[0][3].health == 1  # No overflow to prepline!
    mocked_view.card_getting_attacked.assert_called_once()


def test_get_attacked_targeting_computercard(common_setup):
    mocked_view = common_setup
    target = session.grid[1][3]
    prepcard = session.grid[0][3]
    attacker = Card("A", 10, 1, 1)
    target.get_attacked(attacker)
    assert target.health == 0
    assert prepcard.health == 0  # Overflow damage to prepline!
    assert session.grid[0][3] is None  # Leading to that spot being empty
    mocked_view.card_getting_attacked.assert_called_once()


# Note that `attack` is not being tested here bc there are relevant tests for that
# method in `test_individual_fights` -- LIXME: Should at some point have a clearer
# concept as to which fight-logic-related tests are here and which are there.


def test_activate_with_opposing_card(common_setup):
    """If it deals damage to the opposing card."""
    mocked_view = common_setup
    target = session.grid[2][3]
    session.grid[1][3].activate()
    assert target.health == 0
    assert session.grid[2][3] == None
    mocked_view.card_activate.assert_called_once()
    mocked_view.pos_card_deactivate.assert_called_once()
    mocked_view.handle_player_damage.assert_not_called()


def test_activate_without_opposing_card():
    """If it deals damage to the human player."""
    # (We're not using `common_setup` here bc we need to test the `damagestate` (which
    # would be "mocked away") later on.)
    session.setup()
    session.grid[1][3] = Card("Y", 1, 1, 1)
    session.grid[1][3].activate()
    assert session.grid[2][3] == None
    assert session.view.damagestate.diff == 1


def test_prepare_preconditions(common_setup):
    with pytest.raises(AssertionError):
        # Not in prep line:
        session.grid[1][3].prepare()
    with pytest.raises(AssertionError):
        # Not in prep line:
        session.grid[2][3].prepare()
    with pytest.raises(AssertionError):
        # Not on grid at all:
        Card("X", 1, 1, 1).prepare()


def test_prepare_but_slot_taken(common_setup):
    mocked_view = common_setup
    session.grid[0][3].prepare()
    mocked_view.card_prepare.assert_not_called()
    assert session.grid[0][3] is not None


def test_prepare_with_success(common_setup):
    mocked_view = common_setup
    session.grid[1][3] = None
    session.grid[0][3].prepare()
    mocked_view.card_prepare.assert_called_once()
    assert session.grid[0][3] is None
