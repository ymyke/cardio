from __future__ import annotations
import pdb
import sys
import time
from typing import NamedTuple, Union, List, Optional
from asciimatics.screen import Screen
from asciimatics.effects import Effect, Print
from asciimatics.renderers import StaticRenderer
from asciimatics.event import KeyboardEvent
from .constants import *
from .buffercopy import BufferCopy
from cardio import GridPos, session


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


def show_screen_resolution(screen):
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


def get_keycode(screen: Screen) -> Optional[int]:
    """Non-blocking. Ignores all mouse events. Returns `ord` value of key pressed,
    `None` if no key pressed. Special keys are encoded according to
    `asciimatics.screen.Screen.KEY_*`.
    """
    event = screen.get_event()
    if not isinstance(event, KeyboardEvent):
        # Add a tiny pause if there is no event to reduce CPU load while polling:
        time.sleep(0.02)
        return None
    if event.key_code == ord("$"):  # hard exit
        sys.exit(0)
    if event.key_code == ord("!"):  # debug
        bc = BufferCopy(screen)
        screen.close()
        pdb.set_trace()
        session.view.screen = bc.screen = Screen.open(unicode_aware=True)
        bc.copyback()

    return event.key_code
