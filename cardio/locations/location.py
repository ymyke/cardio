from abc import ABC, abstractmethod
from typing import List
import random


class Location(ABC):
    """Abstract base class for locations.

    - One Location on the map. Contains everything it needs to handle that location.
    - A location has a `rung` (steps from the start) and an `index` attribute, which are
      used to generate the location. The seed is derived from an original seed for the
      entire run.
    """

    marker = "___"

    def __init__(self, base_seed: str, rung: int, index: int, paths: List[int]) -> None:
        self.id = f"{self.marker}_{rung}_{index}"
        self.seed = f"L{rung}_{index}_{base_seed}"  # FIXME Use the id here?
        self.rung = rung  # Steps from start
        self.index = index  # Index position at current rung
        self.paths = paths  # Paths to next locations
        self.generate()

    @abstractmethod
    def generate(self) -> None:
        random.seed(self.seed)
        pass

    @abstractmethod
    def handle(self, view_class: type) -> bool:
        """Returns `True` if the game is is still on, `False` if game is over."""
        pass


# ----- Factory -----


def create_random_location(
    base_seed: str, rung: int, index: int, paths: List[int]
) -> Location:
    # Importing these here to prevent circular imports:
    from .location_directory import location_frequencies

    random.seed(f"L{rung}_{index}_{base_seed}_locationfactory")
    exploded_locations = [
        loc for loc, count in location_frequencies for _ in range(count)
    ]
    location_class = random.choice(exploded_locations)
    return location_class(base_seed, rung, index, paths)
