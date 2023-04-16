from cardio import gg
from cardio.tui.locations.upgraderview import TUIUpgraderView
from .location import Location

# FIXME Also have UH*, UP*, which can update several times (and where you run the risk
# of losing the card?)


class UpgraderLocation(Location):
    which_attribute = "_undefined_"

    def generate(self) -> None:
        super().generate()

    def handle(self) -> bool:
        upgradable_cards = gg.humanplayer.deck.cards
        view = TUIUpgraderView(upgradable_cards)
        card = view.pick()
        setattr(card, self.which_attribute, getattr(card, self.which_attribute) + 1)
        view.show_upgrade(card)
        view.close()
        return True


class PowerUpgraderLocation(UpgraderLocation):
    marker = "UPU"
    which_attribute = "power"


class HealthUpgraderLocation(UpgraderLocation):
    marker = "UHU"
    which_attribute = "health"
