import copy
from typing import List
from . import Card, CardList, Skill

_BLUEPRINTS = [
    Card(name="Hamster", initial_power=0, initial_health=1, cost_fire=0),
    Card(name="Koala", initial_power=1, initial_health=3, cost_fire=1),
    Card(
        name="Porcupine",
        initial_power=1,
        initial_health=2,
        skills=[Skill.AIRDEFENSE],
        cost_fire=1,
    ),
    Card(name="Lynx", initial_power=3, initial_health=2, cost_fire=2),
    Card(name="Weasel", initial_power=1, initial_health=1, cost_fire=1),
]


def create_card_from_blueprint(name: str) -> Card:
    found = [c for c in _BLUEPRINTS if c.name == name]
    assert len(found) == 1
    return copy.deepcopy(found[0])


def create_cards_from_blueprints(namelist: List[str]) -> CardList:
    return [create_card_from_blueprint(n) for n in namelist]
