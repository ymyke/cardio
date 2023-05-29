from cardio import HumanPlayer


def test_humanplayer_init():
    p = HumanPlayer("Human")
    assert p.name == "Human"
    assert p.lives == 1
    assert p.gems == 0
    assert p.spirits == 0
    assert p.deck.name == "main"
    assert p.collection.name == "collection"
    assert p.hamster_blueprint.name == "Hamster"


def test_humanplayer_create_new():
    p = HumanPlayer.create_new("Human")
    assert p.name == "Human"
    assert len(p.collection.cards) > 0
