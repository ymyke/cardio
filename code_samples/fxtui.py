from typing import Optional, List
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Effect, Print, Background
from asciimatics.renderers import FigletText, SpeechBubble, Box, StaticRenderer
from asciimatics import constants
from asciimatics.widgets import PopUpDialog
from asciimatics.exceptions import StopApplication
from asciimatics.event import KeyboardEvent

from cardio import Card, GridPos
from cardio.card_blueprints import create_card_from_blueprint


GRID_WIDTH = 4


def card_to_amstring(c: Card) -> str:
    """Produce asciimatics string from card."""
    s = f"""\
{c.name}
{"💪" * c.power}
{"💓" * c.health}
{"".join(s.value.symbol for s in c.skills)}
"""
    return s


BOX_WIDTH = 20
BOX_HEIGHT = 7
BOX_PADDING = 2


def render_card_at(
    screen, card: Optional[Card], x: int, y: int, highlight: bool = False
) -> List[Effect]:
    """Render card and box at x, y screen position. Draws empty box if `card`
    is `None`.
    """
    BOX_COLOR = Screen.COLOUR_YELLOW
    effects = []
    style = constants.DOUBLE_LINE if highlight else constants.SINGLE_LINE
    pbox = Print(
        screen=screen,
        renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=style),
        x=x,
        y=y,
        colour=BOX_COLOR,
        transparent=True,
    )
    effects.append(pbox)
    if card is not None:
        pcard = Print(
            screen=screen,
            renderer=StaticRenderer(images=[card_to_amstring(card)]),
            y=y + 1,
            x=x + 2,
        )
        effects.append(pcard)
    return effects


def render_card_in_grid(
    screen, card: Optional[Card], pos: GridPos, highlight: bool = False
) -> List[Effect]:
    """Render card at grid position."""
    GRID_MARGIN_LEFT = 10
    GRID_MARGIN_TOP = 10
    return render_card_at(
        screen,
        card,
        x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING),
        y=GRID_MARGIN_TOP,
        highlight=highlight,
    )


# class Grid(Effect):
#     def __init__(self, screen, game_state):
#         super().__init__(screen)
#         # self._state = game_state  # FIXME Have the grid here? Or session/gamestate?
#         self._x = self._screen.width - 10
#         self._y = self._screen.height - 5

#     def _update(self, frame_no):
#         self._screen.print_at(
#             "  ", self._x, self._y, Screen.COLOUR_RED, bg=Screen.COLOUR_RED
#         )

#         text = ">>" + str(frame_no)
#         self._screen.print_at(text, self._x + 3, self._y + 3, Screen.COLOUR_GREEN)

#     @property
#     def frame_update_count(self):
#         # No animation required.
#         return 0

#     @property
#     def stop_frame(self):
#         # No specific end point for this Effect.  Carry on running forever.
#         return 0

#     def reset(self):
#         # Nothing special to do.  Just need this to satisfy the ABC.
#         pass


class GameController(Scene):
    def __init__(self, screen, game_state):
        self._screen = screen
        self.cursor_pos = 0
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
        self.cursor_highlight = render_card_in_grid(
            screen, None, GridPos(0, self.cursor_pos), highlight=True
        )
        super(GameController, self).__init__(effects + self.cursor_highlight, 0)

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

