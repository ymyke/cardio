import random
from typing import List, Optional
import time
from cardio.location import Location, FightLocation

# TODO: There can be levels w/o nodes, where the path just goes straight through. -- How
# should that work exactly? -- Maybe just have a special location kind `NoLocation` and
# that's that?

PATH_PATTERNS = {
    "1-1": [
        [[0]],
    ],
    "1-2": [
        [[0, 1]],
    ],
    "2-1": [
        [[0], [0]],
    ],
    "2-2": [
        [[0], [1]],
        [[0, 1], [1]],
        [[0], [0, 1]],
    ],
    "2-3": [
        [[0], [1, 2]],
        [[0, 1], [2]],
        [[0, 1], [1, 2]],
        [[0, 1, 2], [2]],
        [[0], [0, 1, 2]],
    ],
    "3-2": [
        [[0], [1], [1]],
        [[0], [0], [1]],
        [[0], [0, 1], [1]],
        [[0], [0], [0, 1]],
        [[0, 1], [1], [1]],
    ],
    "1-3": [
        [[0, 1, 2]],
    ],
    "3-1": [
        [[0], [0], [0]],
    ],
    "3-3": [
        [[0], [1], [2]],
        [[0, 1], [1], [2]],
        [[0, 1], [1, 2], [2]],
        [[0], [0, 1], [2]],
        [[0], [1], [1, 2]],
        [[0], [1, 2], [2]],
        [[0], [0, 1], [1, 2]],
        [[0], [0, 1, 2], [2]],
        [[0, 1], [1], [1, 2]],
    ],
}
# (2-3/3-2 etc. could also be mirrored rather than duplicated.)


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

    def _get_paths(self, at_distance: int) -> List[List[int]]:
        in_locs = self._nof_locations(at_distance)
        out_locs = self._nof_locations(at_distance + 1)
        random.seed(f"P{at_distance}_{self.base_seed}")
        return random.choice(PATH_PATTERNS[f"{in_locs}-{out_locs}"])
        # FIXME Add more weight to "fan-out" patterns than to "fan-in" patterns so more
        # separate longer stretches will be generated?

    def get_locations(self, at_distance: int) -> List[Location]:
        locations = []
        noflocations = range(self._nof_locations(at_distance))
        paths = self._get_paths(at_distance)
        for i in noflocations:
            loc = FightLocation(self.base_seed, at_distance, i, paths[i])
            # TODO Need to get the location from some register and based on weights
            locations.append(loc)
        return locations

    def print(self, start: int, end: int):
        pass
