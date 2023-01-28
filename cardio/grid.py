"""Grid class.

Positions:

- GridPos(line index, slot index)
- Lines:
    0: computer's prep line
    1: computer's line
    2: human's line
- Slots: Each line has card slots 0, 1, 2, ... grid.with-1

"""

# FIXME: Should the grid only exist implicitly in the cards? A card would have a GridPos
# object. Would also get rid of the find_in_grid function etc. Grid object would offer
# some convenience functions tapping into GridPos object. Card would have view
# functions, among which one would be gridpos2dpos or so.

from typing import List, Optional, Union, NamedTuple
import logging
from cardio.card import Card


class GridPos(NamedTuple):
    line: int
    slot: int


class GridPosAndCard(NamedTuple):
    pos: GridPos
    card: Card


class Grid:
    width: int
    lines: List[List[Optional[Card]]]

    def __init__(self, width: int = 4) -> None:
        self.width = width
        self.lines = [[None] * width for _ in range(3)]

    def __getitem__(self, linei):
        return self.lines[linei]

    def __iter__(self) -> object:
        return self.lines.__iter__()

    def is_empty(self) -> bool:
        return all(card is None for line in self.lines for card in line)

    def find_card(self, card: Card) -> Optional[GridPos]:
        for linei, line in enumerate(self.lines):
            for sloti in range(self.width):
                if line[sloti] is card:
                    return GridPos(linei, sloti)
        return None

    def get_card(self, pos: GridPos) -> Optional[Card]:
        return self.lines[pos.line][pos.slot]

    def set_card(self, pos: GridPos, card: Card) -> None:
        assert self.lines[pos.line][pos.slot] is None
        self.lines[pos.line][pos.slot] = card

    def clear_position(self, pos: GridPos) -> None:
        self.lines[pos.line][pos.slot] = None

    def get_opposing_card(self, card: Card) -> Optional[Card]:
        pos = self.find_card(card)
        assert pos is not None
        if pos.line == 1:
            return self[2][pos.slot]
        elif pos.line == 2:
            return self[1][pos.slot]
        return None

    def remove_card(self, card: Card) -> None:
        pos = self.find_card(card)
        assert pos is not None
        assert self[pos.line][pos.slot] is card
        self[pos.line][pos.slot] = None
        logging.debug("Removed card from %s", pos)

    def move_card(self, card: Card, to_pos: Union[GridPos, tuple]) -> None:
        """Accepts both a `GridPos` named tuple as well as a normal tuple as the
        `to_pos`.
        """
        to_pos = GridPos(*to_pos)
        from_pos = self.find_card(card)
        assert from_pos is not None
        assert self[to_pos.line][to_pos.slot] is None
        self[to_pos.line][to_pos.slot] = card
        self[from_pos.line][from_pos.slot] = None

    def activate_line(self, linei: int) -> None:
        assert linei in [1, 2]
        for card in self.lines[linei]:
            if card is not None:
                card.activate()

    def prepare_line(self) -> None:
        for card in self.lines[0]:
            if card is not None:
                card.prepare()

    def log(self):
        for line in range(3):
            logging.debug(
                "Grid line %s: %s", line, ", ".join([str(c) for c in self.lines[line]])
            )
