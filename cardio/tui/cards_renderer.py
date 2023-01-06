from typing import List, Literal, NamedTuple, Optional, Tuple, Union
import time
from asciimatics.effects import Effect, Print
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.screen import Screen
from asciimatics import constants
from asciimatics.utilities import BoxTool

from cardio import Card, GridPos

GRID_MARGIN_LEFT = 10
GRID_MARGIN_TOP = 4
BOX_WIDTH = 20
BOX_HEIGHT = 7
BOX_PADDING_TOP = 0
BOX_PADDING_LEFT = 3
DRAW_DECKS_X = 45
DRAW_DECKS_Y = 45  # FIXME Make this relative to the lower border?


class dPos(NamedTuple):
    x: int
    y: int


def gridpos2dpos(pos: GridPos) -> dPos:
    agentgap = 3 if pos.line >= 2 else 0
    return dPos(
        x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING_LEFT),
        y=GRID_MARGIN_TOP + pos.line * (BOX_HEIGHT + BOX_PADDING_TOP) + agentgap,
    )


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
    style = constants.DOUBLE_LINE if highlight else constants.SINGLE_LINE
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
    dpos = gridpos2dpos(pos)
    return render_card_at(
        screen, card, x=dpos.x + xoffset, y=dpos.y + yoffset, highlight=highlight
    )


def redraw_card_in_grid(screen, card, pos):
    render_card_in_grid(screen, card, pos)
    # FIXME Just call render_card_in_grid directly?


def render_highlight_card_at(screen, pos: dPos, highlight: bool = False):
    if highlight:
        style = constants.DOUBLE_LINE
        color = Screen.COLOUR_BLUE
    else:
        style = constants.SINGLE_LINE
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
    return render_highlight_card_at(screen, gridpos2dpos(pos))


def highlight_card_at(screen, pos: dPos, highlight: bool = False):
    show_effects(screen, render_highlight_card_at(screen, pos, highlight))


def highlight_card_in_grid(screen, pos: GridPos, highlight: bool = True):
    highlight_card_at(screen, gridpos2dpos(pos), highlight)


def clear_card_at(screen, x, y):
    screen.clear_buffer(Screen.COLOUR_WHITE, 0, 0, x=x, y=y, w=BOX_WIDTH, h=BOX_HEIGHT)


def clear_card_in_grid(screen, pos: GridPos, xoffset: int = 0, yoffset: int = 0):
    dpos = gridpos2dpos(pos)
    clear_card_at(screen, x=dpos.x + xoffset, y=dpos.y + yoffset)


def show_effects(screen, effects: Union[Effect, List[Effect]], pause: float = 0):
    if not isinstance(effects, list):
        effects = [effects]
    for e in effects:
        e.update(0)
    screen.refresh()
    if pause > 0:
        time.sleep(pause)


class ExtendedBox(BoxTool):
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        self._style = style
        if style == 11:
            self.down_right = "·"
            self.down_left = "·"
            self.up_right = "·"
            self.up_left = "·"
            self.h = "·"
            self.h_inside = "·"
            self.v = "·"
            self.v_inside = "·"
            self.v_left = "·"
            self.v_right = "·"
            self.h_up = "·"
            self.h_down = "·"
            self.cross = "·"
        elif style == 12 and not self.unicode_aware:
            self.down_right = "+"
            self.down_left = "+"
            self.up_right = "+"
            self.up_left = "+"
            self.h = " "
            self.h_inside = " "
            self.v = ""
            self.v_inside = ""
            self.v_left = ""
            self.v_right = ""
            self.h_up = ""
            self.h_down = ""
            self.cross = ""
        elif style == 12 and self.unicode_aware:
            self.down_right = "┌"
            self.down_left = "┐"
            self.up_right = "└"
            self.up_left = "┘"
            self.h = " "
            self.h_inside = " "
            self.v = ""
            self.v_inside = ""
            self.v_left = ""
            self.v_right = ""
            self.h_up = ""
            self.h_down = ""
            self.cross = ""
        else:
            super(ExtendedBox, self.__class__).style.fset(self, style)


def draw_slot_in_grid(screen, pos: GridPos):
    dpos = gridpos2dpos(pos)
    show_effects(
        screen,
        Print(
            screen=screen,
            renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=constants.SINGLE_LINE),
            x=dpos.x,
            y=dpos.y,
            colour=Screen.COLOUR_BLACK,
            attr=Screen.A_BOLD,
        ),
    )
    # (BLACK + BOLD produces dark gray,
    # cf https://github.com/peterbrittain/asciimatics/issues/363)


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


def draw_handdeck_highlight(screen, slot: int, highlight: bool = True) -> None:
    highlight_card_in_grid(screen, GridPos(4, slot), highlight)
    # FIXME Call the highlight_card_in_grid directly rather than via this function?


def draw_drawdeck_highlights(screen, highlights: Tuple[bool, bool]):
    highlight_card_at(screen, dPos(DRAW_DECKS_X, DRAW_DECKS_Y), highlights[0])
    highlight_card_at(
        screen, dPos(DRAW_DECKS_X + BOX_WIDTH + 2, DRAW_DECKS_Y), highlights[1]
    )


def draw_drawdecks(screen: Screen, counts=list):
    # FIXME Should counts be Tuple[int, int]?

    drawcover = "    ⬆️⬆️⬆️⬆️⬆️⬆️⬆⬆️⬆️"
    hamstercover = "      🐹🐹🐹"

    show_effects(
        screen,
        [
            Print(
                screen=screen,
                renderer=Box(
                    BOX_WIDTH, BOX_HEIGHT, uni=True, style=constants.SINGLE_LINE
                ),
                x=DRAW_DECKS_X,
                y=DRAW_DECKS_Y,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen=screen,
                renderer=StaticRenderer(images=[drawcover]),
                x=DRAW_DECKS_X + 1,
                y=DRAW_DECKS_Y + BOX_HEIGHT // 2,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen,
                StaticRenderer([f"⠀{counts[0]}⠀⠀⠀"]),
                x=DRAW_DECKS_X + 1,
                y=DRAW_DECKS_Y + BOX_HEIGHT - 2,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen=screen,
                renderer=Box(
                    BOX_WIDTH, BOX_HEIGHT, uni=True, style=constants.SINGLE_LINE
                ),
                x=DRAW_DECKS_X + BOX_WIDTH + 2,
                y=DRAW_DECKS_Y,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen=screen,
                renderer=StaticRenderer(images=[hamstercover]),
                x=DRAW_DECKS_X + BOX_WIDTH + 2 + 1,
                y=DRAW_DECKS_Y + BOX_HEIGHT // 2,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen,
                StaticRenderer([f"⠀{counts[1]}⠀⠀⠀"]),
                x=DRAW_DECKS_X + BOX_WIDTH + 2 + 1,
                y=DRAW_DECKS_Y + BOX_HEIGHT - 2,
                colour=Screen.COLOUR_YELLOW,
            ),
        ],
    )
