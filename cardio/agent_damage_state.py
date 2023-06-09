import logging

DAMAGE_DIFF_TO_WIN = 5  # Amount of damage difference to win a fight


class AgentDamageState:
    def __init__(self, max_diff: int = DAMAGE_DIFF_TO_WIN) -> None:
        self.diff = 0  # <0: computer damaged, >0: human damaged
        self.max_diff = max_diff

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
        return self.diff <= -self.max_diff

    def has_computer_won(self) -> bool:
        return self.diff >= self.max_diff

    def get_overflow(self) -> int:
        return abs(self.diff) - self.max_diff
