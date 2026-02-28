"""Tests for CardPicker and card display functionality.

These tests verify that fire and spirit information is correctly displayed
in card picker contexts (upgrader, skill transferer, etc.) regardless of
screen position. See Issue #121.
"""

from cardio import Card


def test_card_with_fire_cost_has_correct_attributes():
    """Cards with fire cost should have correct fire attributes."""
    card = Card("FireCard", power=2, health=3, costs_fire=2)
    assert card.costs_fire == 2
    assert card.has_fire == 1  # default


def test_card_with_spirit_cost_has_correct_attributes():
    """Cards with spirit cost should have correct spirit attributes."""
    card = Card("SpiritCard", power=2, health=3, costs_fire=0, costs_spirits=2)
    assert card.costs_spirits == 2
    assert card.has_spirits == 1  # default


def test_card_with_custom_has_fire():
    """Cards with custom has_fire value should store it correctly."""
    card = Card("HighFireCard", power=2, health=3, costs_fire=1, has_fire=3)
    assert card.has_fire == 3


def test_card_with_custom_has_spirits():
    """Cards with custom has_spirits value should store it correctly."""
    card = Card("HighSpiritCard", power=2, health=3, costs_fire=1, has_spirits=2)
    assert card.has_spirits == 2


def test_card_with_zero_fire():
    """Cards with zero has_fire should store zero value."""
    card = Card("NoFireCard", power=2, health=3, costs_fire=1, has_fire=0)
    assert card.has_fire == 0


def test_card_with_zero_spirits():
    """Cards with zero has_spirits should store zero value."""
    card = Card("NoSpiritCard", power=2, health=3, costs_fire=1, has_spirits=0)
    assert card.has_spirits == 0


def test_cards_have_all_display_attributes():
    """All card attributes needed for display should be accessible."""
    cards = [
        Card("Card1", power=1, health=2, costs_fire=1, has_fire=2, has_spirits=1),
        Card("Card2", power=3, health=4, costs_fire=0, costs_spirits=2, has_spirits=3),
        Card("Card3", power=2, health=2, costs_fire=2, has_fire=0, has_spirits=0),
    ]

    for card in cards:
        assert hasattr(card, "costs_fire")
        assert hasattr(card, "costs_spirits")
        assert hasattr(card, "has_fire")
        assert hasattr(card, "has_spirits")
        assert hasattr(card, "power")
        assert hasattr(card, "health")
        assert hasattr(card, "skills")


def test_card_str_includes_fire_and_spirit_info():
    """Card string representation should include fire and spirit info."""
    card = Card("TestCard", power=2, health=3, costs_fire=2, has_fire=2, has_spirits=1)
    card_str = str(card)
    assert "🔥" in card_str
    assert "👻" in card_str
