import time
from typing import Literal, Optional, Union

from asciimatics.constants import DOUBLE_LINE, SINGLE_LINE
from asciimatics.effects import Print
from asciimatics.paths import Path
from asciimatics.renderers import Fire
from asciimatics.screen import Screen

from cardio import Card, GridPos

from .constants import *
from .buffercopy import BufferCopy
from .grid_primitives import show_slot_in_grid
from .utils import dPos, render_value, show_text, show_box


def card_to_amstring(c: Card) -> str:
    """Produce asciimatics string from card."""
    s = f"""\
{c.name}
{render_value(c.power, "💪", surplus_color=Screen.COLOUR_YELLOW)}
{render_value(c.health, "💓", surplus_color=Screen.COLOUR_RED)}
{"".join(s.value.symbol for s in c.skills)}
"""
    return s


def show_card(
    screen: Screen,
    card: Optional[Card],
    pos: Union[GridPos, dPos],
    highlight: bool = False,
    xoffset: int = 0,
    yoffset: int = 0,
) -> None:
    """Draw card. Either at display position or grid position, depending on the type of
    `pos` passed. Draws empty box if `card` is `None`. Highlights card/slot if
    `highlight` is `True`.
    """
    dpos = dPos.from_gridpos(pos) if isinstance(pos, GridPos) else pos
    dpos += (xoffset, yoffset)

    if highlight:
        style = DOUBLE_LINE
        color = Color.BLUE
    else:
        style = SINGLE_LINE
        color = Color.YELLOW

    show_box(screen, BOX_WIDTH, BOX_HEIGHT, dpos, style=style, color=color)
    if card is not None:
        show_text(screen, card_to_amstring(card), dpos + (2, 1))


def redraw_card(screen: Screen, card: Card, pos: GridPos) -> None:
    clear_card(screen, pos)
    show_card(screen, card, pos)


def highlight_card(
    screen: Screen, pos: Union[GridPos, dPos], highlight: bool = True
) -> None:
    show_card(screen, None, pos, highlight)


def clear_card(
    screen: Screen, pos: Union[GridPos, dPos], xoffset: int = 0, yoffset: int = 0
) -> None:
    dpos = dPos.from_gridpos(pos) if isinstance(pos, GridPos) else pos
    dpos += (xoffset, yoffset)
    screen.clear_buffer(
        Screen.COLOUR_WHITE, 0, 0, x=dpos.x, y=dpos.y, w=BOX_WIDTH, h=BOX_HEIGHT
    )


def activate_card(
    screen: Screen, card: Card, pos: GridPos, deactivate: bool = False
) -> None:
    yoffset = +2 if pos.line == 1 else -2
    if deactivate:
        clear_card(screen, pos, yoffset=yoffset)
        show_card(screen, card, pos, yoffset=0)
    else:
        clear_card(screen, pos, yoffset=0)
        show_card(screen, card, pos, yoffset=yoffset)
    time.sleep(0.1)


def burn_card(screen: Screen, pos: GridPos) -> None:
    dpos = dPos.from_gridpos(pos)
    overheight = 4
    overwidth = 2
    fire = Fire(
        height=BOX_HEIGHT + overheight,
        width=BOX_WIDTH + overwidth,
        emitter="*" * BOX_WIDTH,
        intensity=0.8,
        spot=30,
        colours=screen.colours,
        bg=screen.colours >= 256,
    )
    dpos -= (overwidth // 2, overheight)
    fireeffect = Print(screen, fire, y=dpos.y, x=dpos.x, speed=1, transparent=True)
    buffercopy = BufferCopy(screen)
    for i in range(25):
        if i % 5 == 0:
            fire._intensity *= 0.7
        fireeffect.update(0)
        screen.refresh()
        time.sleep(0.02)
        buffercopy.copyback()
    clear_card(screen, pos)
    show_slot_in_grid(screen, pos)


def shake_card(
    screen: Screen, card: Card, pos: GridPos, direction: Literal["h", "v"]
) -> None:
    if direction == "h":
        offset = {"xoffset": -1}
    else:
        offset = {"yoffset": -1}
    for _ in range(4):
        show_card(screen, card, pos)
        time.sleep(0.03)
        clear_card(screen, pos)
        show_card(screen, card, pos, **offset)
        time.sleep(0.03)
        clear_card(screen, pos, **offset)
    show_card(screen, card, pos)


def flash_card(screen: Screen, pos: GridPos) -> None:
    highlight = True
    for _ in range(10):
        show_card(screen, None, pos, highlight=highlight)
        time.sleep(0.2)
        highlight = not highlight


def move_card(
    screen: Screen,
    card: Card,
    from_: Union[GridPos, dPos],
    to: Union[GridPos, dPos],
    steps=10,
) -> None:
    from_ = dPos.from_gridpos(from_) if isinstance(from_, GridPos) else from_
    to = dPos.from_gridpos(to) if isinstance(to, GridPos) else to
    buffercopy = BufferCopy(screen)
    show_card(screen, card, from_)
    p = Path()
    p.jump_to(x=from_.x, y=from_.y)
    p.move_straight_to(x=to.x, y=to.y, steps=steps)
    for x, y in p._steps:
        buffercopy.copyback()
        show_card(screen, card, dPos(x, y))
