from cardio import GridPos, gg
from cardio.card import Card
from tests.utils.humanstrategyvnc import HumanStrategyVnC
from cardio.computer_strategies import Round0OnlyStrategy, PredefinedStrategy
from cardio.agent_damage_state import AgentDamageState
from cardio.blueprints import thecatalog

# TODO Clean up this file.


def equal_logs(generatedlog: str, targetlog: str) -> bool:
    are_equal = "".join(generatedlog.split()) == "".join(targetlog.split())
    if not are_equal:
        # Print the newly generated log for convenience if the logs don't match:
        print(f"\n\nGenerated Log:\n\n{generatedlog}\n\n")
    return are_equal


def test_simple_initial_setup(gg_setup):
    human, grid, vnc, ff = gg_setup
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
    assert equal_logs(vnc.stateslogger.log, target_states_log)


def test_fight_with_no_opponent(gg_setup):
    _, grid, vnc, ff = gg_setup
    hc = ff("HC", 1, 10, 1)
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            0: [
                (GridPos(2, 0), hc),  # type: ignore
            ],
        },
    )
    vnc.handle_fight()
    assert hc.health == 10
    assert vnc._has_human_won()


def test_fight_with_human_power_0(gg_setup):
    """Even though all human cards are powerless, the fight should still take place.
    (This used to be different in earlier versions of the fight logic.)
    """
    _, grid, vnc, ff = gg_setup
    cc = ff("CC", 2, 3, 1)
    hc = ff("HC", 0, 10, 1)
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(1, 0), cc),
                (GridPos(2, 0), hc),
            ],
        },
    )
    vnc.handle_fight()
    assert hc.health == 0
    assert cc.health == 3
    assert gg.humanplayer.lives == 0


def test_deadlock_due_to_all_0_power(gg_setup):
    """All cards with power == 0: should produce a deadlock leading to the computer
    winning.
    """
    _, grid, vnc, ff = gg_setup
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(1, 0), ff("CC", 0, 3, 1)),
                (GridPos(2, 0), ff("HC", 0, 3, 1)),
            ],
        },
    )
    vnc.handle_fight()
    assert gg.vnc._has_computer_won()
    assert gg.vnc.damagestate.is_deadlocked()


def test_deadlock_due_to_cards_not_opposing(gg_setup):
    """Cards have power > 0, but they don't oppose each other: should produce a
    deadlock, leading to the computer winning.
    """
    _, grid, vnc, ff = gg_setup
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(1, 0), ff("CC", 1, 0, 1)),
                (GridPos(2, 1), ff("HC", 1, 0, 1)),
            ],
        },
    )
    vnc.handle_fight()
    assert gg.vnc._has_computer_won()
    assert gg.vnc.damagestate.is_deadlocked()


def test_prepcard_will_not_attack(mocker, gg_setup):
    _, grid, vnc, ff = gg_setup
    prepcard = ff("P", 1, 1, 1)
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(0, 0), prepcard),
                (GridPos(1, 0), ff("X", 1, 1, 1)),
            ],
        },
    )
    spy = mocker.spy(prepcard, "attack")
    vnc.handle_fight()
    # Make sure `attack` was never called with prepcard:
    spy.assert_not_called()


def test_prepare_but_slot_taken(mocker, gg_setup):
    _, grid, vnc, ff = gg_setup
    grid[0][0] = pc = ff("P", 1, 1, 1)
    grid[1][0] = cc = ff("C", 1, 1, 1)
    spy = mocker.spy(vnc, "card_prepare")
    pc.prepare()
    assert grid[0][0] is pc
    assert grid[1][0] is cc
    spy.assert_not_called()


def test_prepare_with_success(mocker, gg_setup):
    _, grid, vnc, ff = gg_setup
    grid[0][0] = pc = ff("P", 1, 1, 1)
    spy = mocker.spy(vnc, "card_prepare")
    pc.prepare()
    assert grid[0][0] is None
    assert grid[1][0] is pc
    spy.assert_called_once()


def test_prepcard_gets_no_damage(gg_setup):
    _, grid, vnc, ff = gg_setup
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            # type: ignore
            0: [
                (GridPos(0, 0), ff("X", 1, 1, 1)),
                (GridPos(1, 0), ff("X", 1, 1, 1)),
                (GridPos(2, 0), ff("X", 10, 1, 1)),
            ],
        },
    )
    vnc.handle_fight()
    assert grid[1][0] is None
    assert grid[0][0].health == 1  # prepcard untouched


def test_human_gets_gems(gg_setup):
    human, grid, vnc, ff = gg_setup
    vnc.computerstrategy = PredefinedStrategy(
        grid=grid,
        cards_per_round={
            # type: ignore
            0: [(GridPos(1, 0), ff("Mouse", 1, 1, 1))],
            1: [(GridPos(2, 1), ff("Cat", 10, 1, 1))],
        },
    )
    vnc.handle_fight()
    assert human.gems == 4
    # (4 because:
    # - Round 0: mouse deals 1 agent damage
    # - Round 1: cat deals 10 agent damage
    # - This results in a diff of -9
    # -> computer dies with 9 - 5 overflow damage = 4 gems
    # Note that mouse and cat are in different slots, so mouse doesn't defend.)


def test_human_decks_managed_correctly(gg_setup):  # FIXME Should get different name?
    human, grid, _, _ = gg_setup
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

    vnc = HumanStrategyVnC(grid=grid, computerstrategy=cs)
    # Override damagestate with better health (the fight will end not because of high
    # enough damage diff but bc player H had no more unplayed cards with power > 0):
    vnc.damagestate = AgentDamageState(max_diff=50)
    gg.vnc = vnc
    vnc.handle_fight()

    assert len(human.deck.cards) == len(original_cards)
    assert human.lives == 0
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

Starting round 6:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1 Hp0h1
38 damage, 1 lives, 0 gems, 6 spirits

Starting round 7:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1 Hp0h1
45 damage, 1 lives, 0 gems, 7 spirits

Final state:
| -           | -           | -           | -           |
| Hp2h94      | Hp2h99      | Hp2h100     | Hp2h100     |
| -           | -           | -           | -           |
Hand: Hp0h1 Hp0h1 Hp0h1 Hp0h1
Used: Kp1h0 Wp1h0 Lp3h0 Hp0h0 Hp0h0 Pp1h0🚀 Hp0h0 Hp0h0
Draw:
Hamster: Hp0h1 Hp0h1
52 damage, 1 lives, 0 gems, 8 spirits
"""

    assert equal_logs(vnc.stateslogger.log, target_states_log)


def test_humanplayer_deck_gets_set_correctly_after_fight(gg_setup):
    human, grid, vnc, _ = gg_setup
    original_cards = thecatalog.find_by_names(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    ).instantiate()
    human.deck.cards = original_cards
    cs = Round0OnlyStrategy(grid=grid, cards=[])
    vnc = HumanStrategyVnC(grid=grid, computerstrategy=cs)
    vnc.handle_fight()
    assert sorted(c.name for c in human.deck.cards) == sorted(
        c.name for c in original_cards
    )


def test_card_humanity(gg_setup):
    """If `is_human` works more or less correctly. FIXME This is rather "hacky". Should
    be simplified and moved to `test_card` once there is some new logic for cards being
    human or not (using an explicit attribute) in place.
    """
    human, grid, vnc, _ = gg_setup

    original_cards = thecatalog.find_by_names(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    ).instantiate()
    assert not any(c.is_human() for c in original_cards)
    human.deck.cards = original_cards
    assert all(c.is_human() for c in original_cards)
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
    vnc = HumanStrategyVnC(grid=grid, computerstrategy=cs)
    vnc.handle_fight()
    assert all(c.is_human() for c in original_cards)
