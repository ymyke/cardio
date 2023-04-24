import copy
from typing import List, Tuple
from . import Card, CardList, Skill


_BLUEPRINTS = [
    Card("Hamster", 0, 1, 0),
    Card("Koala", 1, 3, 1),
    Card("Porcupine", 1, 2, 1, skills=[Skill.AIRDEFENSE]),
    Card("Lynx", 3, 2, 2),
    Card("Weasel", 1, 1, 0, costs_spirits=2),
    Card("Church Mouse", 1, 1, 1, skills=[Skill.FERTILITY]),
]


def create_card_from_blueprint(name: str) -> Card:
    found = [c for c in _BLUEPRINTS if c.name == name]
    assert len(found) == 1
    return copy.deepcopy(found[0])  # TODO Use clone


def create_cards_from_blueprints(namelist: List[str]) -> CardList:
    return [create_card_from_blueprint(n) for n in namelist]


def print_potency_stats():
    """Print potencies of all cards and skills as well as the theoretical current
    potency range.
    """
    print("Cards by potency:")
    cards = sorted(_BLUEPRINTS, key=lambda c: c.potency, reverse=True)
    for c in cards:
        print(f"{c.potency:3} {c.name}")

    print("\nSkills by potency:")
    skills = sorted(list(Skill), key=lambda s: s.value.potency, reverse=True)
    for s in skills:
        print(f"{s.value.potency:3} {s.name} {s.value.symbol}")

    print("\nPotency ranges:")
    minpot, maxpot = get_potency_range()
    print(f"Current max possible potency: {maxpot}")
    print(f"Current min possible potency: {minpot}")
    print(
        "(This is with the current set of skills available and\n" 
        f"under the assumption that all attributes max out at {Card.MAX_ATTR}\n"
        f"and a card can have no more than {Card.MAX_SKILLS} skills.)"
    )


def get_potency_range() -> Tuple[int, int]:
    """Return the theoretical current potency range."""
    skills = sorted(list(Skill), key=lambda s: s.value.potency, reverse=True)
    maxcard = Card(
        name="Max",
        initial_power=Card.MAX_ATTR,
        initial_health=Card.MAX_ATTR,
        costs_fire=0,
        skills=skills[:Card.MAX_SKILLS],
        costs_spirits=0,
        has_spirits=Card.MAX_ATTR,
        has_fire=Card.MAX_ATTR,
    )
    mincard = Card(
        name="Min",
        initial_power=0,
        initial_health=0,
        costs_fire=10,
        skills=[s for s in skills[-Card.MAX_SKILLS:] if s.value.potency < 0],
        costs_spirits=0,  # 0, bc we can't have both types of costs in a card
        has_spirits=0,
        has_fire=0,
    )
    return mincard.potency, maxcard.potency
