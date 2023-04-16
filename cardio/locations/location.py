from abc import ABC, abstractmethod
from typing import List
import random


class Location(ABC):
    marker = "   "

    def __init__(self, base_seed: str, rung: int, index: int, paths: List[int]) -> None:
        self.id = f"{self.__class__.__name__[0]}{rung}_{index}"
        self.seed = f"L{rung}_{index}_{base_seed}"
        self.rung = rung  # Steps from start
        self.index = index  # Index position at current rung
        self.paths = paths  # Paths to next locations
        self.generate()
        # FIXME Should the initializer also take a view base object that will be used to
        # access views by the different locations and that can be used to use different
        # views? (OR: register some basic view object in gg?)

    @abstractmethod
    def generate(self) -> None:
        random.seed(self.seed)
        pass

    @abstractmethod
    def handle(self) -> bool:
        """Returns `True` if the game is is still on, `False` if game is over."""
        pass


# ----- Factory -----


def create_random_location(
    base_seed: str, rung: int, index: int, paths: List[int]
) -> Location:
    # Importing these here to prevent circular imports:
    from .fight_location import FightLocation
    from .no_location import NoLocation
    from .upgrader_location import PowerUpgraderLocation

    known_locations = [  # 1 = "base" frequency
        (NoLocation, 5),
        (FightLocation, 5),
        (PowerUpgraderLocation, 1),
    ]
    random.seed(f"L{rung}_{index}_{base_seed}_locationfactory")
    exploded_locations = [loc for loc, count in known_locations for _ in range(count)]
    location_class = random.choice(exploded_locations)
    return location_class(base_seed, rung, index, paths)
