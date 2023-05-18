from cardio import Card, skills
from .blueprint import Blueprint

all_blueprints = [
    Blueprint(
        original=Card("Hamster", 0, 1, 0),
        description="",
    ),
    Blueprint(
        original=Card("Koala", 1, 3, 1),
        description="",
    ),
    Blueprint(
        original=Card("Porcupine", 1, 2, 1, skills=[skills.Airdefense]),
        description="",
    ),
    Blueprint(
        original=Card("Lynx", 3, 2, 2),
        description="",
    ),
    Blueprint(
        original=Card("Weasel", 1, 1, 0, costs_spirits=2),
        description="",
    ),
    Blueprint(
        original=Card("Church Mouse", 1, 1, 1, skills=[skills.Fertility]),
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
