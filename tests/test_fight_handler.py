from cardio import GridPos
from cardio.grid import GridPosAndCard
from tests.utils.humanstrategyvnc import HumanStrategyVnC
from cardio.computer_strategies import Round0OnlyStrategy
from cardio.blueprints import thecatalog


def test_fight_with_no_opponent(tt_setup):
    human, grid, vnc, ff = tt_setup
    hc = ff("HC", 1, 10, 1)
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid, cards=[GridPosAndCard(GridPos(2, 0), hc)]
    )
    vnc.handle_fight()
    assert hc.health == 10
    assert vnc.damagestate.who_won() == "human"


def test_fight_with_human_power_0(tt_setup):
    """Even though all human cards are powerless, the fight should still take place.
    (This used to be different in earlier versions of the fight logic.)
    """
    human, grid, vnc, ff = tt_setup
    cc = ff("CC", 2, 3, 1)
    hc = ff("HC", 0, 10, 1)
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[GridPosAndCard(GridPos(1, 0), cc), GridPosAndCard(GridPos(2, 0), hc)],
    )
    vnc.handle_fight()
    assert hc.health == 0
    assert cc.health == 3
    assert human.lives == 1


def test_deadlock_due_to_all_0_power(tt_setup):
    """All cards with power == 0: should produce a deadlock leading to the computer
    winning.
    """
    human, grid, vnc, ff = tt_setup
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[
            GridPosAndCard(GridPos(1, 0), ff("CC", 0, 3, 1)),
            GridPosAndCard(GridPos(2, 0), ff("HC", 0, 3, 1)),
        ],
    )
    vnc.handle_fight()
    assert vnc.damagestate.who_won() == "computer"
    assert vnc.damagestate.is_deadlocked()


def test_deadlock_due_to_cards_not_opposing(tt_setup):
    """Cards have power > 0, but they don't oppose each other: should produce a
    deadlock, leading to the computer winning.
    """
    human, grid, vnc, ff = tt_setup
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[
            GridPosAndCard(GridPos(1, 0), ff("CC", 1, 0, 1)),
            GridPosAndCard(GridPos(2, 1), ff("HC", 1, 0, 1)),
        ],
    )
    vnc.handle_fight()
    assert vnc.damagestate.who_won() == "computer"
    assert vnc.damagestate.is_deadlocked()


def test_prepcard_will_not_attack(mocker, tt_setup):
    human, grid, vnc, ff = tt_setup
    prepcard = ff("P", 1, 1, 1)
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[
            GridPosAndCard(GridPos(0, 0), prepcard),
            GridPosAndCard(GridPos(1, 0), ff("X", 1, 1, 1)),
        ],
    )
    spy = mocker.spy(prepcard, "attack")
    vnc.handle_fight()
    # Make sure `attack` was never called with prepcard:
    spy.assert_not_called()


def test_prepare_but_slot_taken(mocker, tt_setup):
    human, grid, vnc, ff = tt_setup
    grid[0][0] = pc = ff("P", 1, 1, 1)
    grid[1][0] = cc = ff("C", 1, 1, 1)
    spy = mocker.spy(vnc, "show_card_prepare")
    pc.prepare()
    assert grid[0][0] is pc
    assert grid[1][0] is cc
    spy.assert_not_called()


def test_prepare_with_success(mocker, tt_setup):
    human, grid, vnc, ff = tt_setup
    grid[0][0] = pc = ff("P", 1, 1, 1)
    spy = mocker.spy(vnc, "show_card_prepare")
    pc.prepare()
    assert grid[0][0] is None
    assert grid[1][0] is pc
    spy.assert_called_once()


def test_prepcard_gets_no_damage(tt_setup):
    human, grid, vnc, ff = tt_setup
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[
            GridPosAndCard(GridPos(0, 0), ff("X", 1, 1, 1)),
            GridPosAndCard(GridPos(1, 0), ff("X", 1, 1, 1)),
            GridPosAndCard(GridPos(2, 0), ff("X", 10, 1, 1)),
        ],
    )
    vnc.handle_fight()
    assert grid[1][0] is None
    assert grid[0][0].health == 1  # prepcard untouched


def test_human_gets_gems(tt_setup):
    human, grid, vnc, ff = tt_setup
    vnc.computerstrategy = Round0OnlyStrategy(
        grid=grid,
        cards=[GridPosAndCard(GridPos(2, 1), ff("Cat", 10, 1, 1))],
    )
    vnc.handle_fight()
    assert human.gems == 5


def test_humanplayer_deck_gets_set_correctly_after_fight(tt_setup):
    human, grid, vnc, ff = tt_setup
    original_cards = thecatalog.find_by_names(
        ["Koala", "Weasel", "Lynx", "Porcupine"]
    ).instantiate()
    human.deck.cards = original_cards
    cs = Round0OnlyStrategy(grid=grid, cards=[])
    vnc = HumanStrategyVnC(grid=grid, computerstrategy=cs, humanplayer=human)
    vnc.handle_fight()
    assert sorted(c.name for c in human.deck.cards) == sorted(
        c.name for c in original_cards
    )
