import logging
import copy
from cardio import session, Card, Deck, GridPos
from cardio.fightview import HumanStrategyVnC
from cardio.agent_strategies import Turn0OnlyStrategy
from cardio.card_blueprints import create_cards_from_blueprints
from .utils.fight_handler_data import (
    is_sublist,
    log_test_simple_initial_setup,
    log_test_human_decks_managed_correctly,
)

# QQ: Could we use a special view that generates output that makes testing much easier?


def test_simple_initial_setup(caplog):
    caplog.set_level(logging.DEBUG)
    session.setup()

    cs = Turn0OnlyStrategy(
        [
            # type: ignore
            (GridPos(0, 1), Card(name="Steed", initial_power=2, initial_health=10)),
            (GridPos(1, 0), Card(name="Dog", initial_power=2, initial_health=5)),
            (GridPos(2, 0), Card(name="Cat", initial_power=1, initial_health=3)),
        ]
    )
    session.view.handle_fight(computerstrategy=cs)

    targetgrid = [[None for _ in range(4)] for _ in range(3)]
    targetgrid[1][0] = Card(
        name="Dog", initial_power=2, initial_health=5, power=2, health=3
    )
    targetgrid[1][1] = Card(
        name="Steed", initial_power=2, initial_health=10, power=2, health=10
    )
    assert [[c for c in session.grid[linei]] for linei in range(3)] == targetgrid
    assert is_sublist(log_test_simple_initial_setup, caplog.text.split("\n"))


def test_human_decks_managed_correctly(caplog, mocker):
    caplog.set_level(logging.DEBUG)
    session.setup()

    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    session.humanagent.deck = Deck(copy.deepcopy(original_cards))

    mocker.patch("cardio.session.view")  # Deactivate the view to improve performance

    session.humanagent.health = 100
    cs = Turn0OnlyStrategy(
        [
            # type: ignore
            (GridPos(1, 0), Card(name="Hulk", initial_power=2, initial_health=100)),
            (GridPos(1, 1), Card(name="Hulk", initial_power=2, initial_health=100)),
            (GridPos(1, 2), Card(name="Hulk", initial_power=2, initial_health=100)),
            (GridPos(1, 3), Card(name="Hulk", initial_power=2, initial_health=100)),
        ]
    )
    mocker.patch("cardio.deck.Deck.shuffle")

    session.view = HumanStrategyVnC(session.grid)
    session.view.handle_fight(computerstrategy=cs)

    assert len(session.humanagent.deck.cards) == len(original_cards)
    assert is_sublist(log_test_human_decks_managed_correctly, caplog.text.split("\n"))
