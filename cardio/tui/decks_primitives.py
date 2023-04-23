from typing import Literal, Tuple
from asciimatics.screen import Screen
from cardio import GridPos, Deck, Card
from .constants import *
from .card_primitives import show_card, move_card, VisualState
from .utils import dPos, show_text, show_box


def show_drawdeck_cursor(screen: Screen, cursor: Literal[0, 1]) -> None:
    pos = dPos(DRAW_DECKS_X, DRAW_DECKS_Y)
    if cursor == 0:
        state0, state1 = VisualState.CURSOR, VisualState.NORMAL
    else:
        state0, state1 = VisualState.NORMAL, VisualState.CURSOR
    show_card(screen, None, pos, state0)
    show_card(screen, None, pos + (BOX_WIDTH + 2, 0), state1)


def show_drawdecks(screen: Screen, drawdeck: Deck, hamsterdeck: Deck) -> None:
    DRAWCOVER = "    ⬆️⬆️⬆️⬆️⬆️⬆️⬆⬆️⬆️"
    HAMSTERCOVER = "      🐹🐹🐹"
    pos = dPos(DRAW_DECKS_X, DRAW_DECKS_Y)
    show_box(screen, pos)
    show_text(screen, pos + (1, BOX_HEIGHT // 2), DRAWCOVER, Color.YELLOW)
    show_text(screen, pos + (1, BOX_HEIGHT - 2), f"⠀{drawdeck.size()}⠀⠀⠀", Color.YELLOW)
    show_box(screen, pos + (BOX_WIDTH + 2, 0))
    show_text(
        screen, pos + (BOX_WIDTH + 2 + 1, BOX_HEIGHT // 2), HAMSTERCOVER, Color.YELLOW
    )
    show_text(
        screen,
        pos + (BOX_WIDTH + 2 + 1, BOX_HEIGHT - 2),
        f"⠀{hamsterdeck.size()}⠀⠀⠀",
        Color.YELLOW,
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


def show_card_to_handdeck(
    screen: Screen, handdeck: Deck, card: Card, from_deck: Deck
) -> None:
    """Show how a card gets drawn from one of the draw decks and moved to the hand."""
    assert from_deck.name in ("Draw", "Hamster")
    starty = DRAW_DECKS_Y - 2
    # (^ When we put `-1` here, there will be a leftover `-` on the screen after moving
    # the cards. How to get rid of that?)
    startx = DRAW_DECKS_X if from_deck.name == "Draw" else DRAW_DECKS_X + BOX_WIDTH + 2
    move_card(
        screen,
        card,
        from_=dPos(startx, starty),
        to=GridPos(4, handdeck.size()),
        steps=5,
    )
