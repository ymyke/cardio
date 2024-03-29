"""Test `Deck` class"""

import pytest
from cardio import Deck, Card, CardList


def create_some_cards() -> CardList:
    return [Card(name, 1, 1, 1) for name in ("A", "B", "C", "D")]


def test_init_without_cardlist():
    d = Deck("n")
    assert isinstance(d, Deck)
    assert d.cards == []
    assert d.name == "n"


def test_init_with_cardlist():
    d = Deck("n", create_some_cards())
    assert isinstance(d, Deck)
    assert [c.name for c in d.cards] == ["A", "B", "C", "D"]


@pytest.mark.disable_never_shuffle
def test_shuffle():
    manycards = [Card(str(i), 1, 1, 1) for i in range(1, 1000)]
    d = Deck("n", manycards.copy())
    assert d.cards == manycards
    d.shuffle()
    assert d.cards != manycards


def test_add_card():
    d = Deck("n", create_some_cards())
    d.add_card(Card("X", 1, 1, 1))
    assert len(d.cards) == 5
    assert d.cards[-1].name == "X"


def test_remove_card():
    d = Deck("n", create_some_cards())
    assert [c.name for c in d.cards] == ["A", "B", "C", "D"]
    d.remove_card(d.cards[1])
    assert [c.name for c in d.cards] == ["A", "C", "D"]


def test_draw_cards():
    d = Deck("n", create_some_cards())
    # Draw some:
    drawncards = d.draw_cards(2)
    assert [c.name for c in drawncards] == ["A", "B"]
    assert [c.name for c in d.cards] == ["C", "D"]
    # Draw more than remain:
    drawncards = d.draw_cards(10)
    assert [c.name for c in drawncards] == ["C", "D"]
    assert d.cards == []
    # Draw more:
    assert d.draw_cards(1) == []


def test_draw_card():
    d = Deck("n", create_some_cards())
    drawncard = d.draw_card()
    assert drawncard.name == "A"
    assert [c.name for c in d.cards] == ["B", "C", "D"]


def test_pick_card():
    d = Deck("n", create_some_cards())
    picked = d.pick_card(2)
    assert picked.name == "C"
    assert [c.name for c in d.cards] == ["A", "B", "D"]


def test_pick_card_out_of_index():
    d = Deck("n")
    with pytest.raises(AssertionError):
        d.pick_card(0)
