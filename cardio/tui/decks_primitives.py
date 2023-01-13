from typing import Tuple

from asciimatics.constants import SINGLE_LINE
from asciimatics.effects import Print
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.screen import Screen

from cardio import GridPos

from .constants import *
from .card_primitives import highlight_card
from .utils import dPos, show_effects


def draw_handdeck_highlight(screen: Screen, slot: int, highlight: bool = True) -> None:
    highlight_card(screen, GridPos(4, slot), highlight)


def draw_drawdeck_highlights(screen: Screen, highlights: Tuple[bool, bool]) -> None:
    highlight_card(screen, dPos(DRAW_DECKS_X, DRAW_DECKS_Y), highlights[0])
    highlight_card(
        screen, dPos(DRAW_DECKS_X + BOX_WIDTH + 2, DRAW_DECKS_Y), highlights[1]
    )


def draw_drawdecks(screen: Screen, counts: Tuple[int, int]) -> None:
    DRAWCOVER = "    ⬆️⬆️⬆️⬆️⬆️⬆️⬆⬆️⬆️"
    HAMSTERCOVER = "      🐹🐹🐹"
    show_effects(
        screen,
        [
            Print(
                screen=screen,
                renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
                x=DRAW_DECKS_X,
                y=DRAW_DECKS_Y,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen=screen,
                renderer=StaticRenderer(images=[DRAWCOVER]),
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
                renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
                x=DRAW_DECKS_X + BOX_WIDTH + 2,
                y=DRAW_DECKS_Y,
                colour=Screen.COLOUR_YELLOW,
            ),
            Print(
                screen=screen,
                renderer=StaticRenderer(images=[HAMSTERCOVER]),
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
