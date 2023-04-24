import pytest
from cardio import Card, GridPos, gg, FightDecks, Skill


@pytest.fixture
def common_setup(mocker, gg_setup):
    gg.grid[0][3] = Card("Z", 1, 1, 1)
    gg.grid[1][3] = Card("Y", 1, 1, 1)
    gg.grid[2][3] = Card("X", 1, 1, 1)
    mocked_vnc = mocker.patch("cardio.card.gg.vnc")
    yield mocked_vnc


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


def test_is_skilled():
    c = Card("X", 1, 2, 3)
    assert not c.is_skilled()
    c.skills = [Skill.FERTILITY]


def test_potency():
    c = Card("X", 3, 2, 1)
    assert c.potency == 11
    c.skills = [Skill.FERTILITY]
    assert c.potency == 20
    c.skills.append(Skill.SOARING)
    assert c.potency == 22
    # Another one:
    c = Card("X", 1, 1, 10)
    assert c.potency == -4
    # One with the costs bonus:
    c = Card("X", 0, 0, 0, costs_spirits=0, has_fire=0, has_spirits=0)
    assert c.potency == 10  # <- 10 for the costs bonus


def test_init_with_both_fire_and_spirit_should_fail():
    with pytest.raises(AssertionError):
        Card("X", 1, 1, costs_fire=1, costs_spirits=1)


def test_reset():
    c = Card("X", 1, 2, 3)
    c.health = c.power = 0
    c.reset()
    assert c.power == 1
    assert c.health == 2


def test_clone():
    c = Card("X", 1, 2, 3)
    d = c.clone()
    assert not d.is_temporary
    assert c != d
    assert c is not d
    assert c.name == d.name
    assert c.power == d.power
    assert c.health == d.health
    assert c.costs_fire == d.costs_fire


def test_make_temp_copy():
    c = Card("X", 1, 2, 3)
    d = c.make_temp_copy()
    assert d.is_temporary
    assert c != d
    assert c is not d
    assert c.name == d.name
    assert c.power == d.power
    assert c.health == d.health
    assert c.costs_fire == d.costs_fire


def test_is_human(gg_setup):
    c = Card("A", 1, 1, 1)
    assert not c.is_human()
    gg.grid[2][2] = c
    assert c.is_human()
    gg.grid[2][2] = None
    assert not c.is_human()
    gg.vnc.decks = FightDecks()
    gg.vnc.decks.draw.add_card(c)
    assert c.is_human()
    gg.vnc.decks = FightDecks()
    assert not c.is_human()
    gg.humanplayer.deck.add_card(c)
    assert c.is_human()


def test_get_grid_pos(common_setup):
    assert gg.grid[2][3].get_grid_pos() == GridPos(2, 3)


def test_get_prep_card(common_setup):
    assert gg.grid[2][3].get_prep_card() == gg.grid[0][3]


def test_die(common_setup):
    mocked_vnc = common_setup
    spirits_before = gg.humanplayer.spirits
    c = gg.grid[2][3]
    assert c.health == 1
    c.die()
    assert c.health == 0
    assert gg.humanplayer.spirits == spirits_before + 1
    mocked_vnc.card_died.assert_called_once()
    assert gg.grid[2][3] is None


def test_no_spirits_when_computer_card_dies(common_setup):
    mocked_vnc = common_setup
    spirits_before = gg.humanplayer.spirits
    c = gg.grid[1][3]
    assert c.health == 1
    c.die()
    assert c.health == 0
    assert gg.humanplayer.spirits == spirits_before
    mocked_vnc.card_died.assert_called_once()
    assert gg.grid[1][3] is None


def test_sacrifice(common_setup):
    mocked_vnc = common_setup
    spirits_before = gg.humanplayer.spirits
    c = gg.grid[2][3]
    assert c.health == 1
    c.sacrifice()
    assert c.health == 0
    assert gg.humanplayer.spirits == spirits_before + 1
    mocked_vnc.card_died.assert_not_called()
    assert gg.grid[2][3] is None


def test_lose_health(common_setup):
    mocked_vnc = common_setup
    c = gg.grid[2][3]
    c.health = 10
    actual_loss = c.lose_health(3)
    assert actual_loss == 3
    assert c.health == 7
    mocked_vnc.card_lost_health.assert_called_once()
    mocked_vnc.card_died.assert_not_called()


def test_lose_health_and_die(common_setup):
    mocked_vnc = common_setup
    c = gg.grid[2][3]
    actual_loss = c.lose_health(100)
    assert actual_loss == 1
    assert c.health == 0
    mocked_vnc.card_died.assert_called_once()


def test_get_attacked_targeting_humancard(common_setup):
    mocked_vnc = common_setup
    target = gg.grid[2][3]
    attacker = Card("A", 10, 1, 1)
    target.get_attacked(attacker)
    assert target.health == 0
    assert gg.grid[0][3].health == 1  # No overflow to prepline!
    mocked_vnc.card_getting_attacked.assert_called_once()


def test_get_attacked_targeting_computercard(common_setup):
    mocked_vnc = common_setup
    target = gg.grid[1][3]
    prepcard = gg.grid[0][3]
    attacker = Card("A", 10, 1, 1)
    target.get_attacked(attacker)
    assert target.health == 0
    assert prepcard.health == 0  # Overflow damage to prepline!
    assert gg.grid[0][3] is None  # Leading to that spot being empty
    mocked_vnc.card_getting_attacked.assert_called_once()


# Note that `attack` is not being tested here bc there are relevant tests for that
# method in `test_individual_fights` -- LIXME: Should at some point have a clearer
# concept as to which fight-logic-related tests are here and which are there.


def test_activate_with_opposing_card(common_setup):
    """If it deals damage to the opposing card."""
    mocked_vnc = common_setup
    target = gg.grid[2][3]
    gg.grid[1][3].activate()
    assert target.health == 0
    assert gg.grid[2][3] == None
    mocked_vnc.card_activate.assert_called_once()
    mocked_vnc.pos_card_deactivate.assert_called_once()
    mocked_vnc.handle_player_damage.assert_not_called()


def test_activate_without_opposing_card(gg_setup):
    """If it deals damage to the human player."""
    # (We're not using `common_setup` here bc we need to test the `damagestate` (which
    # would be "mocked away") later on.)
    gg.grid[1][3] = Card("Y", 1, 1, 1)
    gg.grid[1][3].activate()
    assert gg.grid[2][3] == None
    assert gg.vnc.damagestate.diff == 1


def test_prepare_preconditions(common_setup):
    with pytest.raises(AssertionError):
        # Not in prep line:
        gg.grid[1][3].prepare()
    with pytest.raises(AssertionError):
        # Not in prep line:
        gg.grid[2][3].prepare()
    with pytest.raises(AssertionError):
        # Not on grid at all:
        Card("X", 1, 1, 1).prepare()


def test_prepare_but_slot_taken(common_setup):
    mocked_vnc = common_setup
    gg.grid[0][3].prepare()
    mocked_vnc.card_prepare.assert_not_called()
    assert gg.grid[0][3] is not None


def test_prepare_with_success(common_setup):
    mocked_vnc = common_setup
    gg.grid[1][3] = None
    gg.grid[0][3].prepare()
    mocked_vnc.card_prepare.assert_called_once()
    assert gg.grid[0][3] is None
