"""Test `Decks` class"""

from cardio import Decks, Deck, Card


def test_init_empty_decks():
    d = Decks(Deck(), Deck(), Deck(), Deck())
    assert isinstance(d.draw, Deck)
    assert isinstance(d.hamster, Deck)
    assert isinstance(d.hand, Deck)
    assert isinstance(d.used, Deck)
    assert d.get_all_cards() == []


def test_init_non_empty_decks():
    d = Decks(
        Deck([Card("A", 1, 1, 1)]),
        Deck([Card("B", 1, 1, 1)]),
        Deck([Card("C", 1, 1, 1)]),
        Deck([Card("D", 1, 1, 1)]),
    )
    assert isinstance(d.draw, Deck)
    assert isinstance(d.hamster, Deck)
    assert isinstance(d.hand, Deck)
    assert isinstance(d.used, Deck)
    assert [c.name for c in d.get_all_cards()] == ["A", "B", "C", "D"]
