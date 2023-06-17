import pytest
from collections import namedtuple
from cardio import HumanPlayer, Grid, FightVnC, Card, FightCard

TestSetup = namedtuple("TestSetup", ["human", "grid", "vnc", "ff"])


@pytest.fixture
def tt_setup():
    def fightify(*args, **kwargs) -> FightCard:
        """Convenenience function to create FightCards easily."""
        return FightCard.from_card(Card(*args, **kwargs))

    human = HumanPlayer(name="HP", lives=1)
    grid = Grid(width=4)
    vnc = FightVnC(grid, None, human)
    FightCard.init_fight(vnc, grid)
    yield TestSetup(human, grid, vnc, fightify)


@pytest.fixture(autouse=True)
def never_shuffle(mocker, request):
    """To make tests determistic."""
    if "disable_never_shuffle" in request.keywords:
        return
    mocker.patch("cardio.deck.Deck.shuffle")
