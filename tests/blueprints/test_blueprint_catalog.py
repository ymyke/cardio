"""Test blueprint catalog.

Note that this relies on the catalog being loaded (`thecatalog`/`tc`) and non-empty. No
tests will change the catalog in its persisted state.
"""

import pytest
from cardio import Card
from cardio.blueprints.blueprint import Blueprint
from cardio.blueprints.blueprint_catalog import (
    thecatalog as tc,
    BlueprintNameNotFoundError,
    BlueprintNameExistsError,
    BlueprintEquivalentExistsError,
    BlueprintNameTooLongError,
    BlueprintSkillNameIncludedError,
)


def test_init_load():
    assert len(tc._blueprints) > 0
    assert all(isinstance(b, Blueprint) for b in tc._blueprints)


def test_find_by_name():
    assert len(tc.find_by_name("thisdoesnotexist")) == 0
    assert len(tc.find_by_name(tc._blueprints[0].name)) == 1


def test_find_by_names():
    assert len(tc.find_by_names([tc._blueprints[0].name, tc._blueprints[1].name])) == 2


def test_get():
    assert tc.get(tc._blueprints[0].name) == tc._blueprints[0]


def test_get_non_existing():
    with pytest.raises(BlueprintNameNotFoundError):
        tc.get("thisdoesnotexist")


def test_find_by_potency():
    assert len(tc.find_by_potency(tc._blueprints[0]._original.potency)) > 0


def test_find_by_potency_range():
    assert set(tc.find_by_potency_range(0, 100)) == set(tc._blueprints)


def test_find_gameplay_equals():
    assert len(tc.find_gameplay_equals(tc._blueprints[0])) > 0


def test_add_blueprint_successfully():
    c = Card("X", 1, 1, 1, skills=["xxx"])
    b = Blueprint(c, "desc")
    tc.add_blueprint(b)
    assert b in tc._blueprints


def test_add_blueprint_name_too_long():
    c = Card("X", 1, 1, 1)
    b = Blueprint(c, "desc")
    b.name = "thisnameisdefinitelyverymuchtoooverlylong"
    with pytest.raises(BlueprintNameTooLongError):
        tc.add_blueprint(b)


def test_add_blueprint_skill_name_included():
    c = Card("X", 1, 1, 1)
    b = Blueprint(c, "desc")
    b.name = "xinstanty"
    with pytest.raises(BlueprintSkillNameIncludedError):
        tc.add_blueprint(b)


def test_add_blueprint_name_exists():
    c = tc._blueprints[0]._original
    c.skills = ["xxx"]
    b = Blueprint(c, "desc")
    with pytest.raises(BlueprintNameExistsError):
        tc.add_blueprint(b)


def test_add_blueprint_equivalent_exists():
    c = tc._blueprints[0]._original
    c.name = "DSNTXST"
    b = Blueprint(c, "desc")
    with pytest.raises(BlueprintEquivalentExistsError):
        tc.add_blueprint(b)


def test_remove():
    b = tc._blueprints[-1]
    tc.remove(b)
    assert b not in tc._blueprints
    tc.add_blueprint(b)


def test_instantiate():
    res = tc.find_by_names(["Hamster", "Koala"]).instantiate()
    assert len(res) == 2
    assert all(isinstance(c, Card) for c in res)
