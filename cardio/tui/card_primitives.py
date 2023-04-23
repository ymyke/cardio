from dataclasses import dataclass
import time
from typing import Literal, Optional, Tuple, Union

from asciimatics.constants import DOUBLE_LINE, SINGLE_LINE
from asciimatics.effects import Print
from asciimatics.paths import Path
from asciimatics.renderers import Fire
from asciimatics.screen import Screen

from cardio import Card, GridPos

from .constants import *
from .bufferutils import BufferCopy
from .utils import dPos, render_value, show_text, show_text_ra, show_box


@dataclass(frozen=True)
class VisualStateSpec:
    color: Color
    linestyle: int


class VisualState(Enum):
    """Visual state of a card."""

    NORMAL = VisualStateSpec(Color.YELLOW, SINGLE_LINE)
    MARKED = VisualStateSpec(Color.BLUE, DOUBLE_LINE)
    CURSOR = VisualStateSpec(Color.MAGENTA, DOUBLE_LINE)
    READY = VisualStateSpec(Color.GREEN, DOUBLE_LINE)
    INACTIVE = VisualStateSpec(Color.GRAY, SINGLE_LINE)
    ERROR = VisualStateSpec(Color.RED, DOUBLE_LINE)


def show_card_contents(
    screen: Screen, card: Card, pos: dPos, inactive: bool = False
) -> None:
    """
    On `costs_*` and `has_*`:
    - Show `costs_*` in lower right, only the one that is > 0.
    - Show `has_*` in lower left, only the one that is > 1 (if any).
    """
    color = Color.GRAY if inactive else Color.WHITE
    show_text(screen, pos + (2, 1), card.name, color=color)
    power = render_value(card.power, "💪", surplus_color=Color.YELLOW)
    show_text(screen, pos + (2, 2), power)
    health = render_value(card.health, "💓", surplus_color=Color.RED)
    show_text(screen, pos + (2, 3), health)
    skills = "".join(s.value.symbol for s in card.skills)
    show_text(screen, pos + (2, 4), skills)

    # Don't show `costs_*` and `has_*` for computer cards:
    try:
        if card.get_grid_pos().line in (0, 1):
            # Cards that are on the grid in computer's lines.
            return
    except (AssertionError, AttributeError):
        if pos.y <= dPos.from_gridpos(GridPos(1, 0)).y:
            # Cards that are not yet on the grid but being moved on computer's side.
            return

    # Show `costs_*` in lower right, only the one that is > 0:
    if card.costs_fire > 0:
        costs = render_value(card.costs_fire, "🔥", 3, False, Color.YELLOW)
    elif card.costs_spirits > 0:
        costs = render_value(card.costs_spirits, "👻", 3, False, Color.WHITE)
    else:
        costs = ""
    show_text_ra(screen, pos + (BOX_WIDTH - 1, 5), costs)

    # Show `has_*` in lower left, only the one that is > 1 (if any):
    if card.has_fire > 1:
        has = render_value(card.has_fire, "🔥", 3, False, Color.YELLOW)
    elif card.has_spirits > 1:
        has = render_value(card.has_spirits, "👻", 3, False, Color.WHITE)
    else:
        has = ""
    show_text(screen, pos + (2, 5), has)


def show_card(
    screen: Screen,
    card: Optional[Card],
    pos: Union[GridPos, dPos],
    state: VisualState = VisualState.NORMAL,
    xoffset: int = 0,
    yoffset: int = 0,
) -> None:
    """Draw card. Either at display position or grid position, depending on the type of
    `pos` passed. Draws empty box if `card` is `None`. Highlights card/slot if
    `highlight` is `True`. Displays card as inactive if `inactive` is `True`
    (`highlight` trumps `inactive`). TODO Adjust
    """
    dpos = dPos.cast(pos) + (xoffset, yoffset)
    show_box(screen, dpos, style=state.value.linestyle, color=state.value.color)
    if card:
        show_card_contents(screen, card, dpos, inactive=state == VisualState.INACTIVE)


def redraw_card(
    screen: Screen, card: Optional[Card], pos: Union[GridPos, dPos]
) -> None:
    clear_card(screen, pos)
    show_card(screen, card, pos)


def clear_card(
    screen: Screen, pos: Union[GridPos, dPos], xoffset: int = 0, yoffset: int = 0
) -> None:
    dpos = dPos.cast(pos)
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
        screen.refresh()
    else:
        clear_card(screen, pos, yoffset=0)
        show_card(screen, card, pos, yoffset=yoffset)
        screen.refresh()
    time.sleep(0.1)


def burn_card(screen: Screen, pos: Union[dPos, GridPos]) -> None:
    dpos = dPos.cast(pos)
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


def shake_card(
    screen: Screen, card: Card, pos: Union[dPos, GridPos], direction: Literal["h", "v"]
) -> None:
    if direction == "h":
        offset = {"xoffset": -1}
    else:
        offset = {"yoffset": -1}
    for _ in range(4):
        show_card(screen, card, pos)
        screen.refresh()
        time.sleep(0.03)
        clear_card(screen, pos)
        show_card(screen, card, pos, **offset)
        screen.refresh()
        time.sleep(0.03)
        clear_card(screen, pos, **offset)
        screen.refresh()
    show_card(screen, card, pos)
    screen.refresh()


def flash_card(
    screen: Screen,
    pos: Union[dPos, GridPos],
    states: Tuple[VisualState, VisualState] = (VisualState.NORMAL, VisualState.ERROR),
) -> None:
    """Quickly alternate between two states."""
    for i in range(10):
        show_card(screen, None, pos, state=states[i % 2])
        time.sleep(0.02)
        screen.refresh()


def move_card(
    screen: Screen,
    card: Card,
    from_: Union[GridPos, dPos],
    to: Union[GridPos, dPos],
    steps=10,
) -> None:
    from_ = dPos.cast(from_)
    to = dPos.cast(to)
    buffercopy = BufferCopy(screen)
    show_card(screen, card, from_)
    p = Path()
    p.jump_to(x=from_.x, y=from_.y)
    p.move_straight_to(x=to.x, y=to.y, steps=steps)
    for x, y in p._steps:
        buffercopy.copyback()
        show_card(screen, card, dPos(x, y))
        screen.refresh()
