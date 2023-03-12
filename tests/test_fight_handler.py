import copy
from cardio import gg, Card, Deck, GridPos
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


def test_simple_initial_setup(session_setup):
    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    gg.humanplayer.deck.cards = copy.deepcopy(original_cards)
    gg.vnc.computerstrategy = Round0OnlyStrategy(
        grid=gg.grid,
        cards=[
            # type: ignore
            (GridPos(0, 1), Card("Steed", 2, 10, 1)),
            (GridPos(1, 0), Card("Dog", 2, 5, 1)),
            (GridPos(2, 0), Card("Cat", 1, 3, 1)),
        ],
    )
    gg.vnc.handle_fight()

    target_states_log = """\

Starting round 0:
| -           | -           | -           | -           |
| -           | -           | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
0 damage, 1 lives, 0 gems, 0 spirits

Starting round 1:
| -           | -           | -           | -           |
| Dp2h4       | Sp2h10      | -           | -           |
| Cp1h1       | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
2 damage, 1 lives, 0 gems, 0 spirits

Starting round 2:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used: Cp1h0
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
4 damage, 1 lives, 0 gems, 1 spirits

Final state:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used: Cp1h0
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
8 damage, 1 lives, 0 gems, 1 spirits
"""
    assert equal_logs(gg.vnc.stateslogger.log, target_states_log)


def test_human_gets_gems(session_setup):
    gg.vnc.computerstrategy = PredefinedStrategy(
        grid=gg.grid,
        cards_per_round={
            # type: ignore
            0: [(GridPos(1, 0), Card("Mouse", 1, 1, 1))],
            1: [(GridPos(2, 1), Card("Cat", 10, 1, 1))],
        },
    )
    gg.vnc.handle_fight()
    assert gg.humanplayer.gems == 4


def test_human_decks_managed_correctly(session_setup):  # FIXME Should get different name?
    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    gg.humanplayer.deck.cards = copy.deepcopy(original_cards)
    cs = Round0OnlyStrategy(
        grid=gg.grid,
        cards=[
            # type: ignore
            (GridPos(1, 0), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 1), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 2), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 3), Card("Hulk", 2, 100, 1)),
        ],
    )

    gg.vnc = HumanStrategyVnC(grid=gg.grid, computerstrategy=cs)
    # Override damagestate with better health:
    gg.vnc.damagestate = AgentDamageState(max_diff=50)

    gg.vnc.handle_fight()

    assert len(gg.humanplayer.deck.cards) == len(original_cards)
    assert gg.humanplayer.lives == 0
    target_states_log = """
Starting round 0:
| -           | -           | -           | -           |
| -           | -           | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
0 damage, 1 lives, 0 gems, 0 spirits

Starting round 1:
| -           | -           | -           | -           |
| Hp2h99      | Hp2h100     | Hp2h100     | Hp2h100     |
| Kp1h1       | -           | -           | -           |
Hand: Wp1h1 Lp3h2 Hp0h1 Hp0h1
Used:
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
6 damage, 1 lives, 0 gems, 0 spirits

Starting round 2:
| -           | -           | -           | -           |
| Hp2h98      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Lp3h2 Hp0h1 Hp0h1 Pp1h2🚀
Used: Kp1h0 Wp1h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
10 damage, 1 lives, 0 gems, 2 spirits

Starting round 3:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Pp1h2🚀 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
16 damage, 1 lives, 0 gems, 3 spirits

Starting round 4:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Pp1h2🚀 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
22 damage, 1 lives, 0 gems, 4 spirits

Starting round 5:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Pp1h2🚀 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
28 damage, 1 lives, 0 gems, 5 spirits

Final state:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1
34 damage, 1 lives, 0 gems, 6 spirits
"""

    assert equal_logs(gg.vnc.stateslogger.log, target_states_log)


def test_humanplayer_deck_gets_set_correctly_after_fight(session_setup):
    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    gg.humanplayer.deck.cards = copy.deepcopy(original_cards)
    cs = Round0OnlyStrategy(grid=gg.grid, cards=[])
    gg.vnc = HumanStrategyVnC(grid=gg.grid, computerstrategy=cs)
    gg.vnc.handle_fight()
    assert sorted(c.name for c in gg.humanplayer.deck.cards) == sorted(
        c.name for c in original_cards
    )


def test_card_humanity(session_setup):
    """If `is_human` works more or less correctly. FIXME This is rather "hacky". Should
    be simplified and moved to `test_card` once there is some new logic for cards being
    human or not (using an explicit attribute) in place.
    """
    original_cards = create_cards_from_blueprints(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    )
    assert not any(c.is_human() for c in original_cards)
    gg.humanplayer.deck.cards = original_cards
    assert all(c.is_human() for c in original_cards)
    cs = Round0OnlyStrategy(
        grid=gg.grid,
        cards=[
            # type: ignore
            (GridPos(1, 0), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 1), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 2), Card("Hulk", 2, 100, 1)),
            (GridPos(1, 3), Card("Hulk", 2, 100, 1)),
        ],
    )
    gg.vnc = HumanStrategyVnC(grid=gg.grid, computerstrategy=cs)
    gg.vnc.handle_fight()
    assert all(c.is_human() for c in original_cards)
