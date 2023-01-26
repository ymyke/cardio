from asciimatics.screen import Screen
from asciimatics.renderers import StaticRenderer, FigletText
from cardio import GridPos, session
from cardio.agent_damage_state import AgentDamageState
from .utils import dPos, render_value, show
from .constants import *


class StateWidget:
    NAME_FONT = "rectangles"
    # Options: rectangles, small, chunky, ... (http://www.figlet.org/examples.html)

    def __init__(self, screen: Screen, grid_width: int, max_diff: int) -> None:
        # TODO Remove max_diff, remove scale, implement new state ui
        self.screen = screen
        pos = dPos.from_gridpos(GridPos(1, grid_width))
        fontheight = FigletText("x", self.NAME_FONT).max_height
        self.scale_pos = dPos(pos.x + AGENT_X_OFFSET, pos.y + BOX_HEIGHT - max_diff - 2)
        self.computer_pos = dPos(self.scale_pos.x, self.scale_pos.y - fontheight)
        self.human_pos = dPos(self.scale_pos.x, self.scale_pos.y + max_diff + 4)

    def show_damage_state(self, state: AgentDamageState) -> None:
        DAMAGE_ROW = "${1,2,0}■■■■■■■■■■■■■■■■${7,2,0}"
        NO_DAMAGE_ROW = "${0,1,0}■${0,2,0}..............${0,1,0}■${7,2,0}"
        scale = [NO_DAMAGE_ROW] * state.max_diff * 2
        if state.diff != 0:
            for i in range(0, state.diff, state.diff // abs(state.diff)):
                scale[state.max_diff + i] = DAMAGE_ROW
        show(self.screen, StaticRenderer(images=["\n".join(scale)]), self.scale_pos)

    def show_computerplayer_state(self) -> None:
        show(
            self.screen,
            FigletText("Yshl", self.NAME_FONT),
            self.computer_pos,
            color=Color.GRAY,
        )

    def show_humanplayer_state(self) -> None:
        txt = f"""\
{FigletText("Schnuzgi", self.NAME_FONT)}
{render_value(session.humanplayer.lives, '💓', surplus_color=Screen.COLOUR_RED)}
{render_value(session.humanplayer.gems, '💎', surplus_color=Screen.COLOUR_BLUE)}
{render_value(session.humanplayer.spirits, '👻')}
"""

        show(
            self.screen, StaticRenderer(images=[txt]), self.human_pos, color=Color.GRAY
        )
        # FIXME Maybe worthwhile to further simplify and add the StaticRenderer for the
        # user if it's a simple text that needs to get output?

    def show_all(self, damagestate: AgentDamageState):
        self.show_computerplayer_state()
        self.show_damage_state(damagestate)
        self.show_humanplayer_state()


# Alternative scale:
#         🔳
#         🔳
#         🔳
#         🔳
#         🔳
# ▶️ or 👉 🟥
#         🔳
#         🔳
#         🔳
#         🔳
#         🔳
