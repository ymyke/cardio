"""Using asciimatics only for rendering and doing everything else manually."""

import sys
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics import particles
from asciimatics.renderers import StaticRenderer, Box
from asciimatics.utilities import BoxTool
import time

from cardio.tui.cards_renderer import render_card_in_grid
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
        e.update()
        screen.refresh()
        for _ in range(200000):
            pass


# print(Print(screen, Box(10,10), 10))
# # for i in StaticRenderer(BoxTool(True, 0).box(10, 10)).rendered_text:
# #     print(i)
# #     print()


screen = Screen.open(unicode_aware=True)


xx = render_card_in_grid(
    screen, card_blueprints.create_card_from_blueprint("Hamster"), GridPos(3, 3)
)
for e in xx:
    e.update(0)
e = Print(screen, Box(10, 10), 10, 10)
e.update(0)
screen.refresh()
time.sleep(1)


show_explosion(screen)


xx = render_card_in_grid(
    screen, card_blueprints.create_card_from_blueprint("Hamster"), GridPos(3, 3)
)
for e in xx:
    e.update(0)
e = Print(screen, Box(10, 10), 10, 10)
e.update(0)
screen.refresh()
time.sleep(1)


sys.exit(0)


xx = render_card_in_grid(
    screen, card_blueprints.create_card_from_blueprint("Hamster"), GridPos(3, 3)
)
for e in xx:
    e.update(0)
e = Print(screen, Box(10, 10), 10, 10)
e.update(0)
screen.refresh()
time.sleep(1)


# # Flashing the border:
# FIXME Try also w/ different colors and/or stars...
# highlight = True
# for i in range(10):
#     xx = render_card_in_grid(screen, None, GridPos(3, 3), highlight=highlight)
#     for e in xx:
#         e.update(0)
#         screen.refresh()
#     time.sleep(0.05)
#     highlight = not highlight


screen.clear_buffer(Screen.COLOUR_WHITE, 0, 0, 12, 10, w=100, h=40)
screen.refresh()
time.sleep(1)

screen.close()


# FIXME:
# - Can I move cards?
# - Can I draw an "*" that moves from the attacker to the target?
# - Can I activate cards by moving them towards opponent and back?
# - Can I encapsulate the code better?
# - Can I remove health by blinking it first?
#       💓💓💓💓💓+7
