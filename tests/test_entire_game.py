import logging
import cardio.session as session
from cardio.card import Card
import cardio.handlers as handlers
from cardio.agent_strategies import Turn0OnlyStrategy

# QQ: Could we use a special view that generates output that makes testing much easier?


def test_the_game(caplog):
    caplog.set_level(logging.DEBUG)
    session.setup()
    session.view.non_blocking = True

    cs = Turn0OnlyStrategy(
        [
            ((0, 1), Card(name="Steed", initial_power=2, initial_health=10)),
            ((1, 0), Card(name="Dog", initial_power=2, initial_health=5)),
            ((2, 0), Card(name="Cat", initial_power=1, initial_health=3)),
        ]
    )
    handlers.handle_fight(computerstrategy=cs)

    targetgrid = [[None for _ in range(4)] for _ in range(3)]
    targetgrid[1][0] = Card(
        name="Dog", initial_power=2, initial_health=5, power=2, health=3
    )
    targetgrid[1][1] = Card(
        name="Steed", initial_power=2, initial_health=10, power=2, health=10
    )
    assert [[c for c in session.grid[linei]] for linei in range(3)] == targetgrid

    for logentry in [
        "Cat becomes active",
        "Cat attacks Dog",
        "Dog gets attacked by Cat",
        "Dog new health: 4",
        "Dog becomes active",
        "Dog attacks Cat",
        "Cat gets attacked by Dog",
        "Cat new health: 1",
        "Preparing Steed, moving to computer line",
        "Steed becomes active",
        "Player Schnuzgi loses 2 health, new health 3",
        "Cat becomes active",
        "Cat attacks Dog",
        "Dog gets attacked by Cat",
        "Dog new health: 3",
        "Dog becomes active",
        "Dog attacks Cat",
        "Cat gets attacked by Dog",
        "Cat dies.",
        "Removed card from [2, 0]",
        "Steed becomes active",
        "Player Schnuzgi loses 2 health, new health 1",
        "Dog becomes active",
        "Player Schnuzgi loses 2 health, new health -1",
        "Steed becomes active",
        "Player Schnuzgi loses 2 health, new health -3",
        "Player Schnuzgi loses 1 life, 0 life/lives left, 3 overflow damage",
    ]:
        assert logentry in caplog.text
