# ----- Locations -----
from .fight_location import FightLocation
from .no_location import NoLocation
from .skill_transferer_location import SkillTransfererLocation
from .skill_lottery_location import SkillLotteryLocation
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
    (SkillTransfererLocation, 1),
    (SkillLotteryLocation, 1),
]

# ----- Views -----
from cardio.tui.locations.fightview import TUIFightVnC
from cardio.tui.locations.upgraderview import TUIUpgraderView
from cardio.tui.locations.skill_transferer_view import TUISkillTransfererView
from cardio.tui.locations.skill_lottery_view import TUISkillLotteryView

view_directory = {
    NoLocation: None,
    FightLocation: TUIFightVnC,
    PowerUpgraderLocation: TUIUpgraderView,
    HealthUpgraderLocation: TUIUpgraderView,
    PowerUpgraderMultiLocation: TUIUpgraderView,
    HealthUpgraderMultiLocation: TUIUpgraderView,
    SkillTransfererLocation: TUISkillTransfererView,
    SkillLotteryLocation: TUISkillLotteryView,
}

# ----- Sanity check -----
assert set([loc for loc, _ in location_frequencies]) == set(view_directory.keys())
