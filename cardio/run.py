import random
from typing import List, Optional
import time
from cardio.location import Location, FightLocation
from cardio.path_patterns import PATH_PATTERNS, PathPattern

# TODO: There can be levels w/o nodes, where the path just goes straight through. -- How
# should that work exactly? -- Maybe just have a special location kind `NoLocation` and
# that's that?

# TODO Add tests


class Run:
    base_seed: str
    current_distance: int
    # Doesn't need to store any history bc everything is determined by the seed.

    def __init__(self, base_seed: Optional[str] = None) -> None:
        self.base_seed = base_seed or str(time.time_ns())
        self.current_distance = 0

    def _nof_locations(self, at_distance: int) -> int:
        random.seed(f"N{at_distance}_{self.base_seed}")
        return random.randint(1, 3)

    def _get_paths(self, at_distance: int) -> PathPattern:
        in_locs = self._nof_locations(at_distance)
        out_locs = self._nof_locations(at_distance + 1)
        random.seed(f"P{at_distance}_{self.base_seed}")
        return random.choice(PATH_PATTERNS[f"{in_locs}-{out_locs}"])
        # FIXME Add more weight to "fan-out" patterns than to "fan-in" patterns so more
        # separate longer stretches will be generated?

    def get_locations(self, at_distance: int) -> List[Location]:
        locations = []
        noflocations = range(self._nof_locations(at_distance))
        pathpattern = self._get_paths(at_distance)
        for i in noflocations:
            loc = FightLocation(self.base_seed, at_distance, i, pathpattern.paths[i])
            # TODO Need to get the location from some register and based on weights
            locations.append(loc)
        return locations

    def print(self, start: int, end: int):
        start, end = max(start, end), min(start, end)
        for i in range(start, end - 1, -1):
            pattern = self._get_paths(i).pattern
            lines = list(filter(None, pattern.split("\n")))
            lines[-1] += f"     ← {i}"
            newlines = []
            h_condense = False
            stretch = 6
            i0 = 3
            i1 = 7
            for j, l in enumerate(lines):
                l = f"{l.rstrip():11s}" + stretch * 2 * " "
                c0 = l[i0]
                c1 = l[i1]
                nl = l[:i0] + c0 * stretch + l[i0 + 1 : i1] + c1 * stretch + l[i1 + 1 :]
                if h_condense and j in (1, len(lines) - 2):
                    pass
                else:
                    newlines.append(nl)
            if i < start:
                del newlines[0]
            print("\n".join(newlines))
