import logging
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Background
from asciimatics.renderers import StaticRenderer
from asciimatics.event import KeyboardEvent

from cardio import GridPos, Grid

from cardio.tui.cards_renderer import (
    render_card_in_grid,
    clear_card_in_grid,
    highlight_card_in_grid,
)
from cardio.fight import Fight, FightStatus, WhoWon

# FIXME ^ How to make this import relative?

GRID_WIDTH = 4

# FIXME Todos:
# - Error conditions: Empty decks, cards that can't be played, ...


class FightController(Scene):
    def __init__(self, screen, grid: Grid, fight: Fight):
        # Game related:
        self._grid = grid
        self._fight = fight
        self._fight.status = FightStatus.HUMAN_PLAYING  # FIXME Only for testing

        from cardio import session

        session.view = self  # FIXME Ugly!?

        # View related:
        self._screen = screen
        self.cursor_pickslot_pos = 0  # FIXME Better add a cursor object?
        self.cursor_pickslot_highlight = []
        self.cursor_pickslot_active = False
        self.cursor_pickcard_pos = 0
        self.cursor_pickcard_highlight = []
        self.cursor_pickcard_active = False  # FIXME Setting this to True shows the cursor immediately; otherwise no.
        # FIXME Same with _pickdeck_
        effects = [Background(screen, 0)]  # Need at least 1 effect here

        super().__init__(effects, 0)
        self._fight.play_computer_cards()
        # FIXME Set status to HUMAN_DRAWING
        self.cursor_pickcard_active = True
        self.update()

    def cursor_pickslot_update(self, new_pos: int):
        self.cursor_pickslot_pos = new_pos
        for e in self.cursor_pickslot_highlight:
            self.remove_effect(e)
        self.cursor_pickslot_highlight = render_card_in_grid(
            self._screen, None, GridPos(2, self.cursor_pickslot_pos), highlight=True
        )
        for e in self.cursor_pickslot_highlight:
            self.add_effect(e)

    def cursor_pickcard_update(self, new_pos: int):
        self.cursor_pickcard_pos = new_pos
        for e in self.cursor_pickcard_highlight:
            self.remove_effect(e)
        self.cursor_pickcard_highlight = render_card_in_grid(
            self._screen, None, GridPos(4, self.cursor_pickcard_pos), highlight=True
        )
        for e in self.cursor_pickcard_highlight:
            self.add_effect(e)

    def update(self, additional_effects=None):
        self._effects = []
        if additional_effects is not None:
            self._effects.extend(additional_effects)
        self._effects.append(
            Print(
                self._screen,
                StaticRenderer(
                    images=[f"{self._screen.width} x {self._screen.height}"]
                ),
                self._screen.height - 1,
            )
        )
        # Grid:
        for linei in range(3):
            for sloti in range(4):
                self._effects.extend(
                    render_card_in_grid(
                        self._screen, self._grid[linei][sloti], GridPos(linei, sloti)
                    )
                )
        # Hand:
        for i, card in enumerate(self._fight.handdeck.cards):
            self._effects.extend(render_card_in_grid(self._screen, card, GridPos(4, i)))
        # Cursors:
        if self.cursor_pickcard_active:
            self.cursor_pickcard_highlight = []
            self.cursor_pickcard_update(self.cursor_pickcard_pos)
        if self.cursor_pickslot_active:
            self.cursor_pickslot_highlight = []
            self.cursor_pickslot_update(self.cursor_pickslot_pos)

    def process_human_playing(self, keycode):

        if keycode == Screen.KEY_LEFT:
            self.cursor_pickcard_update(max(0, self.cursor_pickcard_pos - 1))
        elif keycode == Screen.KEY_RIGHT:
            self.cursor_pickcard_update(
                min(len(self._fight.handdeck.cards) - 1, self.cursor_pickcard_pos + 1)
            )
        elif keycode == Screen.KEY_UP:
            self.cursor_pickslot_active = True
            self.cursor_pickslot_pos = min(
                self.cursor_pickcard_pos, self._grid.width - 1
            )
            self._fight.status = FightStatus.HUMAN_PLACINGCARD
            self.update()
        elif keycode in (ord("i"), ord("I")):
            pass  # Inventory!
        elif keycode in (ord("n"), ord("N")):
            self.cursor_pickcard_active = False
            self._fight.status = FightStatus.HUMAN_DONE
            self.update()
            self._fight.handle_round_of_fight()
            # self._screen.clear()
            self.cursor_pickcard_active = (
                True  # FIXME Change this once we have the draw card action
            )
            self.update()

    def activate_card(self, card):
        # Will also be called by card
        pass

    def get_attacked(self, target, attacker) -> None:
        logging.debug("Animating attack %s -> %s", attacker.name, target.name)
        targetpos = self._grid.find_card(target)
        attackerpos = self._grid.find_card(target)
        e = highlight_card_in_grid(self._screen, GridPos(2, 6))
        # self._effects.extend(highlight_card_in_grid(self._screen,targetpos))
        e.extend(render_card_in_grid(self._screen, None, GridPos(1, 6)))
        e.append(
            Print(
                self._screen,
                StaticRenderer(images=["HALLOOOOO"]),
                self._screen.height - 2,
            )
        )

        self._screen.clear()
        self.update()

        # WE WERE HERE. 👇
        # FIXME This module works more or less. But it starts breaking down when we try
        # to add animations. This here doesn't work bc the way `update` is implemented
        # it removes the effect we add here immediately. And `update` gets called
        # immediately after this when the code continues after the `n` key press.

        self.add_effect(
            Print(
                self._screen,
                StaticRenderer(images=["HALLOOOOO"]),
                self._screen.height - 2,
                delete_count=3,
            )
        )

    def process_human_placingcard(self, keycode):
        if keycode == Screen.KEY_LEFT:
            self.cursor_pickslot_update(max(0, self.cursor_pickslot_pos - 1))
        elif keycode == Screen.KEY_RIGHT:
            self.cursor_pickslot_update(
                min(GRID_WIDTH - 1, self.cursor_pickslot_pos + 1)
            )
        elif keycode == Screen.KEY_DOWN:
            # FIXME Check if card can be placed at all
            card = self._fight.handdeck.pick_card(self.cursor_pickcard_pos)
            self._grid[2][self.cursor_pickslot_pos] = card
            self._fight.useddeck.add_card(card)
            logging.debug("Human plays %s in %s", card.name, self.cursor_pickslot_pos)
            self.cursor_pickslot_active = False
            self.cursor_pickcard_update(
                min(len(self._fight.handdeck.cards) - 1, self.cursor_pickcard_pos)
            )
            self._fight.status = FightStatus.HUMAN_PLAYING

            # effects = []
            # for i in range(len(self._fight.handdeck.cards) + 1):
            #     effects.extend(clear_card_in_grid(self._screen, GridPos(4,i)))
            # self.update(effects)
            # FIXME Tried the above to only clear what is necessary but that didn't
            # really work. Also, it didn't clear away the emojis reliably.

            self._screen.clear()
            self.update()
        elif keycode == Screen.KEY_ESCAPE:
            self.cursor_pickslot_active = False
            self._fight.status = FightStatus.HUMAN_PLAYING
            self.update()

    def process_event(self, event):
        # Allow standard event processing first
        if super().process_event(event) is None:
            return

        if not isinstance(event, KeyboardEvent):
            return event

        keycode = event.key_code
        logging.debug("Processing %s, state is %s", keycode, self._fight.status.name)

        # FIXME Testing only:
        if self._fight.status == FightStatus.HUMAN_DRAWING:
            self._fight.status = FightStatus.HUMAN_PLAYING

        if keycode == ord("p"):
            self.add_effect(
                Print(
                    self._screen,
                    StaticRenderer(images=["HALLOOOOO"]),
                    self._screen.height - 2,
                    delete_count=3,
                )
            )

        if self._fight.status == FightStatus.HUMAN_PLAYING:
            self.process_human_playing(keycode)
        if self._fight.status == FightStatus.HUMAN_PLACINGCARD:
            self.process_human_placingcard(keycode)

        # FIXME Todos:
        # - Add animations to fight actions
        # - Fix the failing test
        # - Commit some time
        # - Add HUMAN_DRAWING step
        # - Consolidate fight.Fight and handlers.handle_fight
        # - Add information around agent health and lives
        # - Don't forget to call end_fight at the right point in time.
        # - Add items
        # - Truncate hearts and power etc. if there are too many of them.

        # # If that didn't handle it, check for a key that this demo understands.
        # if isinstance(event, KeyboardEvent):
        #     c = event.key_code
        #     if c in (ord("x"), ord("X")):
        #         raise StopApplication("User exit")
        #     elif c == Screen.KEY_LEFT:
        #         self.update_cursor(max(0, self.cursor_pos - 1))
        #     elif c == Screen.KEY_RIGHT:
        #         self.update_cursor(min(GRID_WIDTH - 1, self.cursor_pos + 1))
        #     elif c == Screen.KEY_UP:
        #         e = Background(self._screen, 0)
        #         self.add_effect(e)  # QQ: Is this how an update could work?
        #         self.remove_effect(e)
        #     elif c == Screen.KEY_DOWN:
        #         pass
        #     elif c in (ord("n"), ord("N")):
        #         self._fight.play_computer_cards()
        #         self.update()
        #         # FIXME Update turn number
        #     elif c in (ord("h"), ord("H")):
        #         self.add_effect(PopUpDialog(self._screen, "Yo!", ["OK"]))
        #         # FIXME Why does this "eat" the first key?
        #         # See https://github.com/peterbrittain/asciimatics/issues/362

        # Simply pass other types of events:
        # FIXME This should only be done if the event was not consumed above...
        return event


def demo(screen, grid, fight):
    screen.play(
        [FightController(screen, grid, fight)], stop_on_resize=True, allow_int=True
    )


def start(grid: Grid, fight: Fight):
    Screen.wrapper(demo, catch_interrupt=False, arguments=[grid, fight])
