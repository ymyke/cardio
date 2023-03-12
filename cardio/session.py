from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Grid, FightVnC, HumanPlayer


grid: Grid
vnc: FightVnC
humanplayer: HumanPlayer

# QQ: Should this rather be Game instead of session? Or should there be a Game class?
