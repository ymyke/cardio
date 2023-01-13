import time
from typing import Optional, List, Literal, Union
from asciimatics.effects import Print, Effect
from asciimatics.screen import Screen
from asciimatics.renderers import Box, StaticRenderer, Fire
from asciimatics.constants import SINGLE_LINE, DOUBLE_LINE
from asciimatics.paths import Path
from cardio import Card, GridPos
from .constants import *
from .buffercopy import BufferCopy
from .utils import show_effects, dPos
from .grid_primitives import draw_slot_in_grid


def card_to_amstring(c: Card) -> str:
    """Produce asciimatics string from card."""
    s = f"""\
{c.name}
{"💪" * c.power}
{"💓" * c.health}
{"".join(s.value.symbol for s in c.skills)}
"""
    return s


def render_card_at(
    screen, card: Optional[Card], x: int, y: int, highlight: bool = False
) -> List[Effect]:
    """Render card and box at x, y screen position. Draws empty box if `card`
    is `None`.
    """
    BOX_COLOR = Screen.COLOUR_YELLOW
    effects = []
    style = DOUBLE_LINE if highlight else SINGLE_LINE
    pbox = Print(
        screen=screen,
        renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=style),
        x=x,
        y=y,
        colour=BOX_COLOR,
    )
    effects.append(pbox)
    if card is not None:
        pcard = Print(
            screen=screen,
            renderer=StaticRenderer(images=[card_to_amstring(card)]),
            y=y + 1,
            x=x + 2,
        )
        effects.append(pcard)
    return effects


def render_card_in_grid(
    screen,
    card: Optional[Card],
    pos: GridPos,
    highlight: bool = False,
    xoffset: int = 0,
    yoffset: int = 0,
) -> List[Effect]:
    """Render card at grid position."""
    dpos = dPos.from_gridpos(pos)
    return render_card_at(
        screen, card, x=dpos.x + xoffset, y=dpos.y + yoffset, highlight=highlight
    )


def redraw_card_in_grid(screen, card, pos):
    clear_card_in_grid(screen, pos)
    show_effects(screen, render_card_in_grid(screen, card, pos))


def render_highlight_card_at(screen, pos: dPos, highlight: bool = False):
    if highlight:
        style = DOUBLE_LINE
        color = Screen.COLOUR_BLUE
    else:
        style = SINGLE_LINE
        color = Screen.COLOUR_YELLOW

    return [
        Print(
            screen=screen,
            renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=style),
            x=pos.x,
            y=pos.y,
            colour=color,
        )
    ]


def activate_card_in_grid(screen, card, pos: GridPos, deactivate: bool = False) -> None:
    import logging

    logging.debug("activate_card_in_grid *** %s %s", card.name, pos)
    yoffset = +2 if pos.line == 1 else -2
    if deactivate:
        clear_card_in_grid(screen, pos, yoffset=yoffset)
        show_effects(screen, render_card_in_grid(screen, card, pos, yoffset=0))
    else:
        clear_card_in_grid(screen, pos, yoffset=0)
        show_effects(screen, render_card_in_grid(screen, card, pos, yoffset=yoffset))
    time.sleep(0.1)


def burn_card_in_grid(screen, card, pos: GridPos) -> None:
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
    fireeffect = Print(
        screen,
        fire,
        y=dpos.y - overheight,
        x=dpos.x - overwidth // 2,
        speed=1,
        transparent=True,
    )
    buffercopy = BufferCopy(screen)
    for i in range(25):
        if i % 5 == 0:
            fire._intensity *= 0.7
        fireeffect.update(0)
        screen.refresh()
        time.sleep(0.02)
        buffercopy.copyback()
    clear_card_in_grid(screen, pos)
    draw_slot_in_grid(screen, pos)


def shake_card_in_grid(
    screen, card: Card, pos: GridPos, direction: Literal["h", "v"]
) -> None:
    if direction == "h":
        offset = {"xoffset": -1}
    else:
        offset = {"yoffset": -1}
    effects1 = render_card_in_grid(screen, card, pos)
    for _ in range(4):
        show_effects(screen, effects1, 0.03)
        clear_card_in_grid(screen, pos)
        effects2 = render_card_in_grid(screen, card, pos, **offset)
        show_effects(screen, effects2, 0.03)
        clear_card_in_grid(screen, pos, **offset)
    show_effects(screen, effects1)


def flash_card_in_grid(screen, pos: GridPos) -> None:
    highlight = True
    for _ in range(10):
        show_effects(
            screen,
            render_card_in_grid(screen, None, pos, highlight=highlight),
            pause=0.2,
        )
        highlight = not highlight


def render_highlight_card_in_grid(screen, pos: GridPos):
    return render_highlight_card_at(screen, dPos.from_gridpos(pos))


def highlight_card_at(screen, pos: dPos, highlight: bool = False):
    show_effects(screen, render_highlight_card_at(screen, pos, highlight))


def highlight_card_in_grid(screen, pos: GridPos, highlight: bool = True):
    highlight_card_at(screen, dPos.from_gridpos(pos), highlight)


def clear_card_at(screen, x, y):
    screen.clear_buffer(Screen.COLOUR_WHITE, 0, 0, x=x, y=y, w=BOX_WIDTH, h=BOX_HEIGHT)


def clear_card_in_grid(screen, pos: GridPos, xoffset: int = 0, yoffset: int = 0):
    dpos = dPos.from_gridpos(pos)
    clear_card_at(screen, x=dpos.x + xoffset, y=dpos.y + yoffset)


def move_card(
    screen, card: Card, from_: Union[GridPos, dPos], to: Union[GridPos, dPos], steps=10
) -> None:
    from_ = dPos.from_gridpos(from_) if isinstance(from_, GridPos) else from_
    to = dPos.from_gridpos(to) if isinstance(to, GridPos) else to
    buffercopy = BufferCopy(screen)
    show_effects(
        screen,
        render_card_at(screen, card, x=from_.x, y=from_.y),
    )
    p = Path()
    p.jump_to(x=from_.x, y=from_.y)
    p.move_straight_to(x=to.x, y=to.y, steps=steps)
    for x, y in p._steps:
        buffercopy.copyback()
        show_effects(screen, render_card_at(screen, card, x, y))
