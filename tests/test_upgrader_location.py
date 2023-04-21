from cardio import Card, Deck, gg
from cardio.locations.upgrader_location import (
    PowerUpgraderLocation,
    HealthUpgraderLocation,
    PowerUpgraderMultiLocation,
    UpgraderView,
)


class FakeUpgraderView(UpgraderView):
    def __init__(self, *args, **kwargs) -> None:
        ...

    def pick(self) -> Card:
        return gg.humanplayer.deck.cards[0]

    def show_destroy(self, card: Card) -> None:
        ...

    def show_upgrade(self, card: Card) -> None:
        ...

    def ask(self, card: Card) -> bool:
        return True

    def close(self) -> None:
        ...

    def message(self, msg: str) -> None:
        ...

    def error(self, msg: str) -> None:
        ...


def test_powerupgraderlocation(gg_setup):
    card = Card("X", 1, 1, 1, None)
    gg.humanplayer.deck = Deck("main", [card])
    loc = PowerUpgraderLocation("0", 0, 0, [])
    loc.handle(view_class=FakeUpgraderView)
    assert card.power == 2
    assert card.initial_power == 2
    assert gg.humanplayer.deck.size() == 1


def test_healthupgraderlocation(gg_setup):
    card = Card("X", 1, 1, 1, None)
    gg.humanplayer.deck = Deck("main", [card])
    loc = HealthUpgraderLocation("0", 0, 0, [])
    loc.handle(view_class=FakeUpgraderView)
    assert card.health == 2
    assert card.initial_health == 2
    assert gg.humanplayer.deck.size() == 1


def test_powerupgraderlocation_multi(gg_setup):
    card = Card("X", 1, 1, 1, None)
    gg.humanplayer.deck = Deck("main", [card])
    loc = PowerUpgraderMultiLocation("0", 0, 0, [])
    # Together with the fake view above, which always confirms in the `ask` method, the
    # following will upgrade the card so often that will get destroyed eventually:
    loc.handle(view_class=FakeUpgraderView)
    assert gg.humanplayer.deck.is_empty()
