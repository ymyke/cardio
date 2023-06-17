from cardio import Card, CardList, Deck, skills
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


def test_get_skill_for_card_without_skills(tt_setup):
    human, *_ = tt_setup
    card = Card("Card", 1, 1, 1, None)
    human.deck = Deck("main", [card])
    loc = SkillLotteryLocation("0", 0, 0, [])
    res = loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert res
    assert card.skills.count() == 1


def test_get_skill_for_card_with_skills(mocker, tt_setup):
    human, *_ = tt_setup
    card = Card("Card", 1, 1, 1, [skills.Spines])
    human.deck = Deck("main", [card])
    loc = SkillLotteryLocation("0", 0, 0, [])
    mocker.patch("random.random", return_value=1)
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 2
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 3
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 4
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 5


def test_get_skill_for_card_with_skills_and_remove_one(mocker, tt_setup):
    human, *_ = tt_setup
    card = Card("Card", 1, 1, 1, [skills.Spines, skills.Soaring, skills.Airdefense])
    human.deck = Deck("main", [card])
    loc = SkillLotteryLocation("0", 0, 0, [])
    mocker.patch("random.random", return_value=0)
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 2
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 1
    assert loc.handle(view_class=FakeSkillLotteryView, humanplayer=human)
    assert card.skills.count() == 0
