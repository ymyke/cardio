import pytest
from cardio import HumanPlayer, Grid, FightVnC, Card, FightCard


@pytest.fixture
def gg_setup():
    def fightify(*args, **kwargs) -> FightCard:
        """Convenenience function to create FightCards easily."""
        return FightCard.from_card(Card(*args, **kwargs))

    humanplayer = HumanPlayer(name="Schnuzgi", lives=1)
    humanplayer.deck.cards = [Card("C", 1, 1, 1)]
    grid = Grid(width=4)
    vnc = FightVnC(grid, None, humanplayer)
    FightCard.init_fight(vnc, grid)
    yield humanplayer, grid, vnc, fightify


@pytest.fixture(autouse=True)
def never_shuffle(mocker, request):
    """To make tests determistic."""
    if "disable_never_shuffle" in request.keywords:
        return
    mocker.patch("cardio.deck.Deck.shuffle")
