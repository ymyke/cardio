import atexit
from typing import List, Optional
from asciimatics.screen import Screen
from ..utils import get_keycode, dPos
from ... import Card
from ..card_primitives import (
    redraw_card,
    show_card,
    shake_card,
    burn_card,
    BOX_WIDTH,
    BOX_PADDING_LEFT,
    BOX_HEIGHT,
    BOX_PADDING_TOP,
)


class TUIUpgraderView:
    def __init__(self, cards: List[Card], debug: bool = False) -> None:
        # TODO Code redundancies w TUIFightVnC & TUIMapView -- Change these to all use
        # the same sceen (i.e., pass some screen object to the initializer)? Or the same
        # code (i.e., inherit from some TUIScreen class or mixin?)
        self.cards = cards
        self.debug = debug
        self.screen = Screen.open(unicode_aware=True)
        self.gross_width = BOX_WIDTH + BOX_PADDING_LEFT
        self.gross_height = BOX_HEIGHT + BOX_PADDING_TOP
        self.cardsperline = self.screen.width // self.gross_width

        atexit.register(self.close)

    def close(self) -> None:
        self.screen.close()

    def dpos_from_cardindex(self, idx: int) -> dPos:
        x = (idx % self.cardsperline) * self.gross_width
        y = idx // self.cardsperline * self.gross_height
        assert (
            x < self.screen.width - self.gross_width
            and y < self.screen.height - self.gross_height
        )
        return dPos(x, y)

    def redraw(self, highlight: Optional[int] = None) -> None:
        self.screen.clear_buffer(0, 0, 0)
        for i, card in enumerate(self.cards):
            do_highlight = i == highlight
            show_card(self.screen, card, self.dpos_from_cardindex(i), do_highlight)
        self.screen.refresh()

    def show_upgrade(self, card: Card) -> None:
        pos = self.dpos_from_cardindex(self.cards.index(card))
        redraw_card(self.screen, card, pos)
        shake_card(self.screen, card, pos, "h")

    def show_destroy(self, card: Card) -> None:
        pos = self.dpos_from_cardindex(self.cards.index(card))
        burn_card(self.screen, pos)

    def pick(self) -> Card:
        cursor = 0
        while True:
            self.redraw(cursor)
            keycode = get_keycode(self.screen)
            if keycode == 13:  # Return
                return self.cards[cursor]
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            if keycode == Screen.KEY_RIGHT:
                cursor = min(len(self.cards) - 1, cursor + 1)
            if keycode == Screen.KEY_DOWN:
                cursor = min(len(self.cards) - 1, cursor + self.cardsperline)
            if keycode == Screen.KEY_UP:
                cursor = max(0, cursor - self.cardsperline)

    def ask(self, card: Card) -> bool:
        self.redraw(self.cards.index(card))
        while True:
            keycode = get_keycode(self.screen)
            if keycode == 13:  # Return
                return True
            if keycode == Screen.KEY_ESCAPE:
                return False
