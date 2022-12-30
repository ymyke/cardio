"""This just shows the sluggishness of moving the cursor left/right."""

#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import sys
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.renderers import Box
from asciimatics.screen import Screen
from asciimatics.scene import Scene


class GameController(Scene):
    def __init__(self, screen):
        self._screen = screen
        self.cursor_pos = 0
        self.cursor_highlight = None
        boxes = [
            Print(
                screen=screen,
                renderer=Box(5, 5, uni=True, style=0),
                x=(5 + 2) * i + 2,
                y=10,
                colour=7,
                transparent=True,
            )
            for i in range(15)
        ]
        super(GameController, self).__init__(boxes, -1)
        self.update_cursor(self.cursor_pos)

    def update_cursor(self, new_pos: int):
        self.cursor_pos = new_pos
        if self.cursor_highlight:
            self.remove_effect(self.cursor_highlight)
        self.cursor_highlight = Print(
            screen=self._screen,
            renderer=Box(5, 5, uni=True, style=2),
            x=(5 + 2) * self.cursor_pos + 2,
            y=10,
            colour=7,
            transparent=True,
        )
        self.add_effect(self.cursor_highlight)

    def process_event(self, event):
        if super(GameController, self).process_event(event) is None:
            return

        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c in (ord("x"), ord("X")):
                raise StopApplication("User exit")
            elif c in (ord("a"), Screen.KEY_LEFT):
                self.update_cursor(self.cursor_pos - 1)
            elif c in (ord("d"), Screen.KEY_RIGHT):
                self.update_cursor(self.cursor_pos + 1)
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            return event


def demo(screen):
    screen.play([GameController(screen)], stop_on_resize=True, allow_int=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=False)
            sys.exit(0)
        except ResizeScreenError:
            pass
