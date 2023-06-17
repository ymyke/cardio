from cardio import GridPos
from cardio.card import Card
from tests.utils.humanstrategyvnc import HumanStrategyVnC
from cardio.computer_strategies import Round0OnlyStrategy
from cardio.agent_damage_state import AgentDamageState
from cardio.blueprints import thecatalog


def equal_logs(generatedlog: str, targetlog: str) -> bool:
    are_equal = "".join(generatedlog.split()) == "".join(targetlog.split())
    if not are_equal:
        # Print the newly generated log for convenience if the logs don't match:
        print(f"\n\nGenerated Log:\n\n{generatedlog}\n\n")
    return are_equal


def test_concrete_fight_1(tt_setup):
    human, grid, vnc, ff = tt_setup
    human.deck.cards = thecatalog.find_by_names(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    ).instantiate()
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[
            # type: ignore
            (GridPos(0, 1), ff("Steed", 2, 10, 1)),
            (GridPos(1, 0), ff("Dog", 2, 5, 1)),
            (GridPos(2, 0), ff("Cat", 1, 3, 1)),
        ],
    )
    vnc.handle_fight()

    target_states_log = """\

Starting round 0:
| -           | -           | -           | -           |
| -           | -           | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
0 damage, 2 lives, 0 gems, 3 spirits

Starting round 1:
| -           | -           | -           | -           |
| Dp2h4       | Sp2h10      | -           | -           |
| Cp1h1       | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
2 damage, 2 lives, 0 gems, 3 spirits

Final state:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used: Cp1h0
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
5 damage, 2 lives, 0 gems, 4 spirits
"""
    assert equal_logs(vnc.stateslogger.log, target_states_log)


def test_concrete_fight_2(tt_setup):
    human, grid, vnc, ff = tt_setup
    original_cards = thecatalog.find_by_names(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    ).instantiate()
    human.deck.cards = original_cards
    cs = Round0OnlyStrategy(
        grid=grid,
        cards=[
            # type: ignore
            (GridPos(1, 0), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 1), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 2), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 3), Card("Hulk", 2, 100, 1)),
        ],
    )

    vnc = HumanStrategyVnC(grid=grid, computerstrategy=cs, humanplayer=human)
    vnc.damagestate = AgentDamageState(max_diff=50)
    vnc.handle_fight()

    assert len(human.deck.cards) == len(original_cards)
    assert human.lives == 1
    target_states_log = """
Starting round 0:
| -           | -           | -           | -           |
| -           | -           | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
0 damage, 2 lives, 0 gems, 3 spirits

Starting round 1:
| -           | -           | -           | -           |
| Hp2h99      | Hp2h100     | Hp2h100     | Hp2h100     |
| Kp1h1       | -           | -           | -           |
Hand: Wp1h1 Lp3h2 Hp0h1 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
6 damage, 2 lives, 0 gems, 3 spirits

Starting round 2:
| -           | -           | -           | -           |
| Hp2h98      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Lp3h2 Hp0h1 Hp0h1 Pp1h2🚀
Used: Kp1h0 Wp1h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
12 damage, 2 lives, 0 gems, 5 spirits

Starting round 3:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Pp1h2🚀 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
18 damage, 2 lives, 0 gems, 6 spirits

Starting round 4:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Pp1h2🚀 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
25 damage, 2 lives, 0 gems, 7 spirits

Starting round 5:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Pp1h2🚀 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
32 damage, 2 lives, 0 gems, 8 spirits

Starting round 6:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1
38 damage, 2 lives, 0 gems, 9 spirits

Starting round 7:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1
45 damage, 2 lives, 0 gems, 10 spirits

Final state:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1
52 damage, 2 lives, 0 gems, 11 spirits
"""

    assert equal_logs(vnc.stateslogger.log, target_states_log)
