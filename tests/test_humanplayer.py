from cardio import HumanPlayer, FightDecks, Card, session


def cards_names(hp: HumanPlayer) -> str:
    return "".join(c.name for c in hp.get_all_human_cards())


def test_get_all_human_cards():
    session.setup()

    # Just the human's cards:
    hp = HumanPlayer("X")
    assert hp.get_all_human_cards() == []
    hp.deck.add_card(Card("A", 1, 1, 1))
    assert cards_names(hp) == "A"

    # With grid:
    session.grid[2][0] = Card("B", 1, 1, 1)
    assert cards_names(hp) == "BA"

    # With fight decks:
    session.view.decks = FightDecks()
    session.view.decks.used.add_card(Card("C", 1, 1, 1))
    assert cards_names(hp) == "CBA"