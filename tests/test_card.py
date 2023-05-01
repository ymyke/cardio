import pytest
from cardio import Card, GridPos, gg, FightDecks, skills
from cardio.skills import SkillSet


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
    assert isinstance(c.skills, SkillSet)
    assert c.skills.count() == 0
    assert c.costs_spirits == 0
    assert c.has_spirits == 1
    assert c.has_fire == 1


def test_is_skilled():
    c = Card("X", 1, 2, 3)
    assert not c.is_skilled()
    c.skills.add(skills.Fertility)
    assert c.is_skilled()


def test_raw_potency():
    c = Card("X", 3, 2, 1)
    assert c.raw_potency == 11
    c.skills.add(skills.Fertility)
    assert c.raw_potency == 20
    c.skills.add(skills.Soaring)
    assert c.raw_potency == 22
    # Another one:
    c = Card("X", 1, 1, 10)
    assert c.raw_potency == -4
    # One with the costs bonus:
    c = Card("X", 0, 0, 0, costs_spirits=0, has_fire=0, has_spirits=0)
    assert c.raw_potency == 10  # <- 10 for the costs bonus


def test_potency(mocker):
    c = Card("X", 3, 2, 1)
    assert c.raw_potency == 11
    mocker.patch("cardio.card.Card.get_raw_potency_range", return_value=(0, 22))
    assert c.potency == 50


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
    damage_left = c.lose_health(3)
    assert damage_left == 0
    assert c.health == 7
    mocked_vnc.card_lost_health.assert_called_once()
    mocked_vnc.card_died.assert_not_called()


def test_lose_health_calculates_damage_left_correctly(common_setup):
    # With shield:
    c = Card("A", 1, 1, 1, skills=[skills.Shield])
    gg.grid[2][3] = c
    damage_left = c.lose_health(2)
    assert damage_left == 0  # 0 because the shield absorbed all the damage
    # Without shield:
    c = Card("A", 1, 1, 1)
    gg.grid[2][3] = c
    damage_left = c.lose_health(2)
    assert damage_left == 1  # 1 because the card only absorbed 1 of 2 damage


def test_lose_health_and_die(common_setup):
    mocked_vnc = common_setup
    c = gg.grid[2][3]
    damage_left = c.lose_health(100)
    assert damage_left == 99
    assert c.health == 0
    mocked_vnc.card_died.assert_called_once()
