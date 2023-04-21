from cardio import Card, CardList, Deck, gg, Skill
from cardio.locations.skill_lottery_location import (
    SkillLotteryLocation,
    SkillLotteryView,
)


class FakeSkillLotteryView(SkillLotteryView):
    def __init__(self, *args, **kwargs) -> None:
        ...

    def pick(self, activecards: CardList) -> Card:
        return activecards[0]

    def show_upgrade(self, card: Card) -> None:
        ...

    def close(self) -> None:
        ...

    def message(self, msg: str) -> None:
        ...

    def error(self, msg: str) -> None:
        ...


def test_get_skill_for_card_without_skills(gg_setup):
    card = Card("Card", 1, 1, 1, None)
    gg.humanplayer.deck = Deck("main", [card])
    loc = SkillLotteryLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillLotteryView)
    assert res
    assert len(card.skills) == 1


def test_get_skill_for_card_with_skills(mocker, gg_setup):
    card = Card("Card", 1, 1, 1, [Skill.SPINES])
    gg.humanplayer.deck = Deck("main", [card])
    loc = SkillLotteryLocation("0", 0, 0, [])
    mocker.patch("random.random", return_value=1)
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 2
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 3
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 4
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 5


def test_get_skill_for_card_with_skills_and_remove_one(mocker, gg_setup):
    card = Card("Card", 1, 1, 1, [Skill.SPINES, Skill.SOARING, Skill.AIRDEFENSE])
    gg.humanplayer.deck = Deck("main", [card])
    loc = SkillLotteryLocation("0", 0, 0, [])
    mocker.patch("random.random", return_value=0)
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 2
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 1
    assert loc.handle(view_class=FakeSkillLotteryView)
    assert len(card.skills) == 0
