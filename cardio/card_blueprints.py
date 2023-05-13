from typing import List
from . import Card, CardList, skills


_BLUEPRINTS = [
    Card("Hamster", 0, 1, 0),
    Card("Koala", 1, 3, 1),
    Card("Porcupine", 1, 2, 1, skills=[skills.Airdefense]),
    Card("Lynx", 3, 2, 2),
    Card("Weasel", 1, 1, 0, costs_spirits=2),
    Card("Church Mouse", 1, 1, 1, skills=[skills.Fertility]),
]


def create_card_from_blueprint(name: str) -> Card:
    found = [c for c in _BLUEPRINTS if c.name == name]
    assert len(found) == 1
    return found[0].copy()


def create_cards_from_blueprints(namelist: List[str]) -> CardList:
    return [create_card_from_blueprint(n) for n in namelist]
