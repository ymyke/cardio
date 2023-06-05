"""`Blueprint` and `BlueprintList` classes."""

from __future__ import annotations
from collections import UserList
from typing import List, Optional, Union
from cardio import Card, CardList


class Blueprint:
    """A small wrapper around a Card that adds a description, but mostly makes sure
    blueprints are handled as such and are instantiated to create cards from them.
    """

    _original: Card
    name: str
    description: str

    def __init__(self, original: Card, description: str) -> None:
        self._original = original
        self.name = original.name
        self.description = description

    def __repr__(self) -> str:
        desc = self.description.replace("'", "\\'").replace('"', '\\"')
        return f"Blueprint(original={repr(self._original)}, description='{desc}')"

    def is_gameplay_equal(self, other: Union[Blueprint, Card]) -> bool:
        if isinstance(other, Blueprint):
            return self._original.is_gameplay_equal(other._original)
        else:
            return self._original.is_gameplay_equal(other)

    def instantiate(self) -> Card:
        return self._original.copy()


class BlueprintList(UserList[Blueprint]):
    def __init__(self, data: Optional[List[Blueprint]] = None) -> None:
        super().__init__(data or [])

    def instantiate(self) -> CardList:
        return [b.instantiate() for b in self.data]
