import copy
from cardio import session, Card, Deck, GridPos
from cardio.humanstrategyvnc import HumanStrategyVnC
from cardio.agent_strategies import Turn0OnlyStrategy
from cardio.card_blueprints import create_cards_from_blueprints

# QQ: Could we use a special view that generates output that makes testing much easier?


def equal_logs(log1: str, log2: str) -> bool:
    return "".join(log1.split()) == "".join(log2.split())


def test_simple_initial_setup():
    cs = Turn0OnlyStrategy(
        [
            # type: ignore
            (GridPos(0, 1), Card(name="Steed", initial_power=2, initial_health=10)),
            (GridPos(1, 0), Card(name="Dog", initial_power=2, initial_health=5)),
            (GridPos(2, 0), Card(name="Cat", initial_power=1, initial_health=3)),
        ]
    )

    session.setup()
    session.view.handle_fight(computerstrategy=cs)

    target_states_log = """\
0:
| -           | -           | -           | -           |
| Dp2h4       | Sp2h10      | -           | -           |
| Cp1h1       | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

1:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

2:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
"""

    assert equal_logs(session.view.states_log, target_states_log)


def test_human_decks_managed_correctly():
    session.setup()

    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    session.humanagent.deck = Deck(copy.deepcopy(original_cards))

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

    session.view = HumanStrategyVnC(session.grid)
    session.view.handle_fight(computerstrategy=cs)

    assert len(session.humanagent.deck.cards) == len(original_cards)

    target_states_log = """
0:
| -           | -           | -           | -           |
| Hp2h99      | Hp2h100     | Hp2h100     | Hp2h100     |
| Kp1h1       | -           | -           | -           |
Hand: Wp1h1 Lp3h2 Hp0h1 Hp0h1
Used: Kp1h1
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

1:
| -           | -           | -           | -           |
| Hp2h98      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Lp3h2 Hp0h1 Hp0h1 Pp1h2🚀
Used: Kp1h0 Wp1h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

2:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Pp1h2🚀 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

3:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Pp1h2🚀 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

4:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Pp1h2🚀 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

5:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1

6:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1

7:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1

8:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1

9:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

10:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

11:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

12:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

13:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand:
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

14:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand:
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

15:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand:
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:

16:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand:
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0 Hp0h0
Draw:
Hamster:
"""

    assert equal_logs(session.view.states_log, target_states_log)
