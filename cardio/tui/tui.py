from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer
from asciimatics.widgets import PopUpDialog
from asciimatics.exceptions import StopApplication
from asciimatics.event import KeyboardEvent

from cardio import GridPos
from cardio.card_blueprints import create_card_from_blueprint

from cardio.tui.cards_renderer import render_card_in_grid

# FIXME ^ How to make this import relative?

GRID_WIDTH = 4


class GameController(Scene):
    def __init__(self, screen, game_state):
        self._screen = screen
        self.cursor_pos = 0
        self.cursor_highlight = []
        self._state = game_state
        
        effects = (
            [
                Print(
                    screen,
                    StaticRenderer(images=[f"{screen.width} x {screen.height}"]),
                    screen.height - 1,
                ),
            ]
            + render_card_in_grid(
                screen, create_card_from_blueprint("Porcupine"), GridPos(0, 0)
            )
            + render_card_in_grid(
                screen, create_card_from_blueprint("Koala"), GridPos(0, 1)
            )
            + render_card_in_grid(
                screen, create_card_from_blueprint("Weasel"), GridPos(0, 2)
            )
            + render_card_in_grid(
                screen, create_card_from_blueprint("Hamster"), GridPos(0, 3)
            )
        )
        super().__init__(effects, 0)
        self.update_cursor(0)

    def update_cursor(self, new_pos: int):
        self.cursor_pos = new_pos
        for e in self.cursor_highlight:
            self.remove_effect(e)
        self.cursor_highlight = render_card_in_grid(
            self._screen, None, GridPos(0, self.cursor_pos), highlight=True
        )
        for e in self.cursor_highlight:
            self.add_effect(e)

    def process_event(self, event):
        # Allow standard event processing first
        if super().process_event(event) is None:
            return

        # If that didn't handle it, check for a key that this demo understands.
        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c in (ord("x"), ord("X")):
                raise StopApplication("User exit")
            elif c == Screen.KEY_LEFT:
                self.update_cursor(max(0, self.cursor_pos - 1))
            elif c == Screen.KEY_RIGHT:
                self.update_cursor(min(GRID_WIDTH - 1, self.cursor_pos + 1))
            elif c == Screen.KEY_UP:
                pass
            elif c == Screen.KEY_DOWN:
                pass
            # elif c in (ord("1"), ord("2"), ord("3"), ord("4")):
            #     self._state.mode = c - ord("1")
            # elif c in (ord("m"), ord("M")):
            #     self._state.show_mini_map = not self._state.show_mini_map
            #     if self._state.show_mini_map:
            #         self.add_effect(self._mini_map)
            #     else:
            #         self.remove_effect(self._mini_map)
            elif c in (ord("h"), ord("H")):
                self.add_effect(PopUpDialog(self._screen, "Yo!", ["OK"]))
                # FIXME Why does this "eat" the first key?
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            return event


def demo(screen):
    # game_state.update_screen(screen)
    screen.play([GameController(screen, None)], stop_on_resize=True, allow_int=True)


Screen.wrapper(demo, catch_interrupt=False)
