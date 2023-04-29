from . import Card
from .skills import get_skilltypes


def print_potency_stats():
    """Print potencies of all cards and skills as well as the theoretical current
    potency range.
    """
    # Import this here to prevent some circular import issues:
    from cardio.card_blueprints import _BLUEPRINTS

    print("Cards by potency:")
    cards = sorted(_BLUEPRINTS, key=lambda c: c.potency, reverse=True)
    for c in cards:
        print(f"{c.potency:3} {c.name}")

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
    )
