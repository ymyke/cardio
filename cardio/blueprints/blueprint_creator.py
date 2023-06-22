"""Rough script to generate new cards."""

#%%
import logging
from collections import defaultdict
import random
import re
from typing import List, Tuple
from cardio.blueprints.card_creator import create_noname_cards
from cardio.blueprints.query_openai import query_openai
from cardio.blueprints import Blueprint, thecatalog
from openai.error import RateLimitError

logging.basicConfig(level=logging.DEBUG)


TITLE = "\n---------- {} ----------\n"


def parse_line(line: str) -> Tuple[int, str, str]:
    i, rest = line.split(":")
    i = int(re.sub(r"[^\d]", "", i))
    if "[" in rest:
        name, rest = rest.split("[")
        name = name.strip()
        name = re.sub(r"[^A-Za-z ]", "", name)
        desc = rest.split("]")[0]
        desc = re.sub(r'[^A-Za-z ,"\']', "", desc)
    elif "-" in rest:
        name, desc = rest.split("-", 1)
        name = name.strip()
        name = re.sub(r"[^A-Za-z ]", "", name)
        desc = desc.strip()
        desc = re.sub(r'[^A-Za-z ,"\']', "", desc)
    else:
        raise ValueError(f"Could not parse line.")
    return i, name, desc


def create_blueprints_and_add_to_catalog(listofwantedpotencies: List[int]):
    # Create a couple of random cards:
    cards = create_noname_cards(listofwantedpotencies)
    for i, c in enumerate(cards):  # Set an index as the name
        c.name = str(i)

    # Prepare openai query:
    print(TITLE.format("Query"))
    query = "\n".join(repr(c) for c in cards)
    print(query)

    print(TITLE.format("Raw response"))
    res = query_openai(query, existing_names=[b.name for b in thecatalog._blueprints])
    print(res)

    print(TITLE.format("Parsed response"))
    not_added = defaultdict(list)
    lines = res.split("\n")
    for line in lines:
        if not line.strip():
            continue
        i, name, desc = parse_line(line)
        print(i, name, desc)
        cards[i].name = name
        b = Blueprint(cards[i], desc)

        try:
            thecatalog.add_blueprint(b)
        except Exception as e:
            not_added[e.__class__.__name__].append(b)

    print(TITLE.format("Not added"))
    for reason, blueprints in not_added.items():
        print(f"{len(blueprints)} blueprints not added because {reason}: ")
        print(", ".join(b.name for b in blueprints))
        print()


# ----- main -----

wanted_potencies = (
    list(range(1, 31)) * 5 + list(range(31, 46)) * 2 + list(range(46, 81))
)
random.shuffle(wanted_potencies)
while wanted_potencies:
    potencies = wanted_potencies[:5]
    while True:
        print()
        print(
            f"********** Potencies {potencies} ({len(wanted_potencies)} left) **********"
        )
        try:
            create_blueprints_and_add_to_catalog(potencies)
        except Exception as e:
            print(f"\n😱😱😱 {type(e).__name__} ERROR: {e} 😱😱😱\n")
        else:
            wanted_potencies = wanted_potencies[5:]
            break

thecatalog.save()
