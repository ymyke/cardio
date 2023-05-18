from cardio import Card
from cardio.blueprints.blueprint import Blueprint


def test_init():
    c = Card("X", 1, 2, 3)
    b = Blueprint(c, "desc")
    assert b.name == "X"
    assert b.description == "desc"
    assert b._original == c


def test_instantiate():
    c = Card("X", 1, 2, 3)
    b = Blueprint(c, "desc")
    d = b.instantiate()
    assert not d == c
    assert d.is_gameplay_equal(c)
    assert d.name == c.name


def test_methods():
    c = Card("X", 1, 2, 3)
    b = Blueprint(c, "desc")
    d = b.instantiate()
    assert b.has_potency(c.potency, exactly=True)
    assert b.is_gameplay_equal(c)
