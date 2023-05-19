"""Rough script to generate new cards."""

#%%
import random
import re
from typing import List, Tuple
from cardio.blueprints.card_generator import create_noname_cards
from cardio.blueprints.query_openai import query_openai
from cardio.blueprints.blueprint_catalog import (
    BlueprintEquivalentExistsError,
    BlueprintNameExistsError,
)
from cardio.blueprints import Blueprint, thecatalog
from openai.error import RateLimitError


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
    cards = create_noname_cards(listofwantedpotencies, exactly=False)
    for i, c in enumerate(cards):  # Set an index as the name
        c.name = str(i)

    # Prepare openai query:
    print(TITLE.format("Query"))
    query = "\n".join(repr(c) for c in cards)
    print(query)

    clashes_names = []
    clashes_gameplay = []

    print(TITLE.format("Raw response"))
    res = query_openai(query, existing_names=[b.name for b in thecatalog._blueprints])
    print(res)

    print(TITLE.format("Parsed response"))
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
        except BlueprintNameExistsError as e:
            clashes_names.append(b)
        except BlueprintEquivalentExistsError as e:
            clashes_gameplay.append(b)

    print(TITLE.format(f"{len(clashes_names)} name clashes"))
    for b in clashes_names:
        print(b.name)

    print(TITLE.format(f"{len(clashes_gameplay)} gameplay clashes"))
    for b in clashes_gameplay:
        print(b.name)


# ----- main -----

wanted_potencies = list(range(5, 81)) * 10
random.shuffle(wanted_potencies)
while wanted_potencies:
    potencies = wanted_potencies[:5]
    while True:
        print(f"********** Potencies {potencies} **********")
        try:
            create_blueprints_and_add_to_catalog(potencies)
        except ValueError:
            print("\n😱😱😱😱😱 VALUE ERROR 😱😱😱😱😱\n")
        except RateLimitError:
            print("\n⏱️⏱️⏱️⏱️⏱️ RATE LIMIT ERROR ⏱️⏱️⏱️⏱️⏱️\n")
        else:
            wanted_potencies = wanted_potencies[5:]
            break


# Don't forget to save!!
