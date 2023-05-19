from . import Card
from .skills import get_skilltypes
from cardio.blueprints import thecatalog


def print_potency_stats():
    """Print potencies of all blueprints and skills as well as the theoretical current
    potency range.
    """
    print("Blueprints by potency:")
    blueprints = sorted(
        thecatalog._blueprints, key=lambda b: b._original.potency, reverse=True
    )
    for b in blueprints:
        print(f"{b._original.potency:3} {b.name}")

    print("\nSkills by potency:")
    skills = sorted(
        get_skilltypes(implemented_only=False),
        key=lambda s: s.potency,
        reverse=True,
    )
    for s in skills:
        print(f"{s.potency:3} {s.name} {s.symbol}")

    print("\nRaw potency ranges:")
    curmin, curmax, theorymax = Card.get_raw_potency_range()
    print(f"Current max possible raw potency: {curmax}")
    print(f"Theoretical max possible raw potency: {theorymax}")
    print(f"Current min possible raw potency: {curmin}")
    print(
        f"""\
Notes:
- This is with the current set of skills available and
under the assumption that all attributes max out at {Card.MAX_ATTR}
and a card can have no more than {Card.MAX_SKILLS} skills.
- Potency is raw potency, normalized to [0, 100]. So
all potencies other than raw potencies are normalized
to that range.
"""
    # TODO I think potency is [-100, 100] currently! What does this mean? Add Overload
    # to Weasel to check.
    )
