import pytest
from cardio import Card
from cardio.blueprints.blueprint import Blueprint
from cardio.blueprints.blueprint_catalog import (
    BlueprintCatalog,
    BlueprintNameNotFoundError,
    BlueprintNameExistsError,
    BlueprintEquivalentExistsError,
)


def test_init_load():
    bc = BlueprintCatalog()
    assert len(bc._blueprints) > 0
    assert all(isinstance(b, Blueprint) for b in bc._blueprints)


def test_find_by_name():
    bc = BlueprintCatalog()
    assert len(bc.find_by_name("thisdoesnotexist")) == 0
    assert len(bc.find_by_name(bc._blueprints[0].name)) == 1


def test_get():
    bc = BlueprintCatalog()
    assert bc.get(bc._blueprints[0].name) == bc._blueprints[0]


def test_get_non_existing():
    bc = BlueprintCatalog()
    with pytest.raises(BlueprintNameNotFoundError):
        bc.get("thisdoesnotexist")


def test_find_by_potency():
    bc = BlueprintCatalog()
    assert len(bc.find_by_potency(bc._blueprints[0]._original.potency)) > 0


def test_find_gameplay_equals():
    bc = BlueprintCatalog()
    assert len(bc.find_gameplay_equals(bc._blueprints[0])) > 0


def test_add_blueprint_successfully():
    bc = BlueprintCatalog()
    c = Card("X", 1, 1, 1, skills=["xxx"])
    b = Blueprint(c, "desc")
    bc.add_blueprint(b)
    assert b in bc._blueprints


def test_add_blueprint_name_exists():
    bc = BlueprintCatalog()
    c = bc._blueprints[0]._original
    c.skills = ["xxx"]
    b = Blueprint(c, "desc")
    with pytest.raises(BlueprintNameExistsError):
        bc.add_blueprint(b)


def test_add_blueprint_equivalent_exists():
    bc = BlueprintCatalog()
    c = bc._blueprints[0]._original
    c.name = "thisnamedoesnotexistforsure"
    b = Blueprint(c, "desc")
    with pytest.raises(BlueprintEquivalentExistsError):
        bc.add_blueprint(b)
