import logging
from typing import Dict, Optional
from cardio.whichplayer import WhichPlayer

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

    def apply_damage(self, to_: WhichPlayer, howmuch: int) -> None:
        assert howmuch >= 0
        sign = 1 if to_ == "human" else -1
        self.diff += sign * howmuch
        logging.debug("%s receives %s damage, diff now at %s", to_, howmuch, self.diff)

    def who_won(self) -> Optional[WhichPlayer]:
        if self.diff >= self.max_diff or self.is_deadlocked():
            return "computer"
        if self.diff <= -self.max_diff:
            return "human"
        return None

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
