from typing import List
from ... import Card, CardList
from ..tuibase import TUIBaseMixin
from ..card_picker import CardPicker


class TUISkillTransfererView(TUIBaseMixin):
    def __init__(self, cards: List[Card], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cards = cards
        self.cardpicker = CardPicker(self.screen, cards)

    def show_upgrade(self, card: Card) -> None:
        self.cardpicker.shake_card(card)

    def show_destroy(self, card: Card) -> None:
        self.cardpicker.burn_card(card)

    def pick_from(self, from_cards: CardList) -> Card:
        self.picked = self.cardpicker.pick(from_cards)
        return self.picked

    def pick_to(self, to_cards: CardList) -> Card:
        return self.cardpicker.pick(to_cards, marks=[self.cards.index(self.picked)])
