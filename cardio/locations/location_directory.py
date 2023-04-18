# ----- Locations -----
from .fight_location import FightLocation
from .no_location import NoLocation
from .upgrader_location import (
    PowerUpgraderLocation,
    HealthUpgraderLocation,
    PowerUpgraderMultiLocation,
    HealthUpgraderMultiLocation,
)

location_frequencies = [  # 1 = "base" frequency
    (NoLocation, 10),
    (FightLocation, 10),
    (PowerUpgraderLocation, 2),
    (HealthUpgraderLocation, 2),
    (PowerUpgraderMultiLocation, 1),
    (HealthUpgraderMultiLocation, 1),
]

# ----- Views -----
from cardio.tui.locations.fightview import TUIFightVnC
from cardio.tui.locations.upgraderview import TUIUpgraderView


view_directory = {
    NoLocation: None,
    FightLocation: TUIFightVnC,
    PowerUpgraderLocation: TUIUpgraderView,
    HealthUpgraderLocation: TUIUpgraderView,
    PowerUpgraderMultiLocation: TUIUpgraderView,
    HealthUpgraderMultiLocation: TUIUpgraderView,
}

# ----- Sanity check -----
assert set([loc for loc, _ in location_frequencies]) == set(view_directory.keys())