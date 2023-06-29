"""Grid class.

Positions:

- GridPos(line index, slot index)
- Lines:
    0: computer's prep line
    1: computer's line
    2: human's line
- Slots: Each line has card slots 0, 1, 2, ... grid.with-1

"""


from typing import List, Optional, NamedTuple
import logging
from cardio.fightcard import FightCard


class GridPos(NamedTuple):
    line: int
    slot: int


class GridPosAndCard(NamedTuple):
    pos: GridPos
    card: FightCard


class Grid:
    width: int
    lines: List[List[Optional[FightCard]]]

    def __init__(self, width: int = 4) -> None:
        self.width = width
        self.lines = [[None] * width for _ in range(3)]

    def __getitem__(self, linei) -> List[Optional[FightCard]]:
        return self.lines[linei]

    def __iter__(self) -> object:
        return self.lines.__iter__()

    def is_empty(self) -> bool:
        return all(card is None for line in self.lines for card in line)

    def find_card(self, card: FightCard) -> Optional[GridPos]:
        for linei, line in enumerate(self.lines):
            for sloti in range(self.width):
                if line[sloti] is card:
                    return GridPos(linei, sloti)
        return None

    def get_card(self, pos: GridPos) -> Optional[FightCard]:
        return self.lines[pos.line][pos.slot]

    def set_card(self, pos: GridPos, card: FightCard) -> None:
        assert self.lines[pos.line][pos.slot] is None
        self.lines[pos.line][pos.slot] = card

    def clear_position(self, pos: GridPos) -> None:
        self.lines[pos.line][pos.slot] = None

    def get_opposing_card(self, card: FightCard) -> Optional[FightCard]:
        pos = self.find_card(card)
        assert pos is not None
        if pos.line == 1:
            return self[2][pos.slot]
        elif pos.line == 2:
            return self[1][pos.slot]
        return None

    def remove_card(self, card: FightCard) -> None:
        pos = self.find_card(card)
        assert pos is not None
        self.clear_position(pos)

    def move_card(self, card: FightCard, to_pos: GridPos) -> None:
        from_pos = self.find_card(card)
        assert from_pos is not None
        assert self[to_pos.line][to_pos.slot] is None
        self[to_pos.line][to_pos.slot] = card
        self[from_pos.line][from_pos.slot] = None

    def __str__(self) -> str:
        s = ""
        for line in range(3):
            s += f"Grid line {line}: {', '.join([str(c) for c in self.lines[line]])}"
        return s

    def log(self):
        logging.debug(str(self))
