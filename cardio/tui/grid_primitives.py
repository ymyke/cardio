from asciimatics.constants import SINGLE_LINE
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.screen import Screen

from cardio import GridPos

from .constants import *
from .utils import dPos, show


def show_empty_grid(screen: Screen, grid_width: int) -> None:
    for linei in range(3):
        for sloti in range(grid_width):
            show_slot_in_grid(screen, GridPos(linei, sloti))
    show_grid_decks_separator(screen, grid_width)


def show_slot_in_grid(screen: Screen, pos: GridPos) -> None:
    dpos = dPos.from_gridpos(pos)
    show(
        screen,
        Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
        dpos,
        color=Color.GRAY,
    )


def show_grid_decks_separator(screen: Screen, grid_width: int) -> None:
    dpos = dPos.from_gridpos(GridPos(4, 0))
    show(
        screen,
        StaticRenderer(["—" * ((BOX_WIDTH + BOX_PADDING_LEFT) * grid_width + 4)]),
        dPos(dpos.x - 2, dpos.y - 3),
        color=Color.GRAY,
    )
