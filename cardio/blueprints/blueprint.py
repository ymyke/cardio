from __future__ import annotations
from typing import Union
from cardio import Card


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
        return f"Blueprint(original={repr(self._original)}, description='{self.description}')"

    def is_gameplay_equal(self, other: Union[Blueprint, Card]) -> bool:
        if isinstance(other, Blueprint):
            return self._original.is_gameplay_equal(other._original)
        else:
            return self._original.is_gameplay_equal(other)

    def has_potency(self, potency: int, exactly: bool = False) -> bool:
        return self._original.has_potency(potency, exactly)

    def instantiate(self) -> Card:
        return self._original.copy()
