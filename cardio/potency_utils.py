from . import Card
from .skills import get_skilltypes
from cardio.blueprints import thecatalog


_skills_by_potency = sorted(
    get_skilltypes(implemented_only=True),
    key=lambda s: s.potency,
    reverse=True,
)
MINCARD = Card(
    name="Min",
    power=0,
    health=1,
    costs_fire=Card.MAX_ATTR,
    skills=[s for s in _skills_by_potency[-Card.MAX_SKILLS :] if s.potency < 0],
    costs_spirits=0,  # 0, bc we can't have both types of costs in a card
    has_spirits=0,
    has_fire=0,
)
MAXCARD = Card(
    name="Max",
    power=Card.MAX_ATTR,
    health=Card.MAX_ATTR,
    costs_fire=0,
    skills=_skills_by_potency[: Card.MAX_SKILLS],  # type: ignore
    costs_spirits=0,
    has_spirits=Card.MAX_ATTR,
    has_fire=Card.MAX_ATTR,
)


def print_potency_stats():
    """Print potencies of all blueprints and skills as well as the theoretical current
    potency range.
    """
    print("Blueprints by potency (core potency in brackets):")
    blueprints = sorted(
        thecatalog._blueprints, key=lambda b: b._original.potency, reverse=True
    )
    for b in blueprints:
        print(f"{b._original.potency:3} {b.name:18} ({b._original.core_potency:3})")

    print("\nSkills by potency:")
    skills = sorted(
        get_skilltypes(implemented_only=True),
        key=lambda s: s.potency,
        reverse=True,
    )
    for s in skills:
        print(f"{s.potency:3} {s.name} {s.symbol}")

    print()
    print("Ranges:")
    print(f"Potency range:      [{MINCARD.potency}, {MAXCARD.potency}]")
    print(f"Core potency range: [{MINCARD.core_potency}, {MAXCARD.core_potency}]")
