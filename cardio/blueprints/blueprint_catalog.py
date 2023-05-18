from typing import List, Optional, Union
from cardio import Card
from .blueprint import Blueprint, BlueprintList
from . import all_blueprints

# TODO:
# - incorporate blueprints here


class BlueprintNameExistsError(Exception):
    pass


class BlueprintEquivalentExistsError(Exception):
    pass


class BlueprintNameNotFoundError(Exception):
    pass


class BlueprintCatalog:
    _blueprints: BlueprintList

    def __init__(self) -> None:
        self._blueprints = BlueprintList([])
        for b in all_blueprints.all_blueprints:
            self.add_blueprint(b)

    def find_by_name(self, name: str) -> BlueprintList:
        """Find all blueprints with name `name`."""
        return BlueprintList([b for b in self._blueprints if b.name == name])

    def get(self, name: str) -> Blueprint:
        res = self.find_by_name(name)
        if len(res) > 1:
            raise BlueprintNameExistsError(
                f"Several blueprints with name '{name}' found in catalog."
            )
        if len(res) == 0:
            raise BlueprintNameNotFoundError(
                f"No blueprint with name '{name}' found in catalog."
            )
        return res[0]

    def find_by_names(self, names: List[str]) -> BlueprintList:
        return BlueprintList([self.get(name) for name in names])

    def find_by_potency(
        self, wanted_potency: int, exactly: bool = False
    ) -> BlueprintList:
        """Find all blueprints with potency `potency` (normalized, i.e., [0, 100])."""
        return BlueprintList(
            [b for b in self._blueprints if b.has_potency(wanted_potency, exactly)]
        )

    def find_by_potency_range(
        self, min_potency: int, max_potency: int
    ) -> BlueprintList:
        """Find all blueprints with potency in the range [min_potency, max_potency]."""
        res = []
        for p in range(min_potency, max_potency + 1):
            res.extend(self.find_by_potency(p, exactly=True))
        return BlueprintList(res)

    def find_gameplay_equals(self, other: Union[Blueprint, Card]) -> BlueprintList:
        """Return all blueprints that are gameplay-equal to `other`."""
        return BlueprintList(
            [b for b in self._blueprints if b.is_gameplay_equal(other)]
        )

    def add_blueprint(self, blueprint: Blueprint) -> None:
        if self.find_by_name(blueprint.name):
            raise BlueprintNameExistsError(
                f"Blueprint with name '{blueprint.name}' already exists."
            )
        eqs = self.find_gameplay_equals(blueprint)
        if eqs:
            raise BlueprintEquivalentExistsError(
                f"Equivalent blueprint to '{blueprint.name}' already exists: {eqs[0].name}."
            )
        self._blueprints.append(blueprint)

    def save(self, filename: Optional[str] = None) -> None:
        filename = filename or "all_blueprints.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("from cardio import Card, skills\n")
            f.write("from .blueprint import Blueprint\n")
            f.write("all_blueprints = [\n")
            for b in self._blueprints:
                s = "# " + "\n# ".join(str(b._original).split("\n"))
                f.write(s + "\n")
                f.write(repr(b))
                f.write(",\n")
            f.write("]\n")


# Create the one catalog that is used throughout the game:
thecatalog = BlueprintCatalog()
