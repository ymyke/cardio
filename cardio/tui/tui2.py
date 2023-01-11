import logging
import sys
import time
import atexit
import copy
from typing import Literal, NamedTuple, Optional, Tuple
from cardio import session, Deck, GridPos, Card, FightViewAndController
from cardio.agent_strategies import AgentStrategy
from cardio.card_blueprints import create_cards_from_blueprints
from asciimatics.screen import Screen
from asciimatics.paths import Path
from asciimatics.event import KeyboardEvent
from .cards_renderer import (
    draw_slot_in_grid,
    draw_drawdecks,
    draw_screen_resolution,
    draw_drawdeck_highlights,
    draw_handdeck_highlight,
    highlight_card_in_grid,
    gridpos2dpos,
    clear_card_in_grid,
    flash_card_in_grid,
    shake_card_in_grid,
    redraw_card_in_grid,
    activate_card_in_grid,
    burn_card_in_grid,
    draw_grid_decks_separator,
    BOX_HEIGHT,  # FIXME
    BOX_WIDTH,  # FIXME
)
from . import cards_renderer

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


class Decks(NamedTuple):
    # QQ: Maybe unnecesary if I refactor decks implicitly via some `state` attribute in
    # the card.
    drawdeck: Deck
    hamsterdeck: Deck
    handdeck: Deck
    useddeck: Deck


def log_decks(decks: Decks):
    for deck, name in zip(
        [decks.handdeck, decks.drawdeck, decks.hamsterdeck, decks.useddeck],
        ["Hand", "Fight", "Hamster", "Used"],
    ):
        logging.debug(
            "%sdeck size: %s (%s)",
            name,
            len(deck.cards),
            ",".join([c.name for c in deck.cards]),
        )


def log_grid(grid):
    for line in range(3):
        logging.debug("Grid line %s: %s", line, ", ".join([str(c) for c in grid[line]]))


def setup_decks() -> Decks:
    drawdeck = Deck()
    drawdeck.cards = session.humanagent.deck.cards
    drawdeck.shuffle()
    hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
    return Decks(drawdeck, hamsterdeck, Deck(), Deck())


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
        startpos = gridpos2dpos(GridPos(0, pos.slot))
        targetpos = gridpos2dpos(GridPos(1, pos.slot))

        clear_card_in_grid(self.screen, pos)
        draw_slot_in_grid(self.screen, pos)
        buffer = copy.deepcopy(self.screen._buffer._double_buffer)
        p = Path()
        p.jump_to(x=startpos.x, y=startpos.y + 1)
        p.move_straight_to(x=targetpos.x, y=targetpos.y, steps=10)
        for x, y in p._steps:
            self.screen._buffer._double_buffer = copy.deepcopy(buffer)
            self.screen.refresh()
            cards_renderer.show_effects(
                self.screen, cards_renderer.render_card_at(self.screen, card, x, y)
            )
        # FIXME Factor out buffer & move functionality

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

    def play_computer_card(self, card: Card, to_pos: GridPos) -> None:
        """Play a computer card to `to_pos`, which can be in line 0 or 1."""
        starty = -5
        startx = 50  # FIXME Calc middle of the grid
        buffer = copy.deepcopy(self.screen._buffer._double_buffer)
        cards_renderer.show_effects(
            self.screen,
            cards_renderer.render_card_at(self.screen, card, x=startx, y=starty),
        )
        p = Path()
        p.jump_to(x=startx, y=starty)
        to_pos = cards_renderer.gridpos2dpos(to_pos)
        p.move_straight_to(x=to_pos.x, y=to_pos.y, steps=5)
        for x, y in p._steps:
            self.screen._buffer._double_buffer = copy.deepcopy(buffer)
            cards_renderer.show_effects(
                self.screen, cards_renderer.render_card_at(self.screen, card, x, y)
            )
        # FIXME Refactor to use buffer & move code

    def place_human_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        startpos = gridpos2dpos(GridPos(4, from_slot))
        targetpos = gridpos2dpos(GridPos(2, to_slot))

        buffer = copy.deepcopy(self.screen._buffer._double_buffer)
        cards_renderer.show_effects(
            self.screen,
            cards_renderer.render_card_at(
                self.screen, card, x=startpos.x, y=startpos.y
            ),
        )
        p = Path()
        p.jump_to(x=startpos.x, y=startpos.y)
        p.move_straight_to(x=targetpos.x, y=targetpos.y, steps=10)
        for x, y in p._steps:
            self.screen._buffer._double_buffer = copy.deepcopy(buffer)
            self.screen.refresh()
            cards_renderer.show_effects(
                self.screen, cards_renderer.render_card_at(self.screen, card, x, y)
            )
        # FIXME Refactor with other move functions
        # FIXME Make a small buffercontroller object

    def redraw_handdeck(self, handdeck: Deck, from_index: int) -> None:
        """Redraw hand from index `from_index`."""
        pos = gridpos2dpos(GridPos(4, from_index))
        self.screen.clear_buffer(
            Screen.COLOUR_WHITE,
            0,
            0,
            x=pos.x,
            y=pos.y,
            w=self.screen.width - pos.x,
            h=BOX_HEIGHT,
        )
        for i, card in list(enumerate(handdeck.cards))[from_index:]:
            cards_renderer.show_effects(
                self.screen,
                cards_renderer.render_card_in_grid(self.screen, card, GridPos(4, i)),
            )
        self.screen.refresh()

    def draw_card_to_handdeck(
        self, handdeck: Deck, card: Card, whichdeck: Literal["draw", "hamster"]
    ) -> None:
        """Show how a card gets drawn from one of the draw decks and moved to the hand.
        `whichdeck` is necessary to know which location to start from.
        """
        # FIXME Maybe implement differently in the future when cards have states: can
        # use those states for `whichdeck`.

        starty = cards_renderer.DRAW_DECKS_Y - 2
        # FIXME ^ When we put `-1` here, there will be a leftover `-` on the screen
        # after moving the cards. How to get rid of that?
        if whichdeck == "draw":
            startx = cards_renderer.DRAW_DECKS_X
        else:
            startx = cards_renderer.DRAW_DECKS_X + cards_renderer.BOX_WIDTH + 2
        buffer = copy.deepcopy(self.screen._buffer._double_buffer)
        cards_renderer.show_effects(
            self.screen,
            cards_renderer.render_card_at(self.screen, card, x=startx, y=starty),
        )
        p = Path()
        p.jump_to(x=startx, y=starty)
        to_pos = cards_renderer.gridpos2dpos(GridPos(4, len(handdeck.cards)))
        p.move_straight_to(x=to_pos.x, y=to_pos.y, steps=5)
        for x, y in p._steps:
            self.screen._buffer._double_buffer = copy.deepcopy(buffer)
            self.screen.refresh()
            cards_renderer.show_effects(
                self.screen, cards_renderer.render_card_at(self.screen, card, x, y)
            )

    def draw_empty_grid(self) -> None:
        for linei in range(3):
            for sloti in range(4):
                draw_slot_in_grid(self.screen, GridPos(linei, sloti))
        draw_grid_decks_separator(self.screen, 4)
        # FIXME Paremetrize width (don't forget to do that also in the base class if I
        # add parameters or something)

    def draw_drawdecks(self, counts: Tuple[int, int]) -> None:
        draw_drawdecks(self.screen, counts)

    def draw_drawdeck_highlights(self, highlights: Tuple[bool, bool]) -> None:
        draw_drawdeck_highlights(self.screen, highlights)

    def draw_handdeck_highlight(self, cursor: int) -> None:
        draw_handdeck_highlight(self.screen, cursor)

    def card_highlight(self, pos: GridPos) -> None:
        highlight_card_in_grid(self.screen, pos)

    def get_keycode(self) -> Optional[int]:
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

    def handle_human_draws_new_card(self, decks: Decks) -> None:
        if not decks.drawdeck.is_empty():
            highlights = [True, False]
        elif not decks.hamsterdeck.is_empty():
            highlights = [False, True]
        else:  # both empty
            return

        while True:
            self.draw_drawdeck_highlights(highlights)
            keycode = self.get_keycode()
            if keycode == Screen.KEY_LEFT and not decks.drawdeck.is_empty():
                highlights = [True, False]
            elif keycode == Screen.KEY_RIGHT and not decks.hamsterdeck.is_empty():
                highlights = [False, True]
            elif keycode == Screen.KEY_UP:
                if highlights[0]:
                    card = decks.drawdeck.draw_card()
                    self.draw_card_to_handdeck(decks.handdeck, card, "draw")
                else:
                    card = decks.hamsterdeck.draw_card()
                    self.draw_card_to_handdeck(decks.handdeck, card, "hamster")
                decks.handdeck.add_card(card)
                self.draw_drawdecks((decks.drawdeck.size(), decks.hamsterdeck.size()))
                return

    def handle_human_places_card(
        self, decks: Decks, grid, card: Card, from_slot: int
    ) -> bool:
        buffer = copy.deepcopy(
            self.screen._buffer._double_buffer
        )  # FIXME Use some buffer function
        cursor = 0
        while True:
            self.screen._buffer._double_buffer = copy.deepcopy(
                buffer
            )  # FIXME Use some buffer function
            self.card_highlight(GridPos(2, cursor))

            keycode = self.get_keycode()
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(grid.width - 1, cursor + 1)
            elif keycode == Screen.KEY_DOWN:
                # FIXME Check if card can be placed at all
                grid[2][cursor] = card
                self.place_human_card(card, from_slot=from_slot, to_slot=cursor)
                decks.useddeck.add_card(card)
                logging.debug("Human plays %s in %s", card.name, cursor)
                # screen._buffer._double_buffer = copy.deepcopy(buffer)
                return True
            elif keycode == Screen.KEY_ESCAPE:
                self.screen._buffer._double_buffer = copy.deepcopy(
                    buffer
                )  # FIXME Use some buffer function
                return False

    def handle_human_plays_card(self, decks: Decks) -> None:
        # FIXME What if hand is empty?
        buffer = copy.deepcopy(
            self.screen._buffer._double_buffer
        )  # FIXME Use some buffer function
        cursor = 0
        while True:
            self.screen._buffer._double_buffer = copy.deepcopy(
                buffer
            )  # FIXME Use some buffer function
            if not decks.handdeck.is_empty():
                self.draw_handdeck_highlight(cursor)

            keycode = self.get_keycode()
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(decks.handdeck.size() - 1, cursor + 1)
            elif keycode == Screen.KEY_UP:
                # FIXME Check if card is playable at all
                # Don't pick the card yet (i.e., don't remove it from the deck yet) because
                # the player might still abort the placing  of the card:
                card = decks.handdeck.cards[cursor]
                res = self.handle_human_places_card(decks, session.grid, card, cursor)
                if res:
                    decks.handdeck.pick_card(cursor)
                    cursor = min(decks.handdeck.size() - 1, cursor)
                    self.redraw_handdeck(decks.handdeck, cursor)
                    buffer = copy.deepcopy(
                        self.screen._buffer._double_buffer
                    )  # FIXME Use some buffer function
                else:
                    # Otherwise, we return bc the process was aborted by the user and won't
                    # update the cursor.
                    # FIXME Implement this w an exception rather than the True/False
                    # mechanics?
                    pass
                # FIXME ^ Use some update_buffer method here once we have the
                # buffercontroller object.
                cursor = min(decks.handdeck.size() - 1, cursor)
            elif keycode in (ord("i"), ord("I")):
                pass  # FIXME Inventory!
            elif keycode in (ord("c"), ord("C")):
                self.screen._buffer._double_buffer = copy.deepcopy(
                    buffer
                )  # FIXME Use some buffer function
                return

    def handle_round_of_fight(
        self, round_num: int, decks: Decks, computerstrategy: AgentStrategy
    ) -> None:
        log_decks(decks)

        # Play computer cards and animate how they appear:
        for pos, card in computerstrategy.cards_to_be_played(session.grid, round_num):
            self.play_computer_card(card, pos)
        # Now also place them in the model:
        computerstrategy.play_cards(session.grid, round_num)

        # Let human draw a card:
        self.handle_human_draws_new_card(decks)

        # Let human play card(s) from handdeck or items in his collection:
        self.handle_human_plays_card(decks)

        log_decks(decks)
        log_grid(session.grid)

        # Activate all cards:
        session.grid.activate_line(2)
        session.grid.activate_line(1)
        session.grid.prepare_line()

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

        log_grid(session.grid)
        return True

    def handle_fight(self, computerstrategy: AgentStrategy) -> None:

        # --- Prepare the fight ---
        # Show empty grid:
        self.draw_empty_grid()

        # Set up human's decks and show the hand deck:
        decks = setup_decks()
        self.draw_drawdecks((decks.drawdeck.size(), decks.hamsterdeck.size()))
        for _ in range(3):
            card = decks.drawdeck.draw_card()
            self.draw_card_to_handdeck(decks.handdeck, card, "draw")
            decks.handdeck.add_card(card)

        card = decks.hamsterdeck.draw_card()
        self.draw_card_to_handdeck(decks.handdeck, card, "hamster")
        decks.handdeck.add_card(card)
        self.draw_drawdecks((len(decks.drawdeck.cards), len(decks.hamsterdeck.cards)))

        # --- Run the fight ---
        fighting = True
        round_num = 0
        while fighting:
            fighting = self.handle_round_of_fight(
                round_num, decks, computerstrategy=computerstrategy
            )
            round_num += 1

        # --- Clean up after fight ---
        session.humanagent.deck.cards = [
            c
            for c in decks.useddeck.cards + decks.handdeck.cards + decks.drawdeck.cards
            if c.name != "Hamster"
        ]
        session.humanagent.deck.reset_cards()


# FIXME Add some border around the whole screen when the human presses "N" until he has
# to do something again?


# FIXME Check if anything should be taken over from handlers.
# FIXME Check if anything should be taken over from tui.
# FIXME Check if anything should be taken over from Fight.
# FIXME Use something like the Fight class with calls to a view object -- similar to how
# it is/was done in the Card class, e.g., when activating a class?
# FIXME Untangle what is UI/view from what is controller/business logic here.
