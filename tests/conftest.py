import pytest


@pytest.fixture(autouse=True)
def never_shuffle(mocker, request):
    """To make tests determistic."""
    if 'disable_never_shuffle' in request.keywords:
        return
    mocker.patch("cardio.deck.Deck.shuffle")
