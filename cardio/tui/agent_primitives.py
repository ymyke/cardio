from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer, FigletText
from cardio import GridPos, session
from .utils import dPos, show_effects
from .constants import *

# FIXME Terminology: agent vs player everywhere?


class StateWidget:
    NAME_FONT = "rectangles"
    # Options: rectangles, small, chunky, ... (http://www.figlet.org/examples.html)

    def __init__(
        self, screen: Screen, grid_width: int, damage_diff_to_win: int
    ) -> None:
        self.screen = screen
        self.damage_diff_to_win = damage_diff_to_win
        pos = dPos.from_gridpos(GridPos(1, grid_width))
        fontheight = FigletText("x", self.NAME_FONT).max_height
        self.scale_pos = dPos(
            pos.x + AGENT_X_OFFSET, pos.y + BOX_HEIGHT - damage_diff_to_win - 2
        )
        self.computer_pos = dPos(self.scale_pos.x, self.scale_pos.y - fontheight)
        self.human_pos = dPos(
            self.scale_pos.x, self.scale_pos.y + damage_diff_to_win + 4
        )

    def show_damage_state(self, damage_diff: int) -> None:
        DAMAGE_ROW = "${1,2,0}■■■■■■■■■■■■■■■■${7,2,0}"
        NO_DAMAGE_ROW = "${0,1,0}■${0,2,0}..............${0,1,0}■${7,2,0}"
        scale = [NO_DAMAGE_ROW] * ((self.damage_diff_to_win - 1) * 2 + 1)
        if damage_diff != 0:
            for i in range(0, damage_diff, damage_diff // abs(damage_diff)):
                scale[self.damage_diff_to_win - 1 + i] = DAMAGE_ROW
        else:
            scale[self.damage_diff_to_win - 1] = DAMAGE_ROW
        show_effects(
            self.screen,
            Print(
                self.screen,
                StaticRenderer(images=["\n".join(scale)]),
                x=self.scale_pos.x,
                y=self.scale_pos.y,
            ),
        )

    def show_computerplayer_state(self) -> None:
        show_effects(
            self.screen,
            Print(
                self.screen,
                FigletText("Yshl", self.NAME_FONT),
                x=self.computer_pos.x,
                y=self.computer_pos.y,
            ),
        )

    def show_humanplayer_state(self) -> None:
        txt = f"""\
{FigletText("Schnuzgi", self.NAME_FONT)}
{'💓' * session.humanplayer.lives}
{'💎' * session.humanplayer.gems}{'⠀'*10} 
{'👻' * session.humanplayer.spirits}+2{'⠀'*10}
"""  # FIXME Make the whitespace more intelligent

        show_effects(
            self.screen,
            Print(
                self.screen,
                StaticRenderer(images=[txt]),
                x=self.human_pos.x,
                y=self.human_pos.y,
            ),
        )
        # FIXME Why isn't this just some simple show_text function?

    def show_all(self, damage_diff: int):
        self.show_computerplayer_state()
        self.show_damage_state(damage_diff)
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
