from abc import ABC, abstractmethod
from typing import List
import random
from cardio.human_player import HumanPlayer


class Location(ABC):
    """Abstract base class for locations.

    - One Location on the map. Contains everything it needs to handle that location.
    - A location has a `rung` (steps from the start) and an `index` attribute, which are
      used to generate the location. The seed is derived from an original seed for the
      entire run.
    """

    marker = "___"
    description = None

    def __init__(self, base_seed: str, rung: int, index: int, paths: List[int]) -> None:
        self.id = f"{self.marker}_{rung}_{index}"
        self.seed = f"L_{self.id}_{base_seed}"
        self.rung = rung  # Steps from start
        self.index = index  # Index position at current rung
        self.paths = paths  # Paths to next locations
        self.generate()

    @abstractmethod
    def generate(self) -> None:
        random.seed(self.seed)
        pass

    @abstractmethod
    def handle(self, view_class: type, humanplayer: HumanPlayer) -> bool:
        """Returns `True` if the current run is is still on, `False` if the run is to be
        ended, e.g., because the player has lost all their lives.
        """
        pass


# ----- Factory -----


def create_random_location(
    base_seed: str, rung: int, index: int, paths: List[int]
) -> Location:
    # Importing these here to prevent circular imports:
    from .location_directory import location_frequencies

    random.seed(f"L{rung}_{index}_{base_seed}_locationfactory")
    locations, weights = zip(*location_frequencies)
    location_class = random.choices(locations, weights=weights)[0]
    return location_class(base_seed, rung, index, paths)
