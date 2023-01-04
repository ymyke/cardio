"""Using asciimatics only for rendering and doing everything else manually."""

from typing import NamedTuple, Tuple, Union, List, Optional
import sys
import copy
import time
from asciimatics.screen import Screen
from asciimatics.effects import Print, Effect
from asciimatics import particles
from asciimatics.renderers import StaticRenderer, Box
from asciimatics.paths import Path
from asciimatics.utilities import BoxTool
from asciimatics.event import KeyboardEvent

from cardio.tui.cards_renderer import (
    dPos,
    gridpos2dpos,
    render_card_in_grid,
    clear_card_in_grid,
    render_card_at,
    clear_card_at,
)
from cardio import Card, card_blueprints, GridPos


class ExtendedBox(BoxTool):
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        self._style = style
        if style == 11:
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
        elif style == 12 and not self.unicode_aware:
            self.down_right = "+"
            self.down_left = "+"
            self.up_right = "+"
            self.up_left = "+"
            self.h = " "
            self.h_inside = " "
            self.v = ""
            self.v_inside = ""
            self.v_left = ""
            self.v_right = ""
            self.h_up = ""
            self.h_down = ""
            self.cross = ""
        elif style == 12 and self.unicode_aware:
            self.down_right = "┌"
            self.down_left = "┐"
            self.up_right = "└"
            self.up_left = "┘"
            self.h = " "
            self.h_inside = " "
            self.v = ""
            self.v_inside = ""
            self.v_left = ""
            self.v_right = ""
            self.h_up = ""
            self.h_down = ""
            self.cross = ""
        else:
            super(ExtendedBox, self.__class__).style.fset(self, style)


class SmallExplosionFlames(particles.ExplosionFlames):
    def _next_particle(self):
        from math import pi, sin, cos
        from random import uniform

        direction = uniform(0, 2 * pi)
        r = 0.8
        return particles.Particle(
            "#",  # or: █
            self._x + sin(direction) * r * 2.0,
            self._y + cos(direction) * r,
            sin(direction) / 2.0,
            cos(direction) / 4.0,
            [
                (Screen.COLOUR_BLACK, 0, 0),
                (Screen.COLOUR_RED, 0, 0),
                (Screen.COLOUR_RED, Screen.A_BOLD, 0),
                (Screen.COLOUR_YELLOW, Screen.A_BOLD, 0),
                (Screen.COLOUR_WHITE, Screen.A_BOLD, 0),
            ],
            5,
            self._burn,
            next_colour=self._colour,
        )


def show_explosion(screen, small: bool = False):
    if small:
        e = SmallExplosionFlames(screen, 10, 30, 22)
        loopfor = 22
    else:
        e = particles.ExplosionFlames(screen, 10, 30, 22)
        loopfor = 30
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    for i in range(loopfor):
        e.update()  # No parameter here b/c ExplosionFlames are no Effects
        screen.refresh()
        screen._buffer._double_buffer = copy.deepcopy(buffer)


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


def show_move():
    card = card_blueprints.create_card_from_blueprint("Hamster")
    show_effects(screen, render_card_at(screen, card, 10, 10))
    time.sleep(1)
    p = Path()
    p.jump_to(10, 10)
    p.move_straight_to(120, 30, 20)

    clear_card_at(screen, 10, 10)
    buffer = copy.deepcopy(screen._buffer._double_buffer)

    for x, y in p._steps:
        clear_card_at(screen, x, y)
        show_effects(screen, render_card_at(screen, card, x, y), 0.03)
        clear_card_at(screen, x, y)
        screen._buffer._double_buffer = copy.deepcopy(buffer)


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


def show_shoot(screen):
    HIT = "🌟"
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    show_effects(
        screen, Print(screen=screen, renderer=StaticRenderer(images=[HIT]), y=30, x=60)
    )
    p = Path()
    p.jump_to(60, 30)
    p.move_straight_to(3, 3, 40)
    for x, y in p._steps:
        screen.clear_buffer(Screen.COLOUR_WHITE, 0, 0, x=x, y=y, w=1, h=1)
        show_effects(
            screen,
            Print(screen=screen, renderer=StaticRenderer(images=[HIT]), y=y, x=x),
        )
        screen._buffer._double_buffer = copy.deepcopy(buffer)


def show_effects(screen, effects: Union[Effect, List[Effect]], pause: float = 0):
    if not isinstance(effects, list):
        effects = [effects]
    for e in effects:
        e.update(0)
    screen.refresh()
    if pause > 0:
        time.sleep(pause)


def show_all_effects(screen):
    card = card_blueprints.create_card_from_blueprint("Hamster")
    show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 4)))
    show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 3)))
    show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 2)))
    show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 1)))
    show_effects(screen, render_card_in_grid(screen, card, GridPos(3, 0)))
    time.sleep(1)
    shake_card(screen)
    show_explosion(screen, True)
    time.sleep(1)
    show_shoot(screen)
    show_move()
    flash_card(screen)
    time.sleep(1)
    show_explosion(screen)
    time.sleep(1)


def get_keycode(screen) -> Optional[int]:
    """Ignore all mouse events. Return key code."""
    event = screen.get_event()
    if not isinstance(event, KeyboardEvent):
        return None
    return event.key_code


def show_some_other_boxes(screen):
    show_effects(
        screen,
        Print(screen, StaticRenderer([ExtendedBox(True, 11).box(20, 7)]), x=20, y=35),
    )
    show_effects(
        screen,
        Print(screen, StaticRenderer([ExtendedBox(True, 12).box(20, 7)]), x=42, y=35),
    )
    show_effects(
        screen,
        Print(screen, StaticRenderer([ExtendedBox(False, 12).box(20, 7)]), x=64, y=35),
    )


def moving_sprite():
    from asciimatics.sprites import Arrow

    p = Path()
    p.jump_to(10, 10)
    p.move_straight_to(140, 20, 60)
    a = Arrow(screen, p)
    for _ in p._steps:
        a._update(0)
        screen.refresh()
        time.sleep(0.1)
    # Note that the Sprite class doesn't redraw the background like my manual routines
    # do.


# def draw_card_at(card: Card, pos: Tuple[int, int]):


class dCard:
    # FIXME: Could/should this rather be a mixin for the cards? -- Then, a card could
    # call its own get_attacked or activate methods when necessary.

    # FIXME The card could find out by itself where it is and how to display itself
    # appropriately. depening on whether it is in a deck (and which one) or in the grid
    # or...
    # Same for the grid, which would also be able to display empty slots.
    # Cards could have animations for when they change from one state/place to another.
    # Under such circumstances, it would make all the more sense to model decks not as
    # decks but as states within cards.

    # empty or not?
    # highlight?
    # offsets?

    def __init__(
        self,
        screen: Screen,
        card: Optional[Card],
        pos: Union[GridPos, dPos, Tuple[int, int]],
    ) -> None:
        self.screen = screen
        self.card = card
        if isinstance(pos, GridPos):
            self.x, self.y = gridpos2dpos(pos)
        else:
            self.x, self.y = pos

    def draw(self):
        show_effects(
            self.screen, render_card_at(self.screen, self.card, self.x, self.y)
        )


# --------------------

screen = Screen.open(unicode_aware=True)


dc = dCard(screen, card_blueprints.create_card_from_blueprint("Koala"), (100, 30))
dc.draw()


card = card_blueprints.create_card_from_blueprint("Hamster")
for linei in range(3):
    for sloti in range(4):
        yoff = 1 if linei == 2 else 0
        # draw_card(card, GridPos(linei, sloti))
        show_effects(
            screen,
            render_card_in_grid(screen, card, GridPos(linei, sloti), yoffset=yoff),
        )


show_some_other_boxes(screen)

while get_keycode(screen) != ord("q"):
    show_explosion(screen)


screen.close()


# FIXME:
# - Can I build nice classes for VCard, VDeck, VDashboard, ...? (V = visual?)
# - How to integrate this new code into the cardio code?
# - Can I activate cards by moving them towards opponent and back?
# - Can I encapsulate the code better?
# - Can I remove health by blinking it first? Or just blink to whole line?
#       💓💓💓💓💓+7
# - Mark empty slots simply with + in the edges or so. Use ExtendedBox for that.
