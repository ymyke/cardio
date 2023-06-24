from typing import Optional, List
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Effect, Print
from asciimatics.renderers import FigletText, SpeechBubble, Box, StaticRenderer
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


BOX_WIDTH = 20
BOX_HEIGHT = 7
BOX_PADDING = 2


def render_card_at(screen, card: Optional[Card], x: int, y: int) -> List[Effect]:
    """Render card and box at x, y screen position. Draws empty box if `card`
    is `None`.
    """
    BOX_COLOR = Screen.COLOUR_YELLOW
    effects = []
    pbox = Print(
        screen=screen,
        renderer=Box(BOX_WIDTH, BOX_HEIGHT, uni=True, style=constants.SINGLE_LINE),
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


def render_card_in_grid(screen, card: Optional[Card], pos: GridPos) -> List[Effect]:
    """Render card at grid position."""
    GRID_MARGIN_LEFT = 10
    GRID_MARGIN_TOP = 10
    return render_card_at(
        screen,
        card,
        x=GRID_MARGIN_LEFT + pos.slot * (BOX_WIDTH + BOX_PADDING),
        y=GRID_MARGIN_TOP,
    )


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
        + boxes
    )
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


Screen.wrapper(boxdemo)

# bubble = SpeechBubble("Hello, hello!", tail="L")
# print(bubble)
