from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer
from cardio import GridPos, session
from .utils import dPos, show_effects
from .constants import *

# FIXME Terminology: agent vs player everywhere?

DAMAGE_DIFF_TO_WIN = (
    5  # FIXME Refactor w the one in fightvnc to some common config or constants module
)


# SCALE = """\
# 🕱
# ⟊
# ⟊
# ⟊
# ⟊
# =
# ⟊
# ⟊
# ⟊
# ⟊
# 🕱
# """
SCALE = u"""\
·
·
·
·
·
${1,2,1}.${7,2,0}
·
·
·
·
·
"""

SCALE = u"""\
🔳
🔳
🔳
🔳
🔳
🟥
🔳
🔳
🔳
🔳
🔳
"""








def show_computerplayer_state(screen: Screen, grid_width: int) -> None:
    pos = dPos.from_gridpos(GridPos(2, grid_width))
    pos = dPos(pos.x + AGENT_X_OFFSET, pos.y + 1 - 10)
    show_effects(
        screen,
        Print(screen, StaticRenderer(images=["– Yshl 🤖"]), x=pos.x, y=pos.y),
    )


    # scale:
    scale_pos = dPos(pos.x-3, pos.y )
    show_effects(
        screen,
        Print(screen, StaticRenderer(images=[SCALE]), x=scale_pos.x, y=scale_pos.y),
    )
    show_effects(
        screen,
        Print(screen, StaticRenderer(images=["▶️"]), x=scale_pos.x-2, y=scale_pos.y+5),
    ) # ▶️ or 👉




def show_humanplayer_state(screen: Screen, grid_width: int) -> None:
    pos = dPos.from_gridpos(GridPos(2, grid_width))
    pos = dPos(pos.x + AGENT_X_OFFSET, pos.y + 1)
    txt = f"""\
– {session.humanplayer.name} {'💓' * session.humanplayer.lives}

{'💎' * session.humanplayer.gems}{'⠀'*10}

{'👻' * session.humanplayer.spirits}{'⠀'*10}
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
