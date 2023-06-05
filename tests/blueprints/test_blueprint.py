from cardio import Card
from cardio.blueprints.blueprint import Blueprint, BlueprintList


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
    assert b.is_gameplay_equal(c)

def test_blueprintlist():
    b1 = Blueprint(Card("X", 1, 2, 3), "desc1")
    b2 = Blueprint(Card("Y", 1, 2, 3), "desc2")
    bpl = BlueprintList([b1, b2])
    assert bpl[0] == b1
    assert bpl[1] == b2
    assert all(isinstance(b, Blueprint) for b in bpl)
    assert all(isinstance(c, Card) for c in bpl.instantiate())