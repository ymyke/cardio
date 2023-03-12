import pytest
from cardio import HumanPlayer, Grid, FightVnC, session, Card


@pytest.fixture
def session_setup():
    session.humanplayer = HumanPlayer(name="Schnuzgi", lives=1)
    session.humanplayer.deck.cards = [Card("C", 1, 1, 1)]
    session.grid = Grid(width=4)
    session.vnc = FightVnC(session.grid, None)
    yield session.humanplayer, session.grid, session.vnc


@pytest.fixture(autouse=True)
def never_shuffle(mocker, request):
    """To make tests determistic."""
    if "disable_never_shuffle" in request.keywords:
        return
    mocker.patch("cardio.deck.Deck.shuffle")
