from typing import List, Optional
from asciimatics.effects import Effect, Print
from asciimatics.renderers import Box, StaticRenderer
from asciimatics.screen import Screen
from asciimatics import constants

from cardio import Card, GridPos

BOX_WIDTH = 20
BOX_HEIGHT = 7
BOX_PADDING = 2


def card_to_amstring(c: Card) -> str:
    """Produce asciimatics string from card."""
    s = f"""\
{c.name}
{"💪" * c.power}
{"💓" * c.health}
{"".join(s.value.symbol for s in c.skills)}
"""
    return s


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
