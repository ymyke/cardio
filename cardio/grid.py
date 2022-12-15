from typing import List, Optional
from cardio.card import Card


class Line:
    """

    Slots are counted 0, 1, 2, ... from left border.
    """

    def __init__(self, width: int) -> None:
        self.slots: List[Optional[Card]] = [None] * width

    def __getitem__(self, sloti: int) -> Optional[Card]:
        return self.slots[sloti]

    def __setitem__(self, sloti, card: Card) -> None:
        assert isinstance(card, Card)
        assert self.slots[sloti] is None
        self.slots[sloti] = card

    def __iter__(self) -> object:
        return self.slots.__iter__()

    def add_card(self, sloti: int, card: Card) -> None:
        self[sloti] = card


class Grid:
    def __init__(self, width: int = 4) -> None:
        self.width = width
        self.prepline = Line(width)
        self.opponentline = Line(width)
        self.playerline = Line(width)
        self.lines = [self.prepline, self.opponentline, self.playerline]
        # FIXME Should there be some CardSlot or some BaseCard or NoCard class for
        # the empty spaces?

    def __repr__(self) -> str:
        repr = ""
        for i, line in enumerate(self):
            repr += f"{i}   "
            for slot in line.slots:
                slotstr = ""
                if slot is not None:
                    slotstr = f"{slot.name[0:6]}|{slot.power}|{slot.health}"
                repr += f"[{slotstr:13s}]"
            repr += "\n"
        return repr

    def __getitem__(self, linei):
        return self.lines[linei]

    def __iter__(self) -> object:
        return self.lines.__iter__()


class GridView:
    # FIXME Make this an ABC with init and update methods?
    def __init__(self, gridmodel: Grid) -> None:
        self.model = gridmodel

    def update(self) -> None:
        pass


class SimpleView(GridView):
    def update(self) -> None:
        print(str(self.model))


class GridController:
    def __init__(self, grid: Grid, gridview: GridView) -> None:
        self.grid = grid
        self.gridview = gridview

    def add_card(self, linei: int, sloti: int, card: Card) -> None:
        self.grid[linei][sloti] = card
        self.gridview.update()

    def handle_round(self) -> None:
        for linei, opponenti in ((2, 1), (1, 2)):
            for sloti in range(self.grid.width):
                if self.grid[linei][sloti] is None:
                    continue  # No card in this slot
                if self.grid[opponenti][sloti] is None:
                    # FIXME Damage the player behind
                    continue
                self.grid[linei][sloti].attack(self.grid[opponenti][sloti])
        
        # FIXME Need some activate method instead of attack.
        # FIXME Then need to add line 0 as well.
        # FIXME It becomes apparent here: Terms like opponent and player are overloaded.
        # FIXME A card that is dead should be removed.

        # Activate player cards
        # Activate opponent
        # Activate from prepline

        # FIXME Check if game over
        self.gridview.update()
