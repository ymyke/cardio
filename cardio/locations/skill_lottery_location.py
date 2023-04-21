import random
from typing import Protocol, Type
from cardio import gg, Card, CardList, Skill
from .location import Location
from .baseview import BaseLocationView


class SkillLotteryView(BaseLocationView, Protocol):
    def __init__(self, cards: CardList) -> None:
        ...

    def pick(self, activecards: CardList) -> Card:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...


class SkillLotteryLocation(Location):
    """Add a random skill to a card.

    If the card already has skills, there is a chance that a random existing skill is
    removed rather than a new one added.

    Notes:
    - There is currently no max number of skills per card. (Should there be?)
    - There are currently no restrictions as to which skills can and cannot be combined
      with which other skills. (Should there be?)
    """

    marker = "SL⚀"

    def generate(self) -> None:
        super().generate()

    def handle(self, view_class: Type[SkillLotteryView]) -> bool:
        view = view_class(gg.humanplayer.deck.cards)
        possible_cards = [
            c for c in gg.humanplayer.deck.cards if len(c.skills) < len(Skill)
        ]
        if not possible_cards:
            view.error("Sorry, you don't have any cards that can get more skills.")
            return True
        card = view.pick(possible_cards)
        if card.skills and random.random() < len(card.skills) / len(Skill):
            skill = random.choice(card.skills)
            card.skills.remove(skill)
            view.show_upgrade(card)
            view.message(f"{card.name} lost the {skill.name} skill. 😢")
        else:
            skill = random.choice(list(set(Skill) - set(card.skills)))
            card.skills.append(skill)
            view.show_upgrade(card)
            view.message(f"{card.name} gained the {skill.name} skill! 🥳")

        view.close()
        return True
