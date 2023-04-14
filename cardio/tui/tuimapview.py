import atexit
from asciimatics.screen import Screen
from .utils import show_screen_resolution, get_keycode, show, show_text, dPos
from ..run import Run
from ..location import Location


class TUIMapView:
    def __init__(self, run: Run, debug: bool = False) -> None:
        # FIXME Code redundancies w TUIFightVnC -- Change these to all use the same
        # sceen (i.e., pass some screen object to the initializer)? Or the same code
        # (i.e., inherit from some TUIScreen class or mixin?)
        self.run = run
        self.debug = debug
        self.topleft = dPos(10, 2)
        self.screen = Screen.open(unicode_aware=True)
        if self.debug:
            show_screen_resolution(self.screen)
        atexit.register(self.close)

    def close(self) -> None:
        self.screen.close()

    def dpos_from_location(self, loc: Location) -> dPos:
        # FIXME This is not nice bc it hardcodes all kinds of things that are flexible
        # in run.get_string.
        num_locations = len(self.run.get_locations())
        if num_locations == 1:
            view_index = 1
        elif num_locations == 2:
            view_index = self.run.current_index * 2
        else:
            view_index = self.run.current_index
        height = 5
        return self.topleft + dPos(view_index * 9, height * 6)

    def redraw(self) -> None:
        self.screen.clear_buffer(0, 0, 0)
        show_text(self.screen, dPos(1, 1), str(self.run.current_rung))
        for i, l in enumerate(self.run.get_string().split("\n")):
            show_text(self.screen, self.topleft + dPos(0, i), l)

        # Mark current location:
        show_text(
            self.screen,
            self.dpos_from_location(self.run.get_current_location()) + dPos(-2, 0),
            ">>",
        )
        show_text(
            self.screen,
            self.dpos_from_location(self.run.get_current_location()) + dPos(3, 0),
            "<<",
        )

        self.screen.refresh()

    def get_next_location(self) -> Location:
        # TODO
        while True:
            self.redraw()
            keycode = get_keycode(self.screen)
            if keycode == Screen.KEY_UP:
                break
        import random

        return random.choice(self.run.get_locations(self.run.current_rung + 1))

    def move_to(self, loc: Location) -> None:
        # FIXME Maybe scroll line-by-line when transitioning from one rung to the next?
        pass
