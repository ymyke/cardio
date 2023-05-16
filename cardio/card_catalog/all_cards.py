from cardio import Card, skills

cards = [
    {
        # Spikelet 🦔 1p 2h
        # costs: 🔥🔥 has: 🔥👻👻👻👻 pot: 10
        "desc": "referring to the spines and high cost in fire to play",
        "card": Card(
            name="Spikelet",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Spines],
        ),
    },
    {
        # Badgeress 🧺 4p 5h
        # costs: 🔥🔥 has: 👻 pot: 20
        "desc": 'based on the strength and vitality of the badger, and the unique skill of collecting "treasures" a Packrat',
        "card": Card(
            name="Badgeress",
            power=4,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat],
        ),
    },
    {
        # Bucklerog 🔰 3p 5h
        # costs: 🔥 has: 🔥👻👻👻 pot: 22
        "desc": 'a play on words with "buckler" a type of small shield and "rog" short for rogue, reflecting the skill of shielding and the medium power and health',
        "card": Card(
            name="Bucklerog",
            power=3,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Shield],
        ),
    },
]
