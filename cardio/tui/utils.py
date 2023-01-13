from __future__ import annotations
from typing import NamedTuple, Union, List
from asciimatics.effects import Effect, Print
from asciimatics.renderers import StaticRenderer
from .constants import *
from cardio import GridPos


class dPos(NamedTuple):
    """Type for display position (as opposed to grid position)."""

    x: int
    y: int

    @classmethod
    def from_gridpos(cls, pos: GridPos) -> dPos:
        """Create dPos from GridPos."""
        agentgap = AGENTGAPSIZE if pos.line >= 2 else 0
        return dPos(
            x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING_LEFT),
            y=GRID_MARGIN_TOP + pos.line * (BOX_HEIGHT + BOX_PADDING_TOP) + agentgap,
        )


def show_effects(screen, effects: Union[Effect, List[Effect]]):
    if not isinstance(effects, list):
        effects = [effects]
    for e in effects:  # type: ignore
        e.update(0)
    screen.refresh()


def draw_screen_resolution(screen):
    txt = f"{screen.width} x {screen.height}"
    show_effects(
        screen,
        Print(
            screen,
            StaticRenderer(images=[txt]),
            x=screen.width - len(txt),
            y=screen.height - 1,
        ),
    )
