import copy
from cardio import session, Card, Deck, GridPos
from cardio.humanstrategyvnc import HumanStrategyVnC
from cardio.computer_strategies import Round0OnlyStrategy, PredefinedStrategy
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.agent_damage_state import AgentDamageState


def equal_logs(generatedlog: str, targetlog: str) -> bool:
    are_equal = "".join(generatedlog.split()) == "".join(targetlog.split())
    if not are_equal:
        # Print the newly generated log for convenience if the logs don't match:
        print(f"\n\nGenerated Log:\n\n{generatedlog}\n\n")
    return are_equal


def test_simple_initial_setup():
    session.setup()
    cs = Round0OnlyStrategy(
        grid=session.grid,
        cards=[
            # type: ignore
            (GridPos(0, 1), Card(name="Steed", initial_power=2, initial_health=10)),
            (GridPos(1, 0), Card(name="Dog", initial_power=2, initial_health=5)),
            (GridPos(2, 0), Card(name="Cat", initial_power=1, initial_health=3)),
        ],
    )
    session.view.handle_fight(computerstrategy=cs)

    target_states_log = """\

Starting round 0:
| -           | -           | -           | -           |
| -           | -           | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 1:
| -           | -           | -           | -           |
| Dp2h4       | Sp2h10      | -           | -           |
| Cp1h1       | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 2:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Final state:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
"""
    assert equal_logs(session.view.stateslogger.log, target_states_log)


def test_human_gets_gems():
    session.setup()
    cs = PredefinedStrategy(
        grid=session.grid,
        cards_per_round={
            # type: ignore
            0: [(GridPos(1, 0), Card(name="Mouse", initial_power=1, initial_health=1))],
            1: [(GridPos(2, 1), Card(name="Cat", initial_power=10, initial_health=1))],
        },
    )
    session.view.handle_fight(computerstrategy=cs)
    assert session.humanplayer.gems == 4


def test_human_decks_managed_correctly():  # FIXME Should get different name?
    session.setup()

    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    session.humanplayer.deck = Deck(copy.deepcopy(original_cards))
    cs = Round0OnlyStrategy(
        grid=session.grid,
        cards=[
            # type: ignore
            (GridPos(1, 0), Card(name="Hulk", initial_power=2, initial_health=100)),
            (GridPos(1, 1), Card(name="Hulk", initial_power=2, initial_health=100)),
            (GridPos(1, 2), Card(name="Hulk", initial_power=2, initial_health=100)),
            (GridPos(1, 3), Card(name="Hulk", initial_power=2, initial_health=100)),
        ],
    )

    session.view = HumanStrategyVnC(session.grid)
    # Override damagestate with better health:
    session.view.damagestate = AgentDamageState(max_diff=50)

    session.view.handle_fight(computerstrategy=cs)

    assert len(session.humanplayer.deck.cards) == len(original_cards)
    assert session.humanplayer.lives == 0
    target_states_log = """
Starting round 0:
| -           | -           | -           | -           |
| -           | -           | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 1:
| -           | -           | -           | -           |
| Hp2h99      | Hp2h100     | Hp2h100     | Hp2h100     |
| Kp1h1       | -           | -           | -           |
Hand: Wp1h1 Lp3h2 Hp0h1 Hp0h1
Used: Kp1h1
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 2:
| -           | -           | -           | -           |
| Hp2h98      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Lp3h2 Hp0h1 Hp0h1 Pp1h2🚀
Used: Kp1h0 Wp1h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 3:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Pp1h2🚀 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 4:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Pp1h2🚀 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Starting round 5:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Pp1h2🚀 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1

Final state:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1
"""

    assert equal_logs(session.view.stateslogger.log, target_states_log)
