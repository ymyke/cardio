import operator
from typing import Literal, Optional
from asciimatics.screen import Screen
from .utils import get_keycode, dPos
from .card_primitives import (
    redraw_card,
    shake_card,
    burn_card,
    show_card,
    BOX_WIDTH,
    BOX_PADDING_LEFT,
    BOX_HEIGHT,
    BOX_PADDING_TOP,
)
from cardio import Card, CardList


class CardPicker:
    def __init__(self, screen: Screen, cards: CardList) -> None:
        self.screen = screen
        self.cards = cards
        self.gross_width = BOX_WIDTH + BOX_PADDING_LEFT
        self.gross_height = BOX_HEIGHT + BOX_PADDING_TOP
        self.cardsperline = self.screen.width // self.gross_width

    def dpos_from_cardindex(self, idx: int) -> dPos:
        # FIXME Should this also accept a `Card`?
        x = (idx % self.cardsperline) * self.gross_width
        y = idx // self.cardsperline * self.gross_height
        assert (
            x < self.screen.width - self.gross_width
            and y < self.screen.height - self.gross_height
        )
        return dPos(x, y)

    def redraw(self, activecards: CardList, highlight: Optional[int] = None) -> None:
        # FIXME Would it be nicer if highlight was Card instead of int?
        activecards = activecards or self.cards
        self.screen.clear_buffer(0, 0, 0)
        for i, card in enumerate(self.cards):
            do_highlight = i == highlight
            show_card(
                self.screen,
                card,
                self.dpos_from_cardindex(i),
                do_highlight,
                inactive=card not in activecards,
            )
        self.screen.refresh()

    def pick(self, activecards: Optional[CardList] = None) -> Card:
        def search(current_cursor: int, dir: Literal[1, -1], offset: int) -> int:
            if dir > 0:
                limit, within = len(self.cards), operator.lt
            else:
                limit, within = 0, operator.ge
            i = current_cursor + dir * offset
            while within(i, limit):
                if self.cards[i] in activecards:  # type:ignore
                    return i
                i += dir
            return current_cursor

        activecards = activecards or self.cards
        cursor = search(-1, 1, 1)
        while True:
            self.redraw(activecards, cursor)
            keycode = get_keycode(self.screen)
            if keycode == 13:  # Return
                return self.cards[cursor]
            if keycode == Screen.KEY_LEFT:
                cursor = search(cursor, -1, 1)
            if keycode == Screen.KEY_RIGHT:
                cursor = search(cursor, 1, 1)
            if keycode == Screen.KEY_DOWN:
                cursor = search(cursor, 1, self.cardsperline)
            if keycode == Screen.KEY_UP:
                cursor = search(cursor, -1, self.cardsperline)

    def confirm(self, card: Card, activecards: Optional[CardList] = None) -> bool:
        activecards = activecards or self.cards
        self.redraw(activecards, self.cards.index(card))
        while True:
            keycode = get_keycode(self.screen)
            if keycode == 13:  # Return
                return True
            if keycode == Screen.KEY_ESCAPE:
                return False

    def shake_card(self, card: Card) -> None:
        pos = self.dpos_from_cardindex(self.cards.index(card))
        redraw_card(self.screen, card, pos)
        shake_card(self.screen, card, pos, "h")

    def burn_card(self, card: Card) -> None:
        pos = self.dpos_from_cardindex(self.cards.index(card))
        burn_card(self.screen, pos)
