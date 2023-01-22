# Figlet fonts: rectangle, small, chunky

from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer, FigletText
from cardio import GridPos, session
from .utils import dPos, show_effects
from .constants import *

# FIXME Terminology: agent vs player everywhere?

DAMAGE_DIFF_TO_WIN = (
    5  # FIXME Refactor w the one in fightvnc to some common config or constants module
)


def show_damage_state(screen: Screen, pos: dPos, damage_diff: int) -> None:
    DAMAGE_ROW = "${1,2,0}■■■■■■■■■■■■■■■■${7,2,0}"
    NO_DAMAGE_ROW = "${0,1,0}■${0,2,0}..............${0,1,0}■${7,2,0}"
    scale = [NO_DAMAGE_ROW] * ((DAMAGE_DIFF_TO_WIN - 1) * 2 + 1)
    if damage_diff != 0:
        for i in range(0, damage_diff, damage_diff // abs(damage_diff)):
            scale[DAMAGE_DIFF_TO_WIN - 1 + i] = DAMAGE_ROW
    else:
        scale[DAMAGE_DIFF_TO_WIN - 1] = DAMAGE_ROW
    show_effects(
        screen,
        Print(screen, StaticRenderer(images=["\n".join(scale)]), x=pos.x, y=pos.y),
    )


def show_computerplayer_state(screen: Screen, grid_width: int) -> None:
    pos = dPos.from_gridpos(GridPos(2, grid_width))
    pos = dPos(pos.x + AGENT_X_OFFSET, pos.y + 1 - 11)
    show_effects(
        screen,
        Print(screen, FigletText("Yshl", "chunky"), x=pos.x, y=pos.y),
    )

    # scale:
    show_damage_state(screen, dPos(pos.x, pos.y + 1), 0)


def show_humanplayer_state(screen: Screen, grid_width: int) -> None:
    pos = dPos.from_gridpos(GridPos(2, grid_width))
    pos = dPos(pos.x + AGENT_X_OFFSET, pos.y + 2)
    txt = f"""\
{FigletText("Schnuzgi", "chunky")}
{'💓' * session.humanplayer.lives}
{'💎' * session.humanplayer.gems}{'⠀'*10} {'👻' * session.humanplayer.spirits}+2{'⠀'*10}
"""  # FIXME Make the whitespace more intelligent

    show_effects(
        screen,
        Print(
            screen,
            StaticRenderer(images=[txt]),
            x=pos.x,
            y=pos.y,
        ),
    )
    # FIXME Why isn't this just some simple show_text function?


# def show_all_states(screen: Screen)->None:
#     show_computerplayer_state(screen, pos[0])
#     show_humanplayer_state(screen, pos[1])
#     show_damage_state(screen, pos[2], damage_diff)


# --- Alternative scale:
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
