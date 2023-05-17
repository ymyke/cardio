# QQ: Let's say we generate a larger list of cards with this generator. Then we add a
# couple of new skills and incorporate new cards with that skill that fit in the
# collection of existing cards in a statistically sound manner. How to do that? Would
# have to define the new skills somehow and tweak their probabilities.

# TODO Need to think about seed?

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


def gen_skills(ignore_levels: int = 0) -> list:
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

    # Which skills:
    min_potency = min(s.potency for s in get_skilltypes(implemented_only=True))
    available_skills = get_skilltypes(implemented_only=True)
    weights = [s.potency + min_potency + 1 for s in available_skills]
    sum_weights = sum(weights)
    probabilities = [w / sum_weights for w in weights]

    skills = list(
        np.random.choice(
            a=available_skills, size=num_skills, replace=False, p=probabilities
        )
    )

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

    # TODO Create name later bc costly op?
    # TODO Have a register and look up card in there and reuse name if already exists?


def add_name(card: Card) -> None:
    card.name = "Randy Rowdy"


def create_noname_card(
    wanted_potency: Optional[int] = None, exactly: bool = False
) -> Card:
    """Create a card with a default name. We add names separately to avoid costly
    operations. `wanted_potency` is the potency we want to card to have. (Normalized
    potency, i.e., [0, 100], not raw potency.)
    """
    assert wanted_potency is None or 0 <= wanted_potency <= 100
    i = 0
    while True:
        card = random_card(i // 1000)
        i += 1
        if i % 1000 == 0:
            logging.debug("Tried %s cards", i)
            logging.debug("Current card:\n%s", card)

        if (wanted_potency is None) or card.has_potency(wanted_potency, exactly):
            return card


def create_noname_cards(potencies: List[int], exactly: bool = False) -> List[Card]:
    return [create_noname_card(p, exactly) for p in potencies]
