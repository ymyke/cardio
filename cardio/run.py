import random
from typing import List, Optional
import time
from cardio.location import Location, create_random_location, NoLocation
from cardio.path_patterns import PATH_PATTERNS, PathPattern


class Run:
    base_seed: str
    # (Doesn't need to store any history bc everything is determined by the seed.)
    current_rung: int   
    current_index: int

    def __init__(self, base_seed: Optional[str] = None) -> None:
        self.base_seed = base_seed or str(time.time_ns())
        self.current_rung = 0
        self.current_index = 0

    def move_to(self, loc:Location) -> None:
        assert loc.rung == self.current_rung +1
        self.current_rung += 1
        self.current_index = loc.index

    def _nof_locations(self, at_rung: int) -> int:
        assert at_rung >= 0
        if at_rung == 0:  # Always start with 1 location on rung 0
            return 1
        random.seed(f"N{at_rung}_{self.base_seed}")
        return random.randint(1, 3)

    def _get_paths(self, at_rung: int) -> PathPattern:
        assert at_rung >= 0
        in_locs = self._nof_locations(at_rung)
        out_locs = self._nof_locations(at_rung + 1)
        random.seed(f"P{at_rung}_{self.base_seed}")
        return random.choice(PATH_PATTERNS[f"{in_locs}-{out_locs}"])

    def get_locations(self, at_rung: Optional[int] = None) -> List[Location]:
        at_rung = at_rung or self.current_rung
        locations = []
        noflocations = range(self._nof_locations(at_rung))
        pathpattern = self._get_paths(at_rung)
        if at_rung == 0:  # Always start with a NoLocation on rung 0
            return [NoLocation(self.base_seed, 0, 0, pathpattern.paths[0])]
        for i in noflocations:
            loc = create_random_location(
                self.base_seed, at_rung, i, pathpattern.paths[i]
            )
            locations.append(loc)
        return locations

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
        upper = lower + howmany - 1
        res = ""
        for i in range(upper, lower - 1, -1):
            # Get and format the path pattern:
            pattern = self._get_paths(i).pattern
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

            if i == start:  # Ignore the outgoing paths on top
                res = lines[-1] + "\n"
            else:
                res += "\n".join(lines) + "\n"

        return res

    def print(self, start: int, end: int, h_condense: bool = False) -> None:
        print(self.get_string(start, end, h_condense))
