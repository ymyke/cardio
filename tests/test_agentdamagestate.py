from cardio.agent_damage_state import (
    AgentDamageState,
    DEADLOCK_ROUNDS_TO_START,
    DEADLOCK_ROUNDS_TO_RESOLVE,
    DAMAGE_DIFF_TO_WIN,
)


def test_init():
    ads = AgentDamageState()
    assert ads.diff == 0
    assert ads.max_diff == DAMAGE_DIFF_TO_WIN
    assert ads.history == {}


def test_damage_computer():
    ads = AgentDamageState()
    ads.damage_computer(2)
    assert ads.diff == -2
    assert not ads.has_computer_won()
    assert not ads.has_human_won()
    ads.damage_computer(4)
    assert ads.diff == -6
    assert not ads.has_computer_won()
    assert ads.has_human_won()
    assert ads.get_overflow() == 1


def test_damage_human():
    ads = AgentDamageState()
    ads.damage_human(3)
    assert ads.diff == 3
    assert not ads.has_human_won()
    assert not ads.has_computer_won()
    ads.damage_human(8)
    assert ads.diff == 11
    assert not ads.has_human_won()
    assert ads.has_computer_won()
    assert ads.get_overflow() == 6


def test_add_to_history():
    ads = AgentDamageState()
    ads.add_to_history(1)
    assert ads.history == {1: 0}
    ads.add_to_history(1)  # Same again, should change nothing
    assert ads.history == {1: 0}
    ads.add_to_history(2)
    assert ads.history == {1: 0, 2: 0}
    ads.damage_computer(2)
    ads.add_to_history(3)
    assert ads.history == {1: 0, 2: 0, 3: -2}
    ads.add_to_history(4)
    assert ads.history == {1: 0, 2: 0, 3: -2, 4: -2}


def test_is_in_deadlock_risk():
    ads = AgentDamageState()
    assert not ads.is_in_deadlock_risk()
    ads.history = {1: 0, 2: 0, 3: 0, 4: 0}
    assert not ads.is_in_deadlock_risk()
    ads.add_to_history(5)
    assert ads.is_in_deadlock_risk()
    ads.diff = -1
    ads.add_to_history(6)
    assert not ads.is_in_deadlock_risk()
    for i in range(DEADLOCK_ROUNDS_TO_START):
        ads.add_to_history(7 + i)
    assert ads.is_in_deadlock_risk()


def test_rounds_left_until_deadlock():
    ads = AgentDamageState()
    assert (
        ads.rounds_left_until_deadlock()
        == DEADLOCK_ROUNDS_TO_START + DEADLOCK_ROUNDS_TO_RESOLVE
    )
    ads.history = {1: 0, 2: 0, 3: 0}
    assert (
        ads.rounds_left_until_deadlock()
        == DEADLOCK_ROUNDS_TO_START + DEADLOCK_ROUNDS_TO_RESOLVE - 3
    )


def test_is_deadlocked():
    ads = AgentDamageState()
    assert not ads.is_deadlocked()
    assert not ads.has_computer_won()
    assert not ads.has_human_won()
    for i in range(DEADLOCK_ROUNDS_TO_START + DEADLOCK_ROUNDS_TO_RESOLVE):
        ads.add_to_history(1 + i)
    assert ads.is_deadlocked()
    assert ads.has_computer_won()
    assert not ads.has_human_won()
