from cardio import Card, Sigil, session, handlers


def do_the_fight(humancard: Card, computercard: Card) -> None:
    # FIXME Deactivate view? Refactor to a fixture in conftest?
    session.setup()
    session.view.non_blocking = True
    session.grid[1][0] = computercard
    session.grid[2][0] = humancard
    handlers.play_game()


def test_vanilla_fight():
    hc = Card(name="Human Card", initial_power=2, initial_health=10)
    cc = Card(name="Computer Card", initial_power=2, initial_health=3)
    do_the_fight(hc, cc)
    assert hc.power == 2
    assert hc.health == 8
    assert cc.power == 2
    assert cc.health == 0
    assert session.computeragent.lives == 0
    assert session.computeragent.health == session.computeragent.initial_health
    # FIXME Check overflow damage == -1
    assert session.grid[1][0] is None


def test_vanilla_with_power_0():
    hc = Card(name="Human Card", initial_power=0, initial_health=10)
    cc = Card(name="Computer Card", initial_power=2, initial_health=3)
    do_the_fight(hc, cc)
    assert hc.health == 0
    assert cc.health == 3
    assert session.humanagent.lives == 0
    assert session.grid[2][0] is None
