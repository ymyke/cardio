from collections import OrderedDict
from typing import List
from cardio import GridPos, Grid, Card


class PlacementAbortedException(Exception):
    pass


class PlacementManager:
    """Makes sure card placement conditions are met, especially in terms of their fire
    and spirits cost.

    There are 3 general cases:

    - `target_card` costs >1 fire: Make sure we have positions with cards marked that
      add up to the necessary fire.
    - `target_card costs 1 fire: Make sure we have a position with a card with at least
      1 fire marked.
    - `target_card` costs 0 fire: Make sure we have a position _without_ a card marked.

    In the latter two cases, `target_card` will immediately placed in the respective
    position.
    """

    def __init__(self, grid: Grid, available_spirits: int, target_card: Card) -> None:
        self.grid = grid
        self.available_spirits = available_spirits
        self.target_card = target_card
        self.marked_positions: OrderedDict = OrderedDict()

    def is_placeable(self) -> bool:
        """Whether `target_card` is placeable at all."""
        if self.available_spirits < self.target_card.costs_spirits:
            return False
        if self.target_card.costs_fire == 0:
            return None in self.grid.lines[2]
        return self.available_fire_in_grid() >= self.target_card.costs_fire

    def is_marked(self, pos: GridPos) -> bool:
        return pos in self.marked_positions

    def can_mark(self, pos: GridPos) -> bool:
        # General pre-conditions for marking:
        if not pos.line == 2 or self.is_marked(pos):
            return False
        # Spirits are simple:
        if self.target_card.costs_spirits > self.available_spirits:
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

    def get_all_pos(self) -> List[GridPos]:
        return list(self.marked_positions.keys())

    def get_last_pos(self) -> GridPos:
        return list(self.marked_positions.keys())[-1]

    def available_fire_in_marked_positions(self) -> int:
        return sum(
            c.has_fire
            for c in (self.grid.get_card(pos) for pos in self.marked_positions)
            if c is not None
        )

    def available_fire_in_grid(self) -> int:
        return sum(c.has_fire for c in self.grid.lines[2] if c is not None)

    def ready_to_place(self) -> bool:
        return (
            len(self.marked_positions) > 0
            and self.available_fire_in_marked_positions() >= self.target_card.costs_fire
            and self.available_spirits >= self.target_card.costs_spirits
        )

    def do_place(self) -> None:
        """Note that this method only handles the grid. Any updates of decks, views, and
        other states (e.g., for spirits count) must be done in addition.
        """
        for pos in self.marked_positions:
            self.grid.clear_position(pos)
        self.grid.set_card(self.get_last_pos(), self.target_card)
        # TODO Update spirits outside
