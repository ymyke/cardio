import pytest
from cardio import Card, gg, FightDecks, skills
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
    assert c.potency == 11
    assert c.core_potency == 10
    c.skills.add(skills.Fertility)
    assert c.potency == 20
    assert c.core_potency == 19
    c.skills.add(skills.Soaring)
    assert c.potency == 22
    assert c.core_potency == 21
    # Another one:
    c = Card("X", 1, 1, 10)
    assert c.potency == -4
    assert c.core_potency == 4
    # One with the costs bonus:
    c = Card("X", 0, 0, 0, costs_spirits=0, has_fire=0, has_spirits=0)
    assert c.potency == 10  # <- 10 for the costs bonus
    assert c.core_potency == 0


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


def test_is_human(gg_setup):
    c = Card("A", 1, 1, 1)
    assert not c.is_human()
    gg.humanplayer.deck.add_card(c)
    assert c.is_human()


def test_is_gameplay_equal():
    c = Card("X", 1, 2, 3)
    d = Card("X", 1, 2, 3)
    assert c.is_gameplay_equal(d)
    d.name = "Y"
    assert c.is_gameplay_equal(d)
    d.power = 2
    assert not c.is_gameplay_equal(d)
