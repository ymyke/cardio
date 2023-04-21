from cardio import Card, CardList, Deck, gg, Skill
from cardio.locations.skill_transferer_location import (
    SkillTransfererLocation,
    SkillTransfererView,
)

message = ""


class FakeSkillTransfererView(SkillTransfererView):
    def __init__(self, *args, **kwargs) -> None:
        ...

    def pick_from(self, from_cards: CardList) -> Card:
        return from_cards[0]

    def pick_to(self, to_cards: CardList) -> Card:
        return to_cards[0]

    def show_destroy(self, card: Card) -> None:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...

    def close(self) -> None:
        ...

    def message(self, msg: str) -> None:
        global message
        message = msg

    def error(self, msg: str) -> None:
        self.message(msg)


def test_successfully_transfer_one_skill_destroying_the_from_card(gg_setup):
    cards = [Card("From", 1, 1, 1, [Skill.SPINES]), Card("To", 1, 1, 1, None)]
    gg.humanplayer.deck = Deck("main", cards)
    loc = SkillTransfererLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillTransfererView)
    assert res == True
    assert gg.humanplayer.deck.size() == 1
    assert gg.humanplayer.deck.cards[0].name == "To"
    assert gg.humanplayer.deck.cards[0].skills == [Skill.SPINES]


def test_successfully_transfer_several_skills_not_destroying_the_from_card(gg_setup):
    cards = [
        Card("From", 1, 1, 1, [Skill.SPINES, Skill.SOARING]),
        Card("To", 1, 1, 1, None),
    ]
    gg.humanplayer.deck = Deck("main", cards)
    loc = SkillTransfererLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillTransfererView)
    assert res == True
    assert gg.humanplayer.deck.size() == 2
    assert gg.humanplayer.deck.cards[0].skills in [[Skill.SPINES], [Skill.SOARING]]
    assert gg.humanplayer.deck.cards[1].skills in [[Skill.SPINES], [Skill.SOARING]]


def test_deck_too_small(gg_setup):
    cards = [Card("From", 1, 1, 1, None)]
    gg.humanplayer.deck = Deck("main", cards)
    loc = SkillTransfererLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillTransfererView)
    assert res == True
    assert "don't have enough cards" in message


def test_no_skilled_cards(gg_setup):
    cards = [Card("From", 1, 1, 1, None), Card("To", 1, 1, 1, None)]
    gg.humanplayer.deck = Deck("main", cards)
    loc = SkillTransfererLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillTransfererView)
    assert res == True
    assert "don't have any cards with skills" in message


def test_no_cards_to_transfer_to(gg_setup):
    cards = [
        Card("A", 1, 1, 1, [Skill.SPINES, Skill.FERTILITY]),
        Card("B", 1, 1, 1, [Skill.SPINES, Skill.AIRDEFENSE]),
        Card("C", 1, 1, 1, [Skill.SPINES, Skill.SOARING]),
    ]
    gg.humanplayer.deck = Deck("main", cards)
    loc = SkillTransfererLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillTransfererView)
    assert res == True
    assert "no combination" in message