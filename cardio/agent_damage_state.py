import logging
from typing import Dict

DAMAGE_DIFF_TO_WIN = 5  # Amount of damage difference to win a fight
DEADLOCK_ROUNDS_TO_START = 5
DEADLOCK_ROUNDS_TO_RESOLVE = 5


def count_equal_items_at_end(lst) -> int:
    if not lst:
        return 0
    last_value = lst[-1]
    count = 1
    for value in reversed(lst[:-1]):
        if value == last_value:
            count += 1
        else:
            break
    return count


class AgentDamageState:
    """Keeps track of the damage difference between human and computer player. Also
    keeps track of deadlock state.
    """

    def __init__(self, max_diff: int = DAMAGE_DIFF_TO_WIN) -> None:
        self.diff = 0  # <0: computer damaged, >0: human damaged
        self.max_diff = max_diff
        self.history: Dict[int, int] = {}  # round_num -> diff

    # FIXME Add WhichPlayer (or similar) type and use it go generalize damage_*,
    # has_*_won as well as ForWhom in skills and instead of potency type in Card.

    def damage_computer(self, howmuch: int) -> None:
        assert howmuch >= 0
        self.diff -= howmuch
        logging.debug("Computer receives %s damage, diff now at %s", howmuch, self.diff)

    def damage_human(self, howmuch: int) -> None:
        assert howmuch >= 0
        self.diff += howmuch
        logging.debug("Human receives %s damage, diff now at %s", howmuch, self.diff)

    def has_human_won(self) -> bool:
        return self.diff <= -self.max_diff and not self.is_deadlocked()

    def has_computer_won(self) -> bool:
        return self.diff >= self.max_diff or self.is_deadlocked()

    def get_overflow(self) -> int:
        return abs(self.diff) - self.max_diff

    def add_to_history(self, round_num: int) -> None:
        """Note that we only store one diff per round to the history, it is assumed to
        be the final diff in a round.
        """
        self.history[round_num] = self.diff

    def is_in_deadlock_risk(self) -> bool:
        return (
            count_equal_items_at_end(list(self.history.values()))
            >= DEADLOCK_ROUNDS_TO_START
        )

    def rounds_left_until_deadlock(self) -> int:
        return (
            DEADLOCK_ROUNDS_TO_START
            + DEADLOCK_ROUNDS_TO_RESOLVE
            - count_equal_items_at_end(list(self.history.values()))
        )

    def is_deadlocked(self) -> bool:
        return self.rounds_left_until_deadlock() <= 0
