from collections import OrderedDict
from typing import List
from cardio import GridPos, Grid, Card


class PlacementManager:
    def __init__(self, grid: Grid, target_card: Card) -> None:
        self.grid = grid
        self.target_card = target_card
        self.marked_positions: OrderedDict = OrderedDict()

    def is_marked(self, pos: GridPos) -> bool:
        return pos in self.marked_positions

    def can_mark(self, pos: GridPos) -> bool:
        # General pre-conditions for marking:
        if not pos.line == 2 or self.is_marked(pos):
            return False
        # Target cards requiring 0 fire:
        card = self.grid.get_card(pos)
        if self.target_card.costs_fire == 0 and card is None:
            return True
        # Target cards requiring >0 fire:
        if self.target_card.costs_fire > 0 and card is not None and card.has_fire > 0:
            return True
        return False

    def mark_pos(self, pos: GridPos) -> None:
        assert self.can_mark(pos), "Cannot mark this position"
        self.marked_positions[pos] = None

    def unmark_pos(self, pos: GridPos) -> None:
        assert self.is_marked(pos)
        del self.marked_positions[pos]

    def mark_or_unmark_pos(self, pos: GridPos) -> bool:
        if self.is_marked(pos):
            self.unmark_pos(pos)
            return False
        else:
            try:
                self.mark_pos(pos)
                return True
            except (AttributeError, AssertionError):
                return False

    def get_all_pos(self) -> List[GridPos]:
        return list(self.marked_positions.keys())

    def get_last_pos(self) -> GridPos:
        return list(self.marked_positions.keys())[-1]

    def ready_to_place(self) -> bool:
        available_fire = sum(
            self.grid.get_card(pos).has_fire  # type:ignore
            for pos in self.marked_positions
            if self.grid.get_card(pos) is not None  # TODO Make nicer
        )
        return available_fire >= self.target_card.costs_fire

    def do_place(self) -> None:
        for pos in self.marked_positions:
            self.grid.clear_position(pos)
        self.grid.set_card(self.get_last_pos(), self.target_card)
        # TODO Card needs to be removed from the deck & needs animation
