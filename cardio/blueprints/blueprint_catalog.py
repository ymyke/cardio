from __future__ import annotations
from pathlib import Path
from collections import defaultdict
from typing import List, Optional, Union
from cardio import Card, jason, skills
from .blueprint import Blueprint, BlueprintList


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


def _get_path(filename: Optional[str]) -> Path:
    filename = filename or "_all_blueprints.json"
    return Path(__file__).resolve().parent / filename


class BlueprintCatalog:
    _blueprints: BlueprintList
    # `_by*potency` allows for fast lookup of blueprints with a given (core) potency:
    _by_potency: dict[int, BlueprintList]
    _by_core_potency: dict[int, BlueprintList]

    def __init__(self, blueprints: Optional[BlueprintList] = None) -> None:
        self._blueprints = blueprints or BlueprintList()
        self._by_potency = defaultdict(BlueprintList)
        self._by_core_potency = defaultdict(BlueprintList)
        for b in self._blueprints:
            self._by_potency[b._original.potency].append(b)
            self._by_core_potency[b._original.core_potency].append(b)

    def find_by_name(self, name: str) -> BlueprintList:
        """Find all blueprints with name `name`"""

        def normalize(x: str) -> str:
            return "".join(c.lower() for c in x if c.isalpha())

        return BlueprintList(
            [b for b in self._blueprints if normalize(b.name) == normalize(name)]
        )

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
        self, min_potency: int, max_potency: Optional[int] = None, *, core: bool
    ) -> BlueprintList:
        """Return all blueprints with potency in the range `[min_potency, max_potency]`.
        If only `min_potency` is given, return all blueprints with potency
        `min_potency`. Use core potency if `core` is True, otherwise use total potency.
        """
        max_potency = max_potency or min_potency
        whichpot = self._by_core_potency if core else self._by_potency
        res = []
        for p in range(min_potency, max_potency + 1):
            res.extend(whichpot[p])
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
        jason.save_file(list(self._blueprints), _get_path(filename))

    @classmethod
    def load(cls, filename: Optional[str] = None) -> BlueprintCatalog:
        return cls(BlueprintList(jason.load_file(_get_path(filename))))


# Create the one catalog that is used throughout the game:
thecatalog = BlueprintCatalog.load()
