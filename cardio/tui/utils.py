from __future__ import annotations
import pdb
import sys
import time
from typing import NamedTuple, Optional, Tuple, Union
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer, Box, Renderer
from asciimatics.event import KeyboardEvent
from asciimatics.constants import SINGLE_LINE
from .constants import *
from .buffercopy import BufferCopy
from cardio import GridPos, session


class dPos(NamedTuple):
    """Type for display position (as opposed to grid position). Supports `+` and `-` for
    easier coordinate calculations, e.g.: `dPos(1, 1) + (2, 3)`
    """

    x: int
    y: int

    def __add__(self, o: Union[dPos, Tuple[int, int]]) -> dPos:
        return dPos(self.x + o[0], self.y + o[1])

    def __sub__(self, o: Union[dPos, Tuple[int, int]]) -> dPos:
        return dPos(self.x - o[0], self.y - o[1])

    @classmethod
    def from_gridpos(cls, pos: GridPos) -> dPos:
        """Create dPos from GridPos."""
        agentgap = AGENTGAPSIZE if pos.line >= 2 else 0
        return dPos(
            x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING_LEFT),
            y=GRID_MARGIN_TOP + pos.line * (BOX_HEIGHT + BOX_PADDING_TOP) + agentgap,
        )


# LIXME Likely obsolete -- delete eventually!
#
# def show_effects(screen, effects: Union[Effect, List[Effect]]):
#     if not isinstance(effects, list):
#         effects = [effects]
#     for e in effects:  # type: ignore
#         e.update(0)
#     screen.refresh()


def show(screen: Screen, renderer: Renderer, pos: dPos, color: Color = Color.WHITE):
    if color is Color.GRAY:
        color_args = dict(colour=Screen.COLOUR_BLACK, attr=Screen.A_BOLD)
        # (BLACK + BOLD produces dark gray,
        # cf https://github.com/peterbrittain/asciimatics/issues/363)
    else:
        color_args = dict(colour=color.value)
    Print(screen=screen, renderer=renderer, x=pos.x, y=pos.y, **color_args).update(0)
    screen.refresh()


def show_text(screen: Screen, text: str, pos: dPos, color: Color = Color.WHITE) -> None:
    show(screen, StaticRenderer(images=[text]), pos, color)


def show_box(
    screen: Screen,
    w: int,
    h: int,
    pos: dPos,
    color: Color = Color.YELLOW,
    style: int = SINGLE_LINE,
) -> None:
    show(screen, Box(w, h, style=style, uni=True), pos, color)


def render_value(
    value: int,
    symbol: str,
    cap_at: int = 5,
    clear_after: bool = True,
    surplus_color: int = Screen.COLOUR_WHITE,
) -> str:
    nofsymbols = min(value, cap_at)
    surplus = value - nofsymbols
    surplus_str = (
        f"${{{surplus_color}}}+{surplus}${{{Screen.COLOUR_WHITE}}}"
        if surplus > 0
        else ""
    )
    value_str = symbol * nofsymbols + surplus_str
    delete_str = ""
    if clear_after:
        delete_str = "⠀" * (cap_at + 4 - len(value_str)) * len(symbol)
    return value_str + delete_str


def show_debug(screen, txt: str):
    screen.clear_buffer(
        Color.WHITE.value, 0, 0, x=0, y=screen.height - 1, w=screen.width, h=1
    )
    show_text(screen, txt, dPos(screen.width // 2, screen.height - 1))


def show_screen_resolution(screen):
    txt = f"{screen.width} x {screen.height}"
    show_text(screen, txt, dPos(screen.width - len(txt), screen.height - 1))


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
