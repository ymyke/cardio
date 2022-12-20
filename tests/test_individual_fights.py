from cardio import Card, Sigil, Agent, session, handlers


def do_the_fight(humancard: Card, computercard: Card) -> None:
    # FIXME Deactivate view? Refactor to a fixture in conftest?
    session.setup()
    session.view.non_blocking = True
    session.grid[1][0] = computercard
    session.grid[2][0] = humancard
    session.humanagent = Agent(name="Schnuzgi", health=5, initial_health=5, lives=1)
    session.computeragent = Agent(name="Leshy", health=5, initial_health=5, lives=1)
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


def test_vanilla_with_no_opponent():
    hc = Card(name="Human Card", initial_power=1, initial_health=10)
    do_the_fight(hc, None)
    assert hc.health == 10
    assert session.computeragent.lives == 0


def test_instant_death():
    hc = Card(
        name="Human Card",
        initial_power=1,
        initial_health=10,
        sigils=[Sigil.INSTANTDEATH],
    )
    cc = Card(name="Computer Card", initial_power=2, initial_health=3)
    do_the_fight(hc, cc)
    assert hc.health == 10
    assert cc.health == 0
    assert session.grid[1][0] is None


def test_soaring():
    hc = Card(
        name="Human Card",
        initial_power=1,
        initial_health=20,
        sigils=[Sigil.SOARING],
    )
    cc = Card(name="Computer Card", initial_power=2, initial_health=3)
    do_the_fight(hc, cc)
    assert hc.health == 10
    assert cc.health == 3
    assert session.grid[1][0] is cc
    assert session.computeragent.lives == 0


def test_soaring_vs_airdefense():
    hc = Card(
        name="Human Card",
        initial_power=1,
        initial_health=20,
        sigils=[Sigil.SOARING],
    )
    cc = Card(
        name="Computer Card",
        initial_power=2,
        initial_health=3,
        sigils=[Sigil.AIRDEFENSE],
    )
    do_the_fight(hc, cc)
    assert hc.health == 16
    assert cc.health == 0
    assert session.grid[1][0] is None
    assert session.computeragent.lives == 0


def test_soaring_and_instantdeath_vs_airdefense():
    hc = Card(
        name="Human Card",
        initial_power=1,
        initial_health=20,
        sigils=[Sigil.SOARING, Sigil.INSTANTDEATH],
    )
    cc = Card(
        name="Computer Card",
        initial_power=2,
        initial_health=3,
        sigils=[Sigil.AIRDEFENSE],
    )
    do_the_fight(hc, cc)
    assert hc.health == 20
    assert cc.health == 0
    assert session.grid[1][0] is None
    assert session.computeragent.lives == 0


def test_soaring_and_instantdeath_vs_no_airdefense():
    hc = Card(
        name="Human Card",
        initial_power=1,
        initial_health=20,
        sigils=[Sigil.SOARING, Sigil.INSTANTDEATH],
    )
    cc = Card(name="Computer Card", initial_power=2, initial_health=3)
    do_the_fight(hc, cc)
    assert hc.health == 10
    assert cc.health == 3
    assert session.grid[1][0] is cc
    assert session.computeragent.lives == 0
