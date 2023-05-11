import pytest
from cardio import Card, FightCard, Grid, GridPos, gg
from cardio import skills as sk

# TODO Use ff here?

@pytest.fixture
def common_setup(mocker, gg_setup):
    grid = Grid(4)
    gg.grid = grid
    # ^ We do this so `is_human` will work correctly. Might become obsolete with a
    # different implementation of `is_human`. Then, `gg_setup` might become obsolete
    # here too. QQ
    c = Card("X", 1, 2, 3)
    mocked_vnc = mocker.patch("cardio.card.gg.vnc")
    fc = FightCard.from_card(c, mocked_vnc, grid)
    grid[0][3] = FightCard.__new__(FightCard)
    grid[1][3] = FightCard.__new__(FightCard)
    grid[2][3] = fc
    yield c, fc, grid, mocked_vnc


def test_from_to_card(common_setup):
    c, fc, *_ = common_setup
    assert isinstance(fc, FightCard)
    assert fc.to_card() is c
    assert fc.name == "X"
    assert fc.power == 1
    assert fc.health == 2
    assert fc.costs_fire == 3


def test_fightcard_leaves_original_untouched(common_setup):
    c, fc, *_ = common_setup
    fc.name = "New"
    fc.power = 10
    fc.health = 0
    x = fc.to_card()
    del fc
    assert x is c
    assert x.name == "X"
    assert x.power == 1
    assert x.health == 2
    assert x.costs_fire == 3


def test_fightcard_simple_method_access(common_setup):
    _, fc, *_ = common_setup
    assert not fc.is_skilled()


def test_copy(common_setup):
    c, fc, *_ = common_setup
    fc2 = fc.copy()
    assert fc2 is not fc
    assert isinstance(fc2, FightCard)
    assert fc2.name == "X"
    assert fc2.vnc is fc.vnc
    assert fc2.grid is fc.grid
    assert fc2.to_card() is c


def test_get_grid_pos(common_setup):
    _, fc, *_ = common_setup
    assert fc.get_grid_pos() == GridPos(2, 3)


def test_get_prep_card(common_setup):
    _, fc, grid, _ = common_setup
    assert fc.get_prep_card() == grid[0][3]


def test_die(common_setup):
    _, fc, grid, mocked_vnc = common_setup
    spirits_before = gg.humanplayer.spirits
    assert fc.health == 2
    fc.die()
    assert fc.health == 0
    assert gg.humanplayer.spirits == spirits_before + 1
    mocked_vnc.card_died.assert_called_once()
    assert grid[2][3] is None


def test_no_spirits_when_computer_card_dies(common_setup):
    _, fc, grid, mocked_vnc = common_setup
    spirits_before = gg.humanplayer.spirits
    grid[1][3], grid[2][3] = fc, grid[1][3]  # Swap cards
    assert fc.health == 2
    fc.die()
    assert fc.health == 0
    assert gg.humanplayer.spirits == spirits_before
    mocked_vnc.card_died.assert_called_once()
    assert grid[1][3] is None


def test_sacrifice(common_setup):
    _, fc, grid, mocked_vnc = common_setup
    spirits_before = gg.humanplayer.spirits
    assert fc.health == 2
    has_fire = fc.sacrifice()
    assert has_fire == 1
    assert fc.health == 0
    assert gg.humanplayer.spirits == spirits_before  # sacrificing must not give spirits
    mocked_vnc.card_died.assert_not_called()
    assert grid[2][3] is None


def test_take_damage(common_setup):
    _, fc, _, mocked_vnc = common_setup
    fc.health = 10
    damage_left = fc.take_damage(3)
    assert damage_left == 0
    assert fc.health == 7
    mocked_vnc.card_lost_health.assert_called_once()
    mocked_vnc.card_died.assert_not_called()


def test_take_damage_calculates_damage_left_correctly(common_setup):
    _, fc, grid, _ = common_setup
    # With shield:
    fc.health = 1
    fc2 = fc.copy()
    fc.skills.add(sk.Shield)
    damage_left = fc.take_damage(2)
    assert damage_left == 0  # Shield and card absorbed all damage
    # Without shield:
    grid[2][3] = fc2
    damage_left = fc2.take_damage(2)
    assert damage_left == 1  # The card only absorbed 1 of 2 damage


def test_take_damage_and_die(common_setup):
    _, fc, _, mocked_vnc = common_setup
    damage_left = fc.take_damage(100)
    assert damage_left == 98
    assert fc.health == 0
    mocked_vnc.card_died.assert_called_once()


# TODO Add tests for prepare and attack?
