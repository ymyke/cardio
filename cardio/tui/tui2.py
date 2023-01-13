import logging
import sys
import atexit
from typing import Literal, Optional
from cardio import session, Deck, GridPos, Card, FightViewAndController
from cardio.agent_strategies import AgentStrategy
from cardio.card_blueprints import create_cards_from_blueprints
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from .constants import BOX_HEIGHT, BOX_WIDTH, DRAW_DECKS_X, DRAW_DECKS_Y  # FIXME
from .card_primitives import (
    burn_card_in_grid,
    redraw_card_in_grid,
    shake_card_in_grid,
    activate_card_in_grid,
    move_card,
    render_card_in_grid,
    highlight_card_in_grid,
)
from .grid_primitives import draw_slot_in_grid, draw_grid_decks_separator
from .decks_primitives import (
    draw_drawdeck_highlights,
    draw_handdeck_highlight,
    draw_drawdecks,
)
from .utils import show_effects, draw_screen_resolution, gridpos2dpos, dPos
from .decks import Decks
from .buffercopy import BufferCopy

# FIXME Todos:
# - Finish fight, e.g. cards that die, ...
# - Add other elements:
#   - Switch agent health to agent damage where the difference between the two must be
#     visualized and indicates loss/win if it exceeds 5.
#   - score/health between human and computer
#   - agent state
# - useddeck?
# - More animations needed for Spine and maybe other skills?

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
        burn_card_in_grid(self.screen, card, pos)

    def card_lost_health(self, card: Card) -> None:
        redraw_card_in_grid(self.screen, card, self.grid.find_card(card))

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pos = self.grid.find_card(target)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        shake_card_in_grid(self.screen, target, pos, "h")

    def card_activate(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to burn a card that is not in the grid"
        activate_card_in_grid(self.screen, card, pos)

    def card_prepare(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, "Trying to prepare a card that is not in the grid"
        assert pos.line == 0, "Calling prepare on card that is not in prep line"
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
        activate_card_in_grid(self.screen, card, pos, deactivate=True)

    # --- Methods specifically for TUI ---

    def _play_computer_card(self, card: Card, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        move_card(
            self.screen,
            card,
            # from_ is just some point off screen and roughly middle of the grid:
            from_=GridPos(-2, self.grid.width // 2),
            to=to,
            steps=5,
        )

    def _place_human_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        move_card(
            self.screen, card, from_=GridPos(4, from_slot), to=GridPos(2, to_slot)
        )

    def _redraw_handdeck(self, handdeck: Deck, from_index: int) -> None:
        """Redraw hand from index `from_index`."""
        pos = gridpos2dpos(GridPos(4, from_index))
        self.screen.clear_buffer(
            # FIXME Add some primitive for this? Either in buffercopy/bufferutils or
            # some clear_handdeck function in the primitives module?
            Screen.COLOUR_WHITE,
            0,
            0,
            x=pos.x,
            y=pos.y,
            w=self.screen.width - pos.x,
            h=BOX_HEIGHT,
        )
        for i, card in list(enumerate(handdeck.cards))[from_index:]:
            show_effects(
                self.screen, render_card_in_grid(self.screen, card, GridPos(4, i))
            )
        self.screen.refresh()

    def _draw_card_to_handdeck(
        self, handdeck: Deck, card: Card, whichdeck: Literal["draw", "hamster"]
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
            self.screen,
            card,
            from_=dPos(startx, starty),
            to=GridPos(4, handdeck.size()),
            steps=5,
        )

    def _draw_empty_grid(self) -> None:
        for linei in range(3):
            for sloti in range(4):
                draw_slot_in_grid(self.screen, GridPos(linei, sloti))
        draw_grid_decks_separator(self.screen, 4)
        # FIXME Paremetrize width (don't forget to do that also in the base class if I
        # add parameters or something)

    def _get_keycode(self) -> Optional[int]:
        """Non-blocking. Ignores all mouse events. Returns `ord` value of key pressed,
        `None` if no key pressed. Special keys are encoded according to
        `asciimatics.screen.Screen.KEY_*`.
        """
        event = self.screen.get_event()
        if not isinstance(event, KeyboardEvent):
            return None
        if event.key_code == ord("$"):
            sys.exit(0)
        return event.key_code
        # FIXME Add a tiny sleep here (and some do_pause parameter) in case there is no
        # key so the while loops don't load CPU that much?

    # --- Controller-type methods ---

    def _handle_human_draws_new_card(self) -> None:
        if not self.decks.drawdeck.is_empty():
            highlights = (True, False)
        elif not self.decks.hamsterdeck.is_empty():
            highlights = (False, True)
        else:  # both empty
            return

        while True:
            draw_drawdeck_highlights(self.screen, highlights)
            keycode = self._get_keycode()
            if keycode == Screen.KEY_LEFT and not self.decks.drawdeck.is_empty():
                highlights = (True, False)
            elif keycode == Screen.KEY_RIGHT and not self.decks.hamsterdeck.is_empty():
                highlights = (False, True)
            elif keycode == Screen.KEY_UP:
                if highlights[0]:
                    card = self.decks.drawdeck.draw_card()
                    self._draw_card_to_handdeck(self.decks.handdeck, card, "draw")
                else:
                    card = self.decks.hamsterdeck.draw_card()
                    self._draw_card_to_handdeck(self.decks.handdeck, card, "hamster")

                self.decks.handdeck.add_card(card)
                draw_drawdecks(
                    self.screen,
                    (self.decks.drawdeck.size(), self.decks.hamsterdeck.size()),
                )
                return

    def _handle_human_places_card(self, card: Card, from_slot: int) -> bool:
        buffercopy = BufferCopy(self.screen)
        cursor = 0  # Cursor within line 2
        while True:
            buffercopy.copyback()
            highlight_card_in_grid(self.screen, GridPos(2, cursor))

            keycode = self._get_keycode()
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(session.grid.width - 1, cursor + 1)
            elif keycode == Screen.KEY_DOWN:
                # FIXME Check if card can be placed at all
                session.grid[2][cursor] = card
                self._place_human_card(card, from_slot=from_slot, to_slot=cursor)
                self.decks.useddeck.add_card(card)
                logging.debug("Human plays %s in %s", card.name, cursor)
                return True
            elif keycode == Screen.KEY_ESCAPE:
                buffercopy.copyback()
                return False

    def _handle_human_plays_card(self) -> None:
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

            keycode = self._get_keycode()
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(self.decks.handdeck.size() - 1, cursor + 1)
            elif keycode == Screen.KEY_UP:
                # FIXME Check if card is playable at all
                # Don't pick the card yet (i.e., don't remove it from the deck yet)
                # because the player might still abort the placing  of the card:
                card = self.decks.handdeck.cards[cursor]
                res = self._handle_human_places_card(card, cursor)
                if res:
                    self.decks.handdeck.pick_card(cursor)
                    cursor = min(self.decks.handdeck.size() - 1, cursor)
                    self._redraw_handdeck(self.decks.handdeck, cursor)
                    buffercopy.update()
                else:
                    # Otherwise, we return bc the process was aborted by the user and won't
                    # update the cursor.
                    # FIXME Implement this w an exception rather than the True/False
                    # mechanics?
                    pass
            elif keycode in (ord("i"), ord("I")):
                pass  # FIXME Inventory!
            elif keycode in (ord("c"), ord("C")):
                buffercopy.copyback()
                return

    def _handle_round_of_fight(self) -> bool:
        self.decks.log()

        # Play computer cards and animate how they appear:
        for pos, card in self.computerstrategy.cards_to_be_played(
            session.grid, self.round_num
        ):
            self._play_computer_card(card, pos)
        # Now also place them in the model:
        self.computerstrategy.play_cards(session.grid, self.round_num)

        # Let human draw a card:
        self._handle_human_draws_new_card()

        # Let human play card(s) from handdeck or items in his collection:
        self._handle_human_plays_card()

        self.decks.log()
        session.grid.log()

        # Activate all cards:
        session.grid.activate_line(2)
        session.grid.activate_line(1)
        session.grid.prepare_line()

        # FIXME Still some things missing below:
        if session.humanagent.has_lost_life():
            session.humanagent.update_lives_and_health_after_death()
            self.computer_wins_fight()
            return False
        if session.computeragent.has_lost_life():
            overflow = session.computeragent.update_lives_and_health_after_death()
            self.human_wins_fight()
            # FIXME Do something w overflow damage here -- maybe just store it in the
            # object right in the update_lives_and_health_after_death function but also
            # pass it to the view for some animation?
            return False
        if session.grid.is_empty():
            # QQ: Should this also break when the grid is "powerless", i.e., no cards
            # with >0 power?
            return False

        session.grid.log()
        return True

    def _setup_and_draw_decks(self) -> None:
        # Set up the 4 decks for the fight:
        drawdeck = Deck()
        drawdeck.cards = session.humanagent.deck.cards
        drawdeck.shuffle()
        hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
        self.decks = Decks(drawdeck, hamsterdeck, Deck(), Deck())

        # Draw the decks and how the first cards get drawn:
        draw_drawdecks(
            self.screen, (self.decks.drawdeck.size(), self.decks.hamsterdeck.size())
        )
        for _ in range(3):
            card = self.decks.drawdeck.draw_card()
            self._draw_card_to_handdeck(self.decks.handdeck, card, "draw")
            self.decks.handdeck.add_card(card)
        card = self.decks.hamsterdeck.draw_card()
        self._draw_card_to_handdeck(self.decks.handdeck, card, "hamster")
        self.decks.handdeck.add_card(card)
        draw_drawdecks(
            self.screen, (self.decks.drawdeck.size(), self.decks.hamsterdeck.size())
        )

    def _reset_human_deck(self) -> None:
        session.humanagent.deck.cards = [
            c
            for c in self.decks.useddeck.cards
            + self.decks.handdeck.cards
            + self.decks.drawdeck.cards
            if c.name != "Hamster"
        ]
        session.humanagent.deck.reset_cards()

    def handle_fight(self, computerstrategy: AgentStrategy) -> None:
        self.computerstrategy = computerstrategy
        # ^ FIXME Should this be in __init__? And/or the entire ComputerAgent object,
        # which could contain the computerstrategy? It will be used for one fight only
        # anyway...
        self._draw_empty_grid()
        self._setup_and_draw_decks()

        # Run the fight:
        fighting = True
        self.round_num = 0
        while fighting:
            fighting = self._handle_round_of_fight()
            self.round_num += 1

        self._reset_human_deck()


# FIXME Check if anything should be taken over from handlers.
# FIXME Check if anything should be taken over from tui.
# FIXME Check if anything should be taken over from Fight.
# FIXME Untangle what is UI/view from what is controller/business logic here.
# FIXME Delete tui, fight, some/all of the old handlers, ...?
# FIXME Check all the signatures in this module and in the primitives module to see if
# type information is complete and correct.
