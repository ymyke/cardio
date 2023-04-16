from .location import Location
from cardio.tui.locations.upgraderview import TUIUpgraderView


class PowerUpgraderLocation(Location):
    marker = "UPU"

    # TODO Have several upgraders?
    # once vs several, Health vs Power? UHU, UPU, UH*, UP*
    # (Maybe the * kinds run the risk of losing the card?)

    def generate(self) -> None:
        super().generate()

    def handle(self) -> bool:
        upgradable_cards = gg.humanplayer.deck.cards
        view = TUIUpgraderView(upgradable_cards)
        card = view.pick()
        card.power += 1
        view.show_upgrade(card)
        view.close()
        return True
