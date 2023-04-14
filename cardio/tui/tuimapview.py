import atexit
from typing import Optional
from asciimatics.screen import Screen
from .utils import show_screen_resolution, get_keycode, show_text, dPos
from ..run import Run
from ..location import Location
from .constants import Color


class TUIMapView:
    def __init__(self, run: Run, debug: bool = False) -> None:
        # FIXME Code redundancies w TUIFightVnC -- Change these to all use the same
        # sceen (i.e., pass some screen object to the initializer)? Or the same code
        # (i.e., inherit from some TUIScreen class or mixin?)
        self.run = run
        self.debug = debug
        self.topleft = dPos(10, 2)
        self.screen = Screen.open(unicode_aware=True)
        atexit.register(self.close)

    def close(self) -> None:
        self.screen.close()

    def dpos_from_location(self, loc: Location) -> dPos:
        # FIXME This is not nice bc it hardcodes all kinds of things that are flexible
        # in run.get_string.
        num_locations = len(self.run.get_locations(loc.rung))
        if num_locations == 1:
            view_index = 1
        elif num_locations == 2:
            view_index = loc.index * 2
        else:
            view_index = loc.index
        height = 5
        return self.topleft + (
            view_index * 9,
            (height - (loc.rung - self.run.current_rung)) * 6,
        )

    def redraw(self, cursor_pos: Optional[int] = None) -> None:
        self.screen.clear_buffer(0, 0, 0)
        show_text(self.screen, dPos(1, 1), str(self.run.current_rung))
        for i, l in enumerate(self.run.get_string().split("\n")):
            show_text(self.screen, self.topleft + (0, i), l, color=Color.GRAY)

        # TODO Show more stuff:
        # - seed
        # - rung
        # - human player info
        # - larger map

        # Mark current location:
        current_loc = self.run.get_current_location()
        show_text(
            self.screen,
            self.dpos_from_location(current_loc) + (-2, 0),
            f">>{current_loc.marker}<<",
            color=Color.YELLOW,
        )

        # Color all accessible locations:
        for loc in self.run.get_accessible_locations(5):
            show_text(
                self.screen,
                self.dpos_from_location(loc),
                f"{loc.marker}",
                color=Color.WHITE,
            )

        # Color the next possible locations including cursor position:
        for i, loc in enumerate(self.run.get_accessible_locations(1)):
            s = f"[[{loc.marker}]]" if i == cursor_pos else f"  {loc.marker}"
            show_text(
                self.screen,
                self.dpos_from_location(loc) - (2, 0),
                s,
                color=Color.BLUE,
            )

        if self.debug:
            show_screen_resolution(self.screen)
        self.screen.refresh()

    def get_next_location(self) -> Location:
        possible_locations = self.run.get_accessible_locations(1)
        cursor = 0
        while True:
            self.redraw(cursor_pos=cursor)
            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_UP:
                break
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(len(possible_locations) - 1, cursor + 1)
        return possible_locations[cursor]

    def move_to(self, loc: Location) -> None:
        # FIXME Maybe scroll line-by-line when transitioning from one rung to the next?
        pass
