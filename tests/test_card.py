import pytest
from cardio import Card, skills
from cardio.skills import SkillSet


def test_init():
    c = Card("X", 1, 2, 3)
    # explicit init:
    assert c.power == 1
    assert c.health == 2
    assert c.costs_fire == 3
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


def test_potency():
    c = Card("X", 3, 2, 1)
    assert c.potency("human") == 11
    assert c.potency("computer") == 10
    c.skills.add(skills.Fertility)
    assert c.potency("human") == 20
    assert c.potency("computer") == 10
    c.skills.add(skills.Soaring)
    assert c.potency("human") == 22
    assert c.potency("computer") == 12
    # Another one:
    c = Card("X", 1, 1, 10)
    assert c.potency("human") == -4
    assert c.potency("computer") == 4
    # One with the costs bonus:
    c = Card("X", 0, 0, 0, costs_spirits=0, has_fire=0, has_spirits=0)
    assert c.potency("human") == 10  # <- 10 for the costs bonus
    assert c.potency("computer") == 0


def test_init_with_both_fire_and_spirit_should_fail():
    with pytest.raises(AssertionError):
        Card("X", 1, 1, costs_fire=1, costs_spirits=1)


def test_copy():
    c = Card("X", 1, 2, 3)
    d = c.copy()
    assert c is not d
    assert c.name == d.name
    assert c.power == d.power
    assert c.health == d.health
    assert c.costs_fire == d.costs_fire


def test_is_gameplay_equal():
    c = Card("X", 1, 2, 3)
    d = Card("X", 1, 2, 3)
    assert c.is_gameplay_equal(d)
    d.name = "Y"
    assert c.is_gameplay_equal(d)
    d.power = 2
    assert not c.is_gameplay_equal(d)
