import pytest
from cardio import HumanPlayer, Grid, FightVnC, gg, Card


@pytest.fixture
def session_setup():
    gg.humanplayer = HumanPlayer(name="Schnuzgi", lives=1)
    gg.humanplayer.deck.cards = [Card("C", 1, 1, 1)]
    gg.grid = Grid(width=4)
    gg.vnc = FightVnC(gg.grid, None)
    yield gg.humanplayer, gg.grid, gg.vnc


@pytest.fixture(autouse=True)
def never_shuffle(mocker, request):
    """To make tests determistic."""
    if "disable_never_shuffle" in request.keywords:
        return
    mocker.patch("cardio.deck.Deck.shuffle")
