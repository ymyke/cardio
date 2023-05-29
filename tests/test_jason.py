import cardio.jason as jason
from cardio import HumanPlayer
from cardio.blueprints import thecatalog
from cardio.run import Run
from cardio.blueprints import Blueprint


def test_encode_decode_humanplayer_inluding_cards_etc():
    c = thecatalog.get("Church Mouse").instantiate()
    hp = HumanPlayer("me")
    hp.deck.add_card(c)
    hp.collection.add_card(c)
    j = jason.encode(hp)
    np = jason.decode(j)
    assert isinstance(np, HumanPlayer)
    assert np.name == hp.name
    assert np.lives == hp.lives
    assert np.gems == hp.gems
    assert np.spirits == hp.spirits
    assert np.deck.size() == hp.deck.size()
    assert np.collection.size() == hp.collection.size()
    assert np.deck.cards[0].name == hp.deck.cards[0].name
    assert np.collection.cards[0].name == hp.collection.cards[0].name


def test_encode_decode_run():
    r = Run()
    j = jason.encode(r)
    nr = jason.decode(j)
    assert isinstance(nr, Run)
    assert nr.base_seed == r.base_seed
    assert nr.current_rung == r.current_rung
    assert nr.current_index == r.current_index


def test_encode_decode_blueprint():
    b = thecatalog._blueprints[-1]
    j = jason.encode(b)
    nb = jason.decode(j)
    assert isinstance(nb, Blueprint)
    assert nb.is_gameplay_equal(b)
    assert nb.name == b.name
