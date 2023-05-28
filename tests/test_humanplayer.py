from cardio import HumanPlayer


def test_humanplayer_init():
    hp = HumanPlayer("Human")
    assert hp.name == "Human"
    assert hp.lives == 1
    assert hp.gems == 0
    assert hp.spirits == 0
    assert hp.deck.name == "main"
    assert hp.collection.name == "collection"
