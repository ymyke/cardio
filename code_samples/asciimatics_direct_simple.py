"""Using asciimatics only for rendering and doing everything else manually."""

from typing import Union, List
import sys
from asciimatics.screen import Screen
from asciimatics.effects import Print, Effect
from asciimatics import particles
from asciimatics.renderers import StaticRenderer, Box
from asciimatics.utilities import BoxTool
import time

from cardio.tui.cards_renderer import render_card_in_grid, clear_card_in_grid
from cardio import Card, card_blueprints, GridPos


class ExtendedBox(BoxTool):
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        self._style = style
        if style == 7:
            self.down_right = "*"
            self.down_left = "*"
            self.up_right = "*"
            self.up_left = "*"
            self.h = "*"
            self.h_inside = "*"
            self.v = "*"
            self.v_inside = "*"
            self.v_left = "*"
            self.v_right = "*"
            self.h_up = "*"
            self.h_down = "*"
            self.cross = "*"
        else:
            super().style(style)


def show_explosion(screen):
    e = particles.ExplosionFlames(screen, 10, 10, 22)
    for i in range(30):
        e.update()  # No parameter here b/c ExplosionFlames are no Effects
        screen.refresh()
        for _ in range(200000):
            pass


def shake_card(screen):
    card = card_blueprints.create_card_from_blueprint("Hamster")
    carde = render_card_in_grid(screen, card, GridPos(3, 3))
    for _ in range(4):
        show_effects(screen, carde, 0.03)
        clear_card_in_grid(screen, GridPos(3, 3))
        card2 = render_card_in_grid(screen, card, GridPos(3, 3), xoffset=-1)
        show_effects(screen, card2, 0.03)
        clear_card_in_grid(screen, GridPos(3, 3), xoffset=-1)

    show_effects(screen, carde)


def flash_card(screen):
    # Flashing the border:
    # FIXME Try also w/ different colors and/or stars...
    highlight = True
    for i in range(10):
        xx = render_card_in_grid(screen, None, GridPos(3, 3), highlight=highlight)
        for e in xx:
            e.update(0)
            screen.refresh()
        time.sleep(0.05)
        highlight = not highlight


def show_effects(screen, effects: Union[Effect, List[Effect]], pause: float = 0):
    if not isinstance(effects, list):
        effects = [effects]
    for e in effects:
        e.update(0)
    screen.refresh()
    if pause > 0:
        time.sleep(pause)


# --------------------

screen = Screen.open(unicode_aware=True)

card = card_blueprints.create_card_from_blueprint("Hamster")

show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 4)))
show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 3)))
show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 2)))
show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 1)))
show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 0)))

time.sleep(1)

flash_card(screen)

time.sleep(1)

show_explosion(screen)

time.sleep(1)
screen.close()


# FIXME:
# - Can I move cards?
# - Can I draw an "*" that moves from the attacker to the target?
# - Can I activate cards by moving them towards opponent and back?
# - Can I encapsulate the code better?
# - Can I remove health by blinking it first? Or just blink to whole line?
#       💓💓💓💓💓+7
