from typing import Literal, Protocol, Type
import random
from cardio import Card, CardList
from cardio.human_player import HumanPlayer
from .location import Location
from .baseview import BaseLocationView


class UpgraderView(BaseLocationView, Protocol):
    def __init__(self, upgradable_cards: CardList, *args, **kwargs) -> None:
        ...

    def pick(self) -> Card:
        ...

    def show_destroy(self, card: Card) -> None:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...

    def confirm(self, card: Card) -> bool:
        ...


class UpgraderLocation(Location):
    which_attribute: str = "_undefined_"
    upgrade_type: Literal["once", "multi"] = "once"

    def generate(self) -> None:
        super().generate()

    def handle(self, view_class: Type[UpgraderView], humanplayer: HumanPlayer) -> bool:
        def _upgrade(card: Card):
            setattr(card, self.which_attribute, getattr(card, self.which_attribute) + 1)
            view.show_upgrade(card)

        upgradable_cards = humanplayer.deck.cards
        view = view_class(upgradable_cards, description=self.description)
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
                    humanplayer.deck.remove_card(card)
                    break

                _upgrade(card)
                if not view.confirm(card):
                    break

        view.close()
        return True


class PowerUpgraderLocation(UpgraderLocation):
    marker = "UPU"
    description = "💪 Upgrade power of a card once."
    which_attribute = "power"


class HealthUpgraderLocation(UpgraderLocation):
    marker = "UHU"
    description = "💓 Upgrade health of a card once."
    which_attribute = "health"


class PowerUpgraderMultiLocation(UpgraderLocation):
    marker = "UP*"
    description = "💪🔄️ Upgrade power of a card multiple times.\n\nBut risk losing it! 💀"
    which_attribute = "power"
    upgrade_type = "multi"


class HealthUpgraderMultiLocation(UpgraderLocation):
    marker = "UH*"
    description = (
        "💓🔄️ Upgrade health of a card multiple times.\n\nBut risk losing it! 💀"
    )
    which_attribute = "health"
    upgrade_type = "multi"
