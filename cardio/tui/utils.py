from __future__ import annotations
import pdb
import random
import sys
import time
from typing import NamedTuple, Optional, Tuple, Union
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer, Box, Renderer
from asciimatics.event import KeyboardEvent
from asciimatics.constants import SINGLE_LINE
from .constants import *
from .bufferutils import BufferCopy
from cardio import GridPos


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
        """Create `dPos` from `GridPos`."""
        agentgap = AGENTGAPSIZE if pos.line >= 2 else 0
        return dPos(
            x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING_LEFT),
            y=GRID_MARGIN_TOP + pos.line * (BOX_HEIGHT + BOX_PADDING_TOP) + agentgap,
        )

    @classmethod
    def cast(cls, pos: Union[GridPos, dPos, Tuple[int, int]]) -> dPos:
        """Convert all kinds of inputs to `dPos`."""
        if isinstance(pos, dPos):
            return pos
        elif isinstance(pos, GridPos):
            return cls.from_gridpos(pos)
        return dPos(pos[0], pos[1])


def show(screen: Screen, pos: dPos, renderer: Renderer, color: Color = Color.WHITE):
    if color is Color.GRAY:
        color_args = dict(colour=Screen.COLOUR_BLACK, attr=Screen.A_BOLD)
        # (BLACK + BOLD produces dark gray,
        # cf https://github.com/peterbrittain/asciimatics/issues/363)
    else:
        color_args = dict(colour=color.value)
    Print(screen=screen, renderer=renderer, x=pos.x, y=pos.y, **color_args).update(0)


def show_text(screen: Screen, pos: dPos, text: str, color: Color = Color.WHITE) -> None:
    show(screen, pos, StaticRenderer(images=[text]), color)


def show_text_ra(
    screen: Screen, pos: dPos, text: str, color: Color = Color.WHITE
) -> None:
    """Right-aligned text."""
    pure_text = str(StaticRenderer([text]))  # Remove asciimatics color codes
    num_asciis = len(pure_text.encode("ascii", "ignore"))
    num_nonasciis = len(pure_text) - num_asciis
    xoffest = num_asciis + 2 * num_nonasciis
    show_text(screen, pos - (xoffest, 0), text, color)


def splash_message(screen: Screen, msg: str) -> None:
    lines = msg.split("\n")
    y = screen.height // 2 - len(lines) // 2
    for line in lines:
        x = screen.width // 2 - len(line) // 2
        show_text(screen, dPos(x, y), line)
        y += 1
    screen.refresh()


def show_box(
    screen: Screen,
    pos: dPos,
    w: int = BOX_WIDTH,
    h: int = BOX_HEIGHT,
    color: Color = Color.YELLOW,
    style: int = SINGLE_LINE,
) -> None:
    show(screen, pos, Box(w, h, style=style, uni=True), color)


def render_value(
    value: int,
    symbol: str,
    cap_at: int = 5,
    clear_after: bool = True,
    surplus_color: Color = Color.WHITE,
) -> str:
    nofsymbols = min(value, cap_at)
    surplus = value - nofsymbols
    surplus_str = (
        f"${{{surplus_color.value}}}+{surplus}${{{Color.WHITE.value}}}"
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
    show_text(screen, dPos(screen.width // 2, screen.height - 1), txt)


def show_screen_resolution(screen):
    txt = f"{screen.width} x {screen.height}"
    show_text(screen, dPos(screen.width - len(txt), screen.height - 1), txt)


def start_debug_mode(screen: Screen):
    bc = BufferCopy(screen)
    screen.close()
    pdb.set_trace()
    screen.open(unicode_aware=True)
    bc.copyback()


def get_keycode(screen: Screen) -> Optional[int]:
    """Non-blocking. Ignores all mouse events. Returns `ord` value of key pressed,
    `None` if no key pressed. Special keys are encoded according to
    `asciimatics.screen.Screen.KEY_*`.
    """
    event = screen.get_event()
    if not isinstance(event, KeyboardEvent):
        # Add a tiny pause if there is no event to reduce CPU load while polling:
        time.sleep(0.05)
        return None
    if event.key_code == ord("$"):  # hard exit
        sys.exit(0)
    if event.key_code == ord("!"):  # debug
        start_debug_mode(screen)
    return event.key_code


def wait_for_any_key(screen: Screen) -> int:
    keycode = None
    while not keycode:
        keycode = get_keycode(screen)
    return keycode


# ----- Figlet fonts -----

FIGLETFONTNAMES = [
    "3-d",
    "3x5",
    "5lineoblique",
    "acrobatic",
    "alligator",
    "alligator2",
    "alphabet",
    "avatar",
    "banner",
    "banner3-D",
    "banner3",
    "banner4",
    "barbwire",
    "basic",
    "bell",
    "big",
    "bigchief",
    "binary",
    "block",
    "bubble",
    "bulbhead",
    "calgphy2",
    "caligraphy",
    "catwalk",
    "chunky",
    "coinstak",
    "colossal",
    "computer",
    "contessa",
    "contrast",
    "cosmic",
    "cosmike",
    "cricket",
    "cursive",
    "cyberlarge",
    "cybermedium",
    "cybersmall",
    "diamond",
    "digital",
    "doh",
    "doom",
    "dotmatrix",
    "drpepper",
    "eftichess",
    "eftifont",
    "eftipiti",
    "eftirobot",
    "eftitalic",
    "eftiwall",
    "eftiwater",
    "epic",
    "fender",
    "fourtops",
    "fuzzy",
    "goofy",
    "gothic",
    "graffiti",
    "hollywood",
    "invita",
    "isometric1",
    "isometric2",
    "isometric3",
    "isometric4",
    "italic",
    "ivrit",
    "jazmine",
    "jerusalem",
    "katakana",
    "kban",
    "larry3d",
    "lcd",
    "lean",
    "letters",
    "linux",
    "lockergnome",
    "madrid",
    "marquee",
    "maxfour",
    "mike",
    "mini",
    "mirror",
    "mnemonic",
    "morse",
    "moscow",
    "nancyj-fancy",
    "nancyj-underlined",
    "nancyj",
    "nipples",
    "ntgreek",
    "o8",
    "ogre",
    "pawp",
    "peaks",
    "pebbles",
    "pepper",
    "poison",
    "puffy",
    "pyramid",
    "rectangles",
    "relief",
    "relief2",
    "rev",
    "roman",
    "rot13",
    "rounded",
    "rowancap",
    "rozzo",
    "runic",
    "runyc",
    "sblood",
    "script",
    "serifcap",
    "shadow",
    "short",
    "slant",
    "slide",
    "slscript",
    "small",
    "smisome1",
    "smkeyboard",
    "smscript",
    "smshadow",
    "smslant",
    "smtengwar",
    "speed",
    "stampatello",
    "standard",
    "starwars",
    "stellar",
    "stop",
    "straight",
    "tanja",
    "tengwar",
    "term",
    "thick",
    "thin",
    "threepoint",
    "ticks",
    "ticksslant",
    "tinker-toy",
    "tombstone",
    "trek",
    "tsalagi",
    "twopoint",
    "univers",
    "usaflag",
    "wavy",
    "weird",
]


def get_random_figlet_font() -> str:
    return random.choice(FIGLETFONTNAMES)
