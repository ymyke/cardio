from typing import Literal, Tuple
from functools import partial

from asciimatics.constants import SINGLE_LINE
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.screen import Screen

from cardio import GridPos, Deck, Card

from .constants import *
from .card_primitives import highlight_card, show_card, move_card
from .utils import dPos, show


def show_handdeck_highlight(screen: Screen, slot: int, highlight: bool = True) -> None:
    highlight_card(screen, GridPos(4, slot), highlight)


def show_drawdeck_highlights(screen: Screen, highlights: Tuple[bool, bool]) -> None:
    highlight_card(screen, dPos(DRAW_DECKS_X, DRAW_DECKS_Y), highlights[0])
    highlight_card(
        screen, dPos(DRAW_DECKS_X + BOX_WIDTH + 2, DRAW_DECKS_Y), highlights[1]
    )


def show_drawdecks(screen: Screen, drawdeck: Deck, hamsterdeck: Deck) -> None:
    DRAWCOVER = "    ⬆️⬆️⬆️⬆️⬆️⬆️⬆⬆️⬆️"
    HAMSTERCOVER = "      🐹🐹🐹"
    yellow_show = partial(show, screen=screen, color=Color.YELLOW)
    yellow_show(
        renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
        pos=dPos(DRAW_DECKS_X, DRAW_DECKS_Y),
    )
    yellow_show(
        renderer=StaticRenderer(images=[DRAWCOVER]),
        pos=dPos(DRAW_DECKS_X + 1, DRAW_DECKS_Y + BOX_HEIGHT // 2),
    )
    yellow_show(
        renderer=StaticRenderer([f"⠀{drawdeck.size()}⠀⠀⠀"]),
        pos=dPos(DRAW_DECKS_X + 1, y=DRAW_DECKS_Y + BOX_HEIGHT - 2),
    )
    yellow_show(
        renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=SINGLE_LINE),
        pos=dPos(DRAW_DECKS_X + BOX_WIDTH + 2, DRAW_DECKS_Y),
    )
    yellow_show(
        renderer=StaticRenderer(images=[HAMSTERCOVER]),
        pos=dPos(DRAW_DECKS_X + BOX_WIDTH + 2 + 1, DRAW_DECKS_Y + BOX_HEIGHT // 2),
    )
    yellow_show(
        renderer=StaticRenderer([f"⠀{hamsterdeck.size()}⠀⠀⠀"]),
        pos=dPos(DRAW_DECKS_X + BOX_WIDTH + 2 + 1, DRAW_DECKS_Y + BOX_HEIGHT - 2),
    )


def redraw_handdeck(screen: Screen, handdeck: Deck, from_index: int) -> None:
    """Redraw hand from index `from_index`."""
    pos = dPos.from_gridpos(GridPos(4, from_index))
    screen.clear_buffer(
        Screen.COLOUR_WHITE,
        0,
        0,
        x=pos.x,
        y=pos.y,
        w=screen.width - pos.x,
        h=BOX_HEIGHT,
    )
    for i, card in list(enumerate(handdeck.cards))[from_index:]:
        show_card(screen, card, GridPos(4, i))
    screen.refresh()


def show_card_to_handdeck(
    screen: Screen, handdeck: Deck, card: Card, whichdeck: Literal["draw", "hamster"]
) -> None:
    """Show how a card gets drawn from one of the draw decks and moved to the hand.
    `whichdeck` is necessary to know which location to start from.
    """
    # FIXME Maybe implement differently in the future when cards have states: can
    # use those states for `whichdeck`.
    starty = DRAW_DECKS_Y - 2
    # FIXME ^ When we put `-1` here, there will be a leftover `-` on the screen
    # after moving the cards. How to get rid of that?
    startx = DRAW_DECKS_X if whichdeck == "draw" else DRAW_DECKS_X + BOX_WIDTH + 2
    move_card(
        screen,
        card,
        from_=dPos(startx, starty),
        to=GridPos(4, handdeck.size()),
        steps=5,
    )
