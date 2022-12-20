from cardio import Card, Sigil, session, handlers

# @pytest.mark.parametrize(
#     "source, symbol",
#     [
#         ("coingecko", "ETH"),
#     ],
# )
# @pytest.mark.net
# def test_working_symbols_are_returned_by_search(source: str, symbol: str):


def test_vanilla_fight():
    # FIXME Deactivate view? Refactor to a fixture in conftest?

    attacker = Card(name="Attacker", initial_power=1, initial_health=10)
    target = Card(name="Target", initial_power=2, initial_health=3)
    session.setup()
    session.view.non_blocking = True
    session.grid[1][0] = target
    session.grid[2][0] = attacker
    handlers.play_game()
    assert attacker.power == 1
    assert attacker.health == 6
    assert session.computeragent.lives == 0
    assert session.grid[1][0] is None


def test_vanilla_with_power_0():
    pass
