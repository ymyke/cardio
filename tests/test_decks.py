"""Test `Decks` class"""

from cardio import FightDecks, Deck, Card


def test_init_empty_decks():
    d = FightDecks()
    assert isinstance(d.draw, Deck)
    assert isinstance(d.hamster, Deck)
    assert isinstance(d.hand, Deck)
    assert isinstance(d.used, Deck)
    assert d.get_all_cards() == []


def test_init_non_empty_decks():
    d = FightDecks()
    d.hand.add_card(Card("A", 1, 1, 1))
    d.used.add_card(Card("B", 1, 1, 1))
    d.draw.add_card(Card("C", 1, 1, 1))
    d.hamster.add_card(Card("D", 1, 1, 1))
    assert isinstance(d.draw, Deck)
    assert isinstance(d.hamster, Deck)
    assert isinstance(d.hand, Deck)
    assert isinstance(d.used, Deck)
    assert [c.name for c in d.get_all_cards()] == ["A", "B", "C", "D"]
