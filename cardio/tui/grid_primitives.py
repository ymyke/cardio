from asciimatics.constants import SINGLE_LINE
from asciimatics.effects import Print
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.screen import Screen

from cardio import GridPos

from .constants import *
from .utils import dPos, show_effects


def show_empty_grid(screen: Screen, grid_width: int) -> None:
    for linei in range(3):
        for sloti in range(grid_width):
            show_slot_in_grid(screen, GridPos(linei, sloti))
    show_grid_decks_separator(screen, grid_width)


def show_slot_in_grid(screen: Screen, pos: GridPos) -> None:
    dpos = dPos.from_gridpos(pos)
    show_effects(
        screen,
        Print(
            screen=screen,
            renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
            x=dpos.x,
            y=dpos.y,
            colour=Screen.COLOUR_BLACK,
            attr=Screen.A_BOLD,
        ),
    )
    # (BLACK + BOLD produces dark gray,
    # cf https://github.com/peterbrittain/asciimatics/issues/363)


def show_grid_decks_separator(screen: Screen, grid_width: int) -> None:
    dpos = dPos.from_gridpos(GridPos(4, 0))
    show_effects(
        screen,
        Print(
            screen,
            StaticRenderer(["—" * ((BOX_WIDTH + BOX_PADDING_LEFT) * grid_width + 4)]),
            x=dpos.x - 2,
            y=dpos.y - 3,
            colour=Screen.COLOUR_BLACK,
            attr=Screen.A_BOLD,
        ),
    )