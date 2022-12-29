from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print, Mirage
from asciimatics.renderers import FigletText, SpeechBubble, Box, StaticRenderer
import asciimatics
from asciimatics import constants

from cardio import Card, GridPos
from cardio.card_blueprints import create_card_from_blueprint


"""
https://asciimatics.readthedocs.io/en/stable/asciimatics.html#asciimatics.screen.Screen.get_event
    Screen.KEY_LEFT, ...
"""


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


def render_card(screen, card: Card, pos: GridPos) -> list:
    GRID_MARGIN_LEFT = 10
    GRID_MARGIN_TOP = 10
    BOX_WIDTH = 20
    BOX_HEIGHT = 7
    BOX_PADDING = 2
    BOX_COLOR = Screen.COLOUR_YELLOW
    pbox = Print(
        screen,
        Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=constants.SINGLE_LINE),
        y=GRID_MARGIN_TOP,
        x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING),
        colour=BOX_COLOR,
        transparent=True,
    )
    pcard = Print(
        screen,
        StaticRenderer(images=[card_to_amstring(card)]),
        GRID_MARGIN_TOP + 1,  # FIXME Make this relative to box
        GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING) + 2,
    )
    return [pbox, pcard]


def boxdemo(screen):
    scenes = []
    centre = (screen.width // 2, screen.height // 2)

    boxes = []
    GRID_MARGIN_LEFT = 10
    GRID_MARGIN_TOP = 10
    BOX_WIDTH = 20
    BOX_HEIGHT = 7
    BOX_PADDING = 2
    BOX_COLOR = Screen.COLOUR_YELLOW
    boxes = [
        Print(
            screen,
            Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=constants.SINGLE_LINE),
            y=GRID_MARGIN_TOP,
            x=GRID_MARGIN_LEFT + i * (BOX_WIDTH + BOX_PADDING),
            colour=BOX_COLOR,
            transparent=True,
        )
        for i in range(GRID_WIDTH)
    ]

    effects = (
        [
            Print(
                screen,
                StaticRenderer(images=[f"{screen.width} x {screen.height}"]),
                screen.height - 1,
            ),
        ]
        + render_card(screen, create_card_from_blueprint("Porcupine"), GridPos(0, 0))
        + render_card(screen, create_card_from_blueprint("Koala"), GridPos(0, 1))
        + render_card(screen, create_card_from_blueprint("Weasel"), GridPos(0, 2))
        + render_card(screen, create_card_from_blueprint("Hamster"), GridPos(0, 3))
        + boxes
    )
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


Screen.wrapper(boxdemo)

# bubble = SpeechBubble("Hello, hello!", tail="L")
# print(bubble)
