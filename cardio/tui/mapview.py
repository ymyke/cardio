from typing import Optional
from asciimatics.screen import Screen
from .utils import show_screen_resolution, get_keycode, show_text, dPos
from ..run import Run
from ..locations.location import Location
from .constants import Color
from .agent_primitives import show_humanplayer
from .tuibase import TUIBaseMixin


class TUIMapView(TUIBaseMixin):
    MAPTOPLEFT = dPos(20, 10)
    AGENTINFO = dPos(70, 2)
    GAMEINFO = dPos(70, 18)

    def __init__(self, run: Run, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.run = run

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
        return self.MAPTOPLEFT + (
            view_index * 9,
            (height - (loc.rung - self.run.current_rung)) * 6,
        )

    def redraw(self, cursor_pos: Optional[int] = None) -> None:
        self.screen.clear_buffer(0, 0, 0)

        # Draw map:
        for i, l in enumerate(self.run.get_string().split("\n")):
            show_text(self.screen, self.MAPTOPLEFT + (0, i), l, color=Color.GRAY)

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

        # Show more agent and other information:
        show_humanplayer(self.screen, self.AGENTINFO)
        show_text(self.screen, self.GAMEINFO, f"Rung: {self.run.current_rung}")
        show_text(
            self.screen,
            self.GAMEINFO + (0, 2),
            f"Seed: {self.run.base_seed}",
            color=Color.GRAY,
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
            if keycode in (Screen.KEY_UP, 13):
                break
            if keycode == Screen.KEY_LEFT:
                cursor = max(0, cursor - 1)
            elif keycode == Screen.KEY_RIGHT:
                cursor = min(len(possible_locations) - 1, cursor + 1)
        return possible_locations[cursor]

    def move_to(self, loc: Location) -> None:
        # FIXME Maybe scroll line-by-line when transitioning from one rung to the next?
        pass
