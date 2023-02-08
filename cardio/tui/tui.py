import atexit
import itertools
from typing import Optional

from asciimatics.screen import Screen

from cardio import Card, Deck, FightVnC, GridPos, session

from .bufferutils import BufferCopy, BufferedScreen
from .card_primitives import (
    activate_card,
    burn_card,
    highlight_card,
    move_card,
    redraw_card,
    shake_card,
    clear_card,
)
from .decks_primitives import (
    show_card_to_handdeck,
    show_drawdeck_highlights,
    show_drawdecks,
    show_handdeck_highlight,
    redraw_handdeck,
)
from .grid_primitives import show_empty_grid, show_slot_in_grid
from .agent_primitives import StateWidget
from .placement_manager import PlacementManager, PlacementAbortedException
from .utils import show_screen_resolution, get_keycode


class TUIFightVnC(FightVnC):
    def __init__(self, debug: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.screen = BufferedScreen()
        self.debug = debug
        if self.debug:
            show_screen_resolution(self.screen())
        atexit.register(self.close)
        self.state_widget = StateWidget(self.screen, self.grid.width, self.damagestate)

    def close(self) -> None:
        self.screen.close()

    # --- Methods from base class ---

    def redraw_view(self) -> None:
        # Switch to off-screen as main screen:
        self.screen.buffer_on()
        # Make all the updates on the off-screen:
        self.screen().clear()
        self.show_empty_grid(self.grid.width)
        all_pos = (
            GridPos(*p)
            for p in itertools.product(
                range(0, len(self.grid.lines)), range(0, self.grid.width)
            )
        )
        for pos in all_pos:
            card = self.grid.get_card(pos)
            if card is not None:
                redraw_card(self.screen(), card, pos)
        redraw_handdeck(self.screen(), self.decks.handdeck, 0)
        self.show_drawdecks(self.decks.drawdeck, self.decks.hamsterdeck)
        self.show_agents_state()
        # Switch back:
        self.screen.buffer_off()

    def card_died(self, card: Card, pos: GridPos) -> None:
        burn_card(self.screen(), pos)
        session.humanplayer.spirits += (
            card.has_spirits
        )  # TODO BZL -- add this to Card class?
        self.show_agents_state()

    def card_lost_health(self, card: Card) -> None:
        redraw_card(self.screen(), card, self.grid.find_card(card))

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pos = self.grid.find_card(target)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        shake_card(self.screen(), target, pos, "h")

    def card_activate(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        activate_card(self.screen(), card, pos)

    def card_prepare(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to prepare a card that is not in the grid"
        assert pos.line == 0, "Calling prepare on card that is not in prep line"
        clear_card(self.screen(), pos)
        show_slot_in_grid(self.screen(), pos)
        move_card(
            self.screen(), card, from_=GridPos(0, pos.slot), to=GridPos(1, pos.slot)
        )

    def pos_card_deactivate(self, pos: GridPos) -> None:
        card = self.grid.get_card(pos)
        assert card is not None
        activate_card(self.screen(), card, pos, deactivate=True)

    # --- Controller-type methods ---

    def show_computer_plays_card(self, card: Card, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        move_card(
            self.screen(),
            card,
            # from_ is just some point off screen and roughly middle of the grid:
            from_=GridPos(-2, self.grid.width // 2),
            to=to,
            steps=5,
        )

    def show_human_places_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        move_card(
            self.screen(), card, from_=GridPos(4, from_slot), to=GridPos(2, to_slot)
        )

    def handle_human_choose_deck_to_draw_from(self) -> Optional[Deck]:
        """Human player draws a card from one of the draw decks (draw oder hamster)."""
        if not self.decks.drawdeck.is_empty():
            highlights = (True, False)
        elif not self.decks.hamsterdeck.is_empty():
            highlights = (False, True)
        else:  # both empty
            return None

        while True:
            show_drawdeck_highlights(self.screen(), highlights)
            keycode = get_keycode(self.screen())
            if keycode == Screen.KEY_LEFT and not self.decks.drawdeck.is_empty():
                highlights = (True, False)
            elif keycode == Screen.KEY_RIGHT and not self.decks.hamsterdeck.is_empty():
                highlights = (False, True)
            elif keycode == Screen.KEY_UP:
                return self.decks.drawdeck if highlights[0] else self.decks.hamsterdeck

    def _handle_human_places_card(
        self, from_slot: int, place_card_callback
    ) -> None:  # TODO Add type hints
        """Human player places a card she chose from her handdeck in her line. Raises
        `PlacementAbortedException` if the process is aborted (either by the code or by
        the player).
        """
        target_card = self.decks.handdeck.cards[from_slot]
        pmgr = PlacementManager(self.grid, session.humanplayer.spirits, target_card)
        # TODO get the placement mgr as a parameter?
        if not pmgr.is_placeable():
            # LIXME Add some animation / user feedback here?
            raise PlacementAbortedException

        buffercopy = BufferCopy(self.screen())
        cursor = 0  # Cursor within line 2
        while not pmgr.ready_to_place():
            buffercopy.copyback()
            cursor_pos = GridPos(2, cursor)
            highlight_card(self.screen(), cursor_pos)

            keycode = get_keycode(self.screen())
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(self.grid.width - 1, cursor + 1)
            elif keycode == Screen.KEY_DOWN:
                if pmgr.is_marked(cursor_pos):
                    pmgr.unmark_pos(cursor_pos)
                elif pmgr.can_mark(cursor_pos):
                    pmgr.mark_pos(cursor_pos)
                    buffercopy.update()
            elif keycode == Screen.KEY_ESCAPE:
                buffercopy.copyback()
                raise PlacementAbortedException
        # TODO => postcondition: pmgr that is ready w/ sacrifice positions and a target_card
        place_card_callback(pmgr, from_slot)
        # TODO Is the callback really a good solution here?
        # Now ready to place:
        # TODO should this even return a placement mgr?

    def handle_human_plays_card(
        self, place_card_callback
    ) -> None:  # TODO Add type hints
        """Human player picks a card from the hand to play. Also handles I key for
        inventory and C to end the turn and start next round of the fight.
        """
        buffercopy = BufferCopy(self.screen())
        cursor = 0  # Cursor within hand deck
        while True:
            buffercopy.copyback()
            keycode = get_keycode(self.screen())
            if keycode in (ord("i"), ord("I")):
                pass  # FIXME Inventory!
                # TODO  BZL
            elif keycode in (ord("c"), ord("C")):
                buffercopy.copyback()
                break

            # Everything cursor-related only if hand is not empty:
            if self.decks.handdeck.is_empty():
                continue
            show_handdeck_highlight(self.screen(), cursor)
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(self.decks.handdeck.size() - 1, cursor + 1)
            elif keycode == Screen.KEY_UP:
                try:
                    # TODO Get and send _place_card callback
                    # TODO Create and send placement mgr
                    self._handle_human_places_card(
                        cursor, place_card_callback=place_card_callback
                    )  # TODO  BZL
                    cursor = min(self.decks.handdeck.size() - 1, cursor)
                    buffercopy.update()
                except PlacementAbortedException:
                    pass

    def show_empty_grid(self, grid_width: int) -> None:
        show_empty_grid(self.screen(), grid_width)

    def show_drawdecks(self, drawdeck: Deck, hamsterdeck: Deck) -> None:
        show_drawdecks(self.screen(), self.decks.drawdeck, self.decks.hamsterdeck)

    def show_card_to_handdeck(
        self, handdeck: Deck, card: Card, whichdeck: Deck
    ) -> None:
        deckname = "draw" if whichdeck == self.decks.drawdeck else "hamster"
        show_card_to_handdeck(self.screen(), handdeck, card, deckname)
        # FIXME Add a name to the Deck class and pass the deck and use the name attribute in show_card_to_handdeck?
        show_drawdecks(self.screen(), self.decks.drawdeck, self.decks.hamsterdeck)

    def show_agents_state(self) -> None:
        self.state_widget.show_all()
