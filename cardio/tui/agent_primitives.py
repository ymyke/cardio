from asciimatics.screen import Screen
from asciimatics.renderers import FigletText
from cardio import GridPos
from cardio.agent_damage_state import AgentDamageState
from cardio.human_player import HumanPlayer
from .utils import dPos, render_value, show, show_text
from .constants import *


NAME_FONT = "rectangles"
# Options: rectangles, small, chunky, ... (http://www.figlet.org/examples.html)


class HumanStateWidget:
    """Shows the state of the human player. This is a separate widget so it can be used
    separately.
    """

    def __init__(self, screen: Screen, humanplayer: HumanPlayer, pos: dPos) -> None:
        self.screen = screen
        self.humanplayer = humanplayer
        self.pos = pos

    def show(self):
        s = f"""\
{FigletText(self.humanplayer.name, NAME_FONT)}
{render_value(self.humanplayer.lives, '💓', surplus_color=Color.RED)}
{render_value(self.humanplayer.gems, '💎', surplus_color=Color.BLUE)}
{render_value(self.humanplayer.spirits, '👻')}
"""
        show_text(self.screen, self.pos, s, color=Color.GRAY)


class StateWidget:
    def __init__(
        self,
        screen: Screen,
        grid_width: int,
        damagestate: AgentDamageState,
        humanplayer: HumanPlayer,
    ) -> None:
        self.screen = screen
        self.damagestate = damagestate
        offset = (AGENT_X_OFFSET, 0)
        self.computer_pos = dPos.from_gridpos(GridPos(0, grid_width)) + offset
        self.deadlock_pos = dPos.from_gridpos(GridPos(2, grid_width)) + offset + (0, -4)
        self.human_pos = dPos.from_gridpos(GridPos(2, grid_width)) + offset
        self.humanstate = HumanStateWidget(screen, humanplayer, self.human_pos + (0, 2))

    def _show_health_bars(self, pos: dPos, diff: int, max_diff: int) -> None:
        bars = render_value(min(max_diff - diff, max_diff), "█ ", 100) + "\n"
        bars *= 2
        show_text(self.screen, pos, bars, color=Color.CYAN)

    def show_computerplayer_state(self) -> None:
        show(
            self.screen,
            self.computer_pos,
            FigletText("Le Chiffre", NAME_FONT),
            color=Color.GRAY,
        )
        self._show_health_bars(
            self.computer_pos + (0, 8),
            -self.damagestate.diff,
            self.damagestate.max_diff,
        )

    def show_humanplayer_state(self) -> None:
        self._show_health_bars(
            self.human_pos, self.damagestate.diff, self.damagestate.max_diff
        )
        self.humanstate.show()

    def show_deadlock_counter(self) -> None:
        if self.damagestate.is_in_deadlock_risk():
            show_text(
                self.screen,
                self.deadlock_pos,
                "🚨 Deadlock imminent 🚨 "
                f"{self.damagestate.rounds_left_until_deadlock()} rounds left",
                color=Color.RED,
            )

    def show_all(self):
        self.show_computerplayer_state()
        self.show_deadlock_counter()
        self.show_humanplayer_state()
