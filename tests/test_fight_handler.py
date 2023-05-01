import copy
import pytest
from cardio import gg, Card, Deck, GridPos
from cardio.humanstrategyvnc import HumanStrategyVnC
from cardio.computer_strategies import Round0OnlyStrategy, PredefinedStrategy
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.agent_damage_state import AgentDamageState
from cardio import attack


def equal_logs(generatedlog: str, targetlog: str) -> bool:
    are_equal = "".join(generatedlog.split()) == "".join(targetlog.split())
    if not are_equal:
        # Print the newly generated log for convenience if the logs don't match:
        print(f"\n\nGenerated Log:\n\n{generatedlog}\n\n")
    return are_equal


def test_simple_initial_setup(gg_setup):
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

Final state:
| -           | -           | -           | -           |
| Dp2h3       | Sp2h10      | -           | -           |
| -           | -           | -           | -           |
Hand: Kp1h3 Wp1h1 Lp3h2 Hp0h1
Used: Cp1h0
Draw: Pp1h2🚀
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
5 damage, 1 lives, 0 gems, 1 spirits
"""
    assert equal_logs(gg.vnc.stateslogger.log, target_states_log)


@pytest.mark.skip(reason="Will produce an endless loop")
def test_endless_loop(gg_setup):
    gg.vnc.computerstrategy = PredefinedStrategy(
        grid=gg.grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(1, 0), Card("X", 1, 0, 1)),
                (GridPos(2, 1), Card("X", 1, 0, 1)),
            ],
        },
    )
    gg.vnc.handle_fight()


def test_prepcard_will_not_attack(mocker, gg_setup):
    gg.vnc.computerstrategy = PredefinedStrategy(
        grid=gg.grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(0, 0), Card("P", 1, 1, 1)),
                (GridPos(1, 0), Card("X", 1, 1, 1)),
            ],
        },
    )
    attack_spy = mocker.spy(attack, "attack")
    gg.vnc.handle_fight()
    # Make sure `attack` was never called with prepcard:
    assert not any(x.kwargs["attacker"].name == "P" for x in attack_spy.call_args_list)


def test_prepare_but_slot_taken(mocker, gg_setup):
    pc = Card("P", 1, 1, 1)
    cc = Card("C", 1, 1, 1)
    gg.grid[0][0] = pc
    gg.grid[1][0] = cc
    mocked_vnc = mocker.patch("cardio.attack.gg.vnc")
    attack.prepare(pc)
    assert gg.grid[0][0] is pc
    assert gg.grid[1][0] is cc
    mocked_vnc.card_prepare.assert_not_called()


def test_prepare_with_success(mocker, gg_setup):
    pc = Card("P", 1, 1, 1)
    gg.grid[0][0] = pc
    mocked_vnc = mocker.patch("cardio.attack.gg.vnc")
    attack.prepare(pc)
    assert gg.grid[0][0] is None
    assert gg.grid[1][0] is pc
    mocked_vnc.card_prepare.assert_called_once()


def test_prepcard_gets_no_damage(gg_setup):
    gg.vnc.computerstrategy = PredefinedStrategy(
        grid=gg.grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(0, 0), Card("X", 1, 1, 1)),
                (GridPos(1, 0), Card("X", 1, 1, 1)),
                (GridPos(2, 0), Card("X", 10, 1, 1)),
            ],
        },
    )
    gg.vnc.handle_fight()
    assert gg.grid[1][0] is None
    assert gg.grid[0][0].health == 1  # prepcard untouched


def test_human_gets_gems(gg_setup):
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
    # (4 because:
    # - Round 0: mouse deals 1 agent damage
    # - Round 1: cat deals 10 agent damage
    # - This results in a diff of -9
    # -> computer dies with 9 - 5 overflow damage = 4 gems
    # Note that mouse and cat are in different slots, so mouse doesn't defend.)


def test_human_decks_managed_correctly(gg_setup):  # FIXME Should get different name?
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
    # Override damagestate with better health (the fight will end not because of high
    # enough damage diff but bc player H had no more unplayed cards with power > 0):
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
12 damage, 1 lives, 0 gems, 2 spirits

Starting round 3:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Pp1h2🚀 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
18 damage, 1 lives, 0 gems, 3 spirits

Starting round 4:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Pp1h2🚀 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
25 damage, 1 lives, 0 gems, 4 spirits

Starting round 5:
| -           | -           | -           | -           |
| Hp2h95      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Pp1h2🚀 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1 Hp0h1
32 damage, 1 lives, 0 gems, 5 spirits

Final state:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1
38 damage, 1 lives, 0 gems, 6 spirits
"""

    assert equal_logs(gg.vnc.stateslogger.log, target_states_log)


def test_humanplayer_deck_gets_set_correctly_after_fight(gg_setup):
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


def test_card_humanity(gg_setup):
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
