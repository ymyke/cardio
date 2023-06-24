from typing import List
from ... import Card
from ..card_picker import CardPicker
from ..tuibase import TUIBaseMixin


class TUIUpgraderView(TUIBaseMixin):
    def __init__(self, cards: List[Card], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cards = cards
        self.cardpicker = CardPicker(self.screen, cards)

    def show_upgrade(self, card: Card) -> None:
        self.cardpicker.shake_card(card)

    def show_destroy(self, card: Card) -> None:
        self.cardpicker.burn_card(card)

    def pick(self) -> Card:
        return self.cardpicker.pick()

    def confirm(self, card: Card) -> bool:
        return self.cardpicker.confirm(card)
