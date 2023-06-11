"""TUIFightVnC

All ready-only methods to update the view, show animations, or handle user interaction.
*Must not* modify any model-related information. Everything model-related and any kind
of game-related logic must take place or be orchestrated in FightVnC.
"""

import itertools
from typing import Callable, Literal, Optional
from asciimatics.screen import Screen
from cardio import FightCard, Deck, FightVnC, GridPos, gg
from ..card_primitives import (
    VisualState,
    show_card,
    activate_card,
    burn_card,
    move_card,
    redraw_card,
    shake_card,
    clear_card,
    flash_card,
)
from ..decks_primitives import (
    show_card_to_handdeck,
    show_drawdeck_cursor,
    show_drawdecks,
    redraw_handdeck,
)
from ..grid_primitives import show_empty_grid, show_slot_in_grid
from ..agent_primitives import StateWidget
from ..utils import show_screen_resolution, get_keycode
from ...placement_manager import PlacementManager, PlacementAbortedException
from ..tuibase import TUIBaseMixin


class TUIFightVnC(TUIBaseMixin, FightVnC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if self.debug:
            show_screen_resolution(self.screen)
        self.state_widget = StateWidget(self.screen, self.grid.width, self.damagestate)

    # --- Methods from base class ---

    def redraw_view(
        self,
        cursor: Optional[GridPos] = None,
        drawdeck_cursor: Optional[Literal[0, 1]] = None,
        pmgr: Optional[PlacementManager] = None,
    ) -> None:
        self.screen.clear_buffer(0, 0, 0)
        show_empty_grid(self.screen, self.grid.width)
        all_pos = (
            GridPos(*p)
            for p in itertools.product(
                range(0, len(self.grid.lines)), range(0, self.grid.width)
            )
        )
        for pos in all_pos:
            card = self.grid.get_card(pos)
            if card is not None:
                redraw_card(self.screen, card, pos)
        redraw_handdeck(self.screen, self.decks.hand, 0)
        show_drawdecks(self.screen, self.decks.draw, self.decks.hamster)

        # Marked positions:
        for pos in pmgr.marked_positions if pmgr else []:
            show_card(self.screen, None, pos, VisualState.MARKED)
        # Cursors:
        if cursor:
            if pmgr and pmgr.ready_to_pick():
                state = VisualState.READY
            else:
                state = VisualState.CURSOR
            show_card(self.screen, None, cursor, state)
        if drawdeck_cursor is not None:
            show_drawdeck_cursor(self.screen, drawdeck_cursor)

        self.state_widget.show_all()
        self.screen.refresh()

    # FIXME Can streamline many of the following by using card.get_grid_pos() directly
    def card_died(self, card: FightCard, pos: GridPos) -> None:
        burn_card(self.screen, pos)
        show_slot_in_grid(self.screen, pos)
        self.redraw_view()  # To update agent state

    def card_lost_health(self, card: FightCard) -> None:
        self.redraw_view()

    # QQ: Should the following all be called something with "show"?
    def card_getting_attacked(self, target: FightCard, attacker: FightCard) -> None:
        pos = self.grid.find_card(target)
        assert pos is not None
        shake_card(self.screen, target, pos, "h")

    def card_activate(self, card: FightCard) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None
        activate_card(self.screen, card, pos)

    def card_prepare(self, card: FightCard) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None
        assert pos.line == 0, "Calling prepare on card that is not in prep line"
        clear_card(self.screen, pos)
        show_slot_in_grid(self.screen, pos)
        move_card(
            self.screen, card, from_=GridPos(0, pos.slot), to=GridPos(1, pos.slot)
        )

    def card_deactivate(self, pos: GridPos) -> None:
        self.redraw_view()

    def fight_ends(self, msg: str) -> None:
        self.message(msg)

    # --- Controller-type methods ---

    def show_computer_plays_card(self, card: FightCard, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        move_card(
            self.screen,
            card,
            # from_ is just some point off screen and roughly middle of the grid:
            from_=GridPos(-2, self.grid.width // 2),
            to=to,
            steps=5,
        )

    def show_human_places_card(
        self, card: FightCard, from_slot: int, to_slot: int
    ) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        move_card(
            self.screen, card, from_=GridPos(4, from_slot), to=GridPos(2, to_slot)
        )

    def show_human_receives_card_from_grid(
        self, card: FightCard, from_slot: int
    ) -> None:
        """E.g., for the fertility skill."""
        move_card(
            self.screen,
            card,
            GridPos(2, from_slot),
            GridPos(4, self.decks.hand.size() - 1),
        )

    def handle_human_choose_deck_to_draw_from(self) -> Optional[Deck]:
        """Human player draws a card from one of the draw decks (draw oder hamster)."""
        if not self.decks.draw.is_empty():
            cursor = 0
        elif not self.decks.hamster.is_empty():
            cursor = 1
        else:  # both empty
            return None

        while True:
            self.redraw_view(drawdeck_cursor=cursor)
            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_LEFT and not self.decks.draw.is_empty():
                cursor = 0
            elif keycode == Screen.KEY_RIGHT and not self.decks.hamster.is_empty():
                cursor = 1
            elif keycode in (Screen.KEY_UP, 13):
                return self.decks.draw if cursor == 0 else self.decks.hamster

    def _handle_card_placement_interaction(self, pmgr: PlacementManager) -> None:
        """Human player picks the cards to sacrifice and the location of the target
        card. All orchestrated by `PlacementManager`. Raises `PlacementAbortedException`
        if the process is aborted (either by the code or by the player). Returns
        regularly when the `PlacementManager` is `ready_to_place`.
        """
        if not pmgr.is_placeable():
            raise PlacementAbortedException

        cursor = 0  # Cursor within line 2
        while not pmgr.ready_to_place():
            cursor_pos = GridPos(2, cursor)
            self.redraw_view(cursor=cursor_pos, pmgr=pmgr)

            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(self.grid.width - 1, cursor + 1)
            elif keycode in (Screen.KEY_DOWN, 13):
                if not pmgr.mark_unmark_or_pick(cursor_pos):
                    flash_card(self.screen, cursor_pos)
            elif keycode == Screen.KEY_ESCAPE:
                raise PlacementAbortedException

    def handle_human_plays_cards(self, place_card_callback: Callable) -> None:
        """Human player picks a card from the hand to play. Also handles I key for
        inventory and C to end the turn and start next round of the fight.
        """
        cursor = 0  # Cursor within hand deck
        while True:
            keycode = get_keycode(self.screen)
            if keycode in (ord("i"), ord("I")):
                pass  # FIXME Inventory! !BZL!
            elif keycode in (ord("c"), ord("C")):
                break

            # Everything cursor-related only if hand is not empty:
            if self.decks.hand.is_empty():
                continue
            self.redraw_view(cursor=GridPos(4, cursor))

            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(self.decks.hand.size() - 1, cursor + 1)
            elif keycode in (Screen.KEY_UP, 13):
                pmgr = PlacementManager(
                    grid=self.grid,
                    available_spirits=gg.humanplayer.spirits,
                    target_card=self.decks.hand.cards[cursor],
                )
                try:
                    self._handle_card_placement_interaction(pmgr)
                except PlacementAbortedException:
                    flash_card(self.screen, GridPos(4, cursor))
                else:
                    place_card_callback(pmgr=pmgr, from_slot=cursor)
                    cursor = min(self.decks.hand.size() - 1, cursor)

    def show_human_draws_new_card(
        self, draw_to: Deck, card: FightCard, draw_from: Deck
    ) -> None:
        show_card_to_handdeck(self.screen, draw_to, card, draw_from)
