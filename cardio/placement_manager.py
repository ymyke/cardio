from typing import List, Optional
from cardio import GridPos, Grid, Card


class PlacementAbortedException(Exception):
    pass


class PlacementManager:
    """Makes sure card placement conditions are met, especially in terms of their fire
    and spirits cost.

    Placing is the term for the entire process here, which consists of 2 steps:

    1. Marking: Marking as many cards as necessary to place the card. Can be 0 (e.g.,
       hamsters or cards that only cost spirits) to n.
    2. Picking: Once sufficient cards are marked (i.e., `ready_to_pick` returns `True`),
       pick a slot to place the new `target_card`. This can be either an empty spot or
       one of the marked spots.

    The actual placing of the `target_card` including model updates etc. must be done
    outside the placement manager (cf `FightVnC._place_card`).

    One of the central methods that orchestrates this process is `mark_unmark_or_pick`.
    """

    def __init__(self, grid: Grid, available_spirits: int, target_card: Card) -> None:
        self.grid = grid
        self.available_spirits = available_spirits
        self.target_card = target_card
        self.marked_positions = set()
        self.placement_position: Optional[GridPos] = None

    # ----- marking -----

    def is_marked(self, pos: GridPos) -> bool:
        return pos in self.marked_positions

    def can_mark(self, pos: GridPos) -> bool:
        card = self.grid.get_card(pos)
        return (
            pos.line == 2
            and not self.is_marked(pos)
            and self.target_card.costs_fire > 0
            and card is not None
            and card.has_fire > 0
        )

    def mark_pos(self, pos: GridPos) -> None:
        assert self.can_mark(pos), "Cannot mark this position"
        self.marked_positions.add(pos)

    def unmark_pos(self, pos: GridPos) -> None:
        assert self.is_marked(pos)
        self.marked_positions.remove(pos)

    def get_marked_positions(self) -> List[GridPos]:
        return list(self.marked_positions)

    # ----- picking -----

    def mark_unmark_or_pick(self, pos: GridPos) -> None:
        """Tries to pick if possible, or mark or unmark."""
        if self.ready_to_pick():
            self.pick_if_possible(pos)
        elif self.is_marked(pos):
            self.unmark_pos(pos)
        elif self.can_mark(pos):
            self.mark_pos(pos)

    def can_pick(self, pos: GridPos) -> bool:
        assert self.ready_to_pick()
        return pos.line == 2 and (
            pos in self.get_marked_positions() or self.grid.get_card(pos) is None
        )

    def pick_if_possible(self, pos: GridPos) -> None:
        assert self.placement_position is None
        if self.can_pick(pos):
            self.placement_position = pos

    def ready_to_pick(self) -> bool:
        return (
            self.available_fire_in_marked_positions() >= self.target_card.costs_fire
            and self.available_spirits >= self.target_card.costs_spirits
        )

    # ----- placing ----

    def is_placeable(self) -> bool:
        """Whether `target_card` is placeable at all."""
        if self.available_spirits < self.target_card.costs_spirits:
            return False
        if self.target_card.costs_fire == 0:
            return None in self.grid.lines[2]
        return self.available_fire_in_grid() >= self.target_card.costs_fire

    def ready_to_place(self) -> bool:
        return self.placement_position is not None

    def available_fire_in_marked_positions(self) -> int:
        return sum(
            c.has_fire
            for c in (self.grid.get_card(pos) for pos in self.get_marked_positions())
            if c is not None
        )

    def available_fire_in_grid(self) -> int:
        return sum(c.has_fire for c in self.grid.lines[2] if c is not None)

    def get_placement_position(self) -> GridPos:
        assert self.ready_to_place()
        return self.placement_position  # type:ignore
