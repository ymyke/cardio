import atexit
import logging
from typing import Literal

from asciimatics.screen import Screen

from cardio import Card, Deck, FightViewAndController, GridPos, session
from cardio.agent_strategies import AgentStrategy
from cardio.card_blueprints import create_cards_from_blueprints

from .buffercopy import BufferCopy
from .card_primitives import (
    activate_card,
    burn_card,
    highlight_card,
    move_card,
    redraw_card,
    shake_card,
    clear_card,
)
from .decks import Decks  # FIXME Move to utils?
from .decks_primitives import (
    draw_card_to_handdeck,
    draw_drawdeck_highlights,
    draw_drawdecks,
    draw_handdeck_highlight,
    redraw_handdeck,
)
from .grid_primitives import draw_empty_grid, draw_slot_in_grid
from .utils import draw_screen_resolution, get_keycode

# FIXME Todos:
# - Finish fight, e.g. cards that die, ...
# - Add other elements:
#   - Switch agent health to agent damage where the difference between the two must be
#     visualized and indicates loss/win if it exceeds 5.
#   - score/health between human and computer
#   - agent state
# - useddeck?
# - More animations needed for Spine and maybe other skills?

# FIXME Check all occurences of `session` and check if I can get rid of it via init or
# so.
# FIXME How would a HumanAgentStrategy (aka automated human) be implemented here?

# FIXME Should be TUIFightVnC
class TUIViewAndController(FightViewAndController):
    def __init__(self, debug: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.screen = Screen.open(unicode_aware=True)
        self.debug = debug
        if self.debug:
            draw_screen_resolution(self.screen)
        atexit.register(self.close)

    def close(self) -> None:
        self.screen.close()

    # --- Methods from base class ---

    def card_about_to_die(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        burn_card(self.screen, pos)

    def card_lost_health(self, card: Card) -> None:
        redraw_card(self.screen, card, self.grid.find_card(card))

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pos = self.grid.find_card(target)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        shake_card(self.screen, target, pos, "h")

    def card_activate(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        activate_card(self.screen, card, pos)

    def card_prepare(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to prepare a card that is not in the grid"
        assert pos.line == 0, "Calling prepare on card that is not in prep line"
        clear_card(self.screen, pos)
        draw_slot_in_grid(self.screen, pos)
        move_card(
            self.screen, card, from_=GridPos(0, pos.slot), to=GridPos(1, pos.slot)
        )

    def pos_card_deactivate(self, pos: GridPos) -> None:
        """Uses a position instead of a card because it could be that the card has died
        and been removed from the grid between being activated and deactivated. In this
        case, `pos` should point to where the card used to be before being removed.
        """
        # FIXME Needs to be adjusted so it works also in cases such as the one described
        # above.
        card = self.grid[pos.line][pos.slot]
        activate_card(self.screen, card, pos, deactivate=True)

    # --- Controller-type methods ---

    def draw_computer_plays_card(self, card: Card, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        move_card(
            self.screen,
            card,
            # from_ is just some point off screen and roughly middle of the grid:
            from_=GridPos(-2, self.grid.width // 2),
            to=to,
            steps=5,
        )

    def draw_human_places_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        move_card(
            self.screen, card, from_=GridPos(4, from_slot), to=GridPos(2, to_slot)
        )

    def handle_human_draws_new_card(self) -> None:
        """Human player draws a card from one of the draw decks (draw oder hamster)."""
        if not self.decks.drawdeck.is_empty():
            highlights = (True, False)
        elif not self.decks.hamsterdeck.is_empty():
            highlights = (False, True)
        else:  # both empty
            return

        while True:
            draw_drawdeck_highlights(self.screen, highlights)
            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_LEFT and not self.decks.drawdeck.is_empty():
                highlights = (True, False)
            elif keycode == Screen.KEY_RIGHT and not self.decks.hamsterdeck.is_empty():
                highlights = (False, True)
            elif keycode == Screen.KEY_UP:
                if highlights[0]:
                    deck = self.decks.drawdeck
                    deckname = "draw"
                else:
                    deck = self.decks.hamsterdeck
                    deckname = "hamster"
                card = deck.draw_card()
                draw_card_to_handdeck(self.screen, self.decks.handdeck, card, deckname)
                self.decks.handdeck.add_card(card)
                draw_drawdecks(self.screen, self.decks.drawdeck, self.decks.hamsterdeck)
                return

    def _handle_human_places_card(self, card: Card, from_slot: int) -> bool:
        """Human player places a card she chose from her handdeck in her line. Returns
        `True` if the card was actually placed, `False` otherweise (i.e., player aborted
        via Escape key).
        """
        buffercopy = BufferCopy(self.screen)
        cursor = 0  # Cursor within line 2
        while True:
            buffercopy.copyback()
            highlight_card(self.screen, GridPos(2, cursor))
            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(session.grid.width - 1, cursor + 1)
            elif keycode == Screen.KEY_DOWN:
                # FIXME Check if card can be placed at all
                session.grid[2][cursor] = card
                self.draw_human_places_card(card, from_slot=from_slot, to_slot=cursor)
                self.decks.useddeck.add_card(card)
                logging.debug("Human plays %s in %s", card.name, cursor)
                return True
            elif keycode == Screen.KEY_ESCAPE:
                buffercopy.copyback()
                return False

    def handle_human_plays_card(self) -> None:
        """Human player picks a card from the hand to play. Also handles I key for
        inventory and C to end the turn and start next round of the fight.
        """
        # FIXME What if hand is empty?
        buffercopy = BufferCopy(self.screen)
        cursor = 0  # Cursor within hand deck
        while True:
            buffercopy.copyback()
            if not self.decks.handdeck.is_empty():
                draw_handdeck_highlight(self.screen, cursor)
            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(self.decks.handdeck.size() - 1, cursor + 1)
            elif keycode == Screen.KEY_UP:
                # FIXME Check if card is playable at all
                # Don't pick the card yet (i.e., don't remove it from the deck yet)
                # because the player might still abort the placing  of the card:
                card = self.decks.handdeck.cards[cursor]
                has_placed = self._handle_human_places_card(card, cursor)
                if has_placed:
                    self.decks.handdeck.pick_card(cursor)
                    cursor = min(self.decks.handdeck.size() - 1, cursor)
                    redraw_handdeck(self.screen, self.decks.handdeck, cursor)
                    buffercopy.update()
                else:
                    # Otherwise, we return bc the process was aborted by the user and
                    # won't update the cursor.
                    # FIXME Implement this w an exception rather than the True/False
                    # mechanics?
                    pass
            elif keycode in (ord("i"), ord("I")):
                pass  # FIXME Inventory!
            elif keycode in (ord("c"), ord("C")):
                buffercopy.copyback()
                return

    def draw_empty_grid(self, grid_width: int) -> None:
        draw_empty_grid(self.screen, grid_width)

    def draw_drawdecks(self, drawdeck: Deck, hamsterdeck: Deck) -> None:
        draw_drawdecks(self.screen, self.decks.drawdeck, self.decks.hamsterdeck)

    def draw_card_to_handdeck(
        self, handdeck: Deck, card: Card, whichdeck: Literal["draw", "hamster"]
    ) -> None:
        draw_card_to_handdeck(self.screen, handdeck, card, whichdeck)


# FIXME Check if anything should be taken over from handlers.
# FIXME Delete tui, fight, some/all of the old handlers, ...?
