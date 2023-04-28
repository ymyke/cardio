from typing import Protocol, Type
import random
from cardio import gg, Card, CardList
from .location import Location
from .baseview import BaseLocationView


class SkillTransfererView(BaseLocationView, Protocol):
    def __init__(self, cards: CardList) -> None:
        ...

    def pick_from(self, from_cards: CardList) -> Card:
        ...

    def pick_to(self, to_cards: CardList) -> Card:
        ...

    def show_destroy(self, card: Card) -> None:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...


def get_to_cards(from_card: Card) -> CardList:
    return [
        c
        for c in gg.humanplayer.deck.cards
        if set(c.skills.get_types()) & set(from_card.skills.get_types()) == set()
    ]


class SkillTransfererLocation(Location):
    """Transfer skills from one card to another.

    If `from_card` has only one skill, the skill will be transferred to `to_card` and
    the `from_card` will be destroyed.

    If `from_card` has several skills, then a) applicable `to_cards` are only those that
    have no skills in common with the `from_card`, and b) one of the `from_card` skills
    will be picked at random and applied to `to_card`.

    Notes:
    - There is currently no max number of skills per card. (Should there be?)
    - There are currently no restrictions as to which skills can and cannot be combined
      with which other skills. (Should there be?)
    """

    # FIXME Add the possibility to pick a different card once a from_card has been
    # selected but before the to_card has been chosen (=escape key functionality)

    marker = "S→→"

    def generate(self) -> None:
        super().generate()

    def handle(self, view_class: Type[SkillTransfererView]) -> bool:
        view = view_class(gg.humanplayer.deck.cards)

        # Check error conditions:
        if gg.humanplayer.deck.size() < 2:
            view.error("Sorry, you don't have enough cards for this.")
            return True

        from_cards = [c for c in gg.humanplayer.deck.cards if c.is_skilled()]
        if len(from_cards) == 0:
            view.error("You don't have any cards with skills unfortunately...")
            return True

        if not any(len(get_to_cards(from_card)) > 0 for from_card in from_cards):
            view.error(
                "There is no combination of cards in your deck\n"
                "that works for a successful skill transfer. Sorry..."
            )
            return True

        # Have the user pick a from_card and a to_card from the list of possible
        # to_cards:
        while True:
            from_card = view.pick_from(from_cards)
            to_cards = get_to_cards(from_card)
            if len(to_cards) > 0:
                to_card = view.pick_to(to_cards)
                break
            view.message(
                "There are no cards you can apply these skill(s) to.\n"
                "Please pick a different card to get the skill(s) from."
            )

        # Apply (random) skill to the second card and destroy the first:
        which_skill = random.choice(from_card.skills.get_types())
        to_card.skills.add(which_skill)
        view.show_upgrade(to_card)
        if from_card.skills.count() == 1:
            view.show_destroy(from_card)
            gg.humanplayer.deck.remove_card(from_card)
        else:
            from_card.skills.remove(which_skill)
            view.show_upgrade(from_card)

        view.close()
        return True
