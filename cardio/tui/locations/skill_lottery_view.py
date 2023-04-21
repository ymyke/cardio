from typing import List
from ... import Card, CardList
from ..card_picker import CardPicker
from ..tuibase import TUIBaseMixin


class TUISkillLotteryView(TUIBaseMixin):
    def __init__(self, cards: List[Card], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cards = cards
        self.cardpicker = CardPicker(self.screen, cards)

    def show_upgrade(self, card: Card) -> None:
        self.cardpicker.shake_card(card)

    def pick(self, activecards: CardList) -> Card:
        return self.cardpicker.pick(activecards)
