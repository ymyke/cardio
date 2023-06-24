from typing import List
from cardio import Card, Deck
from cardio.locations.upgrader_location import (
    PowerUpgraderLocation,
    HealthUpgraderLocation,
    PowerUpgraderMultiLocation,
    UpgraderView,
)


class FakeUpgraderView(UpgraderView):
    def __init__(self, cards: List[Card], *args, **kwargs) -> None:
        self.cards = cards

    def pick(self) -> Card:
        return self.cards[0]

    def show_destroy(self, card: Card) -> None:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...

    def confirm(self, card: Card) -> bool:
        return True

    def close(self) -> None:
        ...

    def message(self, msg: str) -> None:
        ...

    def error(self, msg: str) -> None:
        ...


def test_powerupgraderlocation(tt_setup):
    human, *_ = tt_setup
    card = Card("X", 1, 1, 1, None)
    human.deck = Deck("main", [card])
    loc = PowerUpgraderLocation("0", 0, 0, [])
    loc.handle(view_class=FakeUpgraderView, humanplayer=human)
    assert card.power == 2
    assert human.deck.size() == 1


def test_healthupgraderlocation(tt_setup):
    human, *_ = tt_setup
    card = Card("X", 1, 1, 1, None)
    human.deck = Deck("main", [card])
    loc = HealthUpgraderLocation("0", 0, 0, [])
    loc.handle(view_class=FakeUpgraderView, humanplayer=human)
    assert card.health == 2
    assert human.deck.size() == 1


def test_powerupgraderlocation_multi(tt_setup):
    human, *_ = tt_setup
    card = Card("X", 1, 1, 1, None)
    human.deck = Deck("main", [card])
    loc = PowerUpgraderMultiLocation("0", 0, 0, [])
    # Together with the fake view above, which always confirms in the `confirm` method,
    # the following will upgrade the card so often that will get destroyed eventually:
    loc.handle(view_class=FakeUpgraderView, humanplayer=human)
    assert human.deck.is_empty()
