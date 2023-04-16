from typing import Literal
import random
from cardio import gg
from cardio.tui.locations.upgraderview import TUIUpgraderView
from .location import Location


class UpgraderLocation(Location):
    which_attribute: str = "_undefined_"
    upgrade_type: Literal["once", "multi"] = "once"

    def generate(self) -> None:
        super().generate()

    def handle(self) -> bool:
        upgradable_cards = gg.humanplayer.deck.cards
        view = TUIUpgraderView(upgradable_cards)
        card = view.pick()
        setattr(card, self.which_attribute, getattr(card, self.which_attribute) + 1)
        view.show_upgrade(card)
        if self.upgrade_type == "multi":
            while view.ask(card):
                if random.randint(1, 100) <= 5:  # TODO increase risk
                    view.show_destroy(card)
                    gg.humanplayer.deck.remove_card(card)
                    break
                else:
                    setattr(
                        card,
                        self.which_attribute,
                        getattr(card, self.which_attribute) + 1,
                    )
                    view.show_upgrade(card)

        view.close()
        return True


class PowerUpgraderLocation(UpgraderLocation):
    marker = "UPU"
    which_attribute = "power"


class HealthUpgraderLocation(UpgraderLocation):
    marker = "UHU"
    which_attribute = "health"


class PowerUpgraderMultiLocation(UpgraderLocation):
    marker = "UP*"
    which_attribute = "health"
    upgrade_type = "multi"


class HealthUpgraderMultiLocation(UpgraderLocation):
    marker = "UH*"
    which_attribute = "health"
    upgrade_type = "multi"
