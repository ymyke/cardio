import pytest
from cardio import HumanPlayer, Grid, FightVnC, gg, Card, FightCard


@pytest.fixture
def gg_setup():
    def fightify(*args, **kwargs) -> FightCard:
        """Convenenience function to create FightCards easily."""
        return FightCard.from_card(Card(*args, **kwargs))

    gg.humanplayer = HumanPlayer(name="Schnuzgi", lives=1)
    gg.humanplayer.deck.cards = [Card("C", 1, 1, 1)]
    grid = Grid(width=4)
    gg.vnc = FightVnC(grid, None)
    FightCard.init_fight(gg.vnc, grid)
    yield gg.humanplayer, grid, gg.vnc, fightify


@pytest.fixture(autouse=True)
def never_shuffle(mocker, request):
    """To make tests determistic."""
    if "disable_never_shuffle" in request.keywords:
        return
    mocker.patch("cardio.deck.Deck.shuffle")
