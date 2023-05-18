from cardio import Card, skills
from .blueprint import Blueprint

all_blueprints = [
    # Hamster  0p 1h
    # costs: - has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Hamster",
            power=0,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="",
    ),
    # Koala  1p 3h
    # costs: 🔥 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Koala",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="",
    ),
    # Porcupine 🚀 1p 2h
    # costs: 🔥 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Porcupine",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Airdefense],
        ),
        description="",
    ),
    # Lynx  3p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Lynx",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="",
    ),
    # Weasel  1p 1h
    # costs: 👻👻 has: 🔥👻 pot: 3
    Blueprint(
        original=Card(
            name="Weasel",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="",
    ),
    # Church Mouse 🐭 1p 1h
    # costs: 🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Church Mouse",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="",
    ),
    # Spikelet 🦔 1p 2h
    # costs: 🔥🔥 has: 🔥👻👻👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Spikelet",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description="referring to the spines and high cost in fire to play",
    ),
    # Badgeress 🧺 4p 5h
    # costs: 🔥🔥 has: 👻 pot: 20
    Blueprint(
        original=Card(
            name="Badgeress",
            power=4,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description='based on the strength and vitality of the badger, and the unique skill of collecting "treasures" a Packrat',
    ),
    # Bucklerog 🔰 3p 5h
    # costs: 🔥 has: 🔥👻👻👻 pot: 22
    Blueprint(
        original=Card(
            name="Bucklerog",
            power=3,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description='a play on words with "buckler" a type of small shield and "rog" short for rogue, reflecting the skill of shielding and the medium power and health',
    ),
]
