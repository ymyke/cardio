from enum import Enum
from asciimatics import constants as amconstants

GRID_MARGIN_LEFT = 10
GRID_MARGIN_TOP = 4
BOX_WIDTH = 20
BOX_HEIGHT = 7
BOX_PADDING_TOP = 0
BOX_PADDING_LEFT = 3
DRAW_DECKS_X = 45
DRAW_DECKS_Y = 45
AGENTGAPSIZE = 3  # Gap between the agents
AGENT_X_OFFSET = 7  # Gap between grid and agent information


class Color(Enum):
    BLACK = amconstants.COLOUR_BLACK
    RED = amconstants.COLOUR_RED
    GREEN = amconstants.COLOUR_GREEN
    YELLOW = amconstants.COLOUR_YELLOW
    BLUE = amconstants.COLOUR_BLUE
    MAGENTA = amconstants.COLOUR_MAGENTA
    CYAN = amconstants.COLOUR_CYAN
    WHITE = amconstants.COLOUR_WHITE
    GRAY = 9999  # Will be handled differently via a combo of color & attribute
