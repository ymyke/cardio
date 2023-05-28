import os
from collections import defaultdict
from typing import List, Optional, Union
from cardio import Card, skills
from .blueprint import Blueprint, BlueprintList
from . import all_blueprints


MAX_NAME_LENGTH = 14


class BlueprintNameExistsError(Exception):
    pass


class BlueprintEquivalentExistsError(Exception):
    pass


class BlueprintNameNotFoundError(Exception):
    pass


class BlueprintNameTooLongError(Exception):
    pass


class BlueprintSkillNameIncludedError(Exception):
    pass


class BlueprintCatalog:
    _blueprints: BlueprintList
    # `_by_potency` allows for fast lookup of blueprints with a given potency:
    _by_potency: dict[int, BlueprintList]

    def __init__(self) -> None:
        self._blueprints = BlueprintList()
        self._by_potency = defaultdict(BlueprintList)
        for b in all_blueprints.all_blueprints:
            self.add_blueprint(b)
            self._by_potency[b._original.potency].append(b)

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

    def remove(self, b: Blueprint) -> None:
        self._blueprints.remove(b)

    def find_by_names(self, names: List[str]) -> BlueprintList:
        return BlueprintList([self.get(name) for name in names])

    def find_by_potency(
        self, wanted_potency: int, exactly: bool = False
    ) -> BlueprintList:
        """Find all blueprints with potency `potency` (normalized, i.e., [0, 100])."""
        return self._by_potency[wanted_potency]

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
        def skillname_included(name: str) -> bool:
            skillnames = [
                c.__name__ for c in skills.get_skilltypes(implemented_only=True)
            ]
            skillnames.remove("Underdog")  # Because there's nice under* names
            return any(s.lower()[:5] in name.lower() for s in skillnames)

        if len(blueprint.name) > MAX_NAME_LENGTH:
            raise BlueprintNameTooLongError(
                f"Blueprint name '{blueprint.name}' too long (max {MAX_NAME_LENGTH})."
            )
        if skillname_included(blueprint.name):
            raise BlueprintSkillNameIncludedError(
                f"Blueprint name '{blueprint.name}' includes a skill name."
            )
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
        folder = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(folder, filename)
        with open(path, "w", encoding="utf-8") as f:
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