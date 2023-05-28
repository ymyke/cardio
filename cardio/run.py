import random
from typing import List, Optional
import time
from cardio.locations.location import Location, create_random_location
from cardio.locations.no_location import NoLocation
from cardio.path_patterns import PATH_PATTERNS, PathPattern


class Run:
    """A run is a sequence of locations that are connected by paths.

    - Runs are fully predetermined based on some seed (`base_seed`), i.e., they don't
      adapt based on the player's behavior in any way.
    - Runs are indefinite. A player gets as far as she gets.
    - A run represents the entire map and keeps track of the current location
      (`current_rung` and `current_index`) and the path taken so far (not implemented
      yet, FIXME).
    """

    base_seed: str
    current_rung: int
    current_index: int

    def __init__(
        self,
        base_seed: Optional[str] = None,
        current_rung: int = 0,
        current_index: int = 0,
    ) -> None:
        self.base_seed = base_seed or str(time.time_ns())
        self.current_rung = current_rung
        self.current_index = current_index

    def move_to(self, loc: Location) -> None:
        assert loc.rung == self.current_rung + 1
        self.current_rung += 1
        self.current_index = loc.index

    def nof_locations(self, at_rung: int) -> int:
        assert at_rung >= 0
        if at_rung == 0:  # Always start with 1 location on rung 0
            return 1
        random.seed(f"N{at_rung}_{self.base_seed}")
        return random.randint(1, 3)

    def get_paths(self, at_rung: int) -> PathPattern:
        assert at_rung >= 0
        in_locs = self.nof_locations(at_rung)
        out_locs = self.nof_locations(at_rung + 1)
        random.seed(f"P{at_rung}_{self.base_seed}")
        return random.choice(PATH_PATTERNS[f"{in_locs}-{out_locs}"])

    def get_locations(self, at_rung: Optional[int] = None) -> List[Location]:
        """Get all locations on rung `at_rung`.

        Note that this method creates new location objects with each call. They always
        _look_ identical as long as the seed doesn't change, but they are different
        Python objects. Keep that in mind if you ever think about storing information
        dynamically in location objects.
        """
        at_rung = at_rung or self.current_rung
        locations = []
        noflocations = range(self.nof_locations(at_rung))
        pathpattern = self.get_paths(at_rung)
        if at_rung == 0:  # Always start with a NoLocation on rung 0
            return [NoLocation(self.base_seed, 0, 0, pathpattern.paths[0])]
        for i in noflocations:
            loc = create_random_location(
                self.base_seed, at_rung, i, pathpattern.paths[i]
            )
            locations.append(loc)
        return locations

    def get_current_location(self) -> Location:
        return self.get_locations()[self.current_index]

    def get_accessible_locations(self, for_rungs: int) -> List[Location]:
        """Return a list of all locations that are accessible from the current location
        and within `for_rungs` rungs.
        """
        result = []
        next_accessible_indices = set(self.get_current_location().paths)
        for i in range(1, for_rungs + 1):
            accessible_indices = next_accessible_indices
            next_accessible_indices = set()
            locations = self.get_locations(self.current_rung + i)
            for loc in locations:
                if loc.index in accessible_indices:
                    result.append(loc)
                    next_accessible_indices |= set(loc.paths)
        return result

    def get_string(
        self,
        start: Optional[int] = None,
        howmany: int = 5,
        h_condense: bool = False,
        debug: bool = False,
    ) -> str:
        """
        Todos:
        - Make paths dark grey. Make locations use some fitting color.
        - Use asciimaatics to print the paths coordinates-based.
        - With the above: Use emojis for locations (they have different widths but maybe
          with coordinate-based positioning they can still be aligned well?).
        """

        def v_stretch(line: str) -> str:
            howmuch = 6
            r = f"{line.rstrip():11s}"  # Normalize line length
            i0, i1 = 3, 7  # Positions 3 and 7 are the positions we can stretch
            c0, c1 = r[i0], r[i1]
            return r[:i0] + c0 * howmuch + r[i0 + 1 : i1] + c1 * howmuch + r[i1 + 1 :]

        lower = start or self.current_rung
        upper = lower + howmany
        res = ""
        for i in range(upper, lower - 1, -1):
            # Get and format the path pattern:
            pattern = self.get_paths(i).pattern
            lines = filter(None, pattern.split("\n"))
            lines = list(map(v_stretch, lines))
            if h_condense:
                del lines[1]
                del lines[-2]
            if i < upper:
                del lines[0]
            if debug:
                lines[-1] += f"     ← {i}"

            # Fill in the location names:
            locations = self.get_locations(i)
            for loc in locations:
                lines[-1] = lines[-1].replace("xxx", loc.marker, 1)

            if i == upper:  # Ignore the outgoing paths on top
                res = lines[-1] + "\n"
            else:
                res += "\n".join(lines) + "\n"

        return res

    def print(
        self,
        start: Optional[int] = None,
        howmany: int = 5,
        h_condense: bool = False,
        debug: bool = False,
    ) -> None:
        print(self.get_string(start, howmany, h_condense, debug))
