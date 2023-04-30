from __future__ import annotations
import time
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer, Renderer
from asciimatics.constants import SINGLE_LINE
from asciimatics.screen import Screen

def show(screen: Screen, pos, renderer: Renderer):
    Print(screen=screen, renderer=renderer, x=pos[0], y=pos[1]).update(0)


def show_text(screen: Screen, pos, text: str) -> None:
    show(screen, pos, StaticRenderer(images=[text]))

what = "⛨"

screen = Screen.open(unicode_aware=False)
show_text(screen, (0, 0), f"x{what}x")
screen.refresh()
time.sleep(1)
screen.close()

print(f"x{what}x")

