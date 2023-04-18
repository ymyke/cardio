from typing import Literal, Protocol, Type
import random
from cardio import gg, Card, CardList
from .location import Location
from .baseview import BaseLocationView


class UpgraderView(BaseLocationView, Protocol):
    def __init__(self, upgradable_cards: CardList) -> None:
        ...

    def pick(self) -> Card:
        ...

    def show_destroy(self, card: Card) -> None:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...

    def ask(self, card: Card) -> bool:
        ...


class UpgraderLocation(Location):
    which_attribute: str = "_undefined_"
    upgrade_type: Literal["once", "multi"] = "once"

    def generate(self) -> None:
        super().generate()

    def handle(self, view_class: Type[UpgraderView]) -> bool:
        def _upgrade(card: Card):
            for attr in (self.which_attribute, "initial_" + self.which_attribute):
                setattr(card, attr, getattr(card, attr) + 1)
            view.show_upgrade(card)

        upgradable_cards = gg.humanplayer.deck.cards
        view = view_class(upgradable_cards)
        card = view.pick()
        if self.upgrade_type == "once":
            _upgrade(card)
        else:  # multi
            risk = 0
            while True:
                risk += (100 - risk) / 10
                print(risk)
                if random.randint(1, 100) <= risk:
                    view.show_destroy(card)
                    gg.humanplayer.deck.remove_card(card)
                    break

                _upgrade(card)
                if not view.ask(card):
                    break

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
    which_attribute = "power"
    upgrade_type = "multi"


class HealthUpgraderMultiLocation(UpgraderLocation):
    marker = "UH*"
    which_attribute = "health"
    upgrade_type = "multi"