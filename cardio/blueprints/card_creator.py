# QQ: Let's say we generate a larger list of cards with this generator. Then we add a
# couple of new skills and incorporate new cards with that skill that fit in the
# collection of existing cards in a statistically sound manner. How to do that? Would
# have to define the new skills somehow and tweak their probabilities. I.e., make sure
# the new skill is definitely existent in the card and roll the dice on all the other
# attributes.

import logging
from typing import List, Optional, Tuple
import random
import numpy as np
from cardio import Card
from cardio.skills import get_skilltypes


def pick_from_weights(valsnweights: dict, ignore_levels: int = 0) -> int:
    idx = min(abs(ignore_levels), len(valsnweights) - 1)
    if ignore_levels >= 0:
        values = list(valsnweights.keys())[idx:]
        weights = list(valsnweights.values())[idx:]
    else:
        values = list(valsnweights.keys())[:-idx]
        weights = list(valsnweights.values())[:-idx]
    return random.choices(values, weights, k=1)[0]


def gen_power_health(ignore_levels: int = 0) -> Tuple[int, int]:
    weights = {
        0: 50,
        1: 100,
        2: 90,
        3: 33,
        4: 10,
        5: 5,
        6: 2,
        7: 1,
        8: 0.5,
        9: 0.2,
        10: 0.1,
    }
    power = pick_from_weights(weights, ignore_levels)
    del weights[0]  # No 0 health cards
    health = pick_from_weights(weights, ignore_levels)
    return power, health


def gen_has(ignore_levels: int = 0) -> Tuple[int, int]:
    fire_weights = {
        0: 50,
        1: 100,
        2: 20,
        3: 5,
        4: 2,
        5: 1,
        6: 0.1,
    }
    spritits_weights = {
        0: 50,
        1: 100,
        2: 30,
        3: 10,
        4: 3,
        5: 1,
        6: 0.3,
        7: 0.1,
        8: 0.05,
    }
    has_fire = pick_from_weights(fire_weights, ignore_levels)
    has_spirits = pick_from_weights(spritits_weights, ignore_levels)
    return has_fire, has_spirits


def gen_costs(ignore_levels: int = 0) -> Tuple[int, int]:
    fire_weights = {
        0: 2,
        1: 100,
        2: 50,
        3: 25,
        4: 10,
        5: 3,
        6: 1,
        7: 0.5,
    }
    spirits_weights = {
        0: 2,
        1: 100,
        2: 90,
        3: 80,
        4: 70,
        5: 60,
        6: 50,
        7: 40,
        8: 30,
        9: 20,
        10: 10,
    }
    costs_fire = pick_from_weights(fire_weights, -ignore_levels)
    costs_spirits = pick_from_weights(spirits_weights, -ignore_levels)
    firenotspirits = random.randint(0, 100) < 85
    if firenotspirits:
        costs_spirits = 0
    else:
        costs_fire = 0
    return costs_fire, costs_spirits


def _gen_skills(ignore_levels: int = 0) -> list:
    # How many skills:
    num_skills_weights = {
        0: 100,
        1: 40,
        2: 5,
        3: 1,
        4: 0.1,
        5: 0.01,
        6: 0.001,
    }
    assert max(num_skills_weights.keys()) == Card.MAX_SKILLS
    num_skills = pick_from_weights(num_skills_weights, ignore_levels)

    # Which skills: (Negative potency will be mapped to the same scale.)
    potency_to_weight = {
        0: 100,
        1: 90,
        2: 80,
        3: 70,
        4: 60,
        5: 50,
        6: 40,
        7: 30,
        8: 20,
        9: 10,
        10: 5,
    }
    available_skills = get_skilltypes()
    weights = [potency_to_weight[abs(s.potency)] for s in available_skills]
    sum_weights = sum(weights)
    probabilities = [w / sum_weights for w in weights]

    skills = list(
        np.random.choice(
            a=available_skills, size=num_skills, replace=False, p=probabilities
        )
    )

    return skills


def gen_skills(ignore_levels: int = 0) -> list:
    # Use fix_skill to force a specific skill to be in the card:
    fix_skill = None
    # import cardio
    # E.g.: fix_skill = cardio.skills.Regenerate
    while True:
        skills = _gen_skills(ignore_levels)
        if fix_skill is None or fix_skill in skills:
            return skills


def random_card(ignore_levels: int = 0) -> Card:
    power, health = gen_power_health(ignore_levels)
    has_fire, has_spirits = gen_has(ignore_levels)
    costs_fire, costs_spirits = gen_costs(ignore_levels)
    card = Card(
        name="Randy Rowdy",
        power=power,
        health=health,
        costs_fire=costs_fire,
        costs_spirits=costs_spirits,
        has_fire=has_fire,
        has_spirits=has_spirits,
        skills=gen_skills(ignore_levels),
    )
    return card


def create_noname_card(wanted_potency: Optional[int] = None) -> Card:
    """Create a card with a default name. We add names separately to avoid costly
    operations. `wanted_potency` is the (total) potency we want to card to have.
    """
    i = 0
    while True:
        card = random_card(i // 10000)
        i += 1
        if i % 10000 == 0:
            logging.debug("Tried %s cards to achieve %s", i, wanted_potency)
            logging.debug("Current card:\n%s", card)
        if (wanted_potency is None) or card.potency() == wanted_potency:
            return card


def create_noname_cards(potencies: List[int]) -> List[Card]:
    """Create a list of cards, one for each potency in `potencies`."""
    return [create_noname_card(p) for p in potencies]
