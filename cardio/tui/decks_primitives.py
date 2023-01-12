from typing import Tuple
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.constants import SINGLE_LINE, DOUBLE_LINE
from .constants import *
from .card_primitives import highlight_card_in_grid, highlight_card_at
from .utils import dPos, show_effects
from cardio import GridPos

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
                    BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE
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
                    BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE
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

