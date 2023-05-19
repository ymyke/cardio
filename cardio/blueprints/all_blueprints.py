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
    # Falcon  3p 2h
    # costs: 🔥 has: 🔥 pot: 8
    Blueprint(
        original=Card(
            name="Falcon",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="fast and powerful, low health, fire is the only attribute, has no spirits",
    ),
    # Elephant  1p 6h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Elephant",
            power=1,
            health=6,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="strong and has high health, expensive, fire and spirits attributes",
    ),
    # Firefly 🐭 0p 2h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Firefly",
            power=0,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="weak, low fire attribute cost, high spirit attributes, has the Fertility skill",
    ),
    # Wolf  4p 2h
    # costs: 🔥 has: 👻 pot: 10
    Blueprint(
        original=Card(
            name="Wolf",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="strong and fast, but only fire attribute, low health",
    ),
    # Scorpion 💀 1p 2h
    # costs: 🔥 has: 👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Scorpion",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.InstantDeath],
        ),
        description="poisonous, low power and health, low fire attribute cost, high spirit attribute, has the InstantDeath skill",
    ),
    # Mole 🐩 1p 2h
    # costs: 🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Mole",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog],
        ),
        description="weak, but has potential with the Underdog skill, balanced fire and spirits attributes",
    ),
    # Kangaroo  2p 2h
    # costs: 🔥 has: 🔥🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Kangaroo",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="moderate power and health, high fire attribute, balanced overall",
    ),
    # Phoenix 🪁 2p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Phoenix",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="moderate power and health, medium fire attribute cost, has the Soaring skill",
    ),
    # Chameleon 🐩 2p 2h
    # costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Chameleon",
            power=2,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog],
        ),
        description="moderate power and health, high fire attribute cost, has the Underdog skill, can adapt to different scenarios",
    ),
    # Turtle 🔰 2p 1h
    # costs: 🔥🔥🔥 has: 👻 pot: 9
    Blueprint(
        original=Card(
            name="Turtle",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield],
        ),
        description="has a shield skill, low power and health, high fire attribute cost",
    ),
    # Jaguar  3p 4h
    # costs: 🔥🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Jaguar",
            power=3,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="a powerful and expensive animal, fits with high power and moderate health attributes",
    ),
    # Caterpillar  3p 8h
    # costs: - has: 🔥 pot: 28
    Blueprint(
        original=Card(
            name="Caterpillar",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="low in firepower, but high in health and regeneration, fits with the idea of a slow growing, sturdy creature",
    ),
    # Foxbat 🔰🧺🐭 2p 3h
    # costs: - has: 🔥🔥👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Foxbat",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.Packrat, skills.Fertility],
        ),
        description="a creature with both fiery and spiritual characteristics, with skills that include theft Packrat, deception and defense Shield",
    ),
    # Hydra 🐭🐩💀🔰🧺 2p 8h
    # costs: 👻👻👻👻 has: 🔥🔥👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Hydra",
            power=2,
            health=8,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=4,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="a creature with high spiritual power that can resurrect even after instant death InstantDeath, and has fertility and defense skills Fertility, Shield",
    ),
    # Drakelet  1p 1h
    # costs: 🔥 has: 🔥👻👻👻 pot: 6
    Blueprint(
        original=Card(
            name="Drakelet",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[],
        ),
        description='low powerhealth, low fire cost, but has a decent amount of spirits and no skills "Drakelet" is a small, baby dragon, which fits with the small size of the card',
    ),
    # Glimmer  1p 2h
    # costs: 👻👻👻 has: 🔥 pot: 3
    Blueprint(
        original=Card(
            name="Glimmer",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description='low power, decent health, no fire cost, but high spirit cost "Glimmer" suggests something ethereal or magical which fits with the high spirits cost',
    ),
    # Ant  2p 1h
    # costs: 🔥🔥 has: 👻 pot: 4
    Blueprint(
        original=Card(
            name="Ant",
            power=2,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="decent power, low health, low fire cost, low spirit cost, no skills, but the low health and the small size could be compared to an ant",
    ),
    # Ferret  1p 2h
    # costs: 🔥 has: 🔥👻 pot: 6
    Blueprint(
        original=Card(
            name="Ferret",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="low power, decent health, low fire cost, low spirit cost, no skills, but the name suggests agility and speed which fits with the card's attributes",
    ),
    # Raccoon  2p 1h
    # costs: 🔥🔥 has: 🔥👻 pot: 5
    Blueprint(
        original=Card(
            name="Raccoon",
            power=2,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="decent power, low health, average fire cost, low spirit cost, no skills, The Raccoon is known for its mischievousness and resourcefulness, which could be applied to a card with decent power and average fire cost",
    ),
    # Gecko  0p 2h
    # costs: 🔥 has: 🔥👻 pot: 4
    Blueprint(
        original=Card(
            name="Gecko",
            power=0,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="low power, decent health, low fire cost, low spirit cost, no skills, but the ability to climb walls is associated with geckos, which fits with a card that has decent health",
    ),
    # Froglet  1p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 5
    Blueprint(
        original=Card(
            name="Froglet",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="low powerhealth, low fire cost, low spirits, no skills, but has  spirits A froglet is a young frog and the name relates to the low powerhealth of the card",
    ),
    # Phoenixborn 🐩 0p 2h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Phoenixborn",
            power=0,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Underdog],
        ),
        description="high fire costs, high fire value, and an Underdog skill This name suggests a powerful being that arises from fire and represents rebirth or transformation, fitting with the card's attributes and skill",
    ),
    # Nightwinged  2p 1h
    # costs: 🔥 has: 🔥👻 pot: 6
    Blueprint(
        original=Card(
            name="Nightwinged",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="low health, low fire costs, but quick and agile with high power A name that suggests a fast, stealthy, and fearsome creature of the night",
    ),
    # Lavalope  1p 2h
    # costs: 🔥🔥 has: 🔥 pot: 4
    Blueprint(
        original=Card(
            name="Lavalope",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="low spirits, high fire costs, but with both fire and mobility This name combines the elements of fire and the agility of a jackrabbit, fitting with the card's attributes",
    ),
    # Seraphwing  2p 1h
    # costs: 🔥 has: 👻👻👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Seraphwing",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=0,
            skills=[],
        ),
        description="low fire costs, high spirit, and the Healer skill This name suggests an angelic being capable of healing, fitting with the card's attributes and skill",
    ),
    # Infernorb  1p 2h
    # costs: 🔥🔥🔥 has: 🔥👻👻 pot: 5
    Blueprint(
        original=Card(
            name="Infernorb",
            power=1,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="high fire costs, average attributes, and no skills This name suggests a fiery creature that lacks any special abilities, fitting with the card's attributes ",
    ),
    # Faeox Fairy Fox 🐩 1p 2h
    # costs: 🔥 has: - pot: 7
    Blueprint(
        original=Card(
            name="Faeox Fairy Fox",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Underdog],
        ),
        description="Underdog, weak but with potential",
    ),
    # Spriggle Sprite Squirrel  1p 1h
    # costs: 🔥 has: 👻👻👻👻 pot: 6
    Blueprint(
        original=Card(
            name="Spriggle Sprite Squirrel",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=0,
            skills=[],
        ),
        description="Small, but with high spirit power",
    ),
    # Shadowolf Shadow Wolf  2p 2h
    # costs: 🔥🔥🔥 has: - pot: 4
    Blueprint(
        original=Card(
            name="Shadowolf Shadow Wolf",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[],
        ),
        description="Expensive, but very strong and powerful, with no magic abilities",
    ),
    # Griffox  3p 2h
    # costs: 👻👻👻👻 has: 👻👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Griffox",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=3,
            has_fire=0,
            skills=[],
        ),
        description="powerful, spirited, moderately healthy, and requires some spirits to use",
    ),
    # Pythroar  1p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Pythroar",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[],
        ),
        description="firebased, fragile, fierce name for a creature with low health",
    ),
    # Underrawr 🐩 1p 1h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Underrawr",
            power=1,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Underdog],
        ),
        description="a creature that can thrive with little, but its skills boost its performance",
    ),
    # Chimerex  4p 1h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Chimerex",
            power=4,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="powerful, practically invulnerable, but needs some spirits to use",
    ),
    # Skythorn  3p 2h
    # costs: 🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Skythorn",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="a fantasy creature with thorns on its wings and body The name relates to the power, cost, and fire element of the card",
    ),
    # Shieldcat 🔰 2p 1h
    # costs: 👻👻👻👻👻👻 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Shieldcat",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=6,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="a catlike creature with a shield The name relates to the skills and high spirit cost of the card",
    ),
    # Treewhisper  1p 6h
    # costs: 👻👻👻👻 has: 👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Treewhisper",
            power=1,
            health=6,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description="a creature that speaks to trees and is tied to nature The name relates to the high health and spirit cost, as well as the absence of fire",
    ),
    # Glimmertail  2p 2h
    # costs: 🔥 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Glimmertail",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="a creature with a shiny tail that distracts its opponents The name relates to the low power but presence of fire element",
    ),
    # Hellhound  2p 1h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Hellhound",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=6,
            skills=[],
        ),
        description="This card has high fire costs and low spirits, indicating a creature of the underworld With high power and low health, it's a fierce and dangerous creature that requires sacrifice to summon",
    ),
    # Pixiefox  2p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 8
    Blueprint(
        original=Card(
            name="Pixiefox",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="With balanced stats and average costs, this creature is quick and nimble, able to easily dodge attacks It's a fantastical creature with foxlike features, but with mystical powers like a pixie",
    ),
    # Thunderbird  2p 2h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Thunderbird",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="This card has high fire costs and high fire attribute, which suggest a creature born of fire With balanced stats, this birdlike creature is able to swiftly attack and evade",
    ),
    # Hedgebeast 🦔 2p 1h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Hedgebeast",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Spines],
        ),
        description="This card has low health and high power, suggesting a creature that is a glass cannon With a spines skill, it can repel attacks, but it's not able to withstand many attacks It's a fantastical beast that's part hedgehog and part something else",
    ),
    # Furies  5p 1h
    # costs: 🔥🔥 has: 👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Furies",
            power=5,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description="This card has no fire attribute and high spirits, indicating a creature of the underworld With high power and low health, it's a dangerous creature that requires sacrifice to summon It has no skills, instead relying on its raw strength to take down its enemies The name Furies fits with the theme of creatures from the underworld and their vengeful nature",
    ),
    # Banshee 💀 1p 1h
    # costs: 👻👻👻 has: 🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Banshee",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="instantly deadly, highly spiritual",
    ),
    # Basilisk  5p 1h
    # costs: 🔥 has: - pot: 9
    Blueprint(
        original=Card(
            name="Basilisk",
            power=5,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[],
        ),
        description="strong and powerful, not reliant on elements, no skills",
    ),
    # Siren 🐭 0p 1h
    # costs: 🔥 has: - pot: 8
    Blueprint(
        original=Card(
            name="Siren",
            power=0,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="alluring, has female connotations, fertility ability, fire costs",
    ),
    # Centaur 🐭 1p 2h
    # costs: 🔥 has: - pot: 12
    Blueprint(
        original=Card(
            name="Centaur",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="balanced power and health, fertility ability, fire costs",
    ),
    # Pangolin 🔰 1p 2h
    # costs: 🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Pangolin",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="shield ability, some spiritual elements, low power and health",
    ),
    # Chimera  3p 3h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Chimera",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description=" fire symbols, balanced power and health",
    ),
    # Seraphim 🔰 1p 1h
    # costs: 🔥 has: 🔥🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Seraphim",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Shield],
        ),
        description="Fire element, Shield skill, low power and health",
    ),
    # Medusa 💀 1p 1h
    # costs: 🔥 has: 🔥🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Medusa",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath],
        ),
        description="Instant Death skill, low fire cost, very low power and health",
    ),
    # Gorgon 🔰 3p 1h
    # costs: 🔥🔥 has: 🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Gorgon",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="Shield skill, high fire cost, low health and power",
    ),
    # Nightwing 🦔🪁🐭 1p 1h
    # costs: 🔥🔥🔥 has: - pot: 13
    Blueprint(
        original=Card(
            name="Nightwing",
            power=1,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Spines, skills.Soaring, skills.Fertility],
        ),
        description="fits with soaring skill, has spines for defense, high fertility potential for breeding",
    ),
    # Thunderhoof  3p 2h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Thunderhoof",
            power=3,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[],
        ),
        description="strong and fiery, balanced in spirits and fire, no standout skills",
    ),
    # Stormhare  4p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Stormhare",
            power=4,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="quick and nimble, can handle fire, no skills",
    ),
    # Bansheebee 💀 0p 3h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Bansheebee",
            power=0,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="low power and fire, high spirits for a haunting wail of instant death",
    ),
    # Seedancer 🐭 0p 2h
    # costs: 🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Seedancer",
            power=0,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="low fire, low spirits, high fertility potential for breeding",
    ),
    # Salamander 🔰🐩 1p 2h
    # costs: 👻👻 has: 👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Salamander",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Shield, skills.Underdog],
        ),
        description="a fireloving creature that fits with the card's firerelated costs and underdog skill, which relates to the card's low power and fire attribute values The shield skill also reinforces the card's inherent skill itself",
    ),
    # Firebird 🐭 2p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Firebird",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="costs  fire, has fire, has no spirits, and has a skill related to fertility",
    ),
    # Goblinbat 🐭 3p 1h
    # costs: 🔥 has: - pot: 14
    Blueprint(
        original=Card(
            name="Goblinbat",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="low health, no spirits or fire, but high power and a skill related to fertility",
    ),
    # Minotaur 🔰 4p 1h
    # costs: 🔥 has: 🔥 pot: 14
    Blueprint(
        original=Card(
            name="Minotaur",
            power=4,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="high power, low health, has fire and a defensive skill, like a shield",
    ),
    # Kelpie 🐭 0p 5h
    # costs: 👻👻👻👻👻👻 has: 🔥👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Kelpie",
            power=0,
            health=5,
            costs_fire=0,
            costs_spirits=6,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="high health, high spirits, fertility skill suggests a creature associated with growth and fertility, while the high spirit and low fire attributes reinforce a sense of otherworldliness and etherealness Kelpies are also water spirits with equine or humananimal hybrid features, which fits well with the Fertility skill implying a creature that somehow generates or enhances growth",
    ),
    # Dragonfly  3p 4h
    # costs: 👻 has: 🔥🔥 pot: 13
    Blueprint(
        original=Card(
            name="Dragonfly",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=0,
            has_fire=2,
            skills=[],
        ),
        description="moderate powerhealth, but with high fire attributes and low spirit attributes suggest a creature that is fast, nimble and fierce, with a fiery temper Dragonflies are brightly colored insects with iridescent wings, which give them a sense of speed and agility, and also suggest a fiery personality The high fire attributes reinforce this notion of a creature that is hotheaded and quick to act, while the low spirit attributes might suggest a lack of patience or foresight",
    ),
    # Rat king 🧺 2p 4h
    # costs: 👻👻 has: 🔥🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Rat king",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Packrat],
        ),
        description="moderate powerhealth, with a skill that allows to hoard multiple items, paired with moderate spirit and fire attributes This card suggests a creature that is quick and dexterous, with an eye for useful items Rat kings are a real phenomenon in which several rats become entangled and live together This reinforces the idea of the Packrat skill that involves hoarding objects, however in this case, the Rat king combines the ability to collect with their fighting capabilities The moderate attributes in both spirit and fire suggest that the card is well balanced and capable in all aspects of the game",
    ),
    # Bloodhound  1p 7h
    # costs: 🔥🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Bloodhound",
            power=1,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="high health, medium power, costs fire, good for defense",
    ),
    # Gryphon 🔰 4p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Gryphon",
            power=4,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="medium powerhealth, costs fire, has shield, mythical creature",
    ),
    # Dryad 🐭 1p 3h
    # costs: 🔥 has: 🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Dryad",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="low powerhealth, costs fire, has fertility skill, naturebased",
    ),
    # Fae Bunny 🐭 2p 2h
    # costs: 👻👻 has: 🔥👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Fae Bunny",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description='This card has a high spirit value and the ability Fertility which relates to bunnies being known for their reproductive abilities The name "Fae" gives it a fantastical twist',
    ),
    # Demon Crow 💀 4p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Demon Crow",
            power=4,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='The ability "InstantDeath" is associated with malevolent power, this card has high power and low health, the bird is a crow which is associated with the occult',
    ),
    # Pygmy Rhino 🔰🐩 2p 1h
    # costs: 🔥 has: 🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Pygmy Rhino",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Underdog],
        ),
        description='This card has a shield ability and is an underdog card low power and health, the rhino has a shieldlike form and adding "Pygmy" gives it a fantastical twist fitting for the game',
    ),
    # Arctic Fox 🔰 3p 2h
    # costs: 🔥 has: 🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Arctic Fox",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="This card has a shield ability and is quite balanced with  power and  health The fox is known for its ability to adapt and survive harsh winter conditions, which fits well with the shield ability",
    ),
    # Goblin Rat 💀🧺 1p 3h
    # costs: 🔥🔥🔥 has: 👻 pot: 16
    Blueprint(
        original=Card(
            name="Goblin Rat",
            power=1,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description='This card has the abilities "InstantDeath" and "PackRat" which align with goblins being known for their trickery and association with thievery The rat is an animal associated with scavenging and hoarding, fitting with the PackRat ability',
    ),
    # Dracoon 🔰 5p 2h
    # costs: 🔥 has: 👻 pot: 18
    Blueprint(
        original=Card(
            name="Dracoon",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield],
        ),
        description="Combining a dragon and a raccoon, this card offers a good power value of , but relatively low health of  It has a fire cost of  and has only  spirit, meaning it can only use its shield skill once The name comes from the appearance of a raccoon mixed with a dragon, a creature with firebreathing abilities as well as being protective of its hoard",
    ),
    # Drachling 🔰🐩 4p 2h
    # costs: 👻👻👻👻👻 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Drachling",
            power=4,
            health=2,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Underdog],
        ),
        description="With a high power, and shield and underdog skills, this dragonlike creature is small in health, but not easily defeated The high spirit cost suggests a magical creature",
    ),
    # Manticore 🚀🐭 1p 4h
    # costs: 🔥🔥 has: 🔥 pot: 16
    Blueprint(
        original=Card(
            name="Manticore",
            power=1,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Airdefense, skills.Fertility],
        ),
        description="This mythical creature is known for its fierce and powerful defense mechanisms and air defense skill The fertility skill is also related to myths and legends The low spirit cost suggests it is a common creature in the game",
    ),
    # Flamehound  7p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Flamehound",
            power=7,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[],
        ),
        description="very strong, but expensive, costsfire, three hasfire, no skills",
    ),
    # Armordillo 🔰🧺 2p 1h
    # costs: 🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Armordillo",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat],
        ),
        description="moderate power, low health, Shield ability capable of minimizing damage taken, moderate costsfirecostsspirits",
    ),
    # Flameetle 🐭 4p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Flameetle",
            power=4,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="combines the words 'flame' and 'beetle', implying its fire attribute and insectlike appearance Its low health represents its fragility, while its power and Fertility skill suggest its ability to reproduce and quickly build up a swarm",
    ),
    # Shadowcat 🧺💀 3p 2h
    # costs: 🔥 has: 🔥 pot: 20
    Blueprint(
        original=Card(
            name="Shadowcat",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath],
        ),
        description="low health but high power combined with the Packrat skill suggest a sneaky, quick and efficient hunting animal, while the InstantDeath skill is the animal's deadly appearance, able to instantly neutralize any prey",
    ),
    # Trollsnake 🐩🐭 0p 4h
    # costs: 🔥🔥🔥 has: 🔥👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Trollsnake",
            power=0,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog, skills.Fertility],
        ),
        description="high health with low power, this animal relies on its Underdog skill to defend itself as it grows Its Fertility skill represents its ability to quickly regrow any lost limbs or appendages",
    ),
    # Dragonet 🐭🔰 1p 2h
    # costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Dragonet",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=4,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="This name is a nod to the dragon's firebreathing abilities, as well as its fertility skill The card's name also reflects its lower power and health values",
    ),
    # Shield Beetle 🔰 4p 4h
    # costs: 👻 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Shield Beetle",
            power=4,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="The name Shield Beetle is perfect for a creature with high health and a shield skill, fitting with its armorlike defenses",
    ),
    # Phoenix Cub 🐭 2p 3h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Phoenix Cub",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Fertility],
        ),
        description="The name fits the card's skills and attributes, being similar to Card  However, the cub has less fire power as it is still young and learning to control its abilities",
    ),
    # Sparkcat  5p 2h
    # costs: - has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Sparkcat",
            power=5,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="relates to the card's high power and fire attribute, and the catlike qualities of agility and speed",
    ),
    # Tricksterat 🐭🧺💀 1p 1h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 24
    Blueprint(
        original=Card(
            name="Tricksterat",
            power=1,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description='a play on words for "trickster rat", relates to the card\'s packrat skill and the sly nature of rats',
    ),
    # Ironclaw 🔰💀 3p 2h
    # costs: 🔥🔥 has: 👻 pot: 20
    Blueprint(
        original=Card(
            name="Ironclaw",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield, skills.InstantDeath],
        ),
        description="relates to the card's high defense skill and the clawlike qualities of shields",
    ),
    # Skywhip 🚀💀🐭 0p 5h
    # costs: 🔥 has: 👻👻 pot: 24
    Blueprint(
        original=Card(
            name="Skywhip",
            power=0,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Airdefense, skills.InstantDeath, skills.Fertility],
        ),
        description="relates to the card's air defense skill and high spirits attribute, and the whiplike qualities of fertility",
    ),
    # Blazehorn 🔰 2p 5h
    # costs: 🔥 has: 🔥🔥👻 pot: 20
    Blueprint(
        original=Card(
            name="Blazehorn",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Shield],
        ),
        description="relates to the card's high fire attribute and the hornlike qualities of shields",
    ),
    # Peryton 🐭 6p 1h
    # costs: 🔥 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Peryton",
            power=6,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="The Peryton represents a creature of eternal youth, fertility and divine grace The fertility skill suggests this name while the high power level represents the divine strength",
    ),
    # Wispwarden 🔰🧺💀 1p 3h
    # costs: 🔥🔥 has: - pot: 22
    Blueprint(
        original=Card(
            name="Wispwarden",
            power=1,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Shield, skills.Packrat, skills.InstantDeath],
        ),
        description='name is a combination of "wisp," which is a creature often associated with magic and ethereality, and "warden," which implies protection The high health and shield skill make it seem like a protective creature that can take a lot of hits The instant death also adds to the idea of a powerful guardian',
    ),
    # Flamfuryx 🐭💀 3p 1h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 23
    Blueprint(
        original=Card(
            name="Flamfuryx",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description='name is a combination of "flame," referring to its high fire attribute, and "fury," implying a powerful, aggressive creature The fertility skill adds a sense of reproduction and proliferation, making it a fiery and formidable creature that can easily overpower opponents',
    ),
    # Hydradon 🐭 3p 6h
    # costs: 🔥 has: - pot: 22
    Blueprint(
        original=Card(
            name="Hydradon",
            power=3,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description='name is a combination of "hydra," a mythical creature with multiple heads, and "don," meaning "lord" or "master" The high health and fertility skill make it seem like a dominating and resilient creature that can easily spawn other creatures The low fire attribute suggests that it may have a waterbased aspect, in line with the name',
    ),
    # Corruptorix 💀🐭 2p 3h
    # costs: 🔥 has: 🔥👻 pot: 23
    Blueprint(
        original=Card(
            name="Corruptorix",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description='name is a combination of "corruption," which is in line with the instant death skill, and "rix," which is a suffix denoting royalty or a highranking individual The high power and instant death skills suggest a powerful and malevolent creature that can easily take down opponents, with the fertility skill implying the ability to corrupt others and reproduce',
    ),
    # Ironhideon 🔰 2p 8h
    # costs: 🔥 has: 🔥 pot: 23
    Blueprint(
        original=Card(
            name="Ironhideon",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description='name is a combination of "ironhide," which implies incredible durability, and "don," meaning "lord" or "master" The high health and shield skill make it seem like an imposing and nearly indestructible creature that can easily defend itself and others The low fire attribute adds to the idea of being tough and resilient ',
    ),
    # Gremlin 💀🐩🧺🐭 2p 1h
    # costs: 🔥🔥🔥 has: 🔥 pot: 26
    Blueprint(
        original=Card(
            name="Gremlin",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="packrat skill, higher fire cost, low stats  mischievous creature that causes trouble",
    ),
    # Incubus 🐭🔰💀 2p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 27
    Blueprint(
        original=Card(
            name="Incubus",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="spirit element, fertility skill, shield skill  seductive creature with supernatural abilities",
    ),
    # Gnome 🐩🔰🐭 1p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 24
    Blueprint(
        original=Card(
            name="Gnome",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog, skills.Shield, skills.Fertility],
        ),
        description="small and weak with Underdog and Shield, but the Fertility skill hints at a magical or alchemical affinity, fitting for a gnome",
    ),
    # ReaperWolf 💀🐩 2p 8h
    # costs: 🔥 has: 👻 pot: 27
    Blueprint(
        original=Card(
            name="ReaperWolf",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Underdog],
        ),
        description="Instant Death, Underdog High health, low power, and no fire",
    ),
    # Thundercat 🐭 8p 2h
    # costs: 🔥 has: 🔥 pot: 25
    Blueprint(
        original=Card(
            name="Thundercat",
            power=8,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="High power, low health, strong fire, and Fertility skill",
    ),
    # PhoenixPup 🔰🐭 4p 2h
    # costs: 🔥 has: 🔥👻 pot: 25
    Blueprint(
        original=Card(
            name="PhoenixPup",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="Shield, Fertility, and a good balance between power, health, and fire",
    ),
    # InfernoRat 🐩🔰💀🐭 2p 1h
    # costs: 🔥🔥🔥 has: 🔥🔥 pot: 28
    Blueprint(
        original=Card(
            name="InfernoRat",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="Instant Death, Shield, Underdog, and high fire cost for a relatively low power and health",
    ),
    # ThornyFox 🔰💀🦔🐩 2p 2h
    # costs: 🔥 has: 🔥👻 pot: 26
    Blueprint(
        original=Card(
            name="ThornyFox",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.InstantDeath, skills.Spines, skills.Underdog],
        ),
        description="Shield, Instant Death, Spines, and a good balance between power, health, and spirits",
    ),
    # Drakeling 🔰🧺🦔🐭 0p 2h
    # costs: 🔥 has: 🔥🔥 pot: 26
    Blueprint(
        original=Card(
            name="Drakeling",
            power=0,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Shield, skills.Packrat, skills.Spines, skills.Fertility],
        ),
        description="very fireoriented, strong shield, moderate powerhealth, spines, and packratting tendencies",
    ),
    # Titan 🐭 2p 8h
    # costs: 🔥 has: 🔥👻 pot: 26
    Blueprint(
        original=Card(
            name="Titan",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="very high health, no skills, but very low cost",
    ),
    # Griffin 🐩🧺🔰 3p 3h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 26
    Blueprint(
        original=Card(
            name="Griffin",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Underdog, skills.Packrat, skills.Shield],
        ),
        description="underdog, good powerhealth, strong shield, and packratting tendencies",
    ),
    # BlazeHare  9p 1h
    # costs: - has: 🔥 pot: 27
    Blueprint(
        original=Card(
            name="BlazeHare",
            power=9,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description='relates to the high power and fire attribute and the low health attribute, while the "Hare" part suggests a fast but weak creature, befitting the card\'s high power and low health',
    ),
    # PackFalcon 🐭🔰🧺 3p 1h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="PackFalcon",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Fertility, skills.Shield, skills.Packrat],
        ),
        description='relates to the packrat and shield skills, while "Falcon" sounds noble The high fire attribute and low spirits make this creature look less supernatural',
    ),
    # DeathDrake 🧺💀🐭🔰 2p 1h
    # costs: 🔥🔥🔥🔥🔥🔥🔥 has: 🔥👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="DeathDrake",
            power=2,
            health=1,
            costs_fire=7,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description='relates to the instant death skill, while "Drake" sounds powerful and mythical The high fire cost suggests a creature that is difficult to summon, while the high spirit attribute supports its omenlike nature',
    ),
    # FertileAves 🪁🧺🔰🐭 2p 1h
    # costs: 🔥 has: 🔥👻 pot: 27
    Blueprint(
        original=Card(
            name="FertileAves",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Soaring, skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description='relates to the fertility skill, while "Aves" sounds dignified The card\'s low power and health and high spirits attribute suggest a spirit animal instead of a real one The low fire cost might reflect a creature that is easy to summon',
    ),
    # ShieldBug 🐩🔰 1p 3h
    # costs: - has: 🔥👻👻👻👻 pot: 29
    Blueprint(
        original=Card(
            name="ShieldBug",
            power=1,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Underdog, skills.Shield],
        ),
        description='relates to the shield skill, while "Bug" sounds humble The high spirit attribute reflects the card\'s ability to function as an underdog The high health and low power suggest a creature that can absorb a lot of damage while dealing only little The absence of fire attribute suggests a creature that does not possess any innate magic power',
    ),
    # Kraken 🔰🐩💀 7p 1h
    # costs: 👻👻👻👻 has: 🔥🔥 pot: 28
    Blueprint(
        original=Card(
            name="Kraken",
            power=7,
            health=1,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Shield, skills.Underdog, skills.InstantDeath],
        ),
        description="deadly, expensive, lacks spirits but has strong fire, can potentially kill instantly, underdog",
    ),
    # Sprite 🧺💀🐩 1p 1h
    # costs: - has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Sprite",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath, skills.Underdog],
        ),
        description="small, low powerhealth, cheap, has packrat tendencies and surprising skills up her sleeve",
    ),
    # Blaze Drake 🐭🔰💀 3p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥👻 pot: 30
    Blueprint(
        original=Card(
            name="Blaze Drake",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="a dragonlike creature with firerelated abilities and instant death skill",
    ),
    # Moon Cat 🐭🧺 5p 4h
    # costs: 🔥 has: 🔥👻👻 pot: 30
    Blueprint(
        original=Card(
            name="Moon Cat",
            power=5,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="a magical cat with packrat skill and a high spirit count",
    ),
    # Mist Basilisk 💀 2p 6h
    # costs: - has: 🔥👻 pot: 30
    Blueprint(
        original=Card(
            name="Mist Basilisk",
            power=2,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="a snakelike creature that represents death and has no fire cost",
    ),
    # Thorned Puma 🧺💀🔰🦔 5p 1h
    # costs: 🔥🔥 has: 🔥👻👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Thorned Puma",
            power=5,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath, skills.Shield, skills.Spines],
        ),
        description="a dangerous catlike creature with spines and instant death skills",
    ),
    # Flame Mongoose 🐭🧺 6p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 32
    Blueprint(
        original=Card(
            name="Flame Mongoose",
            power=6,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=4,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="a quick and cunning creature with packrat skill and high fire count",
    ),
    # Serpentine 🔰🧺🐭💀 7p 3h
    # costs: 👻👻👻👻👻👻👻👻👻👻 has: - pot: 34
    Blueprint(
        original=Card(
            name="Serpentine",
            power=7,
            health=3,
            costs_fire=0,
            costs_spirits=10,
            has_spirits=0,
            has_fire=0,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="referring to the high power and low health, as well as the shield skill which can protect the card like a snake's scales The packrat skill could reference their tendency to hoard treasure, and the fertility and instant death skills could allude to the card's ability to both generate and destroy life quickly",
    ),
    # Skylarkspur 🐭🪁🐩🔰 3p 2h
    # costs: 👻 has: 🔥👻👻👻 pot: 30
    Blueprint(
        original=Card(
            name="Skylarkspur",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.Soaring, skills.Underdog, skills.Shield],
        ),
        description='a combination of "skylark", which can symbolize freedom and soaring through the air fitting for the "soaring" skill, and "spur", which can symbolize an underdog rising to the challenge fitting for the "underdog" skill The fertility and shield skills could reference this creature\'s ability to protect and heal others',
    ),
    # Cephalipod 🧺🔰🐭 3p 4h
    # costs: 🔥🔥 has: 👻 pot: 30
    Blueprint(
        original=Card(
            name="Cephalipod",
            power=3,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="a reference to the card's tentacles similar in shape to the packrat skill icon, which are used for both defense and offense, and the high health as many cephalopods are renowned for their regenerative abilities The shield and fertility skills could also reference their nurturing and protective instincts",
    ),
    # Chrysophant 🧺🚀🐭 1p 9h
    # costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Chrysophant",
            power=1,
            health=9,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Packrat, skills.Airdefense, skills.Fertility],
        ),
        description='a reference to the card\'s high spirituality as "chryso" means "gold" and could represent spiritual purity, and its packrat and air defense skills with "phant" referencing the creature\'s defensive and strategic capabilities The fertility skill could also represent the creature\'s ability to create abundance and prosperity',
    ),
    # Pyropard 🧺💀🐭 2p 4h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Pyropard",
            power=2,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.InstantDeath, skills.Fertility],
        ),
        description='a combination of "pyro" referring to fire, fitting for the card\'s high fire attribute and "leopard" fitting for the card\'s agility and skill with the instant death ability The packrat and fertility skills might also reference this creature\'s cunning and resourcefulness in survival',
    ),
    # Wyvern 🐭💀🔰 3p 2h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 31
    Blueprint(
        original=Card(
            name="Wyvern",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="powerful, firebased, some spirits, high health with a touch of fertility, and the defenses of shield and instant death",
    ),
    # Yeti 🐭🔰 9p 2h
    # costs: 🔥🔥🔥🔥 has: 👻👻 pot: 31
    Blueprint(
        original=Card(
            name="Yeti",
            power=9,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="the powerful aura aligns with its high power rating, hardly showing any fire as an element, but certainly a hard hitter",
    ),
    # Fyrewolf 🐭🧺🔰 2p 6h
    # costs: 🔥 has: 🔥🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Fyrewolf",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description='combines "fire" and "wolf" to match the card\'s high fire attribute and attacking skills',
    ),
    # Dreamcat 🔰 1p 9h
    # costs: - has: 🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Dreamcat",
            power=1,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description='combines "dream" and "cat" to match the card\'s high health and protective skills',
    ),
    # Pixiebat 🐭 1p 9h
    # costs: - has: 🔥👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Pixiebat",
            power=1,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description='combines "pixie" and "bat" to match the card\'s high spirits and fertility skills, as well as its low power',
    ),
    # Titanape 🐭🐩🔰 7p 2h
    # costs: 🔥 has: 🔥👻 pot: 34
    Blueprint(
        original=Card(
            name="Titanape",
            power=7,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Underdog, skills.Shield],
        ),
        description='combines "titan" and "ape" to match the card\'s high power and underdog skills, as well as its low health',
    ),
    # Infernowolf 💀🔰🧺🐭 4p 2h
    # costs: 🔥 has: 👻 pot: 35
    Blueprint(
        original=Card(
            name="Infernowolf",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="With a high power and low health, this card is fiercely dangerous Its skills do not necessarily relate directly to its name, but packrat and fertility can hint at the card's fiery nature Shields are needed to counter its high damage output",
    ),
    # Phoenixbat 🧺🔰🐭🪁 0p 4h
    # costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 33
    Blueprint(
        original=Card(
            name="Phoenixbat",
            power=0,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.Soaring],
        ),
        description="With high health and spirit values, this card is difficult to take down and can soar over enemies with its skill of flight Its packrat skill means it can build up a powerful surge of attacks from its flaming aura attacks, and with fertility, it can rapidly reproduce",
    ),
    # Valkyrie 🐭💀🧺 6p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Valkyrie",
            power=6,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="a powerful and mystical female warrior, fitting for a card with high power and fertility abilities, but balanced with lower health and fire cost",
    ),
    # Hoarder 🧺🦔 2p 8h
    # costs: - has: 👻👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Hoarder",
            power=2,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Packrat, skills.Spines],
        ),
        description='this packrat is a creature with high health and a tendency to collect resources, reflected in its "Packrat" skill',
    ),
    # Narwal 🦔💀 7p 2h
    # costs: - has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Narwal",
            power=7,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines, skills.InstantDeath],
        ),
        description='a unicornlike creature with sharp tusks, reflected in its high power and "Spines" skill',
    ),
    # Tanuki 💀🐭🦔 7p 4h
    # costs: 🔥 has: 🔥👻 pot: 36
    Blueprint(
        original=Card(
            name="Tanuki",
            power=7,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility, skills.Spines],
        ),
        description="a mischievous shapeshifting animal in Japanese folklore known for playing deadly pranks on humans The high power and skills of Instant Death and spines fit this character, while Fertility adds to their craftiness overall",
    ),
    # Hippocampus 🔰🐭💀 1p 8h
    # costs: 🔥 has: 🔥👻 pot: 36
    Blueprint(
        original=Card(
            name="Hippocampus",
            power=1,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="a creature from Greek mythology with the upper body of a horse and the lower body of a fish The high health and skills of Shield and Fertility suggest a resilient and prolific creature, while the skill of Instant Death hints at its potential for surprise attacks ",
    ),
    # Nightfox 🧺💀🔰 10p 3h
    # costs: 🔥 has: 🔥👻 pot: 41
    Blueprint(
        original=Card(
            name="Nightfox",
            power=10,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath, skills.Shield],
        ),
        description="The name Nightfox sounds powerful and the card has a high power value The skill InstantDeath adds to the power and the skill Packrat could represent the fox's cunning and resourcefulness, while the Shield skill could relate to the fox being elusive and hard to hit",
    ),
    # Sunhare 🧺🔰🐭 4p 4h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Sunhare",
            power=4,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="The name Sunhare implies a quick and agile creature, which could represent the high fire value and Packrat skill The high health value could also come from the hare's wellknown ability to quickly regenerate The Fertility skill could represent the hare's ability to mate frequently and multiply",
    ),
    # Flamefalcon 🐭🧺💀 5p 4h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Flamefalcon",
            power=5,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="The name Flamefalcon is fitting for a card with high fire attribute and the skills InstantDeath and Fertility Falcons are known for their speed and agility, while the fire attribute and InstantDeath skill could represent the falcon's fiery and deadly nature The Fertility skill could represent the falcon's ability to mate frequently and raise large broods",
    ),
    # Spiritowl 🐩🔰🧺🐭 2p 5h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Spiritowl",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.Underdog, skills.Shield, skills.Packrat, skills.Fertility],
        ),
        description="The name Spiritowl combines the card's high spirit attribute with the skill Packrat, which could represent the owl's wise and cunning nature The Shield skill could represent the owl's protective nature towards its young, while the Underdog skill could represent the owl's ability to outsmart its prey The high health value could also represent the owl's resilience and ability to endure",
    ),
    # Deathviper 💀🧺🐭🔰 3p 2h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Deathviper",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="The name Deathviper represents a deadly and poisonous creature, fitting for a card with the InstantDeath skill The fire attribute and Fertility skill could represent the viper's ability to incubate its eggs, while the Packrat skill could represent the viper's cunning and ability to store venom for later use The relatively low health value could represent the viper's fragility despite its deadly nature",
    ),
    # DragonRock 🔰🐭💀 8p 3h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="DragonRock",
            power=8,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="related to its high power and health, while the rock element reflects the high defense shield skill represented by the shield skill and the ability to stay alive after every attack fertility skill, and instant death which can be caused by its powerful attacks",
    ),
    # FireHound 🐭🧺🔰 7p 4h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="FireHound",
            power=7,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="related to the fire element represented by the cards' ability to manipulate and use this element hasfire and costsfire, hound resembling the packrat skill, and that it's somewhat fragile due to its lower health",
    ),
    # SkyKraken 🪁💀🐩🐭 3p 7h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="SkyKraken",
            power=3,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[
                skills.Soaring,
                skills.InstantDeath,
                skills.Underdog,
                skills.Fertility,
            ],
        ),
        description="related to the card's ability to fly soaring skill, high health, and the underdog skill which suggests that this creature is capable of defending itself from attacks Krakens are mythical creatures that have a reputation for being huge, strong, and hard to defeat",
    ),
    # ShieldTurtle 🔰🐩🐭💀 5p 3h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="ShieldTurtle",
            power=5,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="related to its high defense and ability to shield itself shield skill, high power but relatively low health, and ability to come back to life after being defeated thanks to its fertility skill",
    ),
    # ShadowCub 🐭💀🧺 2p 10h
    # costs: 🔥 has: 🔥👻 pot: 41
    Blueprint(
        original=Card(
            name="ShadowCub",
            power=2,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="related to its low power, high health its ability to survive, and its instant death skill sudden and stealthy like a shadow Cub reflects the fertility and packrat skills",
    ),
    # Dracotaur 🧺🔰 6p 3h
    # costs: - has: 🔥🔥👻👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Dracotaur",
            power=6,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Packrat, skills.Shield],
        ),
        description='combining "dragon" and "centaur", this name reflects the card\'s high power and skill combination of Packrat and Shield, as well as its moderate health and dual firespirit costs that balance out its strength',
    ),
    # Bramblewyrm 🐭🧺💀🦔 5p 5h
    # costs: 🔥 has: 🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Bramblewyrm",
            power=5,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description='combining "bramble" and "wyrm" a type of dragon, this name fits the spiked and sharptoothed card with high power and health, as well as its combination of Fertility and Packrat skills suggesting the ability to propagate and hoard resources, and Spines skill evoking the idea of brambles',
    ),
    # Frostfox 💀🔰🐭 2p 3h
    # costs: - has: 🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Frostfox",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="suggesting a creature that is agile and elusive, this name fits the card's low power and health but high spirit and fire costs that suggest it is highly specialized and difficult to catch, and its skills of InstantDeath and Shield which further evoke the idea of a trickster that can slip past danger and defend itself when cornered",
    ),
    # Phoenixfire 🐭🐩🔰 3p 3h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Phoenixfire",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.Fertility, skills.Underdog, skills.Shield],
        ),
        description="fits the attribute balance, with higher fire costs representing the bird's mythical fire element, along with above average stats and fertility, and the skills that suggest a rebirth in tough fights",
    ),
    # Glowworm 🐭🔰🐩 2p 4h
    # costs: - has: 🔥🔥👻👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Glowworm",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield, skills.Underdog],
        ),
        description="With decent power and health, this card has no attribute costs and moderate spiritfire costs It also has skills that protect it, making it a versatile and adaptable card that will light up any deck",
    ),
    # Unicorn 🧺🔰🐭 4p 7h
    # costs: 👻👻 has: 🔥🔥🔥👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Unicorn",
            power=4,
            health=7,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="This name is already in use, but I would suggest it for this card as it has high spirit values and the skills Packrat and Fertility suggest it could have a magical and nurturing quality, like a unicorn in legends The high health value also reinforces the idea of a creature that is hard to harm",
    ),
    # Gorgonfly 🧺🔰🪁🦔 4p 4h
    # costs: - has: 🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Gorgonfly",
            power=4,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.Shield, skills.Soaring, skills.Spines],
        ),
        description="Combination of gorgon mythical creature with sharp teeth and claws and fly, which fits with the card's spines and ability to soar The powerhealth values are midrange, and the cost values are low, so the name should reflect that",
    ),
    # Phoenixowl 🪁🐭🧺💀🐩 2p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Phoenixowl",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[
                skills.Soaring,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="Combination of phoenix mythical bird that rises from the ashes and owl, which fits with the card's instant death and flying abilities The high health value suggests a strong creature, but its relatively low power means that it is better at surviving than attacking, which is reflected in the name",
    ),
    # Chimeraclaw 🐭🔰💀🧺🐩🦔 3p 3h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Chimeraclaw",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="Combination of chimera mythical creature made of different animal parts and claw, which fits with the card's high number of skills The midrange values for powerhealth suggest a creature that is adaptable, which is reflected in the name",
    ),
    # Thunderpuma 🔰🐩💀 5p 3h
    # costs: - has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Thunderpuma",
            power=5,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.Underdog, skills.InstantDeath],
        ),
        description="Combination of thunder powerful force of nature and puma, which fits with the card's high power value The midrange health value suggests a creature that can dish out damage but is also vulnerable, which is reflected in the name",
    ),
    # Infernewt 🐭🔰 7p 3h
    # costs: - has: 🔥🔥🔥🔥👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Infernewt",
            power=7,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="it's a rare, fiery, and quite hot salamander that is able to shield against other coldblooded animals, yet it has a low spirit as it is still young, hence the high fire cost",
    ),
    # Gloomhound 🔰🐭🐩 8p 7h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Gloomhound",
            power=8,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.Underdog],
        ),
        description="this fierce and gloomylooking canine enjoys being an underdog, will never run out of fire, and is quite fertile, making it a persistent hunter, and feared by its prey",
    ),
    # Spirit Wolf  1p 4h
    # costs: 👻👻👻👻👻👻👻 has: 🔥👻 pot: 4
    Blueprint(
        original=Card(
            name="Spirit Wolf",
            power=1,
            health=4,
            costs_fire=0,
            costs_spirits=7,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="highly spiritual, with decent health and power",
    ),
    # Fire Drake 🍀 0p 2h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 3
    Blueprint(
        original=Card(
            name="Fire Drake",
            power=0,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.LuckyStrike],
        ),
        description="high fire affinity with a lucky strike skill",
    ),
    # Storm Lion  1p 2h
    # costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 3
    Blueprint(
        original=Card(
            name="Storm Lion",
            power=1,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="expensive card with decent power and health",
    ),
    # Aqua Fox  0p 3h
    # costs: 🔥 has: - pot: 4
    Blueprint(
        original=Card(
            name="Aqua Fox",
            power=0,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[],
        ),
        description="no fire or spirits but high health and agility",
    ),
    # Firecat  3p 1h
    # costs: 👻👻👻👻 has: 🔥👻 pot: 5
    Blueprint(
        original=Card(
            name="Firecat",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description=" spirits,  power,  health,  fire,  skills",
    ),
    # Glimmerwing  2p 1h
    # costs: 🔥 has: 🔥 pot: 5
    Blueprint(
        original=Card(
            name="Glimmerwing",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description=" spirit,  power,  health,  fire,  skills",
    ),
    # Aquaconda  2p 3h
    # costs: 🔥🔥 has: 👻👻 pot: 8
    Blueprint(
        original=Card(
            name="Aquaconda",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description=" spirits,  power,  health,  fire,  skills",
    ),
    # Pyrofox  0p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 8
    Blueprint(
        original=Card(
            name="Pyrofox",
            power=0,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[],
        ),
        description=" spirits,  power,  health,  fire,  skills",
    ),
    # Shadowrat  2p 1h
    # costs: 👻 has: 🔥 pot: 5
    Blueprint(
        original=Card(
            name="Shadowrat",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description=" spirit,  power,  health,  fire,  skills",
    ),
    # Harpy  3p 1h
    # costs: 🔥 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Harpy",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="moderately powered and healthy, low cost in fire, average spirits, no special skills",
    ),
    # Sylph  2p 4h
    # costs: 👻👻👻👻 has: 🔥🔥👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Sylph",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=2,
            has_fire=2,
            skills=[],
        ),
        description="with an abundance of spirits, this card is light and airy but also powerful and durable, like a creature with wings",
    ),
    # Whelk  1p 2h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 6
    Blueprint(
        original=Card(
            name="Whelk",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="this is a mollusk with a spiral shell, representing the card's spiraling up powertocost ratio The health is also relatively high for the cost",
    ),
    # Efreet  2p 1h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Efreet",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[],
        ),
        description="this fierce fiery creature is strong but fragile, having low health, representing a dangerously balanced nature of this card",
    ),
    # Tortoise 🔰 0p 1h
    # costs: 👻 has: 🔥🔥 pot: 8
    Blueprint(
        original=Card(
            name="Tortoise",
            power=0,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Shield],
        ),
        description="a creature known for its sturdiness and defense, especially its shell, the name represents the high defense and specifically the shield skill that the card holds",
    ),
    # Mermaid  1p 2h
    # costs: 🔥 has: 👻👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Mermaid",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[],
        ),
        description="low power and health, costly in terms of spirits, no fire element, no skills  Mermaids are mythical creatures associated with the ocean and often portrayed as being beautiful but dangerous",
    ),
    # Dragon  1p 3h
    # costs: 🔥 has: 🔥🔥 pot: 7
    Blueprint(
        original=Card(
            name="Dragon",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[],
        ),
        description="low power, moderate health, costly in terms of fire, no spirits, high fire element, no skills  Dragons are mythical creatures often associated with fire and destruction",
    ),
    # Falconer 🪁 4p 2h
    # costs: 🔥 has: 🔥 pot: 12
    Blueprint(
        original=Card(
            name="Falconer",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="The card's skill is Soaring, which suggests a bird, while the high power and low health suggest a bird handler rather than the bird itself In combination with the cost to play the card  fire, Falconer fits well",
    ),
    # Selkie  2p 2h
    # costs: 👻👻 has: 🔥🔥👻👻 pot: 8
    Blueprint(
        original=Card(
            name="Selkie",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=2,
            has_fire=2,
            skills=[],
        ),
        description="The card has an equal balance of spirits and fire, suggesting a creature related to water The cost to play the card  fire,  spirits suggests something that is elusive and only appears in certain conditions Selkies are mythical creatures that are said to live as seals in the sea but transform into humans on land",
    ),
    # Lemming  1p 3h
    # costs: 🔥 has: 👻👻👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Lemming",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=0,
            skills=[],
        ),
        description="The card has a high spirits attribute, suggesting a small creature that has a lot of energy The name Lemming fits with the game's animal theme, and also makes sense based on the low power and high health, as lemmings are known for their endurance",
    ),
    # Scorpatron 🔰 2p 1h
    # costs: 🔥🔥🔥 has: 🔥 pot: 9
    Blueprint(
        original=Card(
            name="Scorpatron",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="Scorpion  Patronus",
    ),
    # Sparkferret 🧺 2p 1h
    # costs: 🔥 has: 👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Sparkferret",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description="A small, quick creature with a Packrat skill, this card has low health but agile movement, providing an excellent counter to larger and slower enemies Its fire cost is moderate, but its  power makes it a good investment",
    ),
    # Spikeback  4p 1h
    # costs: 🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Spikeback",
            power=4,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="referring to the high power of  and the low health of , as well as the spike on the card, which indicates it is a defensive creature",
    ),
    # Skywhipper 🪁 2p 2h
    # costs: 🔥 has: 🔥👻👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Skywhipper",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="referring to the skill Soaring, combined with the moderate power and health values and the high spirit value that indicate it is a fast, agile creature",
    ),
    # Soulripper 💀 1p 3h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Soulripper",
            power=1,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="referring to the skill InstantDeath, combined with the low power and high health values and the high fire cost which suggest it can be a tricky, elusive adversary",
    ),
    # Packmouse 🧺 2p 1h
    # costs: 🔥 has: - pot: 9
    Blueprint(
        original=Card(
            name="Packmouse",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description="referring to the low attribute values and the presence of the skill Packrat that suggests it is a weak, but devious creature that relies on cunning rather than strength",
    ),
    # Flameclaw  3p 1h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Flameclaw",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[],
        ),
        description='referring to the moderate power and low health values, combined with the high fire and spirit costs, as well as the presence of the keyword "fire" in the name which hints at the card\'s elemental affinity',
    ),
    # Fireflyer 🔰 1p 4h
    # costs: 🔥 has: 👻 pot: 14
    Blueprint(
        original=Card(
            name="Fireflyer",
            power=1,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield],
        ),
        description="fast  health for  costfire, defensive Shield, fiery hasfire",
    ),
    # Moonwolf  5p 1h
    # costs: 👻 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Moonwolf",
            power=5,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="very spiritual hasspirits, costsspirits, swift attacker power, with no extra skills",
    ),
    # Starshell  2p 5h
    # costs: 👻👻 has: 🔥🔥 pot: 12
    Blueprint(
        original=Card(
            name="Starshell",
            power=2,
            health=5,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=0,
            has_fire=2,
            skills=[],
        ),
        description="dual element card  hasfire,  hasspirits, tough exterior  health, low attack  power",
    ),
    # Packbeast 🧺 5p 1h
    # costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Packbeast",
            power=5,
            health=1,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="highly valued for carrying heavy loads, high power and low health with ability to steal cards",
    ),
    # Sunbird 🐭 1p 1h
    # costs: 🔥 has: 👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Sunbird",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="a bird that feeds on sunlight and has high spirit but low fire",
    ),
    # Pixie 🐭 1p 1h
    # costs: 🔥🔥 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Pixie",
            power=1,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="a small, mischievous creature that enhances fertility in other cards, low stats but useful skills",
    ),
    # Stormcrow 💀 2p 3h
    # costs: 🔥🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Stormcrow",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="This card's high health and power, combined with the InstantDeath skill, suggests a powerful and formidable bird of prey The name Stormcrow reflects its power and possible affinity with air elements",
    ),
    # Banshee InstantDeath 💀 2p 2h
    # costs: 🔥 has: 👻 pot: 13
    Blueprint(
        original=Card(
            name="Banshee InstantDeath",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath],
        ),
        description="Banshees are mystical creatures known for their ability to induce instant death through their scream The high powerhealth and the skill align with their deadly reputation",
    ),
    # PhoenixDeath 💀 1p 2h
    # costs: 🔥🔥 has: 🔥👻👻👻👻 pot: 14
    Blueprint(
        original=Card(
            name="PhoenixDeath",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="relates to the Instant Death skill and the high fire cost, suggesting a powerful, fiery creature",
    ),
    # GorgonWrath 💀 2p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 13
    Blueprint(
        original=Card(
            name="GorgonWrath",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="relates to the Instant Death skill and high power, suggesting a dangerous, mythical creature",
    ),
    # Dragonflame 🐩 1p 3h
    # costs: 🔥 has: 🔥🔥🔥 pot: 12
    Blueprint(
        original=Card(
            name="Dragonflame",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=3,
            skills=[skills.Underdog],
        ),
        description="relates to the high fire cost and the Underdog skill, suggesting a fierce and powerful creature with flames",
    ),
    # ChimeraStrength  2p 4h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 14
    Blueprint(
        original=Card(
            name="ChimeraStrength",
            power=2,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[],
        ),
        description="relates to the relatively high power and health values, and the mixed element cost, suggesting a mythical and powerful creature",
    ),
    # FairyFertility 🐭 1p 2h
    # costs: 🔥 has: 🔥 pot: 13
    Blueprint(
        original=Card(
            name="FairyFertility",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="relates to the Fertility skill and the low attribute values, suggesting a small and magical creature with the ability to enhance growth",
    ),
    # Gryphoness 🪁 5p 2h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Gryphoness",
            power=5,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Soaring],
        ),
        description="a flying female creature with balanced fire and spirit costs, soaring ability, and decent powerhealth",
    ),
    # Warg  2p 5h
    # costs: 🔥 has: 🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Warg",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="a wolflike hunter with moderate powerhealth, moderate fire and spirit costs, and no skills",
    ),
    # Leviathan  7p 2h
    # costs: 🔥 has: 🔥 pot: 15
    Blueprint(
        original=Card(
            name="Leviathan",
            power=7,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="high power, aquatic, fire element, no spirit element",
    ),
    # Enchantress 🐭💀 1p 1h
    # costs: 🔥 has: 🔥👻 pot: 18
    Blueprint(
        original=Card(
            name="Enchantress",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="low powerhealth, fertility skill, instant death skill, firealigned",
    ),
    # Pegasus  2p 6h
    # costs: 🔥 has: 🔥👻👻👻👻👻👻 pot: 19
    Blueprint(
        original=Card(
            name="Pegasus",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=1,
            skills=[],
        ),
        description="very high health, high spirit, moderate power, no skills",
    ),
    # Deathbat 💀🧺 3p 1h
    # costs: 🔥🔥 has: 🔥 pot: 17
    Blueprint(
        original=Card(
            name="Deathbat",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="high power with InstantDeath skill, low health, and low spirit values, giving the card a dangerous and risky play style The name comes from a creature that is dark and deadly in nature, befitting of the card's attributes",
    ),
    # Gnomeleon  2p 3h
    # costs: - has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Gnomeleon",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="very low power, decent health, no spirit cost, and no special skills but still has the fire attribute The name is a combination of Gnome and Chameleon, mythical creatures which are known for being elusive and deceptive, fitting with the card's low power and evasive capabilities",
    ),
    # Skyfin 🔰🧺🚀 0p 5h
    # costs: 🔥🔥🔥🔥 has: 🔥👻👻 pot: 20
    Blueprint(
        original=Card(
            name="Skyfin",
            power=0,
            health=5,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat, skills.Airdefense],
        ),
        description='low power but high health, with a very high fire cost, and multiple skills like Shield, Packrat, and Airdefense The name combines "Sky" for the high cost of fire and "Fin" referring to fins or a shield giving this creature a tough exterior The skills add to this metaphor making it hard to take down quickly',
    ),
    # GhostCat 💀 4p 4h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="GhostCat",
            power=4,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath],
        ),
        description="With its high fire attribute, this card is ghostly and untouchable The instant death skill adds to its deadly nature",
    ),
    # ShadowFox 🦔🐭🧺🐩 0p 2h
    # costs: 🔥🔥🔥🔥🔥 has: - pot: 18
    Blueprint(
        original=Card(
            name="ShadowFox",
            power=0,
            health=2,
            costs_fire=5,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Spines, skills.Fertility, skills.Packrat, skills.Underdog],
        ),
        description="With no fire or spirit attributes, this card is elusive like a shadow Its high health, paired with skills like spines and shield, make it a formidable opponent",
    ),
    # Flamehawk 🦔🔰 2p 4h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 18
    Blueprint(
        original=Card(
            name="Flamehawk",
            power=2,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines, skills.Shield],
        ),
        description="With balanced fire and spirit attributes, this card is a fierce predator that uses its spines and shield to defend itself and strike back at foes",
    ),
    # RatMage 🧺 2p 1h
    # costs: - has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="RatMage",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="With low power and health attributes, this card relies on its packrat skill to steal and hoard resources",
    ),
    # DreamLion 🐭💀 2p 1h
    # costs: 🔥🔥🔥 has: 👻👻👻 pot: 19
    Blueprint(
        original=Card(
            name="DreamLion",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="With low fire and high spirit attributes, this card is dreamy and mysterious Its fertility skill allows it to rapidly reproduce, making it a difficult opponent to overcome",
    ),
    # Glitterfly  0p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 3
    Blueprint(
        original=Card(
            name="Glitterfly",
            power=0,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="This creature has a high spirit pool, which is reflected in its ability to fly and burst its way to victory using its speed It's low on power, but boasts moderate health, making the Glitterfly a great closer when the opponent is low on cards The name pays homage to its bright and slightly mesmerizing glow, but don't let the beauty of the creature fool you",
    ),
    # ShadowCat  2p 2h
    # costs: 🔥 has: 🔥 pot: 7
    Blueprint(
        original=Card(
            name="ShadowCat",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="This card's attributes suggest a stealthy animal lurking in the shadows, ready to pounce on its prey The decent power and health, together with a relatively low fire cost make it a good contender for a balanced deck The lack of spirits could suggest a more solitary nature, fitting with a catlike creature",
    ),
    # FlameFox  2p 1h
    # costs: 🔥 has: 👻 pot: 5
    Blueprint(
        original=Card(
            name="FlameFox",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="This card has average health and low power, but the potential for high spirits and the absence of fire in its cost make it more of a spiritual fox than a firey one The alliteration in the name adds to the whimsy of the game, and the foxes' cunning character could go well with some of the game's skill cards",
    ),
    # ThunderDrake  2p 2h
    # costs: 🔥🔥🔥🔥 has: 👻👻 pot: 5
    Blueprint(
        original=Card(
            name="ThunderDrake",
            power=2,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description="The massive fire cost needed to bring out this card suggests a powerful creature indeed With decent attributes otherwise, the lightning name and dragonlike title suggest a fearsome creature dominating the arena The skills in the game should have some effect to show off this card's power",
    ),
    # Gorgonix  0p 4h
    # costs: 🔥 has: - pot: 6
    Blueprint(
        original=Card(
            name="Gorgonix",
            power=0,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[],
        ),
        description="hulking, high health, armored",
    ),
    # Blinkfox  3p 2h
    # costs: 🔥 has: 👻 pot: 8
    Blueprint(
        original=Card(
            name="Blinkfox",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="nimble, fast, hard to catch, spiritpowered magic",
    ),
    # Skywhale 🪁 0p 5h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Skywhale",
            power=0,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="massive health, aerial, soaring skill",
    ),
    # Phoenixfly  2p 3h
    # costs: 🔥🔥🔥 has: 🔥 pot: 7
    Blueprint(
        original=Card(
            name="Phoenixfly",
            power=2,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="very expensive, with high powerhealth, but no spirit attributes, fits with a hypothetical card that requires sacrifices to boost other cards",
    ),
    # Skykraken  2p 2h
    # costs: 🔥 has: 👻 pot: 7
    Blueprint(
        original=Card(
            name="Skykraken",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="Moderate card with balanced values, but high fire costs, implying that this creature is resilient where few else can dwell, eg higher altitudes, near volcanoes, etc",
    ),
    # Furion  3p 3h
    # costs: 🔥 has: 👻 pot: 10
    Blueprint(
        original=Card(
            name="Furion",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="relatively high health for its power, low fire costs, has no spiritual powers, implying that it is a feral creature with no ability to magically control elements, but is instead skilled in combat",
    ),
    # Iceling  3p 2h
    # costs: 🔥🔥 has: 👻 pot: 7
    Blueprint(
        original=Card(
            name="Iceling",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="Small creature with modest stats and a single skillless trait, but has a cold, almost icy exterior both in temperament and adaptation to cold environments",
    ),
    # Fire Lioness  0p 7h
    # costs: 🔥🔥 has: 🔥 pot: 11
    Blueprint(
        original=Card(
            name="Fire Lioness",
            power=0,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="high health, low cost due to no spirits, focused on fire element",
    ),
    # Sting Witch 💀🦔 1p 1h
    # costs: 👻👻👻👻👻 has: 👻 pot: 8
    Blueprint(
        original=Card(
            name="Sting Witch",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Spines],
        ),
        description="low powerhealth, high cost due to spirits, focused on instakill and spines",
    ),
    # Inferno Chameleon  2p 1h
    # costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Inferno Chameleon",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=4,
            skills=[],
        ),
        description="low health, versatile fire element, ability to adapt to different situations",
    ),
    # Ember Fox  1p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻 pot: 8
    Blueprint(
        original=Card(
            name="Ember Fox",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[],
        ),
        description="low power, moderate health and spirits, focused on fire element",
    ),
    # Firewisp  2p 3h
    # costs: 🔥 has: 🔥🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Firewisp",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="a quick, agile creature with a fiery disposition and the ability to manipulate flames",
    ),
    # Sunspear  1p 5h
    # costs: 🔥 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Sunspear",
            power=1,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="a regal and noble creature that shines bright and emits warmth, reflecting its healing and protective abilities",
    ),
    # Pocketthief 🧺 1p 1h
    # costs: 🔥 has: 🔥👻👻👻👻👻 pot: 13
    Blueprint(
        original=Card(
            name="Pocketthief",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="a mischievous and clever animal with a knack for hoarding and stealing resources",
    ),
    # Hellsbane 💀 3p 1h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Hellsbane",
            power=3,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="a fierce and fearsome beast that strikes with deadly precision, capable of dealing instant death to its foes",
    ),
    # Whisker 🧺 1p 3h
    # costs: 🔥 has: 🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Whisker",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="refers to the packrat skill, which involves stealing from opponents and hiding, like a small creature that keeps things hidden away Health is high but power is moderate, hence the name focuses on the skill rather than physical attributes",
    ),
    # Dryadling 🐭 1p 2h
    # costs: 🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Dryadling",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="With a power of , health of , and skill Fertility which suggests growth and propagation, the name Dryadling evokes the idea of a young, magical creature that is just beginning to grow into its powers",
    ),
    # Salamion  3p 2h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥 pot: 12
    Blueprint(
        original=Card(
            name="Salamion",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=5,
            skills=[],
        ),
        description="This card is heavy on fire hasfire and has a decent power and health The name Salamion relates to the heavy use of fire like a salamander and the overall strong, imposing character of the card",
    ),
    # Crustaceon 🔰 3p 1h
    # costs: 👻 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Crustaceon",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="This card is low on spirit but has high defense skill Shield and  power The name Crustaceon relates to its ability to defend itself with its shell, like a crustacean, while still having enough power to attack",
    ),
    # Packrally 🧺 1p 4h
    # costs: 🔥 has: 👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Packrally",
            power=1,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description="This card has good health and skill Packrat, which suggests hoarding and gathering resources The name Packrally evokes the idea of a group of creatures working together to gather resources and protect each other",
    ),
    # Aardvark  0p 7h
    # costs: 🔥 has: 🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Aardvark",
            power=0,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="long snout, strong defense high health, slow movement no fire ability",
    ),
    # Voodoo Bat 💀 1p 2h
    # costs: 🔥 has: 🔥👻👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Voodoo Bat",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="Low power and health make this card seem harmless, but the Instant Death skill strikes terror into the hearts of opponents",
    ),
    # Imp 💀 2p 3h
    # costs: 🔥 has: 👻 pot: 14
    Blueprint(
        original=Card(
            name="Imp",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath],
        ),
        description="This lowcost card with moderate power and health packs a punch with the Instant Death skill, making it a fearsome opponent despite its small presence The lack of fire and spirits suggests an impish creature from the underworld or magical realm",
    ),
    # Pyrogriffin 🐭 2p 1h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Pyrogriffin",
            power=2,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="fire element, fertility skill, high costfire",
    ),
    # Packhound 🐩🧺 2p 3h
    # costs: 🔥 has: 🔥 pot: 17
    Blueprint(
        original=Card(
            name="Packhound",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Underdog, skills.Packrat],
        ),
        description="With the population in the cards world being so geared towards solitary animals, the Underdog and Packrat skills fit a social canid",
    ),
    # Mandrake 💀 3p 2h
    # costs: 🔥 has: 👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Mandrake",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.InstantDeath],
        ),
        description="Mandrakes are known in legend for their deadly scream, which ties in with the Instant Death skill The low Spirit points suggest a magical creature that has difficulty existing in the real world",
    ),
    # Firebat 🔰 5p 2h
    # costs: 🔥 has: 🔥 pot: 18
    Blueprint(
        original=Card(
            name="Firebat",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="High strength with low health and a Shield skill suggests something that swoops in and charges, making a quick attack and then retreating for protection",
    ),
    # Spelunker 🧺 4p 3h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Spelunker",
            power=4,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="high fire and spirit cost, packrat skill, medium health and power",
    ),
    # Tree Nymph  3p 8h
    # costs: 🔥🔥 has: 👻 pot: 18
    Blueprint(
        original=Card(
            name="Tree Nymph",
            power=3,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="low fire presence, high spirit presence, high health, no skills",
    ),
    # Spritesong 🐭 3p 2h
    # costs: 🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Spritesong",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="low fire cost, fertility skill, low power, medium health",
    ),
    # Flamefox 🧺🔰 2p 1h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Flamefox",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.Shield],
        ),
        description="combining fire theme with fox, which suggest agility and quickness, plus the Shield and Packrat skills",
    ),
    # Chimerafly 💀🔰🐩 1p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 20
    Blueprint(
        original=Card(
            name="Chimerafly",
            power=1,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Underdog],
        ),
        description="a mythical creature that combines various animals, which fits with the card's skills, and fly represents the Underdog skill while chimera suggest deadly power",
    ),
    # Basiliskin 💀 5p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Basiliskin",
            power=5,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='combining the skills and attributes power and InstantDeath with the mythical creature Basilisk, and the "kin" ending suggests a smaller version of it',
    ),
    # Shieldturtle 🐩 1p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Shieldturtle",
            power=1,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Underdog],
        ),
        description="a turtle represents high defense and health while the Shield skill supports this, and the name has a nice ring to it",
    ),
    # Spritelion 🔰🐭 1p 3h
    # costs: 👻👻 has: 🔥🔥 pot: 21
    Blueprint(
        original=Card(
            name="Spritelion",
            power=1,
            health=3,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="a playful and fantastical name combining spirit and fertility themes with the attributes of low power and high health, and the Shield skill",
    ),
    # Nymph 🐭 4p 2h
    # costs: 👻 has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Nymph",
            power=4,
            health=2,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="spirited, with ability to boost fertility, spiritbased",
    ),
    # Ratsnake 🐭🧺 3p 1h
    # costs: 🔥 has: 🔥 pot: 20
    Blueprint(
        original=Card(
            name="Ratsnake",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="firebased, packratlike hoarder, with ability to boost fertility",
    ),
    # Shadehound 💀🧺 1p 4h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Shadehound",
            power=1,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="a doglike creature that can blend into shadows, Packrat skill represents their hoarding nature",
    ),
    # Treant  4p 7h
    # costs: 🔥 has: 🔥👻 pot: 20
    Blueprint(
        original=Card(
            name="Treant",
            power=4,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="a powerful, ancient treelike creature with high health and moderate power",
    ),
    # Thornfox 🧺🦔 2p 5h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 20
    Blueprint(
        original=Card(
            name="Thornfox",
            power=2,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Packrat, skills.Spines],
        ),
        description="combines the Spines and Packrat skills with a foxlike creature that is tough and cunning",
    ),
    # Skyguard 🐩🔰🪁 2p 5h
    # costs: 🔥🔥 has: 🔥👻 pot: 23
    Blueprint(
        original=Card(
            name="Skyguard",
            power=2,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog, skills.Shield, skills.Soaring],
        ),
        description="medium strength, good endurance, low flame cost, heartening, shielded, flying",
    ),
    # Spirit Tortoise 🔰🐭 4p 1h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Spirit Tortoise",
            power=4,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="slow, with high defense, having the ability to breed rapidly",
    ),
    # Diamondback  2p 6h
    # costs: - has: 👻 pot: 23
    Blueprint(
        original=Card(
            name="Diamondback",
            power=2,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="very resilient, fastmoving, and adaptible, but with no special powers",
    ),
    # Gryphox 🔰🐭 1p 6h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 25
    Blueprint(
        original=Card(
            name="Gryphox",
            power=1,
            health=6,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="a majestic creature with a large health pool and a shield, and strong fertility powers, suggested by the skill name, and high fire costs",
    ),
    # Pyrolon 🐭 6p 1h
    # costs: 🔥🔥 has: 🔥👻👻👻👻👻👻 pot: 24
    Blueprint(
        original=Card(
            name="Pyrolon",
            power=6,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=6,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="an explosive and fiery creature with high power and fire costs, suggested by the card's high power and fire attributes, and the Fertility skill, which could represent the ability to multiply",
    ),
    # Packrider 🧺💀 3p 3h
    # costs: 🔥 has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Packrider",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath],
        ),
        description="a quick and cunning animal with the ability to hoard resources and instant death powers, suggested by the Packrat and InstantDeath skills, and wellbalanced power and health attributes",
    ),
    # Flamefang 🧺🐭 4p 2h
    # costs: 🔥🔥🔥 has: 🔥🔥 pot: 22
    Blueprint(
        original=Card(
            name="Flamefang",
            power=4,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Packrat, skills.Fertility],
        ),
        description="a fearsome and fiery predator with high fire attributes and strong packrat and fertility abilities, symbolized by the card's high power and fire costs, and the card's Packrat and Fertility skills",
    ),
    # Oxyhorn 🔰 7p 3h
    # costs: 🔥 has: 🔥👻 pot: 24
    Blueprint(
        original=Card(
            name="Oxyhorn",
            power=7,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="a tough and resilient animal with a high shield attribute and strong offensive powers, suggested by the card's high power and health attributes, the Shield skill, and the strong fire attribute",
    ),
    # Sylphidfox 🐩🐭 3p 5h
    # costs: 👻👻👻👻 has: 🔥👻👻 pot: 24
    Blueprint(
        original=Card(
            name="Sylphidfox",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog, skills.Fertility],
        ),
        description="The card's high health and spirit costs suggest an otherworldly creature, hence the Sylphid part of the name Fox fits with the Underdog and Fertility skills as a nimble and fertile animal with cunning ability to adapt and survive",
    ),
    # Dragonfire  10p 4h
    # costs: 🔥🔥 has: 🔥🔥🔥 pot: 25
    Blueprint(
        original=Card(
            name="Dragonfire",
            power=10,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=3,
            skills=[],
        ),
        description="The high power and fire costs clearly suggest a dragon The relatively low health is balanced by its offensive power and the fact that it does not require spirits to summon",
    ),
    # Serenicorn 🐭 3p 9h
    # costs: 🔥 has: - pot: 28
    Blueprint(
        original=Card(
            name="Serenicorn",
            power=3,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="A combination of serene and unicorn, the name reflects the card's high health and fertility skill The low power and fire costs are in line with a peaceful and mythical creature and the absence of fire and spirits suggest a pure and magical being",
    ),
    # Bloodclaw 🧺 8p 3h
    # costs: 🔥 has: 👻 pot: 24
    Blueprint(
        original=Card(
            name="Bloodclaw",
            power=8,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description="The powerful attack and relative lack of defense are reflected in the name The Packrat skill hints at a scavenger or predator that collects trophies of its hunting skills The single spirit requirement suggests a fierce and primal animal ",
    ),
    # Skytalon 🐭🪁🔰 2p 2h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 26
    Blueprint(
        original=Card(
            name="Skytalon",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Fertility, skills.Soaring, skills.Shield],
        ),
        description='This name suggests a birdlike creature with talons, fitting with the skills "Soaring" and "Shield" The high fire cost and low spirits suggest a creature that is fiery and perhaps aggressive, while the balanced power and health suggest versatility The "Fertility" skill could suggest that the creature can mate and reproduce quickly, similar to many birds',
    ),
    # Vipernyx 💀 3p 1h
    # costs: - has: 🔥🔥🔥👻 pot: 25
    Blueprint(
        original=Card(
            name="Vipernyx",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.InstantDeath],
        ),
        description='This name combines the words "viper" and "onyx," suggesting a creature with snakelike abilities and perhaps even a shiny, black appearance The high power and low health suggest a creature that is venomous and dangerous but also vulnerable The "InstantDeath" skill reinforces this idea The high fire cost suggests that the creature might be fiery or have a venom that causes a burning sensation',
    ),
    # Foxfire 🔰🐭 2p 2h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 27
    Blueprint(
        original=Card(
            name="Foxfire",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[skills.Shield, skills.Fertility],
        ),
        description='This name plays with the idea of foxes and fire, suggesting a fiery creature with perhaps a foxlike appearance The balanced power and health suggest a wellrounded creature, while the "Shield" skill and high fire cost suggest that it is difficult to defeat The "Fertility" skill suggests that the creature can reproduce quickly and perhaps has a large pack of offspring',
    ),
    # Darknova 🐭🔰💀 2p 2h
    # costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Darknova",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description='This name suggests a dark and powerful creature, fitting with the high fire cost and strong "InstantDeath" skill The balanced power and health suggest a versatile creature, while the "Fertility" skill could suggest that the creature can create a horde of offspring The low fire and high spirit costs could suggest that the creature is mysterious and perhaps magical',
    ),
    # Skerrow 🐭🧺💀 0p 3h
    # costs: 🔥 has: 🔥👻👻👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Skerrow",
            power=0,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description='This name suggests a small and crafty creature, fitting with the low power but high "Packrat" skill The high spirit cost and "Fertility" skill suggest that the creature is highly social and perhaps even communal The high health and low fire cost suggest that the creature may be difficult to defeat but not particularly aggressive or dangerous',
    ),
    # Armageddon  2p 8h
    # costs: - has: 👻 pot: 27
    Blueprint(
        original=Card(
            name="Armageddon",
            power=2,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="This card's high health and no fire attribute are represented by the name, which suggests a sense of being indestructible Its name also makes sense because the card has no skills, meaning it relies on its strength alone The fantasy element of the name fits with the game's theme",
    ),
    # Whiskerbat 🐭🔰🧺 4p 2h
    # costs: 🔥 has: 🔥🔥👻 pot: 31
    Blueprint(
        original=Card(
            name="Whiskerbat",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield, skills.Packrat],
        ),
        description="This name is related to the Packrat skill and the high Fire attribute of the card The name also relates to the low Spirit attribute of the card as bats are commonly seen as spooky creatures",
    ),
    # Blossomoose 🧺 4p 10h
    # costs: 🔥 has: 🔥👻 pot: 30
    Blueprint(
        original=Card(
            name="Blossomoose",
            power=4,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="This name is fitting for the very high Health attribute of the card and the Packrat skill it possesses Blossomoose sounds like a gentle giant which is reflected in the low Power attribute",
    ),
    # Violephant 🧺🔰💀 3p 5h
    # costs: 👻👻👻 has: 👻👻 pot: 30
    Blueprint(
        original=Card(
            name="Violephant",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Packrat, skills.Shield, skills.InstantDeath],
        ),
        description='This name relates to the high Spirit attribute and the fact that the card possesses two Shield skills, which makes it difficult for the opponent to damage you The name "Violephant" can be linked to the InstantDeath skill since Violephant flowers are known for their healing purposes',
    ),
    # Flametooth 🐭 9p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Flametooth",
            power=9,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="This name is linked to the Fire attribute and the Fertility skill The high Power attribute supports the name Flametooth since it evokes a powerful fiery image",
    ),
    # Gemshell 🐭🔰 1p 8h
    # costs: 🔥🔥 has: 🔥👻 pot: 29
    Blueprint(
        original=Card(
            name="Gemshell",
            power=1,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="This name is linked to the Shield skill and high Health attribute The Fertility skill is also related to the name of the card since it represents the idea of being born from a shell, which in turn can have a shiny effect like a gem",
    ),
    # Spellturtle 🐭🔰 5p 4h
    # costs: 🔥 has: 👻 pot: 29
    Blueprint(
        original=Card(
            name="Spellturtle",
            power=5,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="Powerful with a defense mechanism and fertility Its turtlelike shell makes it a resilient and longlived creature Spellturtle has a strong correlation with magic that makes it highly sought after for its spellbound abilities",
    ),
    # Mysticfox 🐭💀🧺 2p 3h
    # costs: 🔥🔥 has: 🔥👻👻👻 pot: 29
    Blueprint(
        original=Card(
            name="Mysticfox",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="Quick and cunning, able to avoid danger instinctively It's known to hoard valuable magical objects and relics to be used when the situation gets dire",
    ),
    # Mantistaur 🐭💀 2p 7h
    # costs: 🔥 has: 🔥👻 pot: 30
    Blueprint(
        original=Card(
            name="Mantistaur",
            power=2,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="Symbiotically fierce creature born from the merging of a mantis with a bull, the Mantistaur is a skilful and agile fighter, able to decimate enemies with lightning speed, and grow twice his size in a few seconds for a powerful charge",
    ),
    # Swarmant 🐭 2p 3h
    # costs: - has: 🔥👻👻👻👻 pot: 29
    Blueprint(
        original=Card(
            name="Swarmant",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="Born from a mating of two breeds of locust, Swarmant is the quintessential swarm creature, working as a single unit to attack and fend off the enemy Its ability to command other insects is its greatest strength",
    ),
    # Skyhound 🐩🪁🧺🐭 4p 3h
    # costs: 🔥 has: 🔥👻👻👻 pot: 33
    Blueprint(
        original=Card(
            name="Skyhound",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Underdog, skills.Soaring, skills.Packrat, skills.Fertility],
        ),
        description="A creature that adapts to the change of the wind and moves with a flock, alert to danger and able to find which way the wind is blowing Skyhound is a packminded beast that loves to hoard precious items while traveling long distances with their trusted companions",
    ),
    # Goblin 🔰🐩🐭 3p 2h
    # costs: - has: - pot: 35
    Blueprint(
        original=Card(
            name="Goblin",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Shield, skills.Underdog, skills.Fertility],
        ),
        description="low powerhealth, no fire or spirit cost, but skills like Underdog and Shield suggest a scrappy creature that can take bigger foes down with it",
    ),
    # Sableback 🐭🧺💀 4p 4h
    # costs: 👻👻 has: 🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Sableback",
            power=4,
            health=4,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="a creature with a strong backbone to support its high power and health Its skills provide a packratlike ability to gather resources instantly and even an instant death attack can take down tougher foes",
    ),
    # Skyfungus 💀🔰 4p 2h
    # costs: - has: 🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Skyfungus",
            power=4,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield],
        ),
        description="a creature with high attack and one of the few with the Instant Death skill Its shield provides an extra layer of defense in tough situations",
    ),
    # Miragecat 🔰💀🧺 5p 6h
    # costs: 👻👻👻 has: 👻 pot: 35
    Blueprint(
        original=Card(
            name="Miragecat",
            power=5,
            health=6,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield, skills.InstantDeath, skills.Packrat],
        ),
        description="a creature that represents how appearances can be deceiving Although it lacks fire, its skills can make it hard to hit and its high health and power make it a formidable opponent",
    ),
    # Starseer 🐭🧺 3p 3h
    # costs: - has: 🔥👻👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Starseer",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="a creature that can foresee the future, making it a great asset for any team With its fertility and packrat skills, it can gather resources and summon allies to help protect its high spirits",
    ),
    # Changeling 🐭💀🐩🔰 2p 3h
    # costs: 👻 has: 🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Changeling",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
            ],
        ),
        description="balanced stats, but versatile skills including instant death and underdog, fits a creature capable of transformation and deception",
    ),
    # Rattlesnake 💀🔰🧺🦔 5p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 34
    Blueprint(
        original=Card(
            name="Rattlesnake",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Packrat, skills.Spines],
        ),
        description="powerful but weak health, spines indicate an animal with some defense mechanism, packrat skill fits a creature that hoards",
    ),
    # Ratscorn 🧺💀🐩🦔🐭 3p 2h
    # costs: 🔥🔥🔥🔥 has: 🔥👻👻👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Ratscorn",
            power=3,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Underdog,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description='This ferocious creature is a mix between a rat and a mythical beast, as represented by its many skills and high spirited nature The "corn" suffix in its name refers to its ability to collect and hoard items with the packrat skill, while "rats" represents its sneaky and underhanded nature',
    ),
    # Frostbite 💀🔰🐭 3p 7h
    # costs: 🔥 has: 🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Frostbite",
            power=3,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description='With high HP and fertility skill, this fantastical yetilike creature is tough to beat in battle It has the ability to freeze enemies with its icy breath thanks to the "instant death" skill, represented in its name with "frost"',
    ),
    # Armoredillo 💀🐭🔰 2p 6h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Armoredillo",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility, skills.Shield],
        ),
        description='This armored creature has high health and the shield skill, making it tough to take down in battle Its "instant death" skill allows it to quickly dispatch enemies, while its name plays on the word "armored" and the animal "armadillo"',
    ),
    # Ferretix 🔰🐭🧺💀 3p 3h
    # costs: 🔥 has: 🔥👻 pot: 36
    Blueprint(
        original=Card(
            name="Ferretix",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="A combination of the words ferret and matrix, suggesting its ability to store and protect resources skills packrat and shield and its adaptability skill fertility Its high power and moderate health make it a balanced opponent",
    ),
    # Scorpiora 🧺💀🔰 3p 8h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Scorpiora",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Packrat, skills.InstantDeath, skills.Shield],
        ),
        description="A combination of the words scorpion and aurora, suggesting its deadly stinger skill instant death and its luminous body hasspirits Its high health and moderate power make it a sturdy opponent, and the skills packrat and shield add to its defense",
    ),
    # Thundertusk 🔰🧺🐩 6p 5h
    # costs: 🔥 has: 🔥👻👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Thundertusk",
            power=6,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat, skills.Underdog],
        ),
        description="A combination of thunder and tusk, suggesting its powerful attacks skill underdog and its massive size high power and moderate health Its low costsfire, high hasspirits, and moderate hasfire further enforce its strength",
    ),
    # Phoenixie 🔰🐭 5p 6h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Phoenixie",
            power=5,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="A combination of phoenix and pixie, suggesting its ability to rise from the ashes skill fertility and its small, delicate appearance low power, moderate health Its high hasspirits and low costsfire hint at its magical nature, and the skills shield and fertility add to its defense and resurrection abilities",
    ),
    # Thunderox 💀🐭 3p 10h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Thunderox",
            power=3,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="This name reflects the high power maxed out at  and high health close to max at  of the card, as well as its abilities to instantly kill opponents InstantDeath and increase the fertility of allies Fertility",
    ),
    # Hummingjay 🐭🧺 2p 9h
    # costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Hummingjay",
            power=2,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description='The relatively low power and health of this card are reflected in the name, as hummingbirds are small but agile creatures Its focus on increasing the fertility of allies Fertility and hoarding resources Packrat is reflected in the addition of "jay," a bird known for its stash of acorns and other food in the fall',
    ),
    # Enchantigo 🐭🔰🍀🧺 2p 8h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Enchantigo",
            power=2,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.LuckyStrike,
                skills.Packrat,
            ],
        ),
        description='The name combines "enchant" and "tango," reflecting the high value placed on spirits  and fire  to play this card, as well as its abilities to increase the luck of its allies LuckyStrike, shield them Shield, breed more creatures Fertility, and hoard resources Packrat "Enchant" also suggests an element of magic or charm, fitting for a fantastical creature',
    ),
    # Goldenhedge 💀🐭🔰🦔 4p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Goldenhedge",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description='The card\'s high power  and low health  are reflected in the name, with "gold" connoting strength and "hedge" suggesting a prickly, defensive quality These attributes are matched by the card\'s abilities to destroy enemies InstantDeath, breed more creatures Fertility, shield itself Shield, and damage enemies Spines',
    ),
    # Driftwing 🐩🔰🐭🪁 4p 4h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Driftwing",
            power=4,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Underdog, skills.Shield, skills.Fertility, skills.Soaring],
        ),
        description='The name reflects the card\'s abilities to fly Soaring and defend itself Shield, as well as its focus on supporting underdogs Underdog and breeding more creatures Fertility "Drift" carries connotations of floating or gliding, while "wing" suggests flight The name also fits with the card\'s values of high spirits  and fire ',
    ),
    # Vampiricat 🐭💀🐩 5p 6h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Vampiricat",
            power=5,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Underdog],
        ),
        description="the name suggests a powerful and undead feline, fitting for a card with high power and health The skills Fertility and Underdog suggest a cunning and dangerous creature, while InstantDeath hints at its vampiric nature",
    ),
    # Drakespine 🔰🦔🧺💀🚀🪁 4p 3h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Drakespine",
            power=4,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Spines,
                skills.Packrat,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Soaring,
            ],
        ),
        description="the name refers to a mythical creature with dragonlike features and defensive spines The skills Shield, Spines, Airdefense, and Soaring emphasize its defensive and aerial traits Costsfire and hasfire also align with the creature's draconic nature, while Packrat and InstantDeath show that it can be resourceful and dangerous",
    ),
    # Spiritsquirrel 🧺💀🐭 2p 7h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Spiritsquirrel",
            power=2,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.Packrat, skills.InstantDeath, skills.Fertility],
        ),
        description="the name suggests a small and nimble creature, fitting for a card with moderate power and high health The skills Packrat and Fertility suggest a resourceful and multiplying animal, while InstantDeath shows its deadly side The high hasspirits value also aligns with the squirrel's mystical and otherworldly nature",
    ),
    # Infernofox 🔰💀🧺 7p 4h
    # costs: 👻 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Infernofox",
            power=7,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.InstantDeath, skills.Packrat],
        ),
        description="the name suggests a firebased creature with cunning and agility, fitting for a card with high power and moderate health The skills Shield and Packrat show its resourcefulness and defensive capabilities, while InstantDeath represents its cunning and deadly nature The costsspirits and hasfire values also align with its fiery and mystical nature",
    ),
    # Magpie 🔰🐭🧺 2p 10h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Magpie",
            power=2,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description="The name suggests a crafty creature, fitting for a card with the Packrat skill Its Shield and Fertility skills suggest a protective yet fertile nature The balanced fire and spirit costs with low overall values suggest a quick and resourceful creature",
    ),
    # Jackalope 🐭🧺💀 4p 4h
    # costs: - has: 🔥👻 pot: 43
    Blueprint(
        original=Card(
            name="Jackalope",
            power=4,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="Jackalopes are mythical creatures that resemble rabbits with antlers The name is fitting for this card because it has average powerhealth, but with abilities like Fertility, Packrat, and InstantDeath it can surprise opponents",
    ),
    # Dracowl 🐩🔰🐭 6p 8h
    # costs: 👻👻👻 has: 🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Dracowl",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Underdog, skills.Shield, skills.Fertility],
        ),
        description="A powerful, highly spirited creature with three skills, including Shield and Fertility, indicating its resilience and ability to grow stronger over time The 'Drac' in the name references its dragonlike powers and the 'owl' references its high spirits and watchful nature",
    ),
    # Chimeralet 💀🐭 5p 10h
    # costs: 👻👻👻 has: 🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Chimeralet",
            power=5,
            health=10,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="A slightly shorter variation of \"Chimera,\" this name represents the card's Instant Death skill, implying a fierce and deadly nature The 'let' at the end is a diminutive, underscoring the card's smaller size compared to other Chimera creatures The Chimeralet's  power and  health, along with its Fertility skill, indicate a tenacious and strong creature",
    ),
    # Griffwisp 🐭🐩🔰 5p 8h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Griffwisp",
            power=5,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.Underdog, skills.Shield],
        ),
        description='A combination of "Griffin" and "Willo\'thewisp," this name implies a strong, fantastical creature with fire affinity as well as the ability to guide and protect others referenced by its Shield and Underdog skills The Griffwisp\'s  power,  health, and  fire affinity suggest a creature that is both formidable and balanced',
    ),
    # Enchanthorn 🐭💀🐩 8p 5h
    # costs: 👻👻👻 has: 🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Enchanthorn",
            power=8,
            health=5,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Underdog],
        ),
        description="An enchanting creature with Instant Death, Fertility, and Underdog skills, the Enchanthorn's  power and  health suggest a strong and dangerous character The 'thorn' at the end of the name references its spiky, prickly abilities",
    ),
    # Phoenixhare 🐭🔰 9p 7h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Phoenixhare",
            power=9,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="A fiery creature with Shield and Fertility skills, the Phoenixhare embodies the concept of rebirth and regeneration referenced by the Phoenix name while also being nimble and quick referenced by the hare Its  power,  health, and  fire affinity suggest a strong creature that can both defend itself and deal damage",
    ),
    # Krakensaur 🔰💀🧺🦔🪁 2p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Krakensaur",
            power=2,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Spines,
                skills.Soaring,
            ],
        ),
        description="This card has high health and moderate power, with a cost that is not too high The skills include packrat and instant death suggesting its ability to consume prey The name Krakensaur brings together the imagery of a dragonlike reptile and a powerful ocean creature which fits the card's attributes",
    ),
    # Starwhale 💀🔰🐭 5p 5h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Starwhale",
            power=5,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="This card has a good balance of power and health, with a moderate cost to play The skills include instant death and shield, suggesting a formidable opponent Starwhale invokes the image of a massive, otherworldly creature that is aweinspiring and dangerous",
    ),
    # Griffowl 🧺🐭🦔 9p 5h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Griffowl",
            power=9,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Spines],
        ),
        description="This card has high power and health, with a low cost to play The skills include packrat and spines, suggesting a powerful, predatory bird Griffowl combines the imagery of a griffin and an owl, which fits the card's profile perfectly",
    ),
    # Thunderhog 💀🐭🧺 4p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Thunderhog",
            power=4,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Fertility, skills.Packrat],
        ),
        description="fits with the high power and health, and the InstantDeath skill, while also hinting at its association with fire and spirits as seen in the attribute values",
    ),
    # Pandragon 🐭🐩🔰💀 2p 6h
    # costs: 👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Pandragon",
            power=2,
            health=6,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=3,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="combines the ideas of pandas and dragons into a fantastical creature of high health and moderate power, with the skills Fertility and Shield having a nurturing and protective connotation, respectively",
    ),
    # Chimerafoe 🐭🐩💀 9p 5h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Chimerafoe",
            power=9,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Underdog, skills.InstantDeath],
        ),
        description="a play on the mythical creature chimera, indicating a powerful and deadly creature that is also associated with fire and has the skill InstantDeath",
    ),
    # Shadowfox 🧺🐭💀 8p 5h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Shadowfox",
            power=8,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Packrat, skills.Fertility, skills.InstantDeath],
        ),
        description="a mysterious, elusive creature with strong spirits and fire, as well as the skills Packrat and Fertility, possibly indicating a cunning and resourceful nature",
    ),
    # Thorniclaw 🧺🔰🐭🦔 7p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Thorniclaw",
            power=7,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.Spines],
        ),
        description="a name that suggests the spines and high power, while also incorporating the Shield skill and the association with fire seen in the attribute values",
    ),
    # Blazefin 🐭💀🦔 5p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Blazefin",
            power=5,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Fertility, skills.InstantDeath, skills.Spines],
        ),
        description="referring to the high fire attribute and sharp spines, as well as the high power and health stats",
    ),
    # Swarmwing 🐭🧺💀 6p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Swarmwing",
            power=6,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="relating to the Packrat skill and the multiple skills it has, as well as the balanced attributes",
    ),
    # Griffinix 🧺🐭🐩 5p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Griffinix",
            power=5,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Underdog],
        ),
        description="a mix between a griffin and a phoenix, as a reference to the high health and fire attributes and the packrat and fertility skills",
    ),
    # Deathfang 💀🧺🐭🐩 3p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Deathfang",
            power=3,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="referring to the high instant death skill and the spines, as well as the relatively low power",
    ),
    # Armashield 🦔🔰💀🐭 4p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Armashield",
            power=4,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="a mix between an armadillo and a shield, referring to the high health and spines, as well as its shield and instant death skills",
    ),
    # Phoenixcat 💀🐭🔰 9p 4h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Phoenixcat",
            power=9,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Fertility, skills.Shield],
        ),
        description="With strong fire attributes and a shield ability, the Phoenixcat is hard to defeat Instant death and fertility powers only add to its danger, making it a true force to be reckoned with",
    ),
    # Nightshade 🐭🔰💀🐩 3p 3h
    # costs: - has: 🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Nightshade",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="Refers to a plant that is poisonous, linking to InstantDeath skill, and its dark and mythical vibe fits with Shield and Underdog skills",
    ),
    # Shimmerwing 🧺🐭🐩🔰 5p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Shimmerwing",
            power=5,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Underdog, skills.Shield],
        ),
        description="an elegant creature with high health and power, but costly to summon the packrat and shield skills contribute to its resilience",
    ),
    # Starfrost 🧺🔰🐩🐭 4p 8h
    # costs: 👻👻 has: 🔥🔥🔥👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Starfrost",
            power=4,
            health=8,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Packrat, skills.Shield, skills.Underdog, skills.Fertility],
        ),
        description="a magical creature with a lot of spirit power and fertility, but weak against fire the underdog skill adds an element of surprise, while the shield skill protects it",
    ),
    # Thornbeast 🐭🦔🔰 7p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Thornbeast",
            power=7,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Fertility, skills.Spines, skills.Shield],
        ),
        description="a powerful, yet spiky creature with high health and low spirit cost the spines skill adds to its already dangerous physique, while the shield and fertility skills keep it going",
    ),
    # Aerialisk 🐭💀🧺🚀🐩 9p 4h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Aerialisk",
            power=9,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Airdefense,
                skills.Underdog,
            ],
        ),
        description="an airborne creature with a lot of power, but low health and spirit cost the packrat and underdog skills emphasize its ferocity, while the air defense skill makes it a formidable opponent against other flying creatures",
    ),
    # Draconic 🔰🐭💀🐩 3p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Draconic",
            power=3,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="With high power and health, as well as the skills Shield and Underdog, this card inspires an image of a powerful, firebreathing dragon with an impenetrable shield The skills Fertility and InstantDeath add to the sense of awe and danger surrounding this creature",
    ),
    # Glaciate 🔰🦔🐭💀🧺 7p 4h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Glaciate",
            power=7,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Spines,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="The high power and spines of this card, combined with the Shield and Fertility skills, suggest a creature made of ice with sharp, dangerous spikes protruding from its body The Packrat skill adds an element of resourcefulness and cunning to the mix",
    ),
    # Etherion 🧺🐩🔰🐭 3p 10h
    # costs: 👻 has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Etherion",
            power=3,
            health=10,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Underdog, skills.Shield, skills.Fertility],
        ),
        description="With its high health and spirit values, this card brings to mind a mystical, otherworldly creature that can disappear into thin air The skills Packrat and Underdog also suggest an elusive, hardtocatch quality, while Shield and Fertility hint at an ethereal, protective nature",
    ),
    # Sirenade 🐭💀🧺 6p 4h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Sirenade",
            power=6,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="The powerful, seductive allure of a siren is evoked by this card's Fertility skill, while the InstantDeath skill brings to mind the dangerous songs that can lure sailors to their doom The Packrat skill also suggests a creature that can accumulate treasures and resources, while its moderate power and health values suggest a challenging foe",
    ),
    # Vulpineer 🧺🔰🐭 3p 6h
    # costs: - has: 🔥🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Vulpineer",
            power=3,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="An intelligent and cunning creature, the Vulpineer is quick to adapt to its environment and make use of its resources  skills reflected in this card's Packrat and Fertility attributes The Shield skill suggests a defensive, tactical quality, while the moderate power and health values paint a picture of a creature that relies more on wit than brute force",
    ),
    # Necroturtle 💀🧺🐭🔰🐩 2p 3h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Necroturtle",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="a turtlelike creature with the ability to inflict instant death, also a packrat, shielded, fertile, and an underdog",
    ),
    # Sunlioness 🐭🔰🐩 6p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Sunlioness",
            power=6,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Fertility, skills.Shield, skills.Underdog],
        ),
        description="a powerful lioness with high health and fire affinity, also fertile, shielded, and an underdog",
    ),
    # Phoenishark 🧺🔰🐭💀🐩 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Phoenishark",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="a fantastical creature with high powerhealth and water affinity, also a packrat, shielded, fertile, can inflict instant death, and is an underdog",
    ),
    # Mysticorn 🐭🧺💀🔰🐩 7p 9h
    # costs: 👻👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Mysticorn",
            power=7,
            health=9,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="a mystical unicorn with high powerhealth and spirit affinity, also shielded, fertile, a packrat, can inflict instant death, and an underdog",
    ),
    # Deathwing 💀🔰🐭 1p 2h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻 pot: 29
    Blueprint(
        original=Card(
            name="Deathwing",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=5,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="With the skills Instant Death and Shield, this creature represents strength in both attack and defense The name reflects the instant death ability and powerful defense",
    ),
    # Packwolf 🧺🐩🔰🐭💀 9p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Packwolf",
            power=9,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Packrat,
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="This creature has the skills Packrat and Underdog, making it an ideal infiltrator and collector Its high power and health make it a threatening opponent Packwolf represents the creature's packrat abilities, as well as its wolflike strength and cunning",
    ),
    # Faeunicorn 🐭🧺💀 9p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Faeunicorn",
            power=9,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="The high spirit score and Fertility skill of this card suggest a magical creature with healing abilities Its high power and health make it a formidable opponent The name Faeunicorn represents the creature's magical essence and physical toughness",
    ),
    # Shieldrhino 🐭💀🧺🔰 5p 7h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Shieldrhino",
            power=5,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="This creature has the skills Shield and Packrat, indicating that it's an invincible collector The high health score and the rhinolike strength make it difficult to defeat Shieldrhino represents the creature's strength, protective qualities, and natural armor",
    ),
    # Firebug 💀🔰🐭 9p 4h
    # costs: 👻👻👻👻👻 has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Firebug",
            power=9,
            health=4,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="The high spirit score and Fertility skill of this card suggest a creature with the ability to create life from fire Its high power and health make it a threatening opponent The name Firebug represents the creature's fiery nature and insectoid appearance",
    ),
    # Glimmbat 🔰🐩🐭 5p 3h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Glimmbat",
            power=5,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.Shield, skills.Underdog, skills.Fertility],
        ),
        description="a small but tough creature with a shield ability and high fertility",
    ),
    # Thunderhare 🔰🐭🐩🧺💀🚀 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Thunderhare",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
                skills.Airdefense,
            ],
        ),
        description="a fast and powerful rabbit with multiple skills, including air defense and instant death",
    ),
    # Thornoceros 🦔🔰 9p 7h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Thornoceros",
            power=9,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Spines, skills.Shield],
        ),
        description="a spiny rhinoceroslike creature with strong shield and spine abilities",
    ),
    # Nebulion 🐭🚀💀🐩 8p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Nebulion",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Airdefense,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="a mystical creature with high fertility and the ability to defend against air attacks, perfect for a player with a focus on spirits",
    ),
    # Seedpup 🐭 3p 4h
    # costs: 👻 has: 🔥🔥👻👻 pot: 22
    Blueprint(
        original=Card(
            name="Seedpup",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="a small but fertile and determined creature with fertility skills",
    ),
    # SkyDragon 🪁🦔🐭💀🔰🚀 7p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 75
    Blueprint(
        original=Card(
            name="SkyDragon",
            power=7,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Soaring,
                skills.Spines,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Airdefense,
            ],
        ),
        description="high powerhealthspirits, fire cost, soaring, spines, fertility, instant death, shield, airdefense",
    ),
    # ViperHawk 🦔 8p 7h
    # costs: 🔥 has: 🔥👻 pot: 29
    Blueprint(
        original=Card(
            name="ViperHawk",
            power=8,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description="high power, low health, fire cost, spines",
    ),
    # UnderRat 🐭🐩🧺 4p 2h
    # costs: 🔥🔥 has: 🔥 pot: 26
    Blueprint(
        original=Card(
            name="UnderRat",
            power=4,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.Underdog, skills.Packrat],
        ),
        description="low powerhealth, high fire cost, packrat, underdog",
    ),
    # ShieldArmadillo 🧺🔰 4p 6h
    # costs: 🔥🔥🔥 has: 👻👻 pot: 28
    Blueprint(
        original=Card(
            name="ShieldArmadillo",
            power=4,
            health=6,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Packrat, skills.Shield],
        ),
        description="low power, high health, high fire cost, packrat, shield",
    ),
    # Fungaloid 🧺🦔🔰🐭💀 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 75
    Blueprint(
        original=Card(
            name="Fungaloid",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Spines,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="The card has high spirits but requires high fire to use The name's relation to the card highlights its growth aspect, which has skills like Packrat and Fertility The spiky armor is reflected in its Spines and Shield skills, while its deadliness and fragility are reflected in InstantDeath",
    ),
    # Apexlion 🔰💀🪁 7p 4h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Apexlion",
            power=7,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Shield, skills.InstantDeath, skills.Soaring],
        ),
        description="With high power, the name suits the card as the animal is seen as the ultimate predator The name's relation to the card highlights its strength with Shield and InstantDeath abilities The Soaring skill is related to the lions aspect of being a king of the skies",
    ),
    # Ferretora 🐭🧺 3p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Ferretora",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="The name relates to the card's animal theme, with the name being a fusion of ferret and tora Japanese for tiger The name's relation to the card highlights its balance of power and health, with skills like Fertility helping to keep it alive Its other skill, Packrat, is related to what real ferrets do",
    ),
    # Shadowsting 💀 3p 3h
    # costs: 🔥 has: 👻 pot: 16
    Blueprint(
        original=Card(
            name="Shadowsting",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath],
        ),
        description="The name relates to the card's instant death ability, which is represented in its skills The animal theme is represented by a mysterious creature that lives in the shadows, while its fire requirement is reflected in its name",
    ),
    # Armorspike 🦔💀🧺🔰 6p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Armorspike",
            power=6,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Spines, skills.InstantDeath, skills.Packrat, skills.Shield],
        ),
        description="This card has high power, spines and instant death skill Suggesting a name that highlights its spiky armor, deadly capability, and formidable strength",
    ),
    # EnigmaMoth 🧺🐩🔰 3p 10h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="EnigmaMoth",
            power=3,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Packrat, skills.Underdog, skills.Shield],
        ),
        description="An animal of myth has a high health value, shield and underdog skill which makes them unpredictable and hard to target The name is a nod to the creature's elusiveness and defensive abilities",
    ),
    # Furyphoenix 🧺🐭🐩💀 7p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Furyphoenix",
            power=7,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
            ],
        ),
        description="This card has high power  hit points, fertility skill which means it can spawn other creatures, instant death and underdog skill Suggesting a name that highlights its fierce fire, ability to spawn other creatures, and strong defense when outnumbered",
    ),
    # Spirited Bear 🚀🦔🐭🪁💀🧺 10p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Spirited Bear",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Airdefense,
                skills.Spines,
                skills.Fertility,
                skills.Soaring,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="This card's high power and health values, and multiple skills including air defense and fertility make it a dominant force on the field The name reflects its high spirits and strength, while also nodding to its air defense abilities",
    ),
    # Fierceback 🦔💀🧺🔰🐭 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Fierceback",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="This card has spines, instant death skill, high power and HP, and a packrat skill The name refers to its formidable weaponry, its determination to protect its brood and its ability to survive ",
    ),
    # Flameleon 🧺 4p 2h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥 pot: 19
    Blueprint(
        original=Card(
            name="Flameleon",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=5,
            skills=[skills.Packrat],
        ),
        description="This card has high fire affinity, has the ability to store extra fire, and has a skill called Packrat, which fits well with the image of a small lizard that hoards flames and other treasures",
    ),
    # Phoenixcub 💀🐭🔰🧺 3p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Phoenixcub",
            power=3,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="With high health and many skills, this card is already strong and versatile, but as a young phoenix it also has great potential to grow stronger and evolve",
    ),
    # Undergnat 🐩 1p 2h
    # costs: 🔥 has: 🔥🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Undergnat",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Underdog],
        ),
        description="This card has low power and health but the Underdog skill, which makes it stronger when it is outnumbered The name Undergnat plays on this theme of being small but able to annoy opponents, like a pesky little insect",
    ),
    # Shieldpup 💀🔰 2p 1h
    # costs: 🔥🔥 has: 👻 pot: 16
    Blueprint(
        original=Card(
            name="Shieldpup",
            power=2,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Shield],
        ),
        description="With a few defensive skills but low power and health, this card seems like a scrappy little puppy that can bark a lot but isn't too intimidating on its own The name Shieldpup reflects its resilience and potential to grow into a stronger protector",
    ),
    # Bansheeowl 💀🐭🐩 1p 1h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Bansheeowl",
            power=1,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility, skills.Underdog],
        ),
        description="relatively weak, but has InstantDeath skill and has  fire icons, making it deadly against other creatures",
    ),
    # Spriteling 🐭🔰 2p 1h
    # costs: - has: 👻👻 pot: 29
    Blueprint(
        original=Card(
            name="Spriteling",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="small, fast, and has the Fertility and Shield skills to help control the field and protect other creatures",
    ),
    # Chimerafang 🧺🔰💀🐭 4p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Chimerafang",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="ferocious and skilled, with Packrat, Shield, InstantDeath, and Fertility skills and both fire and spirit requirements",
    ),
    # Firetortoise 🔰 1p 2h
    # costs: 🔥🔥🔥 has: 🔥👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Firetortoise",
            power=1,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="slow and heavily costed, but with high defense and a powerful Shield skill to make it difficult to take down",
    ),
    # Pyrodillo 💀🐭🔰🐩🦔 9p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Pyrodillo",
            power=9,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="an armored creature with high power and health, and both fire and spirit requirements, as well as several versatile skills like InstantDeath, Fertility, Shield, Underdog, and Spines",
    ),
    # Gemmog 🔰🐭 2p 2h
    # costs: 🔥 has: 🔥 pot: 21
    Blueprint(
        original=Card(
            name="Gemmog",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="related to gems, as the card has Shield skill",
    ),
    # Fribbit 🐭💀🔰 4p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Fribbit",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="related to frog, as the card has Fertility skill, and high power, but low health",
    ),
    # Pinelmink 🐭🔰🦔 3p 3h
    # costs: 🔥 has: 🔥 pot: 27
    Blueprint(
        original=Card(
            name="Pinelmink",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield, skills.Spines],
        ),
        description="related to pine martens, as the card has Spines skill, and is a balance between power and health",
    ),
    # Dragonsaur 🐭🧺🔰🐩💀🦔 6p 9h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Dragonsaur",
            power=6,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="related to a dinosaur, as the card has many skills and a high cost and health",
    ),
    # Hedgemars 🐭 3p 1h
    # costs: 🔥🔥 has: 👻👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Hedgemars",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="related to hedgehogs and marsupials, as the card has Fertility skill and is lowcost, with high health",
    ),
    # Frostmoth 🐩 5p 2h
    # costs: 👻👻👻 has: 👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Frostmoth",
            power=5,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Underdog],
        ),
        description="a magical moth that lives in colder places, costs spirit, has a little fire, but is very frail",
    ),
    # Infernusaur  6p 2h
    # costs: 👻 has: 🔥 pot: 14
    Blueprint(
        original=Card(
            name="Infernusaur",
            power=6,
            health=2,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="powerful, fiery, low spirits cost, low spirits value, moderate health",
    ),
    # Luckythorn 🍀💀 1p 1h
    # costs: 🔥 has: 🔥 pot: 9
    Blueprint(
        original=Card(
            name="Luckythorn",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.LuckyStrike, skills.InstantDeath],
        ),
        description="lucky and deadly, but weak, firebased, no spirits",
    ),
    # Flamegrizzly 🐭🔰💀 2p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻 pot: 29
    Blueprint(
        original=Card(
            name="Flamegrizzly",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=4,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="strong, high fire cost and fire value, can shield and procreate",
    ),
    # Shieldrex 💀🔰🐭 7p 6h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Shieldrex",
            power=7,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="highly protective, strong and enduring, high spirits value, high fire value",
    ),
    # Fertigore 💀🧺🐭 8p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Fertigore",
            power=8,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Packrat, skills.Fertility],
        ),
        description="Fertile and has  power and health, with the skills InstantDeath and Packrat",
    ),
    # Coralynx  5p 1h
    # costs: 🔥 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Coralynx",
            power=5,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="A small but powerful creature, with  power and  health, and a fiery attribute",
    ),
    # Winglet 🐭🪁💀 4p 1h
    # costs: 🔥 has: 👻 pot: 24
    Blueprint(
        original=Card(
            name="Winglet",
            power=4,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility, skills.Soaring, skills.InstantDeath],
        ),
        description="Has a combination of abilities, with  power and  health, and can fly and be fertile",
    ),
    # Frostback 🔰🐭🦔🧺 4p 6h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Frostback",
            power=4,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[skills.Shield, skills.Fertility, skills.Spines, skills.Packrat],
        ),
        description="A snowloving creature with  power and  health, and the ability to defend itself with a shield, deal damage with spines and be fertile",
    ),
    # Flameknight  9p 3h
    # costs: 🔥🔥🔥🔥🔥🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Flameknight",
            power=9,
            health=3,
            costs_fire=6,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="A strong card with high power and moderate health, with an expensive cost in fire to play",
    ),
    # FertilitySage 🧺💀🔰🐩🐭 3p 5h
    # costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="FertilitySage",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
            ],
        ),
        description='This card has a high health and spirit cost and specializes in increasing the fertility of other cards Its packrat skill helps keep it supplied with enough spirits, and its instant death skill can neutralize a powerful enemy The name "FertilitySage" fits its nurturing nature and speciality in providing support to other cards',
    ),
    # ThornedLynx 💀🐭🔰🦔 4p 6h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="ThornedLynx",
            power=4,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description='This card has spines and high power and health, plus a moderate fire cost Its instant death and shield skills and moderate spirit cost emphasize its fighting abilities Its name "ThornedLynx" reflects its powerful nature and sharp spines',
    ),
    # SpinyImp 🦔 6p 1h
    # costs: - has: 🔥👻 pot: 25
    Blueprint(
        original=Card(
            name="SpinyImp",
            power=6,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description='This cheap card has high power and low health, plus useful spines and moderate fire and spirit costs Its name "SpinyImp" represents its mischievous and spiky nature, with the ability to inflict damage',
    ),
    # ShieldedBasilisk 🧺💀🔰🐭 5p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="ShieldedBasilisk",
            power=5,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description='This card has moderate stats overall, with high fire and spirit costs and shield, instant death, packrat, and fertility skills Its name "ShieldedBasilisk" emphasizes its defensive capabilities, and the instant death skill represents its dangerous nature',
    ),
    # ArmoredRhino 💀🧺🐭🔰 8p 3h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 47
    Blueprint(
        original=Card(
            name="ArmoredRhino",
            power=8,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description='This powerful card has high stats across the board and a moderate fire cost Its skills include instant death, packrat, fertility, and shield Its name "ArmoredRhino" reflects its thick skin, and the instant death skill represents its deadly nature',
    ),
    # Voidragon 🔰🐭🦔🧺💀 6p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Voidragon",
            power=6,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Spines,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="The name relates to the card's high power and health, as well as its attribute of having a lot of spirits and being very costly  in comparison to the Grizzly Bear The card's skills add to its fierce and mystical character, and the name \"Voidragon\" implies a powerful and almost mystical creature",
    ),
    # Starhound 💀🦔🐭🪁🧺🐩 9p 9h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Starhound",
            power=9,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Spines,
                skills.Fertility,
                skills.Soaring,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description='The name "Starhound" relates to the card\'s high power and health values and the fact that it has no costs in fire or spirits, making it a very versatile card The skills also make it a fierce Hunter creature, which makes the name even more fitting',
    ),
    # Windrider 💀🚀🐭🧺🔰 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Windrider",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Airdefense,
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description='The name "Windrider" relates to the card\'s high power and health values especially when looked at its price, as well as its low fire and spirits costs, which are indicated in the card The skills also make it a speedy and agile creature, which makes the name even more fitting',
    ),
    # Skulker 💀 10p 4h
    # costs: 🔥 has: 🔥👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Skulker",
            power=10,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='The name "Skulker" implies a creature that is powerful and sneaky, which relates to the card\'s high power value and its skill "InstantDeath" The card\'s low health values, as well as its low fire and spirit costs, are also taken into account when coming up with this name',
    ),
    # Burrower 🧺🐭 3p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Burrower",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Packrat, skills.Fertility],
        ),
        description='The name "Burrower" suggests a creature that is underground, which relates to the card\'s skill set The card has low power and health values but high spirit cost, which are all taken into account when suggesting this name The name also implies that this card type is best for supporting other creature types',
    ),
    # Faewolf 🔰💀🐭 3p 3h
    # costs: 👻👻👻👻👻 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Faewolf",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.InstantDeath, skills.Fertility],
        ),
        description="has high spirit cost, animal name relates to fertility skill, average powerhealth, and has defensive skills",
    ),
    # Inferna  4p 1h
    # costs: 🔥🔥🔥 has: 🔥 pot: 7
    Blueprint(
        original=Card(
            name="Inferna",
            power=4,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="high fire cost, high power, low health, no skills, and name relates to fire",
    ),
    # Packturtle 🔰🧺💀 4p 10h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Packturtle",
            power=4,
            health=10,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Shield, skills.Packrat, skills.InstantDeath],
        ),
        description="high health, lots of firespirit, defensive skills, and name relates to defensive skill and animal combination",
    ),
    # FertilityFox 🐭 1p 2h
    # costs: 🔥 has: 👻 pot: 13
    Blueprint(
        original=Card(
            name="FertilityFox",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="low powerhealth, minimal fire, one fertility skill, and animal name relates to skill",
    ),
    # Spiritox 🐭🧺💀 5p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Spiritox",
            power=5,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="a powerful creature with high health and strength but requires a lot of fire and spirit to summon and maintain Skills such as fertility and packrat make it a fearsome enemy The 'tox' part of the name indicates it is venomous and dangerous, while 'spirit' references its magical abilities",
    ),
    # Blinkcat 🐭 3p 4h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 20
    Blueprint(
        original=Card(
            name="Blinkcat",
            power=3,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="a quick and agile feline that is somewhat expensive and difficult to summon due to the high fire cost Its fertility skill references its ability to rapidly reproduce, while its low health indicates it can be taken down just as quickly",
    ),
    # Airviper  3p 1h
    # costs: 🔥🔥🔥 has: 👻👻 pot: 6
    Blueprint(
        original=Card(
            name="Airviper",
            power=3,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description="a dangerous reptilian creature that requires spirit to summon and is quite fragile Despite this, its flight skills make it difficult to attack Its name references both its ability to fly and its venomous bite",
    ),
    # ShieldBear 🦔🪁🔰🐭🧺🐩 6p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="ShieldBear",
            power=6,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.Soaring,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="a massive creature with high health and strength but no fire cost Its skills, particularly shield and underdog, indicate a tanklike role Its name references its ability to protect other creatures and take heavy hits",
    ),
    # Featherbat 🪁 2p 2h
    # costs: 🔥 has: 🔥👻👻👻👻👻 pot: 13
    Blueprint(
        original=Card(
            name="Featherbat",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="a flying creature with medium powerhealth and moderate fire cost Its soaring skill makes it difficult to attack, while its name references its feathered wings and its batlike appearance",
    ),
    # Shieldbear 🐭🔰💀 3p 9h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Shieldbear",
            power=3,
            health=9,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="The card has high health and is equipped with several shield skills The name Shieldbear indicates a sturdy, armored creature that is tough to take down",
    ),
    # Faeferret 🐭 1p 2h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Faeferret",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="The card is small low power, low health, but has high spirit and fire attributes, and a fertility skill The name Faeferret has a magical and playful quality to it, which fits with the card's attributes",
    ),
    # Firefox 🐭 1p 2h
    # costs: 🔥 has: 🔥🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Firefox",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="The card is a lowcost card with relatively low power and health, but has high fire attribute and a fertility skill The name Firefox evokes the element of fire and the animal's agility and swiftness",
    ),
    # Shellback 🔰🐩 2p 2h
    # costs: 🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Shellback",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Underdog],
        ),
        description="The card has average power and health, but is equipped with shield and underdog skills The name Shellback indicates a tough, protective creature",
    ),
    # Archelion 🐭🔰🧺 7p 4h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Archelion",
            power=7,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield, skills.Packrat],
        ),
        description="related to the powerhealth ratio and the skill packrat",
    ),
    # Dreamweaver 🦔💀🚀🔰🐭 7p 9h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Dreamweaver",
            power=7,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="high spirited, high health, diverse set of skills",
    ),
    # Chrysalis 🔰🧺🐭💀🚀 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Chrysalis",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Airdefense,
            ],
        ),
        description="related to the protective skills and the equally balanced attributes",
    ),
    # Packratle 🧺🔰💀 2p 3h
    # costs: - has: 🔥🔥👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Packratle",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Packrat, skills.Shield, skills.InstantDeath],
        ),
        description="related to the packrat skill and the name similarity to Armadillo",
    ),
    # Thunderhorn 🐭💀🧺🐩🦔🔰 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Thunderhorn",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description="with high values in power and health, and the skills InstantDeath and Shield, this card is both mighty and hard to defeat The name suggests a powerful and dangerous creature, with a fierce horn that strikes like thunder",
    ),
    # Skylynx 💀🔰🪁🐭 2p 2h
    # costs: 🔥 has: 🔥👻👻👻 pot: 31
    Blueprint(
        original=Card(
            name="Skylynx",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Soaring,
                skills.Fertility,
            ],
        ),
        description="with decent power and health stats, and the skills Soaring and Shield, this card can hold its own The name suggests a majestic and swift creature that can traverse the skies with grace and ease",
    ),
    # Firehoof 💀🐭🐩 8p 3h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Firehoof",
            power=8,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Fertility, skills.Underdog],
        ),
        description="with high power but low health, this card is risky to play However, the skill InstantDeath can help it take down even the strongest enemies The name suggests a creature with hooves that are infused with fire, giving it a dangerous and fiery kick",
    ),
    # Whispup 💀🪁🐭🧺 2p 1h
    # costs: 🔥 has: 🔥👻 pot: 27
    Blueprint(
        original=Card(
            name="Whispup",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Soaring,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="with low power and health, this card seems weak However, the skills Soaring and Fertility suggest a creature that can grow and strengthen quickly The name suggests a small, wispy creature that can flutter and dance in the wind, but has the potential to become much more than it appears",
    ),
    # Armorgator 🐩💀🔰🧺🐭🦔 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Armorgator",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="with high power and health, this card is a formidable opponent The skills Shield and Packrat make it even harder to take down The name suggests a creature with scaly armor that protects its vulnerable spots, and a tenacious fighter that doesn't give up easily",
    ),
    # Mysticboar 🐭🐩🔰 6p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Mysticboar",
            power=6,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=6,
            skills=[skills.Fertility, skills.Underdog, skills.Shield],
        ),
        description="high power and health, some fire and spirits, fertility and shield skills, related to the boar's fighting abilities and mystical attribute",
    ),
    # Solarlynx 🐭🔰💀 9p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Solarlynx",
            power=9,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="high power, low health, some fire and spirits, fertility, shield and instant death skills, related to the lynx's hunting and nocturnal abilities",
    ),
    # Spindlecat 🐩💀🐭🔰🧺 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Spindlecat",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="high power and health, some fire and spirits, fertility, shield, instant death, underdog and packrat skills, related to the cat's agility, survival and collection abilities",
    ),
    # Scalemouse 🔰💀🐭🐩 4p 5h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Scalemouse",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="low power and health, some fire and spirits, fertility, shield, underdog and instant death skills, related to the mouse's small size, armor and defensive qualities",
    ),
    # Flametick 🐭🔰💀 2p 5h
    # costs: 🔥 has: 🔥👻👻 pot: 34
    Blueprint(
        original=Card(
            name="Flametick",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="low power, high health, some fire and spirits, fertility, shield and instant death skills, related to the tick's parasitic nature and fire attribute",
    ),
    # Thunderstag 🧺🐭💀🐩🪁🔰 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Thunderstag",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
                skills.Soaring,
                skills.Shield,
            ],
        ),
        description="high power and health, expensive to use, shielded, able to store resources, deadly, has potential to turn around a losing battle",
    ),
    # Vipertaur 💀🐭🐩🦔🔰 9p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Vipertaur",
            power=9,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description="high power and low health, able to cause instant death, fertile, shielded, spiny and underdog fighter",
    ),
    # Crystanther 🔰 3p 5h
    # costs: 👻👻👻👻👻 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Crystanther",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="low power and health, expensive in spirits, highly spirited, shielded",
    ),
    # Netchimera 💀🐭🦔 5p 1h
    # costs: 🔥 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Netchimera",
            power=5,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility, skills.Spines],
        ),
        description="moderate power, low health, causes instant death and fertility, spiny, not expensive to use",
    ),
    # Spiketale 🧺💀🪁 2p 7h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 29
    Blueprint(
        original=Card(
            name="Spiketale",
            power=2,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath, skills.Soaring],
        ),
        description="moderate power and high health, expensive in fire, packrat and soaring abilities, able to cause instant death",
    ),
    # Mysticore 🐩🔰💀🦔🧺 10p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Mysticore",
            power=10,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
                skills.Packrat,
            ],
        ),
        description="a magical creature with high power and health, costs a bit of fire and spirits, and has both fire and spirit attributes It is also skilled with underdog, shield, instant death, spines, and packrat",
    ),
    # Gryphonfly 🐭🚀🔰 8p 3h
    # costs: 🔥 has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Gryphonfly",
            power=8,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Airdefense, skills.Shield],
        ),
        description="a mythical creature that can fly and has air defense skill, and can create an impact with high power despite its smaller size He has moderate health and lower fire attribute, and costs a bit of fire to cast",
    ),
    # Ratking 💀🐩🧺 1p 6h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 29
    Blueprint(
        original=Card(
            name="Ratking",
            power=1,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Underdog, skills.Packrat],
        ),
        description="a fierce leader of underground armies, with low power and average health but an expert at underdog and packrat skills He costs a bit of fire but has a good spirit supply",
    ),
    # Fertilebacks 🐭🔰 1p 2h
    # costs: 🔥🔥🔥 has: 👻 pot: 17
    Blueprint(
        original=Card(
            name="Fertilebacks",
            power=1,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="a creature skilled at fertility and has shield skill, meaning it can protect itself and its pack with a good health supply He has a higher cost of fire to summon and no fire attribute, but still a valuable addition to a deck",
    ),
    # Flowhound 🐭 1p 5h
    # costs: 🔥🔥 has: 🔥👻 pot: 18
    Blueprint(
        original=Card(
            name="Flowhound",
            power=1,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="medium power, high health, expensive, fertility",
    ),
    # Timberwolf 🧺 4p 2h
    # costs: - has: 🔥👻👻 pot: 27
    Blueprint(
        original=Card(
            name="Timberwolf",
            power=4,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="high power, low health, high spirits and packrat skill",
    ),
    # Thornycat 🦔🧺💀🐭 9p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Thornycat",
            power=9,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="very high powerhealth, expensive, fireskillheavy",
    ),
    # Mistfrog  3p 1h
    # costs: 👻👻 has: 👻 pot: 6
    Blueprint(
        original=Card(
            name="Mistfrog",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="low powerhealth, expensive, high spirit and spiritcost",
    ),
    # Beetleback 🧺 2p 2h
    # costs: 👻👻 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Beetleback",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="lowmedium powerhealth, lowcost spirit, packrat skill",
    ),
    # Constrictor 💀🧺🦔🐭 8p 9h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Constrictor",
            power=8,
            health=9,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description="a large and powerful snake with instant death capability and strong packrat skills",
    ),
    # Skylark 🐭🔰🚀🪁 5p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Skylark",
            power=5,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[skills.Fertility, skills.Shield, skills.Airdefense, skills.Soaring],
        ),
        description="a bird that soars high and has air defense and soaring skills, with decent health stats",
    ),
    # Thornbird 🐭💀🦔 3p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Thornbird",
            power=3,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Fertility, skills.InstantDeath, skills.Spines],
        ),
        description="a small and spiky bird with instant death and spines skills, with high health stats",
    ),
    # Blazebeetle 🦔🔰🐭💀 7p 5h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Blazebeetle",
            power=7,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Spines,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="a fiery bug with spines and shield skills, with high power and low health stats",
    ),
    # Spinefury 🦔 6p 3h
    # costs: - has: 🔥👻👻👻 pot: 30
    Blueprint(
        original=Card(
            name="Spinefury",
            power=6,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description='This creature has relatively low power and health stats, but it does have Spines, which suggests a certain level of defensiveness Its spirits and fire stats are both relatively low, so the name should reflect that "Spinefury" plays off the "spines" skill, while also conveying a sense of urgency and intensity',
    ),
    # Flame 🔰 5p 5h
    # costs: 🔥 has: 👻👻👻 pot: 25
    Blueprint(
        original=Card(
            name="Flame",
            power=5,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Shield],
        ),
        description='turtle  This creature has moderate power and health, but its strength lies mainly in its defensive abilities  specifically, its Shield skill Given its fire stats, a name that plays off "flame" could be fitting "Flameturtle" suggests a creature that is both slow and steady, but also protected by a fiery shell',
    ),
    # Packthorn 🧺🐭🐩💀🦔🔰 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Packthorn",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description='With high power and health, Packthorn is definitely a threat on the battlefield It also has a range of skills, including Packrat, Fertility, and Underdog, that suggest a certain level of resourcefulness and adaptability The "thorn" in its name reinforces its power and danger, while the "pack" suggests a creature that works well with others',
    ),
    # Phoenixwing 🦔🪁🧺💀🐭🔰 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Phoenixwing",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Soaring,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description='With power and health at their maximums, this card is a force to be reckoned with The name ties in nicely with the two fire and spirit attributes at the top range of their allowed values, as well as the skills "Soaring" and "Fertility", which are reminiscent of a mythical bird reborn from its ashes, spreading its wings and rising above all competition',
    ),
    # Goatoble 🪁🐭💀🧺 9p 6h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Goatoble",
            power=9,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Soaring,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description='This card has high power, a decent health score and some skills, but it\'s hampered by its aboveaverage cost yellow fire number and uneven spirit score The name adequately reflects its ramlike disposition, while the "Instant Death" and "Fertility" skills are reminiscent of the oftenduplicitous nature of goats',
    ),
    # Zoomba 🚀💀🐩 3p 1h
    # costs: 🔥🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Zoomba",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Airdefense, skills.InstantDeath, skills.Underdog],
        ),
        description='This tiny chihuahua of a card brings little power, limited health, and a couple of tricks to the table, all at an aboveaverage cost As it turns out, the two fire cost makes it faster than it looks, and "Airdefense" and "Underdog" skill names are reflected in the name choice',
    ),
    # Bullpharoah 🔰🐭💀🦔🧺 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Bullpharoah",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Packrat,
            ],
        ),
        description="With a formidable score and a couple of defensive skills, this card is a leader on the battlefield however, it comes at a cost It has balanced spirit and fire attributes, although a bit shy of what's allowed, and a reasonable cost to both The name choice reflects its status as a powerful leader, with obvious references to the bull, and a nod to its powerful defense, evocative of pharaohs",
    ),
    # Blazepig 🔰🧺🐭🦔💀🚀 10p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Blazepig",
            power=10,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.Spines,
                skills.InstantDeath,
                skills.Airdefense,
            ],
        ),
        description="High power and less impressive health are the theme of this piggy card, with a cost that sits nicely in the middle The skill set is quite impressive, however, including Spines, Shield, Packrat, and Airdefense abilities The name is intended to reflect the spikes and the flame components, but also to lean somewhat into its piggish nature",
    ),
    # Luckfinch 🍀🔰 0p 1h
    # costs: 🔥 has: 🔥👻👻👻👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Luckfinch",
            power=0,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[skills.LuckyStrike, skills.Shield],
        ),
        description="low power, low health, high spirits, regenerative shield, a small, lucky bird",
    ),
    # Sky Guardian 🪁 8p 3h
    # costs: - has: 🔥 pot: 30
    Blueprint(
        original=Card(
            name="Sky Guardian",
            power=8,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="very powerful, low cost, flying",
    ),
    # Inferno Crab  2p 1h
    # costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 6
    Blueprint(
        original=Card(
            name="Inferno Crab",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[],
        ),
        description="low power, low health, high fire costs, moderate spirits, no skills",
    ),
    # Shell Shield 🔰 1p 3h
    # costs: 👻 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Shell Shield",
            power=1,
            health=3,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="low power, moderate health, no fire cost, high spirits, defensive skills",
    ),
    # Blossomice 🐭🔰💀🧺 10p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Blossomice",
            power=10,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="relates to its high Fertility skill The card has moderate power and health and requires little Fire or Spirits to play, making it readily accessible It also has a Shield skill, adding to the card's survivability The name 'Blossomice' is a play on words combining animal and nature elements",
    ),
    # Chimerafox 🐩🧺🐭🔰💀 5p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Chimerafox",
            power=5,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="relates to a fox with a combination of skills, including Fertility, Shield, and Packrat The card has high health and moderate power and requires little Fire or Spirits to play The Chimera is a hybrid creature of various animals, fit for this combination of skills The alliteration of both words creates a unique and memorable name",
    ),
    # Tortoistra 🔰 3p 2h
    # costs: - has: 🔥 pot: 24
    Blueprint(
        original=Card(
            name="Tortoistra",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="a combination of Tortoise and Maestro, relates to the shield attribute which indicates survival and the skill Shield The card has low power and health but also requires no Spirits to play, making it an easy and enduring lategame card The composer reference in the name adds some intelligence to the card",
    ),
    # DemonBull 💀 9p 4h
    # costs: 👻👻👻 has: 🔥🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="DemonBull",
            power=9,
            health=4,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath],
        ),
        description="relates to the high power attribute and the skill InstantDeath, which adds a demonic association to the bull theme The card requires some Spirits, making it more of a mid to lategame card, but it has Fire as its primary cost, which is cheap and easily accessible",
    ),
    # Armorsaur 🐭🐩🧺🦔🔰💀 9p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Armorsaur",
            power=9,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="relates to a dinosaur theme with high health and power, and the skills, Shield, Packrat, and Fertility, adding to its survivability and growth The card requires little Spirits to play, making it easily accessible, and Fire as a primary cost indicates its strength",
    ),
    # Krakenling 🐭💀🦔🐩🧺🔰 4p 5h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Krakenling",
            power=4,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Underdog,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="high health and packrat skills, yet balanced by the low fire and spirits cost The spines skill adds an ability to attack adjacent cards, as if a small, squishy tentacle were sticking out",
    ),
    # Spritelark 🦔🔰💀🧺🐭 4p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Spritelark",
            power=4,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="a mix between a sprite and a lark, very spirited, with some protection skills, yet with low fire and spirits costs A card that can fly and has a complex songlike attack, hitting all adjacent cards in a melodylike way",
    ),
    # Vipervox 🐩🦔 5p 3h
    # costs: 🔥🔥 has: 👻 pot: 19
    Blueprint(
        original=Card(
            name="Vipervox",
            power=5,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Underdog, skills.Spines],
        ),
        description="a sneaky, lowcost card with high power and spiny defense A small snake creature with the skill to surpriseattack with a barklike sound and retreat quickly, leaving the defender with spines",
    ),
    # Thornfury 🐩🧺🐭🔰 7p 4h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Thornfury",
            power=7,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Underdog, skills.Packrat, skills.Fertility, skills.Shield],
        ),
        description="a highly spirited card with a high power, highcost and protective skills It has the added ability to attack two times in a turn, at the cost of damaging itself",
    ),
    # Moltenbeak 💀🔰🚀🦔🧺🐭 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Moltenbeak",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Airdefense,
                skills.Spines,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="a highly offensive, high health, and nocost card with various skills The name incorporates a reference to the fire and skills for air defense, and a powerful beak attack",
    ),
    # FertilityCat 🔰🐭💀 2p 1h
    # costs: 🔥 has: 🔥👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="FertilityCat",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="a card with average health and decent attack power, capable of breeding new cards and populating the field with multiple units to overpower opponents, also has the ability to instantly kill opposing cards",
    ),
    # PackWyvern 🐭💀🧺🔰 7p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="PackWyvern",
            power=7,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="a formidable card with high health and strong attack, also has several skills like Fertility, InstantDeath and Shield that makes it the leader of the pack, symbolizing a loyal and powerful dragon",
    ),
    # AirSpine 🐭💀🚀🦔 8p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="AirSpine",
            power=8,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Spines,
            ],
        ),
        description="a versatile card with high attack and defense power, has skills that can make it a powerful flying force on the battlefield, yet spines that provide great defense when under attack, symbolizing a deadly air defense unit",
    ),
    # Packratling 💀🧺🐭 4p 3h
    # costs: 👻 has: 🔥👻 pot: 32
    Blueprint(
        original=Card(
            name="Packratling",
            power=4,
            health=3,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Packrat, skills.Fertility],
        ),
        description="a small card with low power but decent health and skills like Fertility and Packrat, that allows it to breed and store greater units, symbolizing a sneaky and resourceful creature",
    ),
    # Furylynx 🧺💀🔰🦔🐭 7p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="Furylynx",
            power=7,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description='This card has high power and health, as well as multiple skills to take down opponents The name combines "fury" to represent its high power and "lynx" to represent its agility and skill',
    ),
    # Sproutfox 🐭 4p 1h
    # costs: 👻 has: 🔥🔥👻👻 pot: 19
    Blueprint(
        original=Card(
            name="Sproutfox",
            power=4,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description='This card has moderate power, low health, and only one skill, but it has high spirit and low fire costs The name combines "sprout" to represent its low cost and "fox" to represent its agility',
    ),
    # Deathscreech 💀 4p 5h
    # costs: 👻👻👻 has: 🔥🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Deathscreech",
            power=4,
            health=5,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath],
        ),
        description='This card has moderate power and high health, with a high spirit cost and a single skill to take out opponents The name combines "death" to represent its instant death skill and "screech" to represent its ferocity',
    ),
    # Shieldedspine 🐭🔰🐩🦔🧺💀 5p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Shieldedspine",
            power=5,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.Spines,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description='This card has high power and health, moderate fire costs, and multiple skills to protect itself and take down opponents The name combines "shielded" to represent its skills to protect itself and "spine" to represent its spines skill and general toughness',
    ),
    # Armogator 🧺 6p 4h
    # costs: 🔥🔥 has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Armogator",
            power=6,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description='This card has high power and moderate health, with a moderate fire cost and a single skill to protect itself The name combines "armor" to represent its protection and "gator" to represent its toughness',
    ),
    # Flamebug 🔰 2p 1h
    # costs: 🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Flamebug",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="This card has moderate power and low health, costs low fire resource and has a skill Shield, so it feels like an offensive card that has a defense mechanism The name Flamebug is related to its fire attribute and small size, making it more likely for players to underestimate its potential",
    ),
    # Fertilecat 🐭 5p 4h
    # costs: 🔥 has: 🔥👻 pot: 24
    Blueprint(
        original=Card(
            name="Fertilecat",
            power=5,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="This card has high power and health, costs low fire resource, and has a Fertility skill, which suggests it fights together with more allies The name Fertilecat plays into the high health and strength of the card, while the cat part suggests that it's a fastmoving and aggressive card",
    ),
    # Nightox 🐭🔰🐩🍀🧺🪁 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Nightox",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.LuckyStrike,
                skills.Packrat,
                skills.Soaring,
            ],
        ),
        description="high powerhealth, highly spirited, skillful and lucky",
    ),
    # Thornlynx 🐭🔰🦔💀 2p 4h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Thornlynx",
            power=2,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Spines,
                skills.InstantDeath,
            ],
        ),
        description="low power but spines, balanced health, spirited",
    ),
    # Flamegorilla 💀🧺🐭🔰 4p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Flamegorilla",
            power=4,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="high health, moderately high power, somewhat costly, elusive",
    ),
    # Skybear 🔰🐭🪁🦔 6p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Skybear",
            power=6,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[skills.Shield, skills.Fertility, skills.Soaring, skills.Spines],
        ),
        description="strong and spirited, great for defense, able to soar",
    ),
    # Shadowarmadillo 🔰🧺💀🐭 0p 4h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 33
    Blueprint(
        original=Card(
            name="Shadowarmadillo",
            power=0,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="low power and health, shielded and sneaky",
    ),
    # Fangedrake 🧺🔰🐭💀🦔 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Fangedrake",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="powerful, high health, spines, pack rat, shield, fertility, instant death",
    ),
    # Embersnail 🔰🧺💀🐭 2p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 31
    Blueprint(
        original=Card(
            name="Embersnail",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="low powerhealth, expensive fire cost, no spirits, shield, pack rat, instant death, fertility",
    ),
    # Thunderwolf 💀🧺🔰🦔🐭🍀 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Thunderwolf",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Spines,
                skills.Fertility,
                skills.LuckyStrike,
            ],
        ),
        description="very strong, high spirits and fire, pack rat, shield, spines, fertility, instant death, lucky strike",
    ),
    # Cloudcat 🐩🐭🔰🪁 7p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Cloudcat",
            power=7,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Underdog, skills.Fertility, skills.Shield, skills.Soaring],
        ),
        description="related to its high fire and spirit cost, with soaring skill and an underdog skill, this catlike creature could be a rare breed that lives on clouds",
    ),
    # Serpentowl 💀🦔🔰🐭🧺🪁 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Serpentowl",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Spines,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
            ],
        ),
        description="a creature with high health and power, instant death and spines skills, that resembles an owl with serpentlike features",
    ),
    # Driftoad 🧺💀🔰 8p 2h
    # costs: 👻👻👻 has: 👻 pot: 33
    Blueprint(
        original=Card(
            name="Driftoad",
            power=8,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat, skills.InstantDeath, skills.Shield],
        ),
        description="a small creature with just enough spirit power for some packrat and shield skills, that can drift with the wind, but becomes quite weak without the spirits",
    ),
    # Flametalon 💀🧺🔰🐭🪁🐩 10p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 81
    Blueprint(
        original=Card(
            name="Flametalon",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.Soaring,
                skills.Underdog,
            ],
        ),
        description="a very strong creature with high attack and health, fiery in both its appearance and skills, and with some incredible agility in the air",
    ),
    # Soulshark 🔰🧺💀🐩🦔🐭 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Soulshark",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Underdog,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description="powerful, high health, highly spirited, defensive skills",
    ),
    # Faejaguar 🐭🧺💀🔰🪁 6p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Faejaguar",
            power=6,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
                skills.Soaring,
            ],
        ),
        description="powerful, high health, highly spirited, fertility, soaring",
    ),
    # Ironant  2p 1h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻 pot: 6
    Blueprint(
        original=Card(
            name="Ironant",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[],
        ),
        description="low powerhealth, costly, firebased, no skills",
    ),
    # Gorgontaur 🧺🐭🔰💀 7p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 60
    Blueprint(
        original=Card(
            name="Gorgontaur",
            power=7,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="powerful, high health, medium cost, packrat, defensive skills",
    ),
    # Shadowstag 🔰🐭💀🧺🪁🦔 9p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Shadowstag",
            power=9,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Soaring,
                skills.Spines,
            ],
        ),
        description="The card's high power and health make it a formidable foe, while its skills Shield, Fertility, Packrat create a versatile, capable opponent The name Shadowstag reflects its combination of power and stealth, making it an elusive and dangerous creature",
    ),
    # Boltbat 🐭💀🦔🔰🧺 4p 4h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Boltbat",
            power=4,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="The card's moderate stats and skills Fertility, Instant Death, Spines, Shield, Packrat make it a good allaround choice The name Boltbat reflects both its lightningquick attacks and its ability to strike fear into its prey, fitting for a creature with such versatile skills",
    ),
    # Vortexowl 🐭🔰 7p 3h
    # costs: 🔥 has: 🔥👻👻 pot: 33
    Blueprint(
        original=Card(
            name="Vortexowl",
            power=7,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="The card's high power and low health, combined with skills in Fertility and Shield, suggest a creature that is more strategic than allout berserker The name Vortexowl implies a bird of prey that can use gusts of wind to its advantage, while also having a wise and strategic mind",
    ),
    # Flametortoise  1p 7h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Flametortoise",
            power=1,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="With low power and high health, the flametortoise is a defensive creature The card's skills are quite limited and the cost of fire is relatively high, but the health of the flametortoise makes it durable The name Flametortoise suggests a creature that is hotheaded and battlehardened, able to withstand flames and continue the fight",
    ),
    # Thornferret 🐭🦔 3p 2h
    # costs: 🔥 has: 🔥👻 pot: 20
    Blueprint(
        original=Card(
            name="Thornferret",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Spines],
        ),
        description="The card's relatively low power and health, combined with skills in Fertility and Spines, suggest a quick and nimble creature that relies on its agility and cunning The name Thornferret evokes a small creature that is both ferocious and sneaky, a perfect fit for this card's ability to deal damage from unexpected angles",
    ),
    # Fatesteed 💀🧺🐭 5p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Fatesteed",
            power=5,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[skills.InstantDeath, skills.Packrat, skills.Fertility],
        ),
        description="mix of fieryspritely, high powerhealth",
    ),
    # Runehound 🧺🐭💀 3p 3h
    # costs: 🔥 has: 🔥👻👻👻👻👻👻👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Runehound",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=1,
            skills=[skills.Packrat, skills.Fertility, skills.InstantDeath],
        ),
        description="fast and versatile, packratlike abilities, mid powerhealth",
    ),
    # Armoredrake 💀🐭🧺🔰🦔 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="Armoredrake",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="high healthspines, shield skill, expensive",
    ),
    # Infernafox 🐭🔰💀 7p 5h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Infernafox",
            power=7,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="high power, fiery abilities, mid health",
    ),
    # Furyfer 💀🐭🔰🧺🐩🦔 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Furyfer",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="powerful, spirited, skilled",
    ),
    # Spiritcat 🐭🧺🔰💀🦔 10p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Spiritcat",
            power=10,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="powerful, low health, very skilled",
    ),
    # Wingfox 🐭 4p 2h
    # costs: 🔥 has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Wingfox",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="low powerhealth, flight ability",
    ),
    # Underdogon 🐭🐩💀🚀🧺 2p 10h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Underdogon",
            power=2,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Packrat,
            ],
        ),
        description="high health, low power, underdog ability",
    ),
    # Armorphant 🔰🐩💀🐭 5p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Armorphant",
            power=5,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="balanced, defensive, underdog ability",
    ),
    # Thundercow 💀🐭🔰 1p 7h
    # costs: 🔥🔥🔥 has: 🔥👻👻 pot: 34
    Blueprint(
        original=Card(
            name="Thundercow",
            power=1,
            health=7,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility, skills.Shield],
        ),
        description="high health, high costs, Shield",
    ),
    # Arcticowl  1p 2h
    # costs: 🔥 has: 🔥👻👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Arcticowl",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[],
        ),
        description="low powerhealth, high spirits, ice attribute",
    ),
    # Deathmoth 💀 1p 2h
    # costs: 👻 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Deathmoth",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="low costs, InstantDeath skill",
    ),
    # Spiritpack 💀🔰🐭🧺 8p 9h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Spiritpack",
            power=8,
            health=9,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="high powerhealth, high cost, Packrat skill",
    ),
    # Flamehorn 🧺🐭💀🔰🦔 10p 10h
    # costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Flamehorn",
            power=10,
            health=10,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="very strong, high powerhealth, no ice attribute, Spines skill",
    ),
    # Skywyrm 🪁💀🔰🐭🧺 9p 8h
    # costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Skywyrm",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Soaring,
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="Skywyrms are known to have high health and power, and the ability to fly through the air with ease Soaring skill The InstantDeath skill implies a dangerous aspect, which we can relate with the fire attribute that this card does not have, and the fire and spirits abilities for costavailability can indicate it's a creature that's difficult to obtain and control, similar to a dragon",
    ),
    # Emberlynx 🐭 5p 5h
    # costs: 🔥 has: 🔥👻👻 pot: 27
    Blueprint(
        original=Card(
            name="Emberlynx",
            power=5,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="The balance of the health and power stats of this card is reflected in a name that captures both aspects The Fertility skill suggests the creature is quick to breed, so bring lots of little ones with them  Fire and  Spirit cost",
    ),
    # Shieldonix 🔰🧺💀🐭 5p 6h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Shieldonix",
            power=5,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="The Shield skill is an important characteristic for this card, and as a creature with high health and power, it can be related to a shield being solid and sturdy The Packrat skill refers to a tendency to hoard items or resources, and as such, Shieldonix should be related to an armadillo or a creature with armor scales",
    ),
    # Grimshark 💀🔰🧺🐭 9p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Grimshark",
            power=9,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="Grimshark is a creature known to have very high power and health, which makes it a formidable beast InstantDeath and Shield skills are related to a defensive creature that can also deal a lot of damage The cost and availability of this card will be higher than average, so a name that implies rarity, and menacing qualities can fit well here",
    ),
    # Thornhog 🧺🔰🐭 6p 9h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Thornhog",
            power=6,
            health=9,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="With its high health and the Packrat, Shield and Fertility skills, Thornhog is a tough creature with spiky attributes that produces offspring quickly and enjoys collecting items The  Fire cost suggests an animal that is more imbued with fire attributes",
    ),
    # Spiritcrag 🐩🔰🧺💀🐭🦔 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Spiritcrag",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="high powerhealthspiritfire, multiple skills",
    ),
    # Sunweasel 💀 1p 2h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Sunweasel",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="low powerhealth, high fire cost, instant death skill",
    ),
    # Thornsprite 🦔 2p 2h
    # costs: 🔥 has: 🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Thornsprite",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description="low powerhealth, low cost, spines skill",
    ),
    # Phoenixspark 🐩🪁💀🔰🐭🧺 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Phoenixspark",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.Soaring,
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="very strong, high spiritfire, multiple skills",
    ),
    # Lifedrake 🐭🔰🧺💀 7p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Lifedrake",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="A fierce, strong and valuable dragon with high power and health attributes It is costly to put on the board and requires both fire and spirits, denoted by its attribute values The many skills it possesses give it additional advantages, like Packrat and InstantDeath, both of which suggest its power to amass items and wipe out opponents",
    ),
    # Glimmerlynx 💀🔰🧺🐭 5p 4h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Glimmerlynx",
            power=5,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="A fantastical lynx with a coat that glimmers in various colors Its power and health attributes are above average, denoted by its attribute values, and are complemented by a variety of skills Its inclusion of InstantDeath and Shield skills speaks to its overall cleverness and fighting prowess in battle",
    ),
    # Soaringphoenix 🪁💀🔰🐭🐩 9p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Soaringphoenix",
            power=9,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Soaring,
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="A majestic and highly valuable bird that costs no fire to put on the board and has high spirit requirements Its power and health attributes are very strong and suggest the bird's overall strength, making it hard to defeat Its multiple skills, including Soaring, suggest its ability to rise above opponents and avoid attacks while delivering powerful blows",
    ),
    # Fertilemole 🐭💀🧺 2p 6h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Fertilemole",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="A cute and furry animal that has very low offensive attributes but high health, denoting it is harder to defeat It requires few resources to put on the board and has skills that suggest its value in creating new allies Fertility, while still possessing enough defensive capabilities to be a useful ally in battle with its InstantDeath and Packrat skills",
    ),
    # Flamebeast 💀🐭🪁🐩🔰 5p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Flamebeast",
            power=5,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Soaring,
                skills.Underdog,
                skills.Shield,
            ],
        ),
        description="A fearsome, firebased creature that has high health and aboveaverage power It has a range of highpowered skills that make it a tough opponent, such as InstantDeath and Soaring, as well as Underdog which suggests it can still fight well even if its power or health is reduced The lack of fire cost to play this card and the high spirits requirement suggest that it is not only powerful but highly valuable",
    ),
    # Gorgonite 💀🧺 8p 2h
    # costs: 🔥 has: 🔥👻 pot: 29
    Blueprint(
        original=Card(
            name="Gorgonite",
            power=8,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="very powerful, but low health Instant Death and Packrat skills suggest an almost mythical warriorassassinlike persona",
    ),
    # Dream Ferret  0p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 5
    Blueprint(
        original=Card(
            name="Dream Ferret",
            power=0,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="weak and cheap, but highly spirited The name is a nod to the magical or ethereal quality of the card",
    ),
    # Skitterbat 🐭💀🔰 2p 1h
    # costs: 🔥🔥 has: 🔥 pot: 24
    Blueprint(
        original=Card(
            name="Skitterbat",
            power=2,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="low power and health, only has fire The Fertility, Instant Death and Shield skills suggest a creature with a lot of personality and agility",
    ),
    # Luminorm 🧺💀🐭🔰 4p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Luminorm",
            power=4,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="strong, with high spirits and fire but no spirit costs The Packrat, Instant Death, Fertility and Shield skills suggest a creature with a lot of skills and adaptability The name is a nod to the bright and shimmering quality of the card",
    ),
    # Mystique 🔰🐭 4p 5h
    # costs: - has: 🔥🔥👻 pot: 41
    Blueprint(
        original=Card(
            name="Mystique",
            power=4,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="mysterious, high health, protective and fertile",
    ),
    # Thunderclaw 🧺🔰🚀 7p 5h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Thunderclaw",
            power=7,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.Packrat, skills.Shield, skills.Airdefense],
        ),
        description="powerful, highly spirited, pack animal, air defender",
    ),
    # Spikewhip 🧺🔰🐭💀 3p 5h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Spikewhip",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="dangerous, spikey, spiny, instant killer",
    ),
    # Thornback 🧺🔰🦔🐩 3p 4h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Thornback",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[skills.Packrat, skills.Shield, skills.Spines, skills.Underdog],
        ),
        description="spiny underdog, high spirited, shielded, nimble",
    ),
    # Hellfire 🐩💀🔰 5p 1h
    # costs: 🔥🔥🔥🔥 has: 🔥 pot: 23
    Blueprint(
        original=Card(
            name="Hellfire",
            power=5,
            health=1,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Underdog, skills.InstantDeath, skills.Shield],
        ),
        description="expensive, low health, fiery, underdog",
    ),
    # Cragbison 🔰🧺🐭 3p 6h
    # costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Cragbison",
            power=3,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[skills.Shield, skills.Packrat, skills.Fertility],
        ),
        description="a powerful, tough animal with a shield skill and fertility power",
    ),
    # Fateserpent 💀🐭🔰🧺 8p 7h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 60
    Blueprint(
        original=Card(
            name="Fateserpent",
            power=8,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="a strong creature with instantdeath and protection skills",
    ),
    # Soarspine 🐭🪁💀🦔🔰🧺 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Soarspine",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Soaring,
                skills.InstantDeath,
                skills.Spines,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="an animal with a very high health, soaring, and spines skills",
    ),
    # Voodoomonkey 🐭💀 6p 5h
    # costs: - has: 🔥🔥👻👻👻👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Voodoomonkey",
            power=6,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="has a fertility skill to summon minions and instantdeath skill to eliminate enemies",
    ),
    # Wraithound 🧺🔰💀 2p 2h
    # costs: - has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Wraithound",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat, skills.Shield, skills.InstantDeath],
        ),
        description='a combination of "wraith" instant death skill and "hound" packrat and shield skills that represents this card with all these skills',
    ),
    # Rockrhino  3p 5h
    # costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Rockrhino",
            power=3,
            health=5,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description='a rhino that is big and tough, with high defense against attacks Hence, "rock" represents its sturdiness and unyielding nature',
    ),
    # Glimmagecko 🐭💀🧺🔰 8p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Glimmagecko",
            power=8,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description='a mix of "glimmer" referring to Fertility, Instant Death, and Packrat skills and "gecko" relevant because of the high spirit attribute, representing a small, but cunning creature with solid abilities',
    ),
    # Glimmertusk 🚀🧺 3p 5h
    # costs: 🔥 has: - pot: 19
    Blueprint(
        original=Card(
            name="Glimmertusk",
            power=3,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Airdefense, skills.Packrat],
        ),
        description="A fantastical creature with tough, glittering skin, able to defend itself from air attacks and carry treasure",
    ),
    # Solarhare 🐭🔰🐩 8p 6h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Solarhare",
            power=8,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield, skills.Underdog],
        ),
        description="A rabbitlike creature that draws on the power of the sun and has the ability to create shields, particularly deadly to larger creatures with the underdog skill",
    ),
    # Pyroboa 💀🔰🐭 3p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Pyroboa",
            power=3,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="A fiery, snakelike creature that can bring instant death and increase fertility",
    ),
    # Fabledox 🐩🐭🔰 8p 2h
    # costs: 👻👻 has: 🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Fabledox",
            power=8,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog, skills.Fertility, skills.Shield],
        ),
        description="A small but powerful creature with a mix of fire and spirit attributes, skilled in underdog attacks and shielded by its high health",
    ),
    # Glimmershrew 🧺🔰🐭 3p 4h
    # costs: 🔥 has: 🔥🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Glimmershrew",
            power=3,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="A small, nimble creature with glimmering fur that reflects its low costs and packs a lot of skills The name 'shrew' also reflects its low health",
    ),
    # Thunderbeast 💀🦔🧺🐭🔰🚀 9p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Thunderbeast",
            power=9,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Spines,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.Airdefense,
            ],
        ),
        description="A powerful creature with high power and health, and a skillset that strikes fear into opponents The name reflects its thunderous nature and beastly abilities",
    ),
    # Emberdillo 🔰 4p 3h
    # costs: 🔥 has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Emberdillo",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="A resilient creature with a skill that shields it from attacks Its name reflects its association with fire, as well as its armored nature",
    ),
    # Wisptail 🐭🧺🔰 4p 8h
    # costs: 👻👻👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Wisptail",
            power=4,
            health=8,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=5,
            has_fire=5,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="A highly spirited creature with a skillset that focuses on packbuilding and defense The name reflects its intangible nature and the agility of its tail",
    ),
    # Thornhorn 🔰 5p 1h
    # costs: 👻 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Thornhorn",
            power=5,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="A creature with high power but low health, and a skill that shields it from attacks Its name reflects its tough, pointy exterior",
    ),
    # Glacibear 🐭🧺 8p 4h
    # costs: 🔥 has: 🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Glacibear",
            power=8,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description='the name comes from "glacier" and "bear", which suggests a powerful and resilient animal, fitting for a card with high power and health',
    ),
    # Sylphwing 🧺🐭🔰💀🐩 7p 10h
    # costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Sylphwing",
            power=7,
            health=10,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description='the name comes from "sylph", a nimble and airy creature, and "wing", which suggests freedom and power These qualities evoke the high spirits and health of this card, as well as useful skills like Fertility and Shield',
    ),
    # Nymphox 🐭 0p 1h
    # costs: 👻👻👻 has: 🔥🔥👻👻 pot: 10
    Blueprint(
        original=Card(
            name="Nymphox",
            power=0,
            health=1,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="high spirit, low health, fertility skill",
    ),
    # Phoenixrat 🔰🧺🐭 2p 5h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Phoenixrat",
            power=2,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat, skills.Fertility],
        ),
        description="medium powerhealth, low cost of fire, packrat skill",
    ),
    # Skywyvern 🐭🚀💀🔰🐩 9p 9h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Skywyvern",
            power=9,
            health=9,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Airdefense,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="very strong, high spiritfire, air defense and instant death skill",
    ),
    # Shadowpan 🐭🦔🔰💀🐩 6p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Shadowpan",
            power=6,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="related to the high power and multiple skills, evoking an image of a dark, powerful beast",
    ),
    # Faefer 💀🐭🔰🧺🐩 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Faefer",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description='a combination of "fae" related to the skill "Fertility" and "ferret" related to the small, quick, skilled character of the card',
    ),
    # Flametle 🧺🐭🔰 4p 3h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 34
    Blueprint(
        original=Card(
            name="Flametle",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Packrat, skills.Fertility, skills.Shield],
        ),
        description='a combination of "flame" related to the fire attributes and "beetle" related to the shield skill, evoking an image of a small but fiery and resilient creature',
    ),
    # Phoenixogre 🔰🐩💀🐭🦔 6p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Phoenixogre",
            power=6,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="This card has high stats across the board, making it a powerful play The skills it possesses are Shield, Underdog, InstantDeath, Fertility, and Spines The name Phoenixogre combines two mythical creatures known for their strength and resilience, suggesting a card that is both powerful and resilient",
    ),
    # Pixiecat 🐩 3p 2h
    # costs: - has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Pixiecat",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog],
        ),
        description="This card has moderate stats but possesses the Underdog skill, making it a capable fighter The Pixie part of the name speaks to the card's skill, which implies that it can pull off unexpected victories The cat part is a nod to the animal theme of the game",
    ),
    # Mermaidon 🔰💀 4p 7h
    # costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Mermaidon",
            power=4,
            health=7,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Shield, skills.InstantDeath],
        ),
        description="This card has relatively low stats but possesses the skills Shield and InstantDeath The name Mermaidon combines two words, Mermaid and Don, a nod to the card's defensive nature since mermaids are associated with water and water generally puts out fire and its ability to get rid of an opponent's card instantly since a don is a university professor and often seen as an authority figure",
    ),
    # Flamemongoose 💀🧺🐭🔰 4p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Flamemongoose",
            power=4,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="This card has strong attack stats and skills that include InstantDeath, Packrat, Fertility, and Shield The name Flamemongoose combines two seemingly conflicting elements  fire and an animal that lives predominantly underground  to create a sense of unexpectedness and surprise, which matches the different skills on the card",
    ),
    # Glimmerturtle 🐭🧺🔰 2p 3h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Glimmerturtle",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="This card has decent stats all around but is particularly balanced, with the same amount of spirits and fire Its skills include Fertility, Packrat, and Shield, which can help it play a supportive role on the battlefield The name Glimmerturtle reflects its balanced nature and also hints at its ability to shield and gather resources",
    ),
    # Sunmouse  1p 1h
    # costs: 🔥 has: 👻👻 pot: 4
    Blueprint(
        original=Card(
            name="Sunmouse",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description="This card has a low power and health, but is cheap to summon and only requires one fire to do so It also has a couple of slots for skills The name Sunmouse reflects its fiery attribute and also hints at its small size and agility",
    ),
    # Sunbear 🐭 10p 8h
    # costs: 👻👻 has: 🔥🔥👻 pot: 40
    Blueprint(
        original=Card(
            name="Sunbear",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description='With a power of  and health of , this bear is a strong performer for a low cost Its fiery attribute combined with the "Fertility" skill led to the creation of a bear that is associated with the warmth and energy of the sun',
    ),
    # Molemite  1p 1h
    # costs: 🔥 has: 🔥👻 pot: 4
    Blueprint(
        original=Card(
            name="Molemite",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description='With its small size and average attributes, this card is a basic mole creature with no skills The card was named after a combination of the words "mole" and "dynamite" to give it a more memorable and unique name that fits its explosive potential',
    ),
    # Shieldfin 🐩🦔🐭🔰🧺💀 10p 9h
    # costs: 👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Shieldfin",
            power=10,
            health=9,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.Spines,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="With a high spirit attribute and multiple skills, this card has a variety of unique abilities It is named for its physical appearance, which resembles a fish with armor plating that can defend itself against attacks Its high spirit score further emphasizes its powerful defense",
    ),
    # Flamelete 🐭🧺💀🔰 2p 1h
    # costs: 👻 has: 🔥👻 pot: 31
    Blueprint(
        original=Card(
            name="Flamelete",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description='With both "Fertility" and "InstantDeath" skills and attributes that lean heavily towards the element of fire, the name Flamelete came naturally The card represents a small but powerful creature with the potential to explode at any moment, making it a dangerous opponent for any player',
    ),
    # Windwyrm 🧺🚀🪁 10p 9h
    # costs: 👻 has: 🔥🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Windwyrm",
            power=10,
            health=9,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.Airdefense, skills.Soaring],
        ),
        description="With high power and health, but low spirit and fire, this card's name captures its dominance over the skies and its agility in battle thanks to its Air Defense and Soaring skills, making it hard to bring down",
    ),
    # Furyfox  6p 1h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Furyfox",
            power=6,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="This animal name fits well with the card's high power and low health, but is also associated with agility and quick attacks The card's fire cost and fire property is also reflected in the fox's fiery nature",
    ),
    # Shieldserpent 🐭🧺🔰🚀💀🐩 7p 8h
    # costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Shieldserpent",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
                skills.Airdefense,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="This animal name combines the card's high power, low spirit and high health, which is reflective of the serpent's strong and tough nature Its Shield and Underdog skills also make it particularly hard to defeat",
    ),
    # Krystaur 💀🐭 3p 2h
    # costs: 👻👻 has: 🔥🔥👻 pot: 23
    Blueprint(
        original=Card(
            name="Krystaur",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="related to crystal, spiritual, costly, deadly",
    ),
    # Packdragon 🐭🧺🪁💀🦔🔰 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Packdragon",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.InstantDeath,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description="powerful, expensive, versatile, many skills",
    ),
    # Shieldwolf 🔰🐩💀🧺🐭 4p 3h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Shieldwolf",
            power=4,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="defensive, affordable, skilled, underdog",
    ),
    # Ratwizard  2p 2h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Ratwizard",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="low powerhealth and high cost with no skills, but with a trick up the sleeve",
    ),
    # Phoenixfury 🔰🐩🧺💀🐭 10p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Phoenixfury",
            power=10,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="The card has high power and health, making it almost unbeatable It also has some of the most valuable and expensive attributes, namely fire and spirits The card has a range of skills including Shield and Packrat that enhance and protect its abilities and InstantDeath that makes it a formidable opponent All these attributes combined create an almost indestructible creature, mythical in power and terror, hence the name Phoenixfury",
    ),
    # Thornosaur 🧺🦔💀🐭 7p 1h
    # costs: 🔥🔥 has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Thornosaur",
            power=7,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Packrat,
                skills.Spines,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="The card has a midrange power and low health, but high fire cost and low spirit cost It has a few skills including Spines and InstantDeath, which go well with the name Overall, the card feels like a creature cobbled together from various mythical beasts dinosaur, thorny dragon, able to rapidly kill enemies with its spikes",
    ),
    # Snowtress 💀🐩🐭🧺 4p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Snowtress",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="The card has a moderately low power and health, but is relatively cheap and has a decent amount of spirits and fire It has a range of skills, notably InstantDeath, Underdog, and Fertility The name Snowtress comes from the idea of a graceful and mystical creature with a cold and ruthless heart, capable of defending and attacking with equal ferocity",
    ),
    # Moonhare 🐭 2p 5h
    # costs: 🔥 has: 🔥🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Moonhare",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="high health, slightly costly, fertility skill",
    ),
    # Scuttler 🧺 1p 1h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Scuttler",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="low powerhealth, packrat skill, spirited",
    ),
    # Skywing 🪁 3p 2h
    # costs: - has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Skywing",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Soaring],
        ),
        description="soaring skill, fire attribute, lowcost",
    ),
    # Spikemander 🦔🐭 2p 6h
    # costs: - has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Spikemander",
            power=2,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines, skills.Fertility],
        ),
        description="high health, spines skill, slightly costly",
    ),
    # Nightowl 🐭🐩 2p 4h
    # costs: - has: 👻👻👻👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Nightowl",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=0,
            skills=[skills.Fertility, skills.Underdog],
        ),
        description="a creature of the night, with medium power and health, and the skills Fertility and Underdog fitting for an underrated creature",
    ),
    # Mantistar 🐭🔰🧺💀 2p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Mantistar",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="a small creature with medium health and power, but unique skills Shield, Fertility, InstantDeath that give it a distinguishing character the name relates to its mix of different skills",
    ),
    # Spiketusk 🦔💀🐭 3p 8h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Spiketusk",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Spines, skills.InstantDeath, skills.Fertility],
        ),
        description="a strong and spiky creature with high health and the skills Spines and Fertility the name relates to its spiky appearance",
    ),
    # Shieldox 🐭🔰🧺🦔 4p 7h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Shieldox",
            power=4,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Fertility, skills.Shield, skills.Packrat, skills.Spines],
        ),
        description="a defensive card with average power and high health, and powerful skills such as Shield and Packrat the name relates to its strong defense capabilities",
    ),
    # Springhare 🐭 1p 1h
    # costs: 🔥 has: 👻 pot: 11
    Blueprint(
        original=Card(
            name="Springhare",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="this card has attributes that make it a support card with the skill Fertility, a cost structure that is inexpensive, and fairly balanced powerhealth points",
    ),
    # Hedgewisp 🐭🔰🦔🧺 4p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Hedgewisp",
            power=4,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Fertility, skills.Shield, skills.Spines, skills.Packrat],
        ),
        description="this card has balanced attributes and cost structure, but a range of skills that make it not only hard to kill, but able to support its allies while attacking",
    ),
    # Thunderfury 🐭💀🦔🐩🧺🔰 6p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Thunderfury",
            power=6,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Underdog,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="this card is a strong allaround character with multiple skills, fairly high cost, and highly balanced attributes",
    ),
    # Shieldagon 🔰 3p 7h
    # costs: - has: 🔥👻 pot: 34
    Blueprint(
        original=Card(
            name="Shieldagon",
            power=3,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="this card's strong shield and health can make it exceptionally difficult to attack in battle, and the name 'Shieldagon' plays up this concept of a shieldlike creature",
    ),
    # Baneviper 🔰🐭💀 2p 4h
    # costs: - has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Baneviper",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="relatively high power and health, instant death skill, relatively high fire and spirits, no costs",
    ),
    # Thunderhawk 💀🐭🔰 9p 4h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Thunderhawk",
            power=9,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility, skills.Shield],
        ),
        description="high power, relatively high spirits, instant death skill, fire cost",
    ),
    # Shadowwolf 🐩🔰💀🐭 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Shadowwolf",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="relatively high health, shield skill, underdog skill, relatively high fire and spirits, no fire cost",
    ),
    # Blazeferret 🐭🧺🪁 9p 3h
    # costs: 👻 has: 🔥🔥👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Blazeferret",
            power=9,
            health=3,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.Soaring],
        ),
        description='This name combines "blaze" to represent the strong attack power and "ferret" to represent the small, quick nature of the card',
    ),
    # Skyrider 🔰🧺 1p 2h
    # costs: - has: 🔥👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Skyrider",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat],
        ),
        description='"Sky" represents the card\'s fire attribute and the fact that it has no spirit costs, while "rider" suggests that the card accompanies and defends its owner',
    ),
    # Tombat  1p 3h
    # costs: - has: 🔥 pot: 16
    Blueprint(
        original=Card(
            name="Tombat",
            power=1,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description='This name fuses "tom" from "tomcat" with "bat" to suggest the card\'s low stats and lack of skills',
    ),
    # Earthwing 🧺🔰🐭 4p 2h
    # costs: 🔥 has: 👻👻👻 pot: 31
    Blueprint(
        original=Card(
            name="Earthwing",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="With a balance of power and health, Earthwing is a strong and versatile creature Its packrat like tendencies make it a valuable addition to any deck, and its shield gives it an added layer of defense However, its fertility skill means it must be approached with caution, as it can quickly multiply and overwhelm opponents",
    ),
    # Empressbee 🔰🐭💀 4p 7h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Empressbee",
            power=4,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="high power and health, no fire cost, lots of spirits, skills related to shielding, fertility, and instant death Empressbee suggests a powerful and regal queen of the bees, with the ability to protect and nurture her hive while also wielding deadly stingers",
    ),
    # Wyverngoose 🐩💀🐭🧺 5p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Wyverngoose",
            power=5,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="very high power and health, moderate fire cost, lots of spirits, skills related to being an underdog, instant death, fertility, and packratting Wyverngoose sounds like a formidable and unusual creature, with the strength and cunning to overcome even the toughest of opponents",
    ),
    # Grasshopper 🐩🧺 2p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Grasshopper",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog, skills.Packrat],
        ),
        description="low power and health, low fire cost, moderate spirits, skills related to being an underdog and packratting Grasshopper suggests a nimble and agile creature that can hop quickly out of danger and gather resources efficiently",
    ),
    # Mysticbear 🧺🐭🐩🔰 3p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Mysticbear",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Underdog, skills.Shield],
        ),
        description="strong health and power, high fire cost, medium spirit cost, abilities suggest paranormal attributes",
    ),
    # Faeblin 🧺 0p 3h
    # costs: 🔥🔥 has: 🔥👻👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Faeblin",
            power=0,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="low powerhealth, high fire cost, medium spirit cost, Packrat skill suggests small stature and love for gathering",
    ),
    # Thornmaw 🐭🐩🔰🧺🦔 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Thornmaw",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.Shield,
                skills.Packrat,
                skills.Spines,
            ],
        ),
        description="very strong, high fire cost, medium spirit cost, multiple skills including Spines suggest a dangerous animal with threatening looks",
    ),
    # Flarepup 🐭 2p 1h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Flarepup",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Fertility],
        ),
        description="low powerhealth, low fire cost, low spirit cost, Fertility skill suggests animal traits of high reproductive abilities andor nurturing aspects, while fire cost and name suggest a powerfulenergetic aspect",
    ),
    # Armospire 🐭 2p 6h
    # costs: 🔥 has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Armospire",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="medium powerhealth, low fire cost, low spirit cost, Fertility skill suggests protective abilities, the name suggests a creature with armorlike attributes, spire also implies some type of ability to act as a lookout or sentry",
    ),
    # Quickfox 🔰💀🐭🧺 2p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Quickfox",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="relatively balanced stats, multiple skills including Shield and InstantDeath",
    ),
    # Fatesprite 🔰💀🧺🐭 10p 7h
    # costs: 👻👻👻 has: 🔥🔥🔥🔥👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Fatesprite",
            power=10,
            health=7,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="high stats and skills, including Fertility and InstantDeath",
    ),
    # Phoenixlet 🪁🔰 1p 1h
    # costs: 🔥 has: 🔥🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Phoenixlet",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Soaring, skills.Shield],
        ),
        description="low powerhealth, moderate fire attribute, Soaring and Shield skills",
    ),
    # Spikegnat 💀🐭🧺🪁🔰🐩 3p 1h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Spikegnat",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="high power, low health, multiple skills including InstantDeath and Fertility",
    ),
    # Dragonlord 🔰🐭💀 3p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Dragonlord",
            power=3,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="This card is powerful and has high health, making it fit to be a dragon and to be a lord of all dragons Its high spirit and fire costs have also made it quite exclusive to obtain The Shield skill is fitting given that it is a lord leading its pack Fertility and InstantDeath are also fitting skills, as a dragon is typically very long lived and capable of great destruction",
    ),
    # Hexfire 🔰🧺💀🐭 3p 3h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Hexfire",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="This animal would contain the idea of fire and danger The Shield skill would also help draw out that imagery, conjuring an air of both danger and protection around the creature Packrat is skillfull, because Hexfire could be seen as hoarding its symbolical fire, given that this card has relatively low spirit and fire costs, despite its power Black cats are often considered unlucky and hexed, making the fantasy creature's name befitting a very clever and dangerous animal",
    ),
    # Flametusk 🔰🪁🐭🧺💀 9p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Flametusk",
            power=9,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Soaring,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description='This animal would be a fiery one, as it has a high fire cost and has Shield as well as Packrat skills The name implies it would be a strong animal, like an elephant, which is fitting with its high power and health The Flame part of its name adds to that, but "tusk" hints that it has some sort of physical defense with its tusks, fitting with the Shield ability Soaring skill could work well with that as it implies it is a large and heavy creature that can only fly for a short amount of time',
    ),
    # Soulwing 🪁🔰💀 3p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Soulwing",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[skills.Soaring, skills.Shield, skills.InstantDeath],
        ),
        description="related to the high spirits and has fire attributes, also the skill Soaring",
    ),
    # FertilityBat 🐭💀 4p 4h
    # costs: 🔥🔥 has: 🔥 pot: 27
    Blueprint(
        original=Card(
            name="FertilityBat",
            power=4,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="relates to the Fertility skill, also has fire attribute",
    ),
    # Hoarderhorn 🔰💀🧺🐭 4p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Hoarderhorn",
            power=4,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="relates to the Packrat skill, has both fire and spirits attributes, also has Shield skill",
    ),
    # Packleader 🧺🐭🔰 3p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Packleader",
            power=3,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Shield],
        ),
        description="relates to Packrat and Fertility skills, and has high health, spirits and Packrat skill",
    ),
    # Spikebackula 🧺🔰🐭💀🦔🪁 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Spikebackula",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Soaring,
            ],
        ),
        description="relates to the Spines skill and high power, health, spirits, and fire attributes",
    ),
    # Homunculus 🧺 2p 1h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Homunculus",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="A miniature, artificially created humanoid, representing the low health and cost of the card The skill Packrat, implying a hoarder or collector, fits with the idea of a crafted creature collecting and keeping things",
    ),
    # Pyrothorax 🐭🔰💀🧺 6p 4h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Pyrothorax",
            power=6,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="A creature that combines a fiery nature being associated with the element fire, with a high power and spirit cost, but also quite strong in the presence of spirits or fire Shield, Fertility, and Packrat fit the idea of a creature that hoards and protects valuable resources, like burning embers or flammable materials Instant Death, however, implies a quick end, which could work with the idea that a burning creature doesn't last long if extinguished",
    ),
    # Dreamhare  2p 2h
    # costs: 🔥🔥 has: 👻 pot: 6
    Blueprint(
        original=Card(
            name="Dreamhare",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="balanced, fantastical, fits with other fantastical animal names in game",
    ),
    # Soarhawk 🧺🪁🐭🔰💀 6p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Soarhawk",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Packrat,
                skills.Soaring,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="high spirits, strong fire, flying skills",
    ),
    # Krakenix 🦔🧺🔰🐩🐭💀 9p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Krakenix",
            power=9,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="skillful, balanced, aquatic",
    ),
    # Runebull 🧺🐭🔰💀🦔🐩 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Runebull",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
                skills.Underdog,
            ],
        ),
        description="strong, earthy, skilled",
    ),
    # Flamebugle 🔰🧺🦔🐭 8p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Flamebugle",
            power=8,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[skills.Shield, skills.Packrat, skills.Spines, skills.Fertility],
        ),
        description="firerelated, shielded, low costs",
    ),
    # Mysticcat 🐭💀 2p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻 pot: 34
    Blueprint(
        original=Card(
            name="Mysticcat",
            power=2,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="high health, wellbalanced stats, instant death and fertility skills",
    ),
    # Ghostlynx 🐭 6p 3h
    # costs: 🔥 has: 🔥 pot: 23
    Blueprint(
        original=Card(
            name="Ghostlynx",
            power=6,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="high power, low health, strong fertility skill",
    ),
    # Stormdrake 💀🪁 10p 8h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Stormdrake",
            power=10,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Soaring],
        ),
        description="very high power and health, moderate cost, instant death and soaring skills",
    ),
    # Gorgontail 🦔💀🔰🍀🪁 5p 10h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Gorgontail",
            power=5,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Shield,
                skills.LuckyStrike,
                skills.Soaring,
            ],
        ),
        description="very high health, multiple skills including spines and shields",
    ),
    # Quickarmad  2p 10h
    # costs: 🔥 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Quickarmad",
            power=2,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="high health, low power, no skills",
    ),
    # Stingersaur 🦔 4p 5h
    # costs: - has: 🔥👻👻👻👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Stingersaur",
            power=4,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description="With high power and health and the Spines skill, this card's name relates to its deadly nature, evoking the image of a dinosaur with sharp, poisonous spines",
    ),
    # Firebirdie 🐭🦔 2p 9h
    # costs: - has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Firebirdie",
            power=2,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Spines],
        ),
        description="This card has balanced attributes, both for spirits and fire, and the Fertility and Spines skills The name invokes the idea of a small but potent bird, with flaming feathers and spiky defense mechanisms",
    ),
    # Shieldratle 🔰🧺🦔 1p 4h
    # costs: - has: 🔥 pot: 32
    Blueprint(
        original=Card(
            name="Shieldratle",
            power=1,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat, skills.Spines],
        ),
        description="With low spirits but spiky skills, this card evokes the image of a small, tough rodent with an armadillolike defense mechanism The name hints at both its spines and its shielding ability",
    ),
    # Fertilebear 🔰🐭🦔 7p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Fertilebear",
            power=7,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.Spines],
        ),
        description="With high spirits and fire costs, this card is both strong and expensive Its name references not only its fertility skill but also its strength and bearlike attributes",
    ),
    # Infernodillo 🐩🐭🔰 3p 5h
    # costs: 🔥🔥🔥 has: - pot: 28
    Blueprint(
        original=Card(
            name="Infernodillo",
            power=3,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Underdog, skills.Fertility, skills.Shield],
        ),
        description="This card is quite balanced overall, with a focus on fire costs and the Underdog skill Its name evokes the image of an armored armadillo that can withstand intense heat and fire, fitting for a card with these kinds of attributes",
    ),
    # Faeox 🐭 7p 3h
    # costs: 🔥 has: 🔥👻 pot: 26
    Blueprint(
        original=Card(
            name="Faeox",
            power=7,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="This name suggests a supernatural creature that is both beautiful and mysterious, fitting for a card with moderate power and low health values The relatively low fire cost only  and high spirit cost reflect the Faeox's mystical nature, and their sole skill of Fertility hints at their ability to bring magical life to any situation",
    ),
    # Deathwhale 🧺🐭💀 8p 8h
    # costs: - has: 🔥🔥🔥👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Deathwhale",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.InstantDeath],
        ),
        description="very strong, very expensive, even though it has no fire or spirit powers, it's highly spirited, it's pack rat, fertility, and instant death skills give it a dangerous edge",
    ),
    # Fireborn 🧺🐭💀🔰🐩🦔 7p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Fireborn",
            power=7,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="strong, wellrounded, especially useful against underdog skills, and with great health, even though it's quite expensive",
    ),
    # Shieldhog 🔰🐭💀🧺 6p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Shieldhog",
            power=6,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="exceptionally good defense, OK offense, low cost, and with good health, armored with shield, instant death, and packrat skills, making it useful in a lot of situations",
    ),
    # Embermoose 🐭💀 7p 4h
    # costs: 👻 has: 👻 pot: 33
    Blueprint(
        original=Card(
            name="Embermoose",
            power=7,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="high power, low spirit, low cost, with fertility and instant death skills, good for early play and against deck builders",
    ),
    # Shadowbear 💀🐭🧺🔰 8p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 60
    Blueprint(
        original=Card(
            name="Shadowbear",
            power=8,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description='This card has high power and health, but also high costs in fire and spirits The skills InstantDeath and Shield suggest a bear that is hard to take down, perhaps even a little menacing The name "Shadowbear" relates to this by suggesting a bear that lurks in the shadows, ready to pounce on its prey',
    ),
    # Rainguard 🧺🔰🐭 2p 3h
    # costs: 🔥 has: - pot: 27
    Blueprint(
        original=Card(
            name="Rainguard",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description='With moderate power and health, no fire or spirit cost, and skills like Packrat and Shield, this card seems like a protector The name "Rainguard" relates to this by suggesting a creature that shields and protects others from the elements',
    ),
    # Nightdrake 🐭🔰🧺💀 8p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Nightdrake",
            power=8,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description='A card with high power, high health, and skills like Fertility and Packrat suggests a dragonlike creature The name "Nightdrake" relates to this by suggesting a fierce dragon that hunts in the darkness',
    ),
    # Dirtmole 🧺 5p 2h
    # costs: - has: - pot: 26
    Blueprint(
        original=Card(
            name="Dirtmole",
            power=5,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description='With low power, moderate health, and only packrat skills, this card seems like a simple mole that burrows underground The name "Dirtmole" relates to this by suggesting a creature that lives and thrives in dirt and tunnels',
    ),
    # Blazebug 🧺💀🐭🔰🪁 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Blazebug",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Soaring,
            ],
        ),
        description='This card has high power and health, as well as skills like InstantDeath and Shield, suggesting a creature that is hard to bring down The high fire cost and the name "Blazebug" both relate to this by suggesting a creature that is hot and fiery, and perhaps even explosive',
    ),
    # Hauntbear 🧺🐭💀 2p 4h
    # costs: - has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Hauntbear",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Packrat, skills.Fertility, skills.InstantDeath],
        ),
        description="relates to the InstantDeath skill, and the fact that this card has relatively high health with decent power",
    ),
    # Shieldon 🧺🐭🔰💀 5p 2h
    # costs: 👻👻👻 has: 🔥👻 pot: 36
    Blueprint(
        original=Card(
            name="Shieldon",
            power=5,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="relates to the Shield skill, and the fact that this card has high power with lower health and costsspirits",
    ),
    # Mysticat 🐭🔰 7p 6h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Mysticat",
            power=7,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="related to magic and the high spirits, which are both present in the card's attributes \"Cat\" is chosen due to the card's high agility qualities and, though fragile, it can grant extra health to allies Fertility and protect itself Shield",
    ),
    # Thornrat 🔰🐩🐭💀🦔 4p 3h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Thornrat",
            power=4,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="animal name based on porcupine, one of the characterizing features of the card's skills, Spines, which inflict damage to attackers in close combat The name also relates to defensive qualities offered by Shield and Underdog skills",
    ),
    # Furygator 🐭💀🔰🪁 8p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Furygator",
            power=8,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Soaring,
            ],
        ),
        description="relates to the high Power attribute and the Instant Death skill The card has the ability to survive more damage than most of the cards with Shield, but will succumb to vastly dominant foes \"Gator\" is chosen to balance the card's attributes as alligatorcrocodile represents a good relation of both high Power and some of the animal's strength",
    ),
    # Seedraptor 🐭💀🧺 7p 4h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Seedraptor",
            power=7,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description='This card has high power and decent health, making it a force to be reckoned with on the battlefield The skills of fertility, packrat, and instant death hint at a stealthy, deadly predator that can strike quickly and efficiently The "seed" part of the name plays off the idea of seeds being small, but able to grow into something much larger, just like this card\'s potential to dominate the field',
    ),
    # Nightfeline 🔰🐭💀 4p 4h
    # costs: 🔥 has: 🔥🔥👻👻👻👻👻👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Nightfeline",
            power=4,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="With good health and decent power for its cost, this card seems like a solid allaround choice Its shield skill might suggest a defensive, protective creature, while the fertility and instant death skills could indicate a sneaky, nocturnal hunter The name highlights the card's dark side as well as its feline characteristics, adding to the mystery surrounding it",
    ),
    # Skyserpent 🐩🧺🐭🔰💀🪁 7p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Skyserpent",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Soaring,
            ],
        ),
        description="This powerful card is expensive but can match its cost with its high stats and numerous skills, including the unique soaring skill The underdog skill could hint at the idea of an underdog rising to great heights, just like this serpent that takes to the skies Its name suggests an epic, mystical quality that befits such a formidable creature",
    ),
    # Thornyak  6p 8h
    # costs: 🔥 has: 🔥👻 pot: 25
    Blueprint(
        original=Card(
            name="Thornyak",
            power=6,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description='This card has great health and decent power but no special skills The name and appearance of this creature suggest a tough, spiky beast that can take a lot of punishment while dealing out damage with its horns The name also contains a nod to the card\'s small size, with the "yak" part being a playful twist on "yakety yak"',
    ),
    # Pixieblade 🔰🐭🐩🧺 7p 6h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Pixieblade",
            power=7,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.Underdog, skills.Packrat],
        ),
        description="related to their high power and mix of skills shield, packrat, fertility, underdog, all of which give it a bit of an unpredictable character",
    ),
    # Fairywisp 🐭 7p 6h
    # costs: 🔥 has: 🔥👻 pot: 31
    Blueprint(
        original=Card(
            name="Fairywisp",
            power=7,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="related to its high power and the fertility skill, wisps are often associated with magic and the fantastical",
    ),
    # Crabkin 🧺🐭 2p 1h
    # costs: 👻👻👻 has: 🔥🔥🔥🔥🔥🔥 pot: 21
    Blueprint(
        original=Card(
            name="Crabkin",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=0,
            has_fire=6,
            skills=[skills.Packrat, skills.Fertility],
        ),
        description="related to its high fire attribute, crabs relate to the sea which is often associated with fire in mythology, and the packratfertility skill combination giving it a unique character",
    ),
    # Insectaur 🦔💀🔰🧺🐭 10p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Insectaur",
            power=10,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="related to its high powerhealth, the spines skill, and the shieldpackratfertilityinstakill abilities, the insectlike name fits well with the combination of skills",
    ),
    # Shellhog 🔰 2p 4h
    # costs: 🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Shellhog",
            power=2,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="related to its high health and shield skill, shellhog fits with the card's defensive abilities and low power",
    ),
    # Vixenmane 💀🐩🔰🐭🧺 8p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Vixenmane",
            power=8,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="relates to the high power and health attributes, the shield skill, and the packrat skill, making the card appear strong and defensive",
    ),
    # Jadeclaw 🐭💀🧺 4p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Jadeclaw",
            power=4,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="relates to the cost of the card and its low power and health attributes, while the instant death skill and fertility skill imply that the card is cunning and quick",
    ),
    # Nightpaw 💀 3p 2h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Nightpaw",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="related to the low power and health attributes and the instant death skill the card appears to strike in the night or under the cover of darkness, making the card appear elusive and sneaky",
    ),
    # Thornshell 🐭🧺🔰 2p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Thornshell",
            power=2,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="related to the high health attribute and shield and fertility skills, makes the card appear strong defensively and indirectly deadly",
    ),
    # Fertipod 🐭🧺💀 2p 2h
    # costs: 🔥🔥 has: - pot: 24
    Blueprint(
        original=Card(
            name="Fertipod",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description='The name is related to the fertility skill and low cost "Pod" represents a small size, also related to low power and health',
    ),
    # Polarcheon 🔰🧺💀🦔🐭 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Polarcheon",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description='The name is related to the high power, health and spirit attributes, as well as the shield skill "Polar" represents their strength, while "cheon" short for chameleon is a fantastical creature related to the spirit skill',
    ),
    # Blazebat 🐭💀🧺 6p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Blazebat",
            power=6,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description='The name is related to the fire skill, low cost and high fire attribute "Blaze" represents the card\'s fiery nature, and "bat" is a fantastical creature that can relate to its low powerhealth ratings',
    ),
    # Spikewyrm 🦔🐭 3p 3h
    # costs: - has: 🔥👻 pot: 31
    Blueprint(
        original=Card(
            name="Spikewyrm",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Spines, skills.Fertility],
        ),
        description='The name is related to the spines and fertility skills, and the relatively low power and health attributes "Wyrm" represents a fantasy serpent that can relate to the spine skill, and "spike" to the skill and the fertility skill',
    ),
    # Armosaurus 🐭💀 3p 7h
    # costs: 🔥🔥 has: 🔥👻👻👻 pot: 33
    Blueprint(
        original=Card(
            name="Armosaurus",
            power=3,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description='The name is related to the armored nature of the card, represented by the fertility and instant death skills, as well as its relatively high health "Armo" represents the armor attribute, while "saurus" represents the large size and strength of the dinosaur family',
    ),
    # Banesnake 💀🔰🧺🐭 6p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Banesnake",
            power=6,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="strong, high health, costly, highly fire and spirit, skilled spines, shield and death",
    ),
    # Wispwolf 🔰💀 2p 1h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Wispwolf",
            power=2,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield, skills.InstantDeath],
        ),
        description="low powerhealth, expensive fire, glows with spirit, skilled shield and death",
    ),
    # Pegasusfly 🐭🧺🪁🔰💀 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="Pegasusfly",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="very strong, highly spirit, highflying, multiskilled packrat, fertility, soaring, shield, death",
    ),
    # Moleraptor 🧺🐭🐩💀🔰 3p 6h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Moleraptor",
            power=3,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="medium powerhealth, fire and spirit, packrat, fertility, underdog, shield, death",
    ),
    # Serpentsky 🪁🔰🐭💀🚀 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Serpentsky",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Soaring,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Airdefense,
            ],
        ),
        description="very strong, highly spirit, aerial, multiskilled shield, fertility, death, air defense",
    ),
    # Thornbeetle 🦔🐭🔰🐩🧺 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Thornbeetle",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description='related to "spines" skill, high attack and defense, and no costs for spirits, medium costs for fire',
    ),
    # Shieldkitten 🔰🧺🐭💀 7p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Shieldkitten",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description='related to "shield" and "packrat" skills, medium attack and defense, and mediumlow costs for fire and spirits',
    ),
    # Phoenixape 🐩💀🔰🐭🚀🦔 10p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 79
    Blueprint(
        original=Card(
            name="Phoenixape",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Airdefense,
                skills.Spines,
            ],
        ),
        description='related to "airdefense" skill, very high attack and good defense, high spirit cost, mediumlow cost for fire',
    ),
    # Neblizard 🧺 1p 1h
    # costs: - has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Neblizard",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description='related to "packrat" skill, very low attack and defense, and no costs for spirits and fire',
    ),
    # Mysticowl 🐭🐩🧺🔰 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Mysticowl",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Fertility, skills.Underdog, skills.Packrat, skills.Shield],
        ),
        description="relates to the high power and health attributes, as well as the skills Fertility, Underdog, Shield and Packrat, suggesting a wise healer who can protect and support allies",
    ),
    # Starlynx 🐩🔰🍀💀🐭 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Starlynx",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.LuckyStrike,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="relates to the high spirit and fire attributes, moderate health and power, and the skills Underdog, Shield, LuckyStrike, InstantDeath, and Fertility, suggesting a swift and lucky creature with a powerful starry gaze",
    ),
    # Thornbeak 🦔🪁🧺🔰💀🐭 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Thornbeak",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Soaring,
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="relates to the spines and high spirit attribute, as well as the high health, moderate power, and skills Spines, Soaring, Packrat, Shield, InstantDeath, and Fertility, suggesting a dangerous bird with a tough exterior",
    ),
    # Gorgonbear 🐭💀 2p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Gorgonbear",
            power=2,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=6,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description='This card has a high power and health but is quite costly to play Additionally, it has the skills Fertility and InstantDeath, which indicate a powerful creature with the ability to both create life and destroy it The name "Gorgonbear" encompasses the monsterlike nature of the card, as well as the idea of death and transformation associated with the Gorgon legend',
    ),
    # Skypackrat 🦔💀🧺🪁🐭🐩 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Skypackrat",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Packrat,
                skills.Soaring,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="With a high power and health and multiple skills including Spines, InstantDeath, and Packrat, this card suggests a nimble, scavenging creature that can hold its own in battle The name Skypackrat conveys the idea of an agile, airborne rodent that is both resourceful and potentially dangerous",
    ),
    # Spineviper 💀🐭🦔🔰🧺 3p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Spineviper",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Spines,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="This card has moderate power and health, but its skills  InstantDeath, Fertility, Spines, Shield, and Packrat  make it a formidable adversary The name Spineviper conveys the sense of a sleek, deadly creature that can attack from multiple angles and also defend itself",
    ),
    # Airshielder 🚀🐭🐩🔰💀🧺 4p 5h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Airshielder",
            power=4,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Airdefense,
                skills.Fertility,
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description='With aboveaverage power and health and skills including Airdefense, Shield, InstantDeath, Packrat, and Fertility, this card suggests a creature that is wellrounded and hard to defeat The name "Airshielder" emphasizes the protective aspect of the card\'s skills, while also implying a creature that is mobile and quick to evade attack',
    ),
    # Spiritedhog 🐭🐩🧺💀🔰 5p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Spiritedhog",
            power=5,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="This card has aboveaverage health and an impressive number of spirits, as well as skills including Fertility, Underdog, and InstantDeath The name Spiritedhog conveys the idea of a tenacious, energetic animal that can fight against the odds and also harness the forces of life and death",
    ),
    # Netherwolf 💀 5p 4h
    # costs: 🔥🔥🔥 has: 🔥🔥 pot: 21
    Blueprint(
        original=Card(
            name="Netherwolf",
            power=5,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.InstantDeath],
        ),
        description="This card is expensive in terms of fire costs with a high power of  and health of , It has a fire power of , and two of its skills are focused on sudden death The name Netherwolf fits well into the theme of powerful, deathpredicting animal traits of the card",
    ),
    # Silverwysp 💀🧺🦔🪁🐭🔰 9p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Silverwysp",
            power=9,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Spines,
                skills.Soaring,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="This card is extremely powerful in all attributes Its skills vary widely, and include InstantDeath and Shield, among others The name Silverwysp relates to the high spiritfire power of the card, and it indicates the card's magical properties",
    ),
    # Voidhound 💀🧺🔰🐩🐭 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Voidhound",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
            ],
        ),
        description="This card is powerful, with high spiritfire attributes, health, and power Its set of skills ranges from InstantDeath to Underdog and Packrat The card name Voidhound relates to card's low health and its ability to enact sudden death, correlating with the hellish constituents of dark voids",
    ),
    # Skyshell 💀🔰🦔 4p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Skyshell",
            power=4,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=6,
            skills=[skills.InstantDeath, skills.Shield, skills.Spines],
        ),
        description="This card has high health, with a lower power and fire cost, and is blessed with skills such as Shield and Spines The name Skyshell implies the card is related to the sky and is protected from harm, relating to the high health and Shield attribute",
    ),
    # Thornmoth 💀🐭🔰 4p 5h
    # costs: 🔥 has: 🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Thornmoth",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility, skills.Shield],
        ),
        description='This card\'s stats are modest, so the name "Thornmoth" suggests a small but spiky and defensive creature Its skills include "Shield" and "Fertility," which underscore the creature\'s protective and nurturing nature',
    ),
    # Emberbat  2p 2h
    # costs: 🔥 has: 👻👻👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Emberbat",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=0,
            skills=[],
        ),
        description='This card has low stats and no skills, but its attributes suggest a small but agile creature with a fiery spirit The name "Emberbat" sounds like a nimble and fiery critter that could become stronger with the right support',
    ),
    # Fertiledillo 🐭 5p 3h
    # costs: 🔥 has: 🔥🔥🔥 pot: 23
    Blueprint(
        original=Card(
            name="Fertiledillo",
            power=5,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=3,
            skills=[skills.Fertility],
        ),
        description='This card\'s high "Fertility" skill and modest stats suggest a nurturing creature with a lot of offspring The name "Fertiledillo" combines "fertile" with "armadillo," which either suggests an armored critter that provides a lot of support for its young or a sticky creature that multiplies quickly',
    ),
    # Wingrat 🐭🧺🪁 7p 2h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Wingrat",
            power=7,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.Soaring],
        ),
        description="With its power level of , health of , and soaring ability, Wingrat swings in to attack from above with its packrat hoard, dealing extra damage to opposing creatures",
    ),
    # Wolfwing 🧺 1p 2h
    # costs: 🔥🔥🔥🔥 has: 🔥🔥🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Wolfwing",
            power=1,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Packrat],
        ),
        description="With a power level of , health of , and  fire cost, Wolfwing is a rare creature that swoops in with its packrat ability to defend and attack with ferocious pack tactics",
    ),
    # Chromadrake 🐩🐭🔰💀 6p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="Chromadrake",
            power=6,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="Chromadrake is a formidable creature with immense size, power, and health Its instant death ability allows it to target opponents with a ferocious bite, ensuring victory in battle",
    ),
    # Lumberaptor 🐭🦔💀 8p 3h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Lumberaptor",
            power=8,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Fertility, skills.Spines, skills.InstantDeath],
        ),
        description="With power level  and health , the Lumberaptor is a highly spirited creature with deadly spines that can take down any opponent",
    ),
    # Fertifowl 🐭 3p 5h
    # costs: - has: 🔥🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Fertifowl",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description='related to the skill Fertility and the high health and moderate power of the card combines "fertile" with "fowl" to fit the fantastical animal theme',
    ),
    # Thornviper 🦔 2p 1h
    # costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Thornviper",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Spines],
        ),
        description='related to the skill Spines and the moderate powerlow health of the card combines "thorn" with "viper" to suggest a dangerous, venomous creature',
    ),
    # Spirihawk  6p 4h
    # costs: 👻 has: 🔥👻👻👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Spirihawk",
            power=6,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=4,
            has_fire=1,
            skills=[],
        ),
        description='related to the high spirit attribute and moderate healthpower of the card combines "spirit" with "hawk" to suggest a creature with heightened senses or abilities',
    ),
    # Blazeworm  4p 1h
    # costs: 🔥🔥🔥 has: 👻 pot: 7
    Blueprint(
        original=Card(
            name="Blazeworm",
            power=4,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description='related to the skillless card\'s high powerlow health and cost in fire combines "blaze" with "worm" to suggest a creature that is both fiery and slippery',
    ),
    # Shieldjag 💀🔰🐭 6p 3h
    # costs: 👻 has: 🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Shieldjag",
            power=6,
            health=3,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description='related to the skills Shield and Fertility and the moderate powerhealthattribute values of the card combines "shield" with "jag" to suggest a creature that is both protective and powerful',
    ),
    # Shieldrake 🐭💀🔰 2p 4h
    # costs: 🔥 has: 👻👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Shieldrake",
            power=2,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="A mythical creature that resembles a dragon, yet shedding its scales to form a powerful shield to protect itself Shieldrake has relatively high power and health, a medium spirit cost, and a fire cost that suits its scaly nature Shieldrake's abilities include Instant Death for attacking, Shield for protection, and Fertility, which represents the creatures ability to reproduce and shed its scales",
    ),
    # Stormjaw 💀🔰 4p 2h
    # costs: 🔥🔥 has: 👻👻👻 pot: 23
    Blueprint(
        original=Card(
            name="Stormjaw",
            power=4,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Shield],
        ),
        description="A fierce mythical beast resembling a wolf with electrifying powers Stormjaw packs a real punch with high power and a medium spirit cost Its cost in fire matches its electric energy This cards abilities include Instant Death for targeting enemy creatures and Shield for protection The name suggests the creature's ability to attack swiftly and fiercely with its powerful jaws and electric energy",
    ),
    # Packrat 🧺 1p 4h
    # costs: 🔥🔥🔥 has: 👻👻 pot: 13
    Blueprint(
        original=Card(
            name="Packrat",
            power=1,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description="A nimble rat skilled at collecting things Packrat has low attacking power, but its high health and Packrat ability means it can collect other cards from the deck Like a real packrat, this card is useful in collecting useful items other cards and has high survivability when threatened",
    ),
    # Sparrowcat 🐭 2p 3h
    # costs: - has: 🔥 pot: 26
    Blueprint(
        original=Card(
            name="Sparrowcat",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="A small, fast feline creature with low power, but good health, no spirit cost and good Fertility Sparrowcat moves quickly and steadily with the wind, its agility making it difficult for other creatures to target The name reflects its agility and flighty nature, as well as its feline characteristics",
    ),
    # Pyrosaur 🔰🐭🧺 8p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻👻👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Pyrosaur",
            power=8,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description="Combines 'pyro' fire and 'dinosaur' Relates to its high power and fire costs",
    ),
    # Wisplet 🐭💀🔰 2p 2h
    # costs: - has: 🔥🔥👻 pot: 38
    Blueprint(
        original=Card(
            name="Wisplet",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="Combines 'whisp' spirit and 'applet' small, weak Relates to its low powerhealth and high spirit count",
    ),
    # Chimeralope 🐭💀🔰🧺 4p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Chimeralope",
            power=4,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="'Chimera' combining different animals and 'antelope' Relates to its high health and packrat skill",
    ),
    # Gloworm  2p 3h
    # costs: - has: 🔥👻👻👻👻👻 pot: 22
    Blueprint(
        original=Card(
            name="Gloworm",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[],
        ),
        description="Relates to its high spirit count and low powerhealth",
    ),
    # Vampbat 💀🔰🧺 1p 2h
    # costs: 🔥 has: 🔥👻 pot: 23
    Blueprint(
        original=Card(
            name="Vampbat",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Packrat],
        ),
        description="powerful, low health, expensive, InstantDeath, Shield",
    ),
    # Brushcat 🐭🐩🧺 4p 1h
    # costs: 🔥🔥 has: 🔥👻 pot: 25
    Blueprint(
        original=Card(
            name="Brushcat",
            power=4,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Underdog, skills.Packrat],
        ),
        description="moderate power, low health, not very expensive, Fertility, Underdog",
    ),
    # Archdemon 🐭🔰🧺💀🐩 7p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Archdemon",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="very powerful, durable, highly spirited and fiery, Shield, Packrat, Fertility, InstantDeath, Underdog",
    ),
    # Tyrannodon 💀🐩🐭 5p 3h
    # costs: 🔥 has: 🔥👻 pot: 32
    Blueprint(
        original=Card(
            name="Tyrannodon",
            power=5,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Underdog, skills.Fertility],
        ),
        description="powerful but low health, not very expensive, InstantDeath, Fertility, Underdog",
    ),
    # Gravewolf 🐭 4p 10h
    # costs: 🔥🔥 has: 🔥👻👻👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Gravewolf",
            power=4,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="has fire, low spirit, high health, one skill, Fertility",
    ),
    # Pixiedillo 🐭🧺💀🔰 3p 2h
    # costs: 🔥 has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Pixiedillo",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="has little cost, low powerhealth, several skills including InstantDeath, Packrat, Shield, and Fertility",
    ),
    # Boarglow 🐭 7p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Boarglow",
            power=7,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Fertility],
        ),
        description="has relatively low cost, high powerhealth, one skill, Fertility",
    ),
    # Dracowolf 🐭🧺🔰🪁 4p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Dracowolf",
            power=4,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Fertility, skills.Packrat, skills.Shield, skills.Soaring],
        ),
        description="high stats and multiple skills",
    ),
    # Fertileant 🐭 0p 8h
    # costs: - has: - pot: 30
    Blueprint(
        original=Card(
            name="Fertileant",
            power=0,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="low attack, high health and one skill, Fertility",
    ),
    # Shieldshark 🔰 10p 6h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Shieldshark",
            power=10,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield],
        ),
        description="high powerhealth, has a shield skill and requires some fire and spirits to play",
    ),
    # Moondove 🐭🔰 5p 4h
    # costs: 👻👻👻👻👻👻👻👻 has: 👻👻 pot: 24
    Blueprint(
        original=Card(
            name="Moondove",
            power=5,
            health=4,
            costs_fire=0,
            costs_spirits=8,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="moderate powerhealth, fertility skill, requires spirits to play",
    ),
    # Airrat 🚀🔰🧺💀 3p 3h
    # costs: 🔥 has: 👻 pot: 28
    Blueprint(
        original=Card(
            name="Airrat",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[
                skills.Airdefense,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="low powerhealth, air defense skill, packrat skill, instant death skill, requires fire to play",
    ),
    # Luckyhorn 🍀🐭💀 5p 5h
    # costs: 🔥 has: 🔥👻👻👻👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Luckyhorn",
            power=5,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=1,
            skills=[skills.LuckyStrike, skills.Fertility, skills.InstantDeath],
        ),
        description="high powerhealth, lucky strike and fertility skills, requires fire and spirits to play",
    ),
    # Shieldhorn 🔰🧺🐭🐩💀🦔 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Shieldhorn",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="relating to the Shield skill and high health, power is strong, but not OP, the name represents protection with a fantastical twist, the horns could be some sort of shield or armor",
    ),
    # Charmowl 🐭🧺💀🚀🍀 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Charmowl",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Airdefense,
                skills.LuckyStrike,
            ],
        ),
        description="relating to the Fertility skill and Lucky Strike with only airdefense, the name represents good fortune and a mystical creature, and the owl relation aims to be swift and agile",
    ),
    # Firebirdog 🪁🐭 4p 5h
    # costs: 🔥 has: 🔥 pot: 25
    Blueprint(
        original=Card(
            name="Firebirdog",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Soaring, skills.Fertility],
        ),
        description="relating to the Soaring and Fertility skills, suggests a creature with both wings and agility, with ability to produce fire, the dog relation refers to a loyal, but a bit ferocious, creature",
    ),
    # Hedgeback 🦔🧺🔰🐭 8p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Hedgeback",
            power=8,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Spines, skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="relating to the Spines skill, the name suggests a creature that is both small and defenseful, like a hedgehog but with a fantasy twist, high health and power, while somewhat expensive",
    ),
    # Spritiguard 🔰💀🐭🧺🦔🐩 7p 10h
    # costs: 👻👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Spritiguard",
            power=7,
            health=10,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Spines,
                skills.Underdog,
            ],
        ),
        description="relating to the Shield, InstantDeath, Fertility, and Packrat skills, the name refers to a tiny creature that offers protection and help, and perfect balance, it has high power and health, but somewhat expensive and requires spirits to play",
    ),
    # Chaosmite 💀🐩🧺🐭 5p 5h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Chaosmite",
            power=5,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="relates to high powerhealth, high firespirit costs, and the combination of skills such as InstantDeath and Fertility that create a sense of disorder or chaos",
    ),
    # Mooncub 💀🧺🐭🔰 5p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Mooncub",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="relates to high health, high spirit, and the inclusion of skills like Shield and Packrat which suggest protection and collecting resources, reminiscent of the idea of a bear cub and the moon",
    ),
    # Wyvernix 🍀🧺🔰🐭💀 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Wyvernix",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.LuckyStrike,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="relates to high powerhealth, fire attribute, and the inclusion of skills such as LuckyStrike and InstantDeath that suggest an agile and deadly creature",
    ),
    # Faeowl 🐭 2p 2h
    # costs: 👻👻👻 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Faeowl",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="relates to the low powerhealth and spirit attribute, and the inclusion of the Fertility skill that suggests a nurturing and magical creature",
    ),
    # Thornstag 🔰💀🐭 7p 4h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Thornstag",
            power=7,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.InstantDeath, skills.Fertility],
        ),
        description="relates to high power, range of fire and spirit attributes, and the inclusion of the skills Shield and InstantDeath that suggest a tough and dangerous creature with a fierce reputation",
    ),
    # Stingrat 🧺 4p 1h
    # costs: 🔥🔥 has: - pot: 12
    Blueprint(
        original=Card(
            name="Stingrat",
            power=4,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Packrat],
        ),
        description='The card has low health and no spirits or fire, but has a relatively high power for its cost The skill "Packrat" suggests it collects things, so "Stingrat" is a name that could be associated with someone or something small but powerful with a tendency to collect or hoard things',
    ),
    # Dragonling 🧺🐩🐭🦔🔰💀 9p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Dragonling",
            power=9,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Underdog,
                skills.Fertility,
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description='The card has very high power and health, and has all  spirits and fire It also has a variety of skills, including "Spines" and "InstantDeath" "Dragonling" suggests a small or young dragon, which fits with the name of the game and the fantasy theme, while also conveying strength and danger',
    ),
    # Trickster 🐩 3p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Trickster",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog],
        ),
        description='The card has low power and health, but has the "Underdog" skill and is relatively low cost "Trickster" suggests a character who is clever and cunning, able to use their wits to outmaneuver stronger opponents',
    ),
    # Thornsaur 🐭🦔 10p 4h
    # costs: 🔥🔥 has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Thornsaur",
            power=10,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Spines],
        ),
        description="high power, low health, spines and fertility",
    ),
    # Shieldhawk 🔰🐭🦔 7p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Shieldhawk",
            power=7,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.Spines],
        ),
        description="high health, some power, shield, and high fire and spirits cost",
    ),
    # Foxfair 🐭 4p 1h
    # costs: - has: 🔥🔥👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Foxfair",
            power=4,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="low health and power, fertility, and balanced spirits and fire cost",
    ),
    # Magmafish  3p 3h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Magmafish",
            power=3,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="moderate powerhealth, high fire cost, no skills",
    ),
    # Ratpacker 🐭💀🧺 4p 5h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Ratpacker",
            power=4,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="moderate powerhealthcosts, fertility, instant death, and packrat skills",
    ),
    # Sandlion 🐩 1p 2h
    # costs: 👻👻 has: 🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Sandlion",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog],
        ),
        description=" spirits,  powerhealth, underdog skill",
    ),
    # Nightstag 🦔💀 2p 3h
    # costs: - has: 👻 pot: 27
    Blueprint(
        original=Card(
            name="Nightstag",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Spines, skills.InstantDeath],
        ),
        description=" powerhealth, spines and instant death skill",
    ),
    # Infernix  2p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Infernix",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description=" powerhealth,  fire cost, no skills",
    ),
    # Ancestral 🐭 3p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Ancestral",
            power=3,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description=" power,  health,  fire cost, fertility skill",
    ),
    # Terrafox 🐭 2p 1h
    # costs: 🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Terrafox",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description=" power,  health,  fire cost, fertility skill",
    ),
    # Galafox 🔰🐭💀 3p 6h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Galafox",
            power=3,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description='related to the "fertility" skill, this creature is likely a breed of fox that is known for being fast and cunning Its high power and health implies that it is able to outwit its opponents and persevere, even under extreme conditions The "instant death" skill suggests a formidable, deadly aspect to it as well',
    ),
    # Willowisp 🔰🐭 2p 6h
    # costs: - has: 🔥🔥👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Willowisp",
            power=2,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility],
        ),
        description='The low power and high health stats suggest a creature that is elusive and hard to catch or pin down The "shield" and "fertility" skills might have something to do with its magical abilities  perhaps this beast can produce a blinding light, and is capable of regenerating and reproducing quickly',
    ),
    # Sunviper 💀🐩🔰🐭 7p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Sunviper",
            power=7,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="sounds fierce and powerful, matching the high power and health, but with high spirit attributes as well",
    ),
    # Spikeosaur 🧺🔰💀🦔🐩 5p 8h
    # costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Spikeosaur",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
                skills.Underdog,
            ],
        ),
        description="high health and power, with spines as a relevant skill",
    ),
    # Dreamrat 🐭🧺💀 4p 3h
    # costs: - has: 🔥🔥👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Dreamrat",
            power=4,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="low fire and spirit attributes, with skills like fertility and packrat suggesting a shrewd or sneaky creature",
    ),
    # Shieldclaw 🐩🔰💀🦔🧺🐭 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Shieldclaw",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="very strong, with skills like shield and spines for defense, but also capable of dealing damage with high power and skills like underdog and instant death",
    ),
    # Valkyriege 🐭🔰🐩🧺💀 7p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Valkyriege",
            power=7,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="female Nordic godlike creature with high power and health, fertility, shield, and underdog skills, making it a strong, balanced, and mythical creature",
    ),
    # Salamandren 💀 1p 4h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Salamandren",
            power=1,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="firebreathing, amphibious creature with limited power and health but the InstantDeath skill, making it a sneaky and versatile fighter",
    ),
    # Sparkling  0p 1h
    # costs: - has: 🔥🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Sparkling",
            power=0,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="small, fire elemental creature with low power and no cost, that can be summoned easily and adds to the fire attribute Has no skills but can be used in combination with other fire cards to create powerful combos",
    ),
    # Armorgon 🐭🧺💀🔰 4p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Armorgon",
            power=4,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="large, heavilyarmored dinosaurlike creature with high health and fertility Its packrat and InstantDeath skills make up for low power and relatively high cost",
    ),
    # Glimmerhorn 🐭🔰💀🐩🦔🧺 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Glimmerhorn",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
                skills.Spines,
                skills.Packrat,
            ],
        ),
        description="high powerhealth, expensive, highly skilled, regenerative, spiky",
    ),
    # Coyotebug 🐩🦔🔰🐭 1p 3h
    # costs: 🔥🔥 has: 🔥👻 pot: 27
    Blueprint(
        original=Card(
            name="Coyotebug",
            power=1,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Underdog, skills.Spines, skills.Shield, skills.Fertility],
        ),
        description="low powerhealth, cheap, fire attribute, skilled, underdog, spiky",
    ),
    # Grasswhistle 🧺 1p 9h
    # costs: - has: 🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Grasswhistle",
            power=1,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Packrat],
        ),
        description="low power, high health, low cost, highly spirited, hoarding",
    ),
    # Spikeking 💀🧺🐭🐩🔰🦔 10p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Spikeking",
            power=10,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="high power, decent health, fire attribute, highly spirited, skilled, spiky",
    ),
    # Blazejag 🔰🐭🦔💀🧺🪁 7p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Blazejag",
            power=7,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Spines,
                skills.InstantDeath,
                skills.Packrat,
                skills.Soaring,
            ],
        ),
        description="relates to the high power and health stats, fire attribute, and spiky skills",
    ),
    # Earthrat 🐭🧺🔰 2p 3h
    # costs: 🔥🔥 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Earthrat",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="relates to the medium power and health stats, low fire cost, and fertility and packrat skills Also conveys an image of a sturdy and resourceful creature",
    ),
    # Mooncat  1p 8h
    # costs: 🔥 has: 👻👻👻 pot: 17
    Blueprint(
        original=Card(
            name="Mooncat",
            power=1,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[],
        ),
        description="relates to high health, moonspectralspiritual aspects, and the no fire attribute and skills",
    ),
    # Thornbear 🔰🐩🐭🦔💀🧺 6p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Thornbear",
            power=6,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
                skills.Spines,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="relates to high power and health stats, high spirit attribute plus the skills of shieldspinesfertility, and the animal being a bear but with thorns",
    ),
    # Bansheep 💀🔰🐭 2p 3h
    # costs: 🔥🔥 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Bansheep",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="relates to medium power and health stats, medium fire cost, and the skills of shieldinstant deathfertility The name is a fusion between banshee and sheep, conveying a ghostly but harmless yet powerful animal",
    ),
    # Dynataur 🐭🔰💀🐩 7p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Dynataur",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description="related to the attributes power and health, as well as the skills Underdog and Fertility",
    ),
    # Starwolf 🐩🐭 5p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Starwolf",
            power=5,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Underdog, skills.Fertility],
        ),
        description="related to the attributes power, health, and cost, as well as the skills Underdog and Fertility",
    ),
    # Faepony 🐩🐭 1p 5h
    # costs: 🔥 has: 👻 pot: 21
    Blueprint(
        original=Card(
            name="Faepony",
            power=1,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Underdog, skills.Fertility],
        ),
        description="related to the attributes health, costsfire, and skills Underdog and Fertility",
    ),
    # Flamant 🐭 2p 1h
    # costs: 🔥 has: 🔥🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Flamant",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="related to the attributes power, hasspirits, and skills Fertility",
    ),
    # Fatesnake 🐭💀🔰🦔🧺🐩 10p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 82
    Blueprint(
        original=Card(
            name="Fatesnake",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description='This card has a lot of variety in skills and attributes, making it seem like it could be fated to be any number of creatures The "snake" part comes from it having both fire and spirits often associated with opposing forces and "fate" because of its diverse skill set that gives it the ability to manipulate the game',
    ),
    # Frostlynx 🔰🐭🧺💀 8p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Frostlynx",
            power=8,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description='This card has pretty solid stats, but the skills and cost indicate more defense than offense "Frost" makes sense because of the shield skill and the high health, and "lynx" as it is a tricky creature that is good at avoiding attacks',
    ),
    # Inksquid 🔰💀🐭🧺 5p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Inksquid",
            power=5,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description='This card has relatively low stats, so needed a name that lent it a bit of menace "Ink" comes from the shield skill, as well as indicating a sneaky and dirty fighter "Squid" plays off this idea further by indicating that it has tentacles that can attack from a distance',
    ),
    # Spiritbug 💀🐭 0p 1h
    # costs: 🔥🔥🔥 has: 🔥👻👻👻👻 pot: 17
    Blueprint(
        original=Card(
            name="Spiritbug",
            power=0,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description='This card has very low stats overall, but high spirit attribute and the ability to deal with other cards indicated by Death and Fertility skills "Spirit" was an obvious choice, and "bug" was chosen as it suggests something capable of growing stronger over time and being resilient in the face of danger',
    ),
    # Thundergoat 🐩💀🧺🔰🐭 5p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Thundergoat",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="powerful, durable, spirited, fiery, versatile, but risky with InstantDeath skill",
    ),
    # Spikehound 💀🐭🐩🧺🦔🔰 7p 7h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Spikehound",
            power=7,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description="powerful, durable, spirited, fiery, versatile, and formidable with its many skills",
    ),
    # FennecFox 🐭💀🔰 4p 5h
    # costs: 🔥 has: 🔥👻 pot: 36
    Blueprint(
        original=Card(
            name="FennecFox",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="agile, weak, but hard to catch with its Shield skill and sneaky with its InstantDeath skill",
    ),
    # Zephyrcat  0p 2h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 5
    Blueprint(
        original=Card(
            name="Zephyrcat",
            power=0,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[],
        ),
        description="weak and cheap, but swift with its Windrider skill and agile with its Shield skill",
    ),
    # MysticHorn 🐭 2p 2h
    # costs: 🔥🔥🔥 has: 👻 pot: 13
    Blueprint(
        original=Card(
            name="MysticHorn",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="high powerhealth but expensive",
    ),
    # Serpenlily 🐭 4p 6h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 26
    Blueprint(
        original=Card(
            name="Serpenlily",
            power=4,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="high powerhealth, but expensive",
    ),
    # Chimwhale 🐭🔰💀 8p 10h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Chimwhale",
            power=8,
            health=10,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="very high powerhealth but very expensive",
    ),
    # Luminant 🐭🔰🐩💀 9p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Luminant",
            power=9,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
            ],
        ),
        description="very high powerhealth, but very cheap and highly skilled",
    ),
    # Mantimera 🔰💀🐭🪁🐩🧺 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Mantimera",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Soaring,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description="related to mantis and chimera, high powerhealth, shield, instant death, fertility, soaring, underdog, packrat",
    ),
    # Thornowl 💀🔰🦔 7p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Thornowl",
            power=7,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Shield, skills.Spines],
        ),
        description="related to owl, spines, shield, instant death, medium powerhealth, low cost",
    ),
    # Fireferret 🧺🔰🐭💀🦔 3p 5h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Fireferret",
            power=3,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="related to ferret, high fire cost, packrat, low powerhealth, shield, fertility, instant death, spines",
    ),
    # Aquafox 🐭 3p 2h
    # costs: - has: 🔥👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Aquafox",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="related to fox, low fire cost, high spirits, fertility, low powerhealth",
    ),
    # Chryserpent 🐭💀🔰🦔 8p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Chryserpent",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="related to serpent and chrysophant, high powerhealth, no fire cost, shield, spines, fertility, instant death",
    ),
    # Thornmancer 🦔🐭🧺💀 3p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Thornmancer",
            power=3,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=6,
            has_fire=3,
            skills=[
                skills.Spines,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="The card with the highest health and highest number of skills The 'Thorn' reflects the spines on the card and 'mancer' refers to the magical nature of the card",
    ),
    # Drakonix 🐭🔰 10p 3h
    # costs: 🔥 has: 🔥👻 pot: 37
    Blueprint(
        original=Card(
            name="Drakonix",
            power=10,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="With high power and low health, the 'dra' is inspired by dragons and 'konix' refers to a powerful creature that is difficult to defeat",
    ),
    # Fertileon 🐭🔰🧺 3p 2h
    # costs: 🔥 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Fertileon",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield, skills.Packrat],
        ),
        description="With average stats and 'fertility' as a skill, the name 'Fertileon' combines 'fertile' and 'leon' lion to suggest a strong, thriving animal",
    ),
    # Wyverndillo 🪁🧺🐭🐩🦔🔰 7p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Wyverndillo",
            power=7,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Soaring,
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description="With high power and health and 'soaring' as a skill, the name 'Wyverndillo' refers to a creature that is armored like an armadillo but also has wings like a wyvern",
    ),
    # SpiritBat 🪁🔰 1p 3h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻 pot: 31
    Blueprint(
        original=Card(
            name="SpiritBat",
            power=1,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=6,
            skills=[skills.Soaring, skills.Shield],
        ),
        description="With relatively low cost and high spirit point, SpiritBat is an agile creature with moderate health and shield ability Its Soaring and Shield skills make it a good addition to any deck that needs a quick and effective shield bearer",
    ),
    # ChimeraWolf 🐭💀🧺🚀🔰 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="ChimeraWolf",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Airdefense,
                skills.Shield,
            ],
        ),
        description="A powerful and expensive creature that can pack a punch, ChimeraWolf is an excellent hitter with a high health stat It also has various skills such as Fertility and Packrat which can help you get the most out of your deck However, be careful  its high cost comes with a higher risk",
    ),
    # ThornSerpent 💀🐭🦔🔰 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="ThornSerpent",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description="With a combination of high power, moderate health, and great set of skills including InstantDeath and Spines, ThornSerpent is a deadly addition to any team Its skills allow it to take out other cards effectively, making it an excellent choice if you need to bolster the weaker aspect of your deck",
    ),
    # SkyHare 🐭🧺🪁💀 2p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="SkyHare",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.InstantDeath,
            ],
        ),
        description="Despite its low power, SkyHare excels at dodging and retreating Its moderately high health and Soaring skill make it a hard target to catch, and its InstantDeath and Packrat skills can significantly lower a card's effectiveness This makes it a fantastic addition to any deck that needs a quick support card",
    ),
    # ShieldCrab 🔰 8p 1h
    # costs: 🔥🔥 has: 🔥👻👻👻 pot: 23
    Blueprint(
        original=Card(
            name="ShieldCrab",
            power=8,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="With a high power rating, ShieldCrab can hit hard and effectively Its Shield skill also makes it an excellent protective card to have in a more defensive team Its high cost and relatively low health make it a card that requires strategic placement",
    ),
    # Furyhorn 🪁💀🧺🐭 8p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Furyhorn",
            power=8,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.Soaring,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="relates to high power and health, and the skills InstantDeath and Packrat",
    ),
    # Wingcat 🧺🐭 1p 6h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Wingcat",
            power=1,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility],
        ),
        description="relates to high health and the skill Fertility, and the fact that it doesn't have fire",
    ),
    # Shieldgoat 🔰🐭 1p 2h
    # costs: 🔥🔥 has: 🔥🔥🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Shieldgoat",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="relates to having a Shield skill, the high cost to fire ratio, and its low power and health",
    ),
    # Turtleshell 🔰 0p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 9
    Blueprint(
        original=Card(
            name="Turtleshell",
            power=0,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="relates to having a Shield skill, low power, and only having fire",
    ),
    # Spikefox  5p 2h
    # costs: 🔥 has: 👻 pot: 12
    Blueprint(
        original=Card(
            name="Spikefox",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="relates to high power and having no fire, and it's a small creature with a striking appearance",
    ),
    # MysticRat 🐩🧺🔰🦔🐭💀 1p 3h
    # costs: 🔥 has: 👻👻👻👻 pot: 41
    Blueprint(
        original=Card(
            name="MysticRat",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=0,
            skills=[
                skills.Underdog,
                skills.Packrat,
                skills.Shield,
                skills.Spines,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="highly skilled, symbolic of small creatures with magical powers, balanced stats",
    ),
    # ThunderHawk  6p 2h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻👻👻 pot: 18
    Blueprint(
        original=Card(
            name="ThunderHawk",
            power=6,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[],
        ),
        description="strong in power with fire elements, weak in health, aerial creature",
    ),
    # ShadowFrog 🐭💀🧺 1p 2h
    # costs: 👻👻 has: 🔥🔥👻👻👻 pot: 27
    Blueprint(
        original=Card(
            name="ShadowFrog",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="low power and health, swift with high spirits and elemental spirit power, skilled",
    ),
    # ChimeraBat 🚀🐭 5p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 21
    Blueprint(
        original=Card(
            name="ChimeraBat",
            power=5,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Airdefense, skills.Fertility],
        ),
        description="strong in power, low in health, aerial creature with fire power and air defense skills",
    ),
    # ShellSpike 🔰🐭🐩🦔 2p 2h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 31
    Blueprint(
        original=Card(
            name="ShellSpike",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.Underdog, skills.Spines],
        ),
        description="balanced stats with shield and spines skills, fire elements with high health and average power",
    ),
    # Chimerafel 💀🧺🐩🔰🦔🐭 7p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Chimerafel",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
                skills.Shield,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description="With high power and health, and almost all elemental costs, this card is a true powerhouse Furthermore, it has a variety of skills including InstantDeath, Packrat and Fertility, that imply it's a fearsome card that can be difficult to put down Chimerafel is a combination of Chimera and Felfire, fitting for a fiery, multiheaded creature that spells doom for its opponents",
    ),
    # Fertileclipse 🦔🐭💀 7p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Fertileclipse",
            power=7,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.Spines, skills.Fertility, skills.InstantDeath],
        ),
        description="Another strong card with very high health and a mixture of elemental costs The card's Spines, Fertility and InstantDeath skills make it a fearsome defense card, meaning that Fertileclipse is a fitting name for a dark, magical creature that radiates power and fertility, but also brings darkness and destruction",
    ),
    # Firehawk  2p 1h
    # costs: 🔥🔥🔥🔥 has: 🔥👻👻 pot: 4
    Blueprint(
        original=Card(
            name="Firehawk",
            power=2,
            health=1,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="costs a lot of fire, has fire and spirits, high power, low health, no skills",
    ),
    # Ashmouse  1p 2h
    # costs: 🔥🔥 has: 👻👻 pot: 5
    Blueprint(
        original=Card(
            name="Ashmouse",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description="low power and health, low costs for both fire and spirits, has some spirit",
    ),
    # Shellshield 🔰 1p 2h
    # costs: 🔥🔥 has: 👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Shellshield",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Shield],
        ),
        description="low power and health, moderate cost for fire, has some spirit, a shielding skill",
    ),
    # Gryphonix 🧺🔰🐩🐭🦔🪁 8p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Gryphonix",
            power=8,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
                skills.Spines,
                skills.Soaring,
            ],
        ),
        description="very strong with multiple skills, no fire cost, has both fire and spirit",
    ),
    # Wispling 🐭🐩🪁🧺 8p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Wispling",
            power=8,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[skills.Fertility, skills.Underdog, skills.Soaring, skills.Packrat],
        ),
        description="A small, highly spirited and powerful creature with no elemental affinity The name relates to its high power and health, as well as its pack rat skill which might suggest it likes collecting things and is therefore wise",
    ),
    # Spinekraken 🐭🔰💀🦔 5p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Spinekraken",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="A big creature with spines and an affinity for spirits, but no elemental affinity The name relates to its big size, good health and power stats, its high spirit count, and its spines skill",
    ),
    # Turtleling 🐭🔰 1p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 19
    Blueprint(
        original=Card(
            name="Turtleling",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="A small, slow creature with a shell and a fire affinity The name relates to its low power and health stats, its high defense rating due to its shield skill, and its fire element",
    ),
    # Fertilepanther 🐭 3p 3h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 20
    Blueprint(
        original=Card(
            name="Fertilepanther",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="A highly skilled predator with no elemental affinity The name relates to its fertility skill, which suggests it breeds quickly and is therefore quite common, as well as its good powerhealth balance, and its other skills which aid in its hunting abilities",
    ),
    # Titanosaur 🐩🐭💀🔰 7p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Titanosaur",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="massive size, extremely high powerhealth, no spiritfire costs, instant death skill, underdog skill, fertility skill, shield skill",
    ),
    # Chimerafelis 💀🐭🔰🧺 5p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Chimerafelis",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="fantasy feline with high health and power, no spiritfire costs, instant death skill, fertility skill, shield skill, packrat skill",
    ),
    # Pixieling 🧺 3p 1h
    # costs: 🔥 has: 🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Pixieling",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="cute and small creature with low health and power, cheap to cast fire cost, packrat skill for resourcefulness",
    ),
    # Infernopup 🔰 1p 2h
    # costs: 🔥 has: 🔥🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Infernopup",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Shield],
        ),
        description="small and firebased creature with low health and power, cheap cost for fire, shield skill",
    ),
    # Tempestia 🚀🔰💀🐭🧺🐩 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Tempestia",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Airdefense,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="Related to the skills Airdefense, Shield, InstantDeath Suggests an animal with control over air or storms that can repel or strike back at enemies, but is vulnerable to certain attacks",
    ),
    # Flitmouse  1p 2h
    # costs: 🔥🔥 has: 👻 pot: 4
    Blueprint(
        original=Card(
            name="Flitmouse",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[],
        ),
        description="Related to low power, low health, and probably a small animal that you can't catch with ease Like a bird, bat, or squirrel, but infused with fantasy elements",
    ),
    # Fertilepuma 🧺🐩🐭💀 5p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Fertilepuma",
            power=5,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Packrat,
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="Related to skills Fertility, Packrat, Underdog and its high powerhealth attributes Suggests a powerful and fertile feline that can draw allies and produces many offspring, but is prone to being underestimated or treated as a lesser animal by other fantasy creatures",
    ),
    # Phantombear 🐭💀🧺🐩 9p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Phantombear",
            power=9,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="Related to skills Fertility, InstantDeath, Packrat, Underdog, high power but relatively low health Suggests a ghostly or ethereal bear that lures in smaller creatures only to consume them, but can't handle serious attacks",
    ),
    # Spikedrake 🦔💀🔰🐩🐭 3p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Spikedrake",
            power=3,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
            ],
        ),
        description="relates to spines skill, fire element, good health, low spirits",
    ),
    # Emberlion 💀🐭🧺🐩🔰 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Emberlion",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Underdog,
                skills.Shield,
            ],
        ),
        description="relates to instant death and fire element skills, high in both fire and spirit costs, powerful stats",
    ),
    # Foxsprite  6p 2h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Foxsprite",
            power=6,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="This card has moderate power and health, but has low costs for both fire and spirits It also has no skills The name suggests a small, magical animal, fitting for a card with low costs and no skills The name also hints at its low power and health values, suggesting a nimble and tricky character, like a fox",
    ),
    # Thornwolf 🦔🔰🐭🧺🪁💀 6p 5h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Thornwolf",
            power=6,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Spines,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.InstantDeath,
            ],
        ),
        description="This card has moderate power and health, but high costs for fire and skills such as spines and shield The name suggests a powerful, dangerous animal with a focus on defense and protection, fitting for a card with high shield and spines skills The thorn element in the name also hints at its spines skill and high fire costs",
    ),
    # Fertilityfrog 🔰💀🐩🐭 3p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Fertilityfrog",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
                skills.Fertility,
            ],
        ),
        description="This card has low power, but high health and a range of skills including shield, instant death, and fertility The name hints at its high fertility skill, suggesting an animal that is good at breeding and growing its numbers The frog element in the name relates to its low power and suggests a small, hopping animal",
    ),
    # Wyvernan 💀🔰🧺 7p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Wyvernan",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Shield, skills.Packrat],
        ),
        description="an awesome sounding name fitting for a strong and attackheavy card, with the bonus of the Shield skill taking some hits and Packrat helping with cost reduction",
    ),
    # Pangosser 🔰🧺 3p 3h
    # costs: 🔥 has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Pangosser",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Packrat],
        ),
        description="relatively low attack, but high health and Shield make this animal a tough tank, with Packrat keeping costs down",
    ),
    # Bloodhedge 🔰🧺🐭 9p 4h
    # costs: 👻👻 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Bloodhedge",
            power=9,
            health=4,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=6,
            has_fire=4,
            skills=[skills.Shield, skills.Packrat, skills.Fertility],
        ),
        description="The name plays on the Fertility skill and the animal's strong suits, featuring high attack and Shield, but relatively low health",
    ),
    # Deathwhisp 💀 2p 7h
    # costs: 🔥 has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Deathwhisp",
            power=2,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="With Instant Death skill on board, Deathwhisp is a deadly contender with low power and high health, yet low costs and no spirit dependency",
    ),
    # FaeriePhant 💀🔰🐭 9p 5h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="FaeriePhant",
            power=9,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="With a high cost of fire and spirit dependency, FaeriePhant's fertility skill comes in handy to make up for its lack of spirits in terms of defense its offense is powerful with high power and good health",
    ),
    # Packrataur 🐭🧺 2p 9h
    # costs: 🔥🔥 has: 🔥👻 pot: 32
    Blueprint(
        original=Card(
            name="Packrataur",
            power=2,
            health=9,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="A midrange priced card, Packrataur has moderate power and good health, plus the Fertility skill to increase your army, while its Packrat skill will help it build up the required resources faster",
    ),
    # Soaragon 🧺🐭🐩💀🪁 9p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Soaragon",
            power=9,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Soaring,
            ],
        ),
        description="Master survivor with its builtin skills especially the Underdog skill to keep it alive in tougher battles, and relatively cheap overall, Soaragon is a strong ally that has the potential to soar above competitors with high power and health",
    ),
    # Thornscaled 🐭🧺💀🔰🦔 5p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Thornscaled",
            power=5,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="With Spines and Shield skills at its disposal, Thornscaled is a defensive powerhouse, made more so with good health However, it's not without some offensive prowess with moderate power",
    ),
    # Sea Ogre 🧺🐭🐩 3p 10h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Sea Ogre",
            power=3,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Underdog],
        ),
        description="powerful, healthy, has fire and spirits, a packrat, can thrive in unexpected situations, and has superior breeding abilities",
    ),
    # Thorny Lizard 🦔🐭💀🔰 6p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Thorny Lizard",
            power=6,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.Spines,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="highly offensive, low defense, fiery and spirited, has spines, can shield itself from attacks, and has the power to cause instant death",
    ),
    # Cloud Phoenix 🐭🔰💀 7p 9h
    # costs: 👻👻👻👻👻👻 has: 🔥🔥🔥👻👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Cloud Phoenix",
            power=7,
            health=9,
            costs_fire=0,
            costs_spirits=6,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="powerful, high health, very spirited, can shield itself and has a powerful instant death ability Its cost is mostly spiritbased, and it has a strong flourishing aura",
    ),
    # Dragon Fly 🐭💀🔰🐩🪁🧺 6p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Dragon Fly",
            power=6,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
                skills.Soaring,
                skills.Packrat,
            ],
        ),
        description="high health, very spirited, can shield itself, has amazing breeding abilities, excellent underdog skills, and can thrive even in low spirit states while soaring the skies",
    ),
    # Fire Beetle 🔰 3p 1h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Fire Beetle",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=4,
            skills=[skills.Shield],
        ),
        description="low health, fiery, heavily armored, and has a remarkable ability to provide shielding",
    ),
    # Puffcat 🐩 2p 2h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Puffcat",
            power=2,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog],
        ),
        description="This card has relatively low power and health and is not very expensive to play, but it has the Underdog skill The name Puffcat is fitting as it implies a cute and unassuming creature that might surprise you with an unexpected boost",
    ),
    # Windsprite 🐭💀🚀🪁 1p 1h
    # costs: 🔥 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Windsprite",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Soaring,
            ],
        ),
        description="This card doesn't have outstanding stats, but it has  different skills, some of which involve Air Airdefense, Soaring Its name should imply something graceful and airy, hence Windsprite",
    ),
    # Sunbeast 🐩🐭💀🔰 3p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Sunbeast",
            power=3,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="This card is very expensive to play and has high health, but only moderate power In keeping with the potentially dangerous aspect of a card that powerful, it also has InstantDeath and Shield skills The name Sunbeast implies a radiant, almost terrifying creature that shines with blinding power",
    ),
    # Voidrat 💀🧺🔰 1p 2h
    # costs: 🔥🔥 has: 👻 pot: 21
    Blueprint(
        original=Card(
            name="Voidrat",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Packrat, skills.Shield],
        ),
        description="This card has low power and health, high costs and no Fire, but it does have InstantDeath, Packrat and Shield skills The name Voidrat is fitting as it suggests something small and sneaky, but with a hidden danger that can make it unexpectedly lethal",
    ),
    # Gleaming 🐭💀🧺🔰 7p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Gleaming",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="This card is very powerful in all respects and has a wide range of skills The name Gleaming is appropriate because it suggests something bright and shimmering, perhaps because it is covered in gemstones or radiates a strong, magical aura",
    ),
    # Emberfox 🔰🧺💀🚀🐩🐭 3p 4h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Emberfox",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Underdog,
                skills.Fertility,
            ],
        ),
        description="The name incorporates the animal name \"fox,\" and suggests a fiery nature which fits well with the card's skill set The Shield skill is also represented in the name, as foxes are known for their defensive abilities The name also fits well with the card's cost values",
    ),
    # Armadragon 🐭🔰 2p 4h
    # costs: 🔥🔥 has: 🔥👻 pot: 24
    Blueprint(
        original=Card(
            name="Armadragon",
            power=2,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Shield],
        ),
        description='This name incorporates both "arma" from the Armadillo card, as well as "dragon" which suggests a fantastical nature The high cost of the card is reflected in the dragon name, and the Fertility and Shield skills work well with a defensive, armored dragonlike creature',
    ),
    # Thornsiren 💀🧺🐭 3p 9h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Thornsiren",
            power=3,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Packrat, skills.Fertility],
        ),
        description='The name suggests a mythical creature that uses thorns to attack, in line with the card\'s skillset The high health is implied in the name "siren," as mythical sirens are often associated with strength and power The Fertility skill is also represented in the name, as sirens are known for their allure and reproductive nature',
    ),
    # Reaperfowl 🐭🪁🔰💀🧺🐩 10p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Reaperfowl",
            power=10,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Soaring,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="high power, high health, deathdealing skills",
    ),
    # Shadowhare 🔰🐭💀🚀🧺 9p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Shadowhare",
            power=9,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Packrat,
            ],
        ),
        description="high powerhealth, shadow skills for defense and offense",
    ),
    # Drakeshift 💀🧺🔰🐭 8p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Drakeshift",
            power=8,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="high power, low cost, fire attributes, shapeshifting skills",
    ),
    # Thorned Elk 🔰🐭🧺💀🦔 6p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Thorned Elk",
            power=6,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Spines,
            ],
        ),
        description="high health, defensive skills, spines",
    ),
    # Faebug 🐭💀 3p 3h
    # costs: - has: 🔥🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Faebug",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="low powerhealth, fertility skills",
    ),
    # Ferretling 🐭 2p 2h
    # costs: 🔥 has: 🔥🔥 pot: 15
    Blueprint(
        original=Card(
            name="Ferretling",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="fertile, small, medium power and health, no skills",
    ),
    # Fluttercat 💀🧺 3p 2h
    # costs: 🔥 has: 👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Fluttercat",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="a small and agile creature that can evade enemy attacks thanks to the Packrat skill and its relatively low health It also has the InstantDeath skill, showcasing its ability to use swift strikes to kill other creatures",
    ),
    # Thunderbear 🧺🐭🔰🐩🦔💀 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Thunderbear",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
                skills.Spines,
                skills.InstantDeath,
            ],
        ),
        description="a beast of immense power and health, with the Fertility and Shield skills indicating its ability to protect and nurture other creatures It also has the Packrat, Underdog, and Spines skills, suggesting a ferocious and protective nature",
    ),
    # Spikeball 🐩🔰 2p 1h
    # costs: - has: 🔥👻👻👻 pot: 27
    Blueprint(
        original=Card(
            name="Spikeball",
            power=2,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Underdog, skills.Shield],
        ),
        description="a small, yet tough and spirited creature, with the Shield and Underdog skills making it resilient in combat Its low power is countered by its high health and the Shield skill, making it a potentially annoying opponent to remove from the field",
    ),
    # Froghorn 🐭 4p 4h
    # costs: 🔥 has: 🔥 pot: 21
    Blueprint(
        original=Card(
            name="Froghorn",
            power=4,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="a creature with high powerhealth, low fire cost, and the skill Fertility, which could relate to the frog's ability to lay many eggs at once",
    ),
    # Uniclaw 🐭 5p 1h
    # costs: - has: 🔥 pot: 28
    Blueprint(
        original=Card(
            name="Uniclaw",
            power=5,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="a creature with high power, low health, and low fire cost, with the skill Fertility, which relates to the unicorn's mythical ability to create new life",
    ),
    # Packmunk 🔰🐭🧺 8p 5h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Packmunk",
            power=8,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description="a creature with very high powerhealth, many skills, and higher spirits than fire cost, indicating determination and hard work, like a pack animal, and the skill Packrat",
    ),
    # Basiliskite 🔰🪁🐭💀🧺 4p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Basiliskite",
            power=4,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Soaring,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="a very strong creature with lots of health and fire cost, with skills like Shield and Soaring, which relate to the basilisk's mythical ability to turn to stone and the idea of taking to the air like a kite",
    ),
    # Spindlecub 💀🧺🔰🐭 3p 4h
    # costs: 🔥🔥 has: 🔥👻 pot: 37
    Blueprint(
        original=Card(
            name="Spindlecub",
            power=3,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="low powerhealth, costs a bit, has skills, and spindly like a baby animal",
    ),
    # Spiritfox 🐭🔰🧺 3p 4h
    # costs: - has: 🔥🔥🔥👻👻👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Spiritfox",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=3,
            skills=[skills.Fertility, skills.Shield, skills.Packrat],
        ),
        description="moderate powerhealth, low cost, highly spirited, can use skills to shield itself, and speedy",
    ),
    # Rockhog  1p 4h
    # costs: 🔥🔥 has: 🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Rockhog",
            power=1,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="low power and no skills, but hard to defeat, like a rocky crag",
    ),
    # MysticRaven 💀🐭🧺 3p 2h
    # costs: 🔥 has: 🔥👻👻👻 pot: 30
    Blueprint(
        original=Card(
            name="MysticRaven",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility, skills.Packrat],
        ),
        description=" power,  health, costsfire , hasspirits , Instant Death, Fertility, and Packrat skills suggest a magical and clever bird with dark powers",
    ),
    # ShadowFerret 🔰🐭🧺 3p 2h
    # costs: - has: 🔥👻 pot: 38
    Blueprint(
        original=Card(
            name="ShadowFerret",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description=" power,  health, costsfire , hasspirits , Shield, Fertility, and Packrat skills suggest a quick and stealthy animal with defensive capabilities",
    ),
    # ThunderRam 🐩🔰 3p 3h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 23
    Blueprint(
        original=Card(
            name="ThunderRam",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Underdog, skills.Shield],
        ),
        description=" power,  health, costsfire , hasspirits , Underdog and Shield skills suggest a determined and strong animal, possibly one that can also cause damage with its horns",
    ),
    # Phoenixdragon 🧺🐩🚀🐭💀🔰 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Phoenixdragon",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Underdog,
                skills.Airdefense,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description=" power,  health, costsfire , hasspirits , hasfire , and a range of skills including Packrat, Underdog, Airdefense, Fertility, InstantDeath, and Shield suggest a legendary creature with highly destructive powers and the ability to resurrect from its own ashes",
    ),
    # Pricklehog  3p 2h
    # costs: 🔥🔥 has: 👻👻 pot: 8
    Blueprint(
        original=Card(
            name="Pricklehog",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description=' power,  health, costsfire , hasspirits , no skills, spiky appearance due to higher defense, possible aggression expressed via the word "hog"',
    ),
    # Phoenixlite 🐭🔰🧺💀 5p 6h
    # costs: 👻👻👻 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Phoenixlite",
            power=5,
            health=6,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description='The card has high power and health making it ideal to fight battles, while the high costs of spirits and fire, make it much more special Costly but useful skills like "Fertility" and "Shield" make it a very special card',
    ),
    # Spinegrizz 🐭🐩🧺💀🦔🔰 7p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Spinegrizz",
            power=7,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
                skills.Spines,
                skills.Shield,
            ],
        ),
        description='With high power, health, and skills like "Fertility", "Underdog", and "Spines", this card is a combination of a grizzly bear and spines, making it hard to defeat The name is a combination of the words \'spine\' and \'grizz\' which accurately represents the card\'s attributes and skills',
    ),
    # Fantiguar 🐭🧺🦔 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Fantiguar",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[skills.Fertility, skills.Packrat, skills.Spines],
        ),
        description="a fantastical jaguarlike creature that is powerful and tough but also has fertility powers, representing its ability to produce offspring and grow its pack with ease",
    ),
    # Chirrut 🐩🐭🦔🧺 8p 5h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Chirrut",
            power=8,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Underdog, skills.Fertility, skills.Spines, skills.Packrat],
        ),
        description="a fantastical birdlike creature that is fierce and resilient despite being relatively small and cheap to deploy, with underdog skills representing its fighting spirit",
    ),
    # Turtloch 💀🔰 2p 3h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 22
    Blueprint(
        original=Card(
            name="Turtloch",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Shield],
        ),
        description="a fantastical tortoiselike creature with a tough exterior and a shield, representing its ability to withstand attacks and block damage",
    ),
    # Hareon 💀🐭🔰🦔 4p 2h
    # costs: 🔥 has: 🔥👻 pot: 34
    Blueprint(
        original=Card(
            name="Hareon",
            power=4,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="a fantastical harelike creature with high fertility powers, instant death abilities, and spines, representing its speed and power in multiplying and attacking",
    ),
    # Ghostrat 💀 1p 2h
    # costs: 🔥 has: 🔥 pot: 11
    Blueprint(
        original=Card(
            name="Ghostrat",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="a fantastical rodentlike creature with instant death abilities, representing its sneaky nature and deadly attack",
    ),
    # Soarshell 🐩🪁 2p 10h
    # costs: - has: 🔥🔥👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Soarshell",
            power=2,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Underdog, skills.Soaring],
        ),
        description="This name relates to the Soaring skill and the high health value, as well as the low fire and spirit values, which suggest a flying creature that is resilient and hard to bring down",
    ),
    # Gorgonlance 🔰🐩🧺💀🐭🦔 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Gorgonlance",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="relates to the InstantDeath skill and strong overall attributes",
    ),
    # Spinespike 💀🧺🦔 4p 4h
    # costs: 🔥 has: 👻 pot: 28
    Blueprint(
        original=Card(
            name="Spinespike",
            power=4,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.InstantDeath, skills.Packrat, skills.Spines],
        ),
        description="relates to the Spines skill and strong allaround attributes",
    ),
    # Spiritant 🐭🧺🔰🪁 3p 8h
    # costs: 👻👻 has: 🔥🔥🔥👻👻👻 pot: 43
    Blueprint(
        original=Card(
            name="Spiritant",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.Shield, skills.Soaring],
        ),
        description="relates to the high spirits attribute , fertility skill, and packrat collectingmanaging resources skill",
    ),
    # Razorlynx  3p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Razorlynx",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[],
        ),
        description="relates to the high fire attribute , the sharp claws of the lynx, and high power ",
    ),
    # Shieldkraken 💀🧺🔰 6p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Shieldkraken",
            power=6,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Packrat, skills.Shield],
        ),
        description="relates to the shield skill and high health , with a nod to the sea since krakens are often depicted guarding treasure",
    ),
    # Fatedrake 🐩💀🔰🐭 5p 7h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Fatedrake",
            power=5,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description='relates to the underdog and fertility skills, as well as the high fire and spirit attributes The word "fate" implies a sense of destiny and overcoming obstacles, while "drake" suggests power and strength',
    ),
    # Wispmunk  3p 3h
    # costs: 🔥 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Wispmunk",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description='relates to low spirits attribute and small size "Wisp" represents a light or a flickering flame, which could relate to its small power  and fire attribute',
    ),
    # Hareion 🧺🐭🪁 5p 9h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Hareion",
            power=5,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Soaring],
        ),
        description='This name alludes to the animal species Hare rabbit, an animal known for its speed, which fits well with the Soaring skill The prefix "ion" implies this card\'s power and health attributes as well as the fire and spirit costs The name also incorporates "reproduction" Fertility as seen in the suffix "reion" Lastly, Packrat skill alludes to the animal species rat, hence this card\'s name incorporates "hare" and "rat" to create "Hareion"',
    ),
    # Flameowl 🐩🧺🦔 5p 4h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Flameowl",
            power=5,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.Underdog, skills.Packrat, skills.Spines],
        ),
        description='This name communicates the fire attribute as well as the birdlike qualities this card exhibits through its underdog skill and the skillpackrat The prefix "flame" represents the fire aspect of the card, and "owl" corresponds to the bird species "owl" since both animals typically have qualities of invisibility and silence which can fit well with the Packrat and Underdog skills',
    ),
    # Spiritbear 🐩💀🐭🧺 4p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Spiritbear",
            power=4,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description='This is a name that communicates this card\'s high spirit attribute as well as the high power and health it possesses The prefix "spirit" represents the card\'s highest attribute as well as its spirit attribute The suffix "bear" refers to the animal species "bear" which represents the power and health attributes of this card',
    ),
    # Shimmerlynx 🔰💀 2p 2h
    # costs: - has: 🔥👻👻 pot: 30
    Blueprint(
        original=Card(
            name="Shimmerlynx",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield, skills.InstantDeath],
        ),
        description="The card's power and health match that of a lynx, which is a majestic and stealthy feline The skill Shield suggests that it is well protected from attacks, and the skill InstantDeath implies that its enemies better keep their distance The name Shimmerlynx suggests that it is an elusive, radiant, and supernatural creature",
    ),
    # Firepuma 🧺🐩🐭 2p 5h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥🔥👻👻 pot: 31
    Blueprint(
        original=Card(
            name="Firepuma",
            power=2,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Packrat, skills.Underdog, skills.Fertility],
        ),
        description="The card's power, health, and red attribute values indicate that it has a connection to fire The skill Packrat represents its tendency to gather resources and stockpile them for later use The skill Underdog suggests that it is a small but feisty creature that can surprise its enemies The skill Fertility could indicate that it is able to reproduce quickly The name Firepuma suggests that it is a sleek, fierce, and fiery wildcat",
    ),
    # Radiantox 💀🐭 2p 6h
    # costs: - has: 🔥🔥👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Radiantox",
            power=2,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="The card's power and health are high, and the blue attribute value indicates that it has a connection to spirits The skill InstantDeath suggests that it is a very powerful creature that can kill its enemies instantly The skill Fertility could indicate that it has a lot of offspring The name Radiantox implies that it is a shining, mystical, and powerful beast that is able to transcend between the physical and spiritual realms",
    ),
    # Fertilehare 🐭🧺 1p 2h
    # costs: 👻👻👻👻👻 has: - pot: 14
    Blueprint(
        original=Card(
            name="Fertilehare",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="The card's power and health are low, but the high cost in spirits indicates that it has great potential The skills Fertility and Packrat suggest that it is a creature that can quickly multiply and hoard resources The name Fertilehare implies that it is a prolific and swift creature that is able to thrive in any environment",
    ),
    # Empressant 🐩💀🐭🔰🧺🦔 7p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Empressant",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.Spines,
            ],
        ),
        description="high powerhealthspiritsfire, multiple skills",
    ),
    # Stormowl 🔰🪁🧺💀🐭🦔 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Stormowl",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Soaring,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="high healthspirits, soaring skill, multiple skills",
    ),
    # Seedmouse 🐭🧺🔰💀 3p 3h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Seedmouse",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=7,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="low powerhealthFire cost, high spirits, fertility skill",
    ),
    # Mysticstag 💀🐭🐩🔰🪁 4p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Mysticstag",
            power=4,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Shield,
                skills.Soaring,
            ],
        ),
        description="The name reflects the balance between the card's high power and health, as well as its moderate spirit and fire costs The skills add a fantastical element, especially InstantDeath and Shield, which contribute to the mystical aura of the stag",
    ),
    # Wildhare  2p 3h
    # costs: 🔥 has: 👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Wildhare",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[],
        ),
        description='The name suits the card\'s low cost and relatively average stats, which mirror a common woodland creature The skills may be unexpected in such a small animal, hence the "wild" aspect of the name',
    ),
    # Azurelion 🧺🐭💀🔰 6p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Azurelion",
            power=6,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="The name denotes power and elegance, which are both reflected in the card's high stats and the Packrat skill The Fertility and InstantDeath skills add to the theme of a majestic, otherworldly lion",
    ),
    # Pyropuma 💀🐭🧺 10p 5h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Pyropuma",
            power=10,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.InstantDeath, skills.Fertility, skills.Packrat],
        ),
        description="The name combines fire and a fierce animal, which is fitting for a card with high power, moderate health, and moderately high fire cost The skills add a bit of unpredictability, showcasing the fire and agility of the puma",
    ),
    # Shieldram 🐩🔰💀🐭 9p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="Shieldram",
            power=9,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="The name emphasizes the Shield and Underdog skills, both of which are reflected in the card's high health and low power The high cost of fire and spirits suggest a more defensive strategy, which fits well with the image of a ram defending its flock with its sturdy horns",
    ),
    # Spiketurtle 🦔🔰🚀🐭💀🧺 10p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Spiketurtle",
            power=10,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Shield,
                skills.Airdefense,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="The card has high power, health, and great defences by having both Shield and Airdefense skills The name suggests a durable, wellprotected creature with spines and a tough shell, fitting the card's abilities",
    ),
    # Shieldrat 🔰🧺 9p 4h
    # costs: 🔥🔥 has: 👻 pot: 33
    Blueprint(
        original=Card(
            name="Shieldrat",
            power=9,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield, skills.Packrat],
        ),
        description="The card is nimble and has high shield value, mitigating the low health The name suggests a small, agile creature that evades attacks and protects itself from those it cannot dodge",
    ),
    # Thornpup 🔰 3p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 14
    Blueprint(
        original=Card(
            name="Thornpup",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="The card has decent power, low health, but can mitigate damage by using Shield The name suggests a small and tough creature, ferocious despite its size, with an arsenal of thorns to defend itself",
    ),
    # Gigantox 🧺🔰🐩💀🐭 10p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Gigantox",
            power=10,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="relatively cheap, high powerhealth, fire and spirit elements",
    ),
    # Enchantilisk 🔰🐭 9p 3h
    # costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Enchantilisk",
            power=9,
            health=3,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="high power, low health, fire element, shield ability",
    ),
    # Cactonix 🐭💀🔰🦔 9p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Cactonix",
            power=9,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="high powerhealth, fire and spirit elements, spines and fertility abilities",
    ),
    # Soarcrab 🪁💀 3p 3h
    # costs: 🔥🔥🔥 has: - pot: 15
    Blueprint(
        original=Card(
            name="Soarcrab",
            power=3,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Soaring, skills.InstantDeath],
        ),
        description="midpower, midhealth, high fire cost, with the ability to fly and the threat of instant death",
    ),
    # Fertigoat 🔰🐩🐭 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Fertigoat",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[skills.Shield, skills.Underdog, skills.Fertility],
        ),
        description="goatlike creature with fertility aspect, balanced fire and spirits, strong but costly",
    ),
    # Stonetusk 🐭 3p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥 pot: 29
    Blueprint(
        original=Card(
            name="Stonetusk",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=4,
            skills=[skills.Fertility],
        ),
        description="creature with high health and moderate power but lacking in spirits, possibly resembling a tusked stone animal",
    ),
    # Swarmice 🐭🦔🔰💀🧺🐩 5p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 66
    Blueprint(
        original=Card(
            name="Swarmice",
            power=5,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="small but numerous creature with a balance of spirits and fire, many skills, quite expensive",
    ),
    # Skyfinch  5p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Skyfinch",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="birdlike creature with low health and moderate power, mostly firealigned",
    ),
    # Spikepup 🐭💀 2p 1h
    # costs: 🔥 has: 🔥 pot: 19
    Blueprint(
        original=Card(
            name="Spikepup",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="young creature with low power and health but high fertility, and skills related to fertility and instant death, resembling a spiky puppy or hedgehog",
    ),
    # Dragonwing 🔰🐭🪁🐩🦔💀 10p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Dragonwing",
            power=10,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Soaring,
                skills.Underdog,
                skills.Spines,
                skills.InstantDeath,
            ],
        ),
        description="This card is powerful  power and has the ability to fly Soaring skill, plus it's a good survivor Shield skill Its name relates to both its firepower and the ability to fly",
    ),
    # Skyshark 🦔🪁🐭 1p 2h
    # costs: 🔥🔥 has: 👻👻 pot: 17
    Blueprint(
        original=Card(
            name="Skyshark",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Spines, skills.Soaring, skills.Fertility],
        ),
        description="relatively weak, but quick and nimble with spines and the ability to fly",
    ),
    # Snapwisp 🔰💀 3p 3h
    # costs: - has: 🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Snapwisp",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.InstantDeath],
        ),
        description="midrange in terms of powerhealth, but quick and skilled with a shield and the ability to instantly kill opponents",
    ),
    # Flamephoenix 🪁💀🐭🐩🧺 10p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Flamephoenix",
            power=10,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Soaring,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description="extremely powerful and sturdy, with the ability to fly, instantly kill, promote fertility, work as the underdog, and hoard resources for future use",
    ),
    # Fyrewyvern 🧺🐭💀🪁 3p 2h
    # costs: 🔥 has: 🔥 pot: 29
    Blueprint(
        original=Card(
            name="Fyrewyvern",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Soaring,
            ],
        ),
        description="dragonlike creature that breathes fire, but has no spirits, has strong power and health, multiple skills including Packrat and InstantDeath",
    ),
    # Flameserpent 🐭 3p 3h
    # costs: 🔥 has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Flameserpent",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="snakelike creature with fire attributes, medium powerhealth and one fertility related skill",
    ),
    # Spectraptor 🔰🐭🐩🪁💀🧺 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Spectraptor",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Underdog,
                skills.Soaring,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="spectral birdlike creature with lots of spirits, no fire, very strong and lots of skills, including Shield and Underdog",
    ),
    # Voidvole 🐭🧺💀 1p 1h
    # costs: 🔥 has: 🔥🔥🔥 pot: 24
    Blueprint(
        original=Card(
            name="Voidvole",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="small rodentlike creature with no spirits and low fire, fertility and instant death skills, weak in both power and health",
    ),
    # Shield 🔰🐭💀 3p 10h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Shield",
            power=3,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="Taur  This card has a lot of health and is quite powerful, but is also quite expensive to deploy The ShieldTaur combines the protective qualities of a shield with the legendary fearsomeness of the Minotaur, making it a fitting name",
    ),
    # Gauntreeper 🐭 10p 5h
    # costs: 🔥 has: 🔥🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Gauntreeper",
            power=10,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description="Despite its high power, this card has a low health value, making it vulnerable to attack The Gauntreeper uses its power to strike fear in the hearts of its foes, even when they may have the advantage in battle Its name combines the idea of being gaunt and skinny with the ability to creep up on its prey",
    ),
    # Packadel 🔰🧺🐭💀🦔🪁 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 75
    Blueprint(
        original=Card(
            name="Packadel",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Soaring,
            ],
        ),
        description="This card has a lot of spirit energy and is wellrounded in many ways The Packadel is a mythical creature, part bird and part rodent, that travels in packs, using its many skills to outmaneuver its enemies The name reflects its pack mentality and form",
    ),
    # Cloudomorph 🐭🚀 6p 9h
    # costs: 🔥 has: 🔥👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Cloudomorph",
            power=6,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.Airdefense],
        ),
        description="With decent health and power, the Cloudomorph is not a weak card, but it relies on its ability to defend against air attacks As its name suggests, it is able to change its form in order to better blend in with the clouds and protect itself from attackers",
    ),
    # Cacoonfly 🦔 1p 3h
    # costs: 🔥 has: 🔥🔥 pot: 10
    Blueprint(
        original=Card(
            name="Cacoonfly",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Spines],
        ),
        description="This name is an amalgamation of 'cocoon' and 'fly', two words that relate to the skills of this card, Spines and Fire The name alludes to the idea of a Spinecovered insectoid creature undergoing metamorphosis, much like a reallife butterfly, and emerging with the capacity to create devastating Fire attacks",
    ),
    # Sharkfin  2p 3h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Sharkfin",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="a creature that is powerful, wellprotected, but requires a significant amount of resources to play",
    ),
    # Packmink 🧺 1p 2h
    # costs: 🔥 has: 🔥 pot: 10
    Blueprint(
        original=Card(
            name="Packmink",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="a card with a small size and weight, but the skill to scavenge and gather resources, perfect for the role of a pack rat",
    ),
    # Shelldog 🐭🔰 8p 4h
    # costs: - has: 🔥🔥👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Shelldog",
            power=8,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.Shield],
        ),
        description="a creature with good defense, and the ability to multiply with some skills that add protection to the card",
    ),
    # Lemmingling  0p 3h
    # costs: - has: 🔥 pot: 14
    Blueprint(
        original=Card(
            name="Lemmingling",
            power=0,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="a small but sturdy creature with no skills, useful only as a blocker, it is expendable but tough to kill",
    ),
    # Necrodragon 💀🪁🔰🐩🧺🐭 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Necrodragon",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Soaring,
                skills.Shield,
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="powerful, robust, very efficient, balanced skills focused on defense and breeding",
    ),
    # Nightbear 🔰🚀🧺🦔💀🐭 10p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 79
    Blueprint(
        original=Card(
            name="Nightbear",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Airdefense,
                skills.Packrat,
                skills.Spines,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="powerful, quite efficient, heavily defensive, with skills for defense, spines and breeding",
    ),
    # Sparkant  10p 8h
    # costs: 👻👻👻👻👻👻 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Sparkant",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=6,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="related to spirit, high spirit value, no fire cost",
    ),
    # Thornhawk 🦔🐭🔰💀🧺 2p 6h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Thornhawk",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Spines,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="high health, low power, spines and shield skill",
    ),
    # Chromawolf 🔰🐭💀🧺🐩 8p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Chromawolf",
            power=8,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="high power and health, no spiritfire cost, underdog skill",
    ),
    # Fertiledon 🦔💀🐭🐩 9p 6h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Fertiledon",
            power=9,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[
                skills.Spines,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="high power, low health, fertility and instant death skill",
    ),
    # Soarshark 🚀🔰🐩🪁💀🐭 8p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Soarshark",
            power=8,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Airdefense,
                skills.Shield,
                skills.Underdog,
                skills.Soaring,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="high power and health, air defense skill, fire cost",
    ),
    # Bramblecat 🐭🦔🧺 5p 7h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Bramblecat",
            power=5,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.Fertility, skills.Spines, skills.Packrat],
        ),
        description='This card has powerful spines Spines skill and a decent amount of health, making it a formidable opponent The name "Bramblecat" reflects its spiky nature, while also bringing to mind a creature that is both cunning and elusive',
    ),
    # Flameling  6p 2h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Flameling",
            power=6,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[],
        ),
        description='The card has a high fire cost and is quite powerful, but lacks health The name "Flameling" reflects its fiery nature and its relative youth or small size',
    ),
    # Spiritbeast 🧺🔰💀🐩🐭🦔 10p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 80
    Blueprint(
        original=Card(
            name="Spiritbeast",
            power=10,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description='A strong card with many skills Packrat, Shield, InstantDeath, Underdog, Fertility, Spines, this creature is a force to be reckoned with The name "Spiritbeast" reflects its high spirit count, while also bringing to mind a creature that is both fierce and otherworldly',
    ),
    # Serpentix 💀🧺 2p 5h
    # costs: - has: 🔥🔥🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Serpentix",
            power=2,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="This card has moderate power and health, with no cost in spirits The two Instant Death skills hint at a deadly and stealthy serpent, while the Packrat skill implies a hoarding nature",
    ),
    # Skyrover 🪁 2p 2h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 11
    Blueprint(
        original=Card(
            name="Skyrover",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Soaring],
        ),
        description="This card has moderate power and health, with a moderate cost in fire and spirits The Soaring skill implies an agile and nimble flying creature, while the other attribute values suggest a small and unassuming rover",
    ),
    # Blackwidow 💀🐭🐩🦔 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Blackwidow",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="refers to the spines skill and high power, also referencing its instant death ability",
    ),
    # Firefoxin 💀🧺🔰🐭 5p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Firefoxin",
            power=5,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="mix of fox and inferno, referencing both firerelated attributes and the shield skill",
    ),
    # Spiritlynx 💀🧺🐭 4p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Spiritlynx",
            power=4,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Packrat, skills.Fertility],
        ),
        description='high spirits align with the "spirit" aspect in the name and the fertility skill could imply that the lynx is a fertile animal',
    ),
    # Firearmo 🐭💀🔰 8p 2h
    # costs: 🔥 has: 🔥👻 pot: 38
    Blueprint(
        original=Card(
            name="Firearmo",
            power=8,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description='high power and shield skill attributes are related to armor, and adding in the fire cost attribute creates an overall "firearm" reference',
    ),
    # Hydraeagle 🔰💀🐭🐩🦔🧺 7p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Hydraeagle",
            power=7,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Spines,
                skills.Packrat,
            ],
        ),
        description="relates to the multiheaded attribute of the card and the fact that it has flying skills, hence the eagle part of the name The high powerhealth is also symbolized in the name",
    ),
    # Owlynx 🔰🐭🧺 5p 2h
    # costs: 🔥🔥🔥 has: 🔥 pot: 29
    Blueprint(
        original=Card(
            name="Owlynx",
            power=5,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description="combines the owl and lynx animals to highlight the fact that this card has special skills Fertility, Shield, and Packrat and high power The name also relates to the fact that the card is somewhat expensive to play",
    ),
    # Soarwhale 🦔🧺🔰💀🪁🐭 8p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 82
    Blueprint(
        original=Card(
            name="Soarwhale",
            power=8,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
                skills.Soaring,
                skills.Fertility,
            ],
        ),
        description="refers to the fact that the card has Soaring skill and is a very powerful one, hence the whale part of the name The Spines skill is also incorporated in the name This card is quite spirited, related to the Hasspirits attribute, which is also a trait of whales",
    ),
    # Underspike 💀🐭🔰🦔🧺🐩 6p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Underspike",
            power=6,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Spines,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description="relates to the Underdog skill and the fact that the card has Spines The high health is symbolized in the name and the fact that it is somewhat expensive to play",
    ),
    # Earthhog  6p 2h
    # costs: - has: 🔥👻👻 pot: 25
    Blueprint(
        original=Card(
            name="Earthhog",
            power=6,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="relates to the low power, low costs, and high health attributes of the card The name also sounds like a creature that is slow but tough, which matches the Armadillolike nature of the card",
    ),
    # Necrolion 💀🐭🧺 8p 4h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Necrolion",
            power=8,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility, skills.Packrat],
        ),
        description="related to death and high power",
    ),
    # Phoenixley 🐭 3p 3h
    # costs: 🔥 has: 🔥👻👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Phoenixley",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="related to fire and fertility, but also a smallish animal",
    ),
    # Chimairicorn 🐩🔰💀🚀🐭🧺 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Chimairicorn",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="related to a chimera, uses both spirits and fire, strong and has many skills",
    ),
    # Turtletuff 🔰 3p 1h
    # costs: - has: 🔥👻 pot: 23
    Blueprint(
        original=Card(
            name="Turtletuff",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="related to a turtle, good at defense, and has high health",
    ),
    # Spikedon 🧺🐭🦔💀🔰 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Spikedon",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Spines,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="related to spines, a strong animal with high health and many skills",
    ),
    # Skysnake 🐭💀🔰🐩 5p 4h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Skysnake",
            power=5,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="relates to the skills InstantDeath and Soaring, which suggest quick movement and deadly force The high fire cost also hints at an exotic and rare creature that could live in the skies",
    ),
    # Moonbeast 🔰🧺🐭 5p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Moonbeast",
            power=5,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Shield, skills.Packrat, skills.Fertility],
        ),
        description="relates to the high health and packrat skill, which suggest a fortified creature that is hard to take down and can store things The low spirit cost and higher fire cost suggest a darker, less common creature that may be more active at night",
    ),
    # Hedgehog 🐭🪁🔰 2p 4h
    # costs: 🔥 has: 👻 pot: 26
    Blueprint(
        original=Card(
            name="Hedgehog",
            power=2,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility, skills.Soaring, skills.Shield],
        ),
        description="relates to the Shield skill and high health, which suggest a creature that is heavily armored and hard to pierce The low power and fire cost suggest a small, but resilient creature that can protect itself from attacks",
    ),
    # Infernowl 💀🐩🪁🔰🐭 6p 4h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Infernowl",
            power=6,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Soaring,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="relating to fire and spirits, the owl aspect could relate to the InstantDeath skill",
    ),
    # Gryffmouse 💀🔰🐭🚀🧺🦔 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Gryffmouse",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Airdefense,
                skills.Packrat,
                skills.Spines,
            ],
        ),
        description="relating to the mouse aspect, with traits of a griffin emphasized due to the high powerhealth, and the Spines and Airdefense skills",
    ),
    # Thornhedge 🔰🧺🐭🦔🐩 8p 5h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Thornhedge",
            power=8,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.Spines,
                skills.Underdog,
            ],
        ),
        description="relating to the Spines and Shield skills, as well as the low cost and high health",
    ),
    # Moongon 🔰🐭🐩💀🪁🧺 6p 6h
    # costs: 👻👻 has: 🔥🔥🔥🔥👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Moongon",
            power=6,
            health=6,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Soaring,
                skills.Packrat,
            ],
        ),
        description="relating to the Fertility skill and the fact that it requires spirits to play, with the InstantDeath and Packrat skills adding some mystery",
    ),
    # Blinkrat 🧺🔰🐭🐩 4p 3h
    # costs: 🔥 has: 🔥 pot: 35
    Blueprint(
        original=Card(
            name="Blinkrat",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.Underdog],
        ),
        description="relating to the speed implied by the Packrat and Shield skills, as well as the low spirit cost",
    ),
    # Flameox 🔰🐭🧺 4p 8h
    # costs: 🔥🔥🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Flameox",
            power=4,
            health=8,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description="relates to the fire cost and hasfire attribute, while also fitting with the high power and health The skills make it sound powerful and strongwilled, and the ox is a strong, sturdy animal",
    ),
    # Fiend 💀 1p 1h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Fiend",
            power=1,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.InstantDeath],
        ),
        description="low powerhealth and high costs equate to a small, weak creature that requires a lot to play The Instant Death skill matches its malevolent nature, and fiends are often associated with devils and demons, creatures of the underworld",
    ),
    # Luckviper 🍀💀🐭 2p 6h
    # costs: 🔥🔥 has: 🔥👻 pot: 28
    Blueprint(
        original=Card(
            name="Luckviper",
            power=2,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.LuckyStrike, skills.InstantDeath, skills.Fertility],
        ),
        description='the skills, especially Lucky Strike, imply a strong amount of unpredictability and "luck" Viper relates to its sneakiness and agility, while the low power but high health give it a laconic but dangerous appearance',
    ),
    # Aerohawk 🪁🧺💀 10p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Aerohawk",
            power=10,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Soaring, skills.Packrat, skills.InstantDeath],
        ),
        description='related to "Soaring" skill, high power and decent health, expensive',
    ),
    # Flamehorse 🐭🔰🐩 3p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Flamehorse",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Fertility, skills.Shield, skills.Underdog],
        ),
        description='related to "Fertility" and "Underdog" skills, high health but low power and cost, highly spirited',
    ),
    # Specterowl 💀🐩🐭🧺 3p 3h
    # costs: 👻👻👻👻👻👻👻👻👻👻 has: 🔥👻 pot: 26
    Blueprint(
        original=Card(
            name="Specterowl",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=10,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description='related to "InstantDeath" and "Packrat" skills, low power and cost but high spirits, has some spirits and no fire',
    ),
    # Glowsaur 🧺🐭💀 7p 6h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Glowsaur",
            power=7,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.InstantDeath],
        ),
        description='related to "Packrat" and "InstantDeath" skills, high powerhealth but no skills, moderate cost and spirits',
    ),
    # Thornboar 🧺🐭🦔🔰 9p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Thornboar",
            power=9,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=6,
            has_fire=4,
            skills=[skills.Packrat, skills.Fertility, skills.Spines, skills.Shield],
        ),
        description="relates well to the spines and shield skill, as well as high power and health",
    ),
    # Enchantrix 💀🧺🔰🐭 3p 10h
    # costs: 👻👻 has: 🔥🔥🔥👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Enchantrix",
            power=3,
            health=10,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="has high spirit count and fertility skill, also fits with the instant death and shield",
    ),
    # Fireimpala 🐭 3p 2h
    # costs: 🔥🔥 has: 🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Fireimpala",
            power=3,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="relates to fire cost and low health, as well as the fertility skill",
    ),
    # Beastchamp 💀🐭 9p 5h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Beastchamp",
            power=9,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="high power, relatively low cost and the instant death skill made me think of a powerful champion",
    ),
    # Shadowpike 🔰💀🐭🐩🧺 3p 6h
    # costs: - has: 🔥🔥🔥👻👻👻👻👻 pot: 60
    Blueprint(
        original=Card(
            name="Shadowpike",
            power=3,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description="has instant death and underdog skill, as well as high spirit count",
    ),
    # Whelpix  3p 1h
    # costs: 👻👻👻👻👻 has: 🔥👻 pot: 4
    Blueprint(
        original=Card(
            name="Whelpix",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=5,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="This card has low power and health, no fire requirements, and low spirit requirements However, it has all of its spirit requirements and no weaknesses The name Whelpix describes a small, magical creature that is easy to care for but still needs attention",
    ),
    # Shieldlynx 🔰💀🐭🐩🧺 4p 5h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Shieldlynx",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description="With an even mix of fire and spirit requirements, this card has average power and health values but also has a range of skills making it adaptable to different situations The name Shieldlynx suggests a sturdy creature with sharp reflexes to avoid danger",
    ),
    # Gorgonmole 🐭💀🧺🔰🐩 9p 6h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 63
    Blueprint(
        original=Card(
            name="Gorgonmole",
            power=9,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="With high power and good health values, as well as a range of skills, this card is a fairly strong allrounder The mole part of the name, however, emphasizes its lack of fire requirements The Gorgon aspect adds a feeling of danger and awe",
    ),
    # Shielddrake 🔰🐭🧺🪁🦔💀 6p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Shielddrake",
            power=6,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.Spines,
                skills.InstantDeath,
            ],
        ),
        description="The card has high power and health, giving it a tanklike quality It also has the skills Shield and Packrat, so the name Shielddrake conveys both its defensive capabilities and toughness",
    ),
    # Faelemur 🧺🐭 3p 2h
    # costs: 👻👻👻 has: 🔥🔥 pot: 21
    Blueprint(
        original=Card(
            name="Faelemur",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Packrat, skills.Fertility],
        ),
        description='The card doesn\'t have high power or health but is cheap to play and has the Packrat and Fertility skills Lemurs are small and quick, fitting the attributes of the card The "Fae" part alludes to its fertility, tying in with the Fertility skill',
    ),
    # Skyraven 🪁🐭 6p 2h
    # costs: 👻👻👻 has: 🔥👻 pot: 22
    Blueprint(
        original=Card(
            name="Skyraven",
            power=6,
            health=2,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Soaring, skills.Fertility],
        ),
        description="The card has high power and the soaring skill, and combined with the Fertility skill, the name Skyraven suits it perfectly Ravens are usually associated with black magic, which complements the Soaring skill well",
    ),
    # Deathant 💀 2p 2h
    # costs: 🔥🔥🔥 has: 🔥👻👻 pot: 13
    Blueprint(
        original=Card(
            name="Deathant",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="The card has low power and health but has the InstantDeath skill, and since it's also expensive to play, the name Deathant suggests that it's not a card to be ignored The \"ant\" part of the name denotes its small size and low power and health, while also tying in with the InstantDeath skill",
    ),
    # Skysphinx 🔰💀🪁🐭🧺 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Skysphinx",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Soaring,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="This card has high power and health with a good balance of fire and spirit costs The skills it possesses  Shield, InstantDeath, Soaring, Fertility, Packrat  suggest a regal and powerful creature, and the name fits with that image",
    ),
    # Thornfalcon 🔰🐭🦔🪁🚀🧺 8p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Thornfalcon",
            power=8,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Spines,
                skills.Soaring,
                skills.Airdefense,
                skills.Packrat,
            ],
        ),
        description="This card has high power and health, low costs, and a good mix of Fire and Spirit The skills suggest a creature that can both defend itself with Shield and Spines, while also attacking with Soaring and Airdefense Thornfalcon, while simple, fits the card's aggressive and dangerous nature",
    ),
    # Flamegull  2p 4h
    # costs: 🔥🔥🔥🔥 has: 🔥 pot: 7
    Blueprint(
        original=Card(
            name="Flamegull",
            power=2,
            health=4,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="This card is cheap and has a low power and health, but its Fire cost is high The lack of skills suggests a basic Fire creature, and Flamegull fits with that theme The name also suggests a creature that swoops in quickly, which fits the card's cheap cost",
    ),
    # Thunderlion 💀🪁🧺🐩🐭🔰 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Thunderlion",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Soaring,
                skills.Packrat,
                skills.Underdog,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="This card has high power and health, with a low cost and good balance of Fire and Spirit The skills suggest a creature that's powerful and can protect itself with Shield and Soaring while also attacking with InstantDeath and Packrat Thunderlion fits with the card's powerful nature and the Thunder aspect fits with both InstantDeath and Soaring",
    ),
    # Miracle  2p 4h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 12
    Blueprint(
        original=Card(
            name="Miracle",
            power=2,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[],
        ),
        description="relates to its low powerhealth, high costs of fire, but also its minor spirit attribute and lack of special skills, which can be interpreted as being a wildcard or miracle card",
    ),
    # Skyscribe 🐭🧺🪁 3p 3h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Skyscribe",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat, skills.Soaring],
        ),
        description="related to Soaring skill and its dual firespirit attribute focus, high spirit attribute, and decent health and power",
    ),
    # Sporehawk 🐭 2p 5h
    # costs: 🔥 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Sporehawk",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="the name suggests something mystical and otherworldly, which is suitable for a card that has the ability to boost fertility The combination of moderate power and health and low cost make the Sporehawk a versatile bird for any deck",
    ),
    # Batragon  2p 2h
    # costs: 🔥 has: - pot: 6
    Blueprint(
        original=Card(
            name="Batragon",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[],
        ),
        description="the name evokes a fantastical monster with the impressive health for such a small animal, but not so much when it comes to power Its low cost and lack of fire and spirit attributes translate into a creature that can hold up against attacks but doesn't pack much of a punch",
    ),
    # Firemouse 🐭 1p 2h
    # costs: 🔥🔥🔥 has: 🔥 pot: 11
    Blueprint(
        original=Card(
            name="Firemouse",
            power=1,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="a tiny creature that has mighty fertility powers, but otherwise is not very impressive, with low power and health and a high spirit cost Its name and lack of fire attribute suggests that it is not a creature that is directly moving towards a target, but rather running away from danger",
    ),
    # Spikedillo 🐩🦔 1p 4h
    # costs: 👻👻👻 has: 🔥👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Spikedillo",
            power=1,
            health=4,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Underdog, skills.Spines],
        ),
        description="a creature that combines decent health with low power, but has strong defensive capabilities with the presence of both spines and the underdog skill Its high spirit cost and ability to regenerate spirit suggest a creature that is tough and perhaps selfsufficient",
    ),
    # Festyte 💀🐩🔰🐭🧺🦔 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Festyte",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.Spines,
            ],
        ),
        description="a creature with impressive health and power, but also an imposing cost and many powerful skills, including instant death and shield The name evokes something of a demonic creature, which fits the theme of a powerful and expensive card",
    ),
    # Raccoons 🔰🧺 4p 5h
    # costs: 🔥 has: 👻 pot: 27
    Blueprint(
        original=Card(
            name="Raccoons",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Shield, skills.Packrat],
        ),
        description="medium powerhealth, shielding, hoarding",
    ),
    # Leolynn 🐭🐩💀🧺🔰 5p 9h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Leolynn",
            power=5,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="high health, fertility, underdog, elementneutral",
    ),
    # Pangrizzly 🧺🦔🔰 7p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Pangrizzly",
            power=7,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.Spines, skills.Shield],
        ),
        description="high powerhealth, spines, shielding, fire element",
    ),
    # Thornbee 🔰💀🧺🐭🐩🦔 4p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Thornbee",
            power=4,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="packrat, instant death, fertility, low powerhealth",
    ),
    # Sea Serpent  0p 3h
    # costs: 🔥 has: 🔥👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Sea Serpent",
            power=0,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="high health, aquatic, some spirit, no fire",
    ),
    # Deathstalker 💀🐭 8p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 36
    Blueprint(
        original=Card(
            name="Deathstalker",
            power=8,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="high power, instant death skill, fertility skill, fire and spirit cards required",
    ),
    # Pack Mongoose 🐭🦔🔰💀🐩🧺 8p 9h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 80
    Blueprint(
        original=Card(
            name="Pack Mongoose",
            power=8,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description="multiple skills, high stats, requires both spirits and fire cards",
    ),
    # Packophage 🧺🐭💀 3p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Packophage",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.Packrat, skills.Fertility, skills.InstantDeath],
        ),
        description="relates to the Packrat skill and its ability to collect items phage making it sound like an animal with a tendency to consume things",
    ),
    # PorcuniDefender 🔰🦔🐭🐩 3p 5h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="PorcuniDefender",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.Spines, skills.Fertility, skills.Underdog],
        ),
        description='relates to the Porcupine card that has similar health and spines skill ni as a suffix reminiscent of Latin language that relates to the fact that the card is very defensive, and sounds like porcine, which means "like a pig"',
    ),
    # Scissoright 💀🧺 6p 6h
    # costs: 🔥 has: 🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Scissoright",
            power=6,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="relates to the InstantDeath skill and the razorsharp claws of the animal right as a suffix, which implies that it is the right card to play, sounds catchy, and sounds like scissor and righteous",
    ),
    # Chimertaur 🐭🧺🐩💀🪁🔰 7p 9h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Chimertaur",
            power=7,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Underdog,
                skills.InstantDeath,
                skills.Soaring,
                skills.Shield,
            ],
        ),
        description="relates to multiple skills and the fact that the card is very strong Chimera  taur implying the card has parts of beasts, taur being reminiscent of centaur, which often symbolizes strength",
    ),
    # Armordillar  7p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 17
    Blueprint(
        original=Card(
            name="Armordillar",
            power=7,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[],
        ),
        description="relates to the high health and armored aspect of the card ar making it sound like an animal with a similar body shape to an armadillo, but with armor instead of tough skin",
    ),
    # Saphirion 🐩🐭💀🔰 6p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Saphirion",
            power=6,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="related to sapphire, which is blue, a shield, and magical, which this card also reflects with its high health, shield skill and overall powerfulness",
    ),
    # Starwing 🪁💀🔰🧺🐭🐩 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Starwing",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Soaring,
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="this card is the most costly in terms of fire and spirits, and its Soaring skill reflects that The name suggests a majestic and very powerful creature with fire power",
    ),
    # Stonehide 🐭🔰💀 3p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Stonehide",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=6,
            skills=[skills.Fertility, skills.Shield, skills.InstantDeath],
        ),
        description="related to high health and shield skill",
    ),
    # Nineclaws 🐩🔰🧺🪁💀🐭 7p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Nineclaws",
            power=7,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.Packrat,
                skills.Soaring,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="related to high power and packrat skill",
    ),
    # Skycharger 💀🐩🔰🧺🐭 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Skycharger",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="related to high spirit and fire costs",
    ),
    # Thornpaw 🐩🔰🐭🦔🧺💀 7p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Thornpaw",
            power=7,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
                skills.Spines,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="related to spines and underdog skill",
    ),
    # Funguspike 🐭🧺 5p 3h
    # costs: 🔥 has: 👻 pot: 27
    Blueprint(
        original=Card(
            name="Funguspike",
            power=5,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="related to low fire costs and fertile skill",
    ),
    # Miramoth 💀🔰🧺🐭 5p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Miramoth",
            power=5,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description='With high power and health, this fantastical creature has a balance of fire and spirits, and comes equipped with several skills including "Instant Death" and "Fertility" The name "Miramoth" implies an elegant and magical nature, befitting of such a formidable legendary warrior',
    ),
    # Fangiant 💀 3p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 16
    Blueprint(
        original=Card(
            name="Fangiant",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='With a higher power than health, Fangiant comes in at a moderate cost and is equipped with the skill "Instant Death" The name "Fangiant" nods to the Creature\'s largerthanlife reputation for being a powerful and deadly predator',
    ),
    # Pyrocat 🧺 1p 5h
    # costs: - has: 🔥🔥 pot: 26
    Blueprint(
        original=Card(
            name="Pyrocat",
            power=1,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Packrat],
        ),
        description='With increased fire but no spirits, this card also has no cost and is equipped with a pack rat skill The name "Pyrocat" references its affinity for fire and strong feline characteristics',
    ),
    # Shieldfle 🔰 10p 1h
    # costs: 🔥 has: - pot: 24
    Blueprint(
        original=Card(
            name="Shieldfle",
            power=10,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Shield],
        ),
        description='With the skill "Shield" and a high health attribute compared to other creature cards, Shieldfle is designed to protect your other creatures The name "Shieldfle" plays off the card\'s defensive nature and evokes images of a small, agile creature like a flying insect',
    ),
    # Grimbear 🐭🔰💀🧺🐩 8p 6h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 60
    Blueprint(
        original=Card(
            name="Grimbear",
            power=8,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description='The final card in our deck is a fortified and wellrounded warrior, with high power and health, several skills like "Fertility" and "Shield," and mostly fire and spirits The name "Grimbear" implies a fierce and resilient predator, while still nodding to its ursine form',
    ),
    # Shieldback 🔰💀🧺 2p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Shieldback",
            power=2,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Shield, skills.InstantDeath, skills.Packrat],
        ),
        description="high health and power, expensive, Shield skill, Packrat skill, InstantDeath skill",
    ),
    # Packweasel 🐭🧺💀🔰 3p 3h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Packweasel",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="balanced stats, high Spirits, Fertility skill, Packrat skill, InstantDeath skill, Shield skill",
    ),
    # Sproutling 🐭 1p 1h
    # costs: 👻👻👻 has: 🔥👻 pot: 10
    Blueprint(
        original=Card(
            name="Sproutling",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="low power and health, but has Fertility skill, and high Spirits",
    ),
    # Doomfalcon 💀🔰🪁 3p 6h
    # costs: 🔥 has: 🔥👻 pot: 30
    Blueprint(
        original=Card(
            name="Doomfalcon",
            power=3,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Shield, skills.Soaring],
        ),
        description="powerful, high health, Shield, Soaring, and deadly InstantDeath skill",
    ),
    # Nectarfox 🐭💀🔰 4p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Nectarfox",
            power=4,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="high power, moderate health, Fertility skill, and highly spirited",
    ),
    # Thornwyrm 🦔🐩🐭 3p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Thornwyrm",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Spines, skills.Underdog, skills.Fertility],
        ),
        description="high health, Spines and Underdog skills, and overall a tough and slow creature with a strong defense",
    ),
    # Firebud  3p 1h
    # costs: 🔥 has: 🔥🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Firebud",
            power=3,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="low power, low health, but with a low costsfire and high hasfire stats, and no skills",
    ),
    # Dustrhino 🐭💀🧺🔰🐩🦔 8p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="Dustrhino",
            power=8,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="very high power and health, with a variety of skills Fertility, Shield, Packrat, Spines, InstantDeath, and Underdog, but at a high fire cost",
    ),
    # FertilityHawk 🐭💀🪁🔰 1p 1h
    # costs: 🔥 has: 🔥👻 pot: 26
    Blueprint(
        original=Card(
            name="FertilityHawk",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Soaring,
                skills.Shield,
            ],
        ),
        description='The name fits the card as it has the skill Fertility and has a low cost in fire spirits The "Hawk" part of the name references the Soaring skill, which enables the card to attack flying creatures as well as ground creatures',
    ),
    # FrostRhino 💀🐭🪁 6p 7h
    # costs: 🔥 has: 🔥👻 pot: 39
    Blueprint(
        original=Card(
            name="FrostRhino",
            power=6,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Fertility, skills.Soaring],
        ),
        description='With very high health and decent power, the card name needs to express strength "Frost" gives a sense of a big, scary, and almost unreachable animal The "Rhino" part of the name emphasizes the high value of health attribute of this creature, and its skill Soaring',
    ),
    # AuraFrog  2p 1h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 8
    Blueprint(
        original=Card(
            name="AuraFrog",
            power=2,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[],
        ),
        description='A small and cheap creature that benefits from spirits, the name needed to reflect its low cost "Aura" represents its low cost in spirits and "Frog" brings to mind small size and weaker power attributes',
    ),
    # ShieldedBear 🔰🚀🧺💀🦔🐭 7p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="ShieldedBear",
            power=7,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Airdefense,
                skills.Packrat,
                skills.InstantDeath,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description='A very strong creature with the Shield skill, the name reflects the high power and skill attributes "Bear" tells us that it is a big and strong animal and "Shielded" shows us the skill the card has',
    ),
    # ThornWeasel 🧺💀🐭 2p 2h
    # costs: 🔥 has: 👻 pot: 26
    Blueprint(
        original=Card(
            name="ThornWeasel",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat, skills.InstantDeath, skills.Fertility],
        ),
        description='With a relatively low attribute range in both power and health, this creature needs a name that balances its strengths and weaknesses "Thorn" refers to the skill Spines and "Weasel" reflects the lower attributes and faster and smaller size of this creature',
    ),
    # Luminwolf 🔰🐭💀 8p 4h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Luminwolf",
            power=8,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="very powerful, costs fire, shield, fertility, instant death",
    ),
    # Shakitail  1p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 4
    Blueprint(
        original=Card(
            name="Shakitail",
            power=1,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="The name suggests a small and nimble creature with a sharp or dangerous tail, fitting for a creature with low power and health but high fire costs",
    ),
    # Fertigiant 🧺🔰🐭 2p 8h
    # costs: 🔥 has: 👻 pot: 36
    Blueprint(
        original=Card(
            name="Fertigiant",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description='This name combines "fertility" with "giant," fitting for a creature with high health and three fertility skills The name also suggests a large and powerful creature, fitting for a card with decent power',
    ),
    # Aquaspark 🧺🔰🐭 3p 7h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Aquaspark",
            power=3,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="This fantastical animal has five in each attribute that suggests balance, but also cheapness in terms of mana cost The skills Packrat, Shield, and Fertility paint a creature with a horde of children to carry around objects along with its high health and good combat abilities",
    ),
    # Raccofence 🐭🦔🧺 3p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Raccofence",
            power=3,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=5,
            skills=[skills.Fertility, skills.Spines, skills.Packrat],
        ),
        description="the cost of one fire mana and high fire points on this creatureinspired name suggest somewhat of an attachment to fire in nature At the same time, its immense power is in balance with a not so high health, still enough for a creature of its class Spines, Packrat, and Fertility are the skills possessed by this card, and suggest a creature that can harm back when attacked, but also reproduces rapidly, thus will never run out of resources",
    ),
    # Dragonlet 🔰🪁💀🧺🐭 3p 4h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Dragonlet",
            power=3,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Shield,
                skills.Soaring,
                skills.InstantDeath,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="This card has mediocre values for all attributes, but a wide range of skills The name \"Dragonlet\" suggests a small and young dragon, which matches the card's low power and health The card's unique set of skills may be interpreted as undeveloped powers that a young dragon might possess",
    ),
    # Skullwhip 🔰🐭💀🧺🦔 3p 4h
    # costs: - has: 🔥🔥🔥👻👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Skullwhip",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Spines,
            ],
        ),
        description='This card has good power and health for its cost, and a substantial amount of fire and spirit mana The name "Skullwhip" sounds menacing and dangerous, fitting for a strong and efficient card The name also hints towards the card\'s skill Spines, which could be interpreted as thornlike appendages that could be seen as a "whip"',
    ),
    # Aquafin 🐭💀🦔 3p 10h
    # costs: 👻👻👻👻👻👻 has: 🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Aquafin",
            power=3,
            health=10,
            costs_fire=0,
            costs_spirits=6,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.InstantDeath, skills.Spines],
        ),
        description="This card has excellent health but lower power, and much of its mana is tied to spirits The name \"Aquafin\" references aquatic creatures like dolphins or sharks but adds a mythical twist to it, fitting for the game's theme The name also alludes to the card's focus on spirits, as it is associated with water and fluidity",
    ),
    # Serpentaur 🔰🐩💀🧺 9p 7h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Serpentaur",
            power=9,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description='This card has very high values for power and health but comes with a relatively high cost The name "Serpentaur" combines the mythical creatures of serpents and centaurs, and these creatures should both evoke imagery of strength, flexibility, and power, all attributes that fit this card',
    ),
    # Blazeclaw 🔰🐭🧺💀🐩 6p 6h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Blazeclaw",
            power=6,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
                skills.Underdog,
            ],
        ),
        description='This card has good values for both power and health and a reasonable balance of fire and spirit mana The name "Blazeclaw" brings together two strong and aggressive words and feels fitting for a card that focuses on attacking The name also alludes to the card\'s skill Fertility, as claws could be seen as a metaphor for growth and life',
    ),
    # Thunderbeak 🔰🪁🐭💀 9p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="Thunderbeak",
            power=9,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Soaring,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="high powerhealth, fireheavy, spiritheavy, with skills such as Shield, Soaring, Fertility, and InstantDeath",
    ),
    # Direwolf 🐭💀 7p 8h
    # costs: 👻👻👻👻 has: 🔥🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Direwolf",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="high health, spiritheavy, with the Fertility and InstantDeath skills",
    ),
    # Luckyhippo 🐭💀🧺🐩🔰🍀 8p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 75
    Blueprint(
        original=Card(
            name="Luckyhippo",
            power=8,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Underdog,
                skills.Shield,
                skills.LuckyStrike,
            ],
        ),
        description="high powerhealth, spiritheavy, with a range of skills including Fertility, InstantDeath, Packrat, Underdog, Shield, and LuckyStrike",
    ),
    # Firecrustacean  2p 1h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 4
    Blueprint(
        original=Card(
            name="Firecrustacean",
            power=2,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="low powerhealth, fireheavy, no skills",
    ),
    # Packelephant 🔰💀🧺🍀🐭 5p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Packelephant",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
                skills.LuckyStrike,
                skills.Fertility,
            ],
        ),
        description="very powerful, highly spirited, many different skills, packlike animal",
    ),
    # Spikewyvern 🦔🐭🐩🧺💀🔰 10p 7h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 80
    Blueprint(
        original=Card(
            name="Spikewyvern",
            power=10,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="extremely strong, high health, spines and wings, mythical creature",
    ),
    # Fertilechimera 🐭💀🔰🧺🦔 3p 5h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Fertilechimera",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Spines,
            ],
        ),
        description="relatively strong, various skills including fertility, mythical creature made up of many animals",
    ),
    # Fiercecat  1p 1h
    # costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Fiercecat",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=4,
            skills=[],
        ),
        description="small, low powerhealth, but with a fiery spirit and fierce loyalty to fire element",
    ),
    # Skyling 🪁 2p 2h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 13
    Blueprint(
        original=Card(
            name="Skyling",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Soaring],
        ),
        description="moderately powerful, lowmoderate health, with the special skill of flying",
    ),
    # Spikeonyx 🦔 3p 2h
    # costs: 🔥 has: 👻 pot: 11
    Blueprint(
        original=Card(
            name="Spikeonyx",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Spines],
        ),
        description="moderate power and health, with tough defenses thanks to its spines, but with no fire element",
    ),
    # Glimmertalon 🐩🪁 10p 3h
    # costs: - has: 🔥🔥👻👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Glimmertalon",
            power=10,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=2,
            skills=[skills.Underdog, skills.Soaring],
        ),
        description="A magical birdlike creature known for its extraordinary speed and agility high power, low health, Underdog and Soaring skills",
    ),
    # Sparkweasel 🧺 2p 3h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Sparkweasel",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="A small and quick creature that can steal and hoard valuable resources low powerhealth, expensive to summon, Packrat skill",
    ),
    # Thornedon 🔰💀🧺 2p 8h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Thornedon",
            power=2,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.Shield, skills.InstantDeath, skills.Packrat],
        ),
        description="A large and powerful creature covered in razorsharp thorns high health, Shield, InstantDeath, and Packrat skills",
    ),
    # Sparkmoth 🧺 4p 3h
    # costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Sparkmoth",
            power=4,
            health=3,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="short and catchy, relates well with fire attribute and Packrat skill",
    ),
    # Nightcat 🧺🐭💀🔰 8p 6h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Nightcat",
            power=8,
            health=6,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description="relates to high powerhealth and the skill InstantDeath also has equal fire and spirits",
    ),
    # MysticKracken 🔰🐭💀🧺 9p 10h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 74
    Blueprint(
        original=Card(
            name="MysticKracken",
            power=9,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="high powerhealth, expensive, has shield, fertility, instant death, and packrat skills, which represent its mysterious and powerful nature",
    ),
    # Glowhare 🔰🐭 2p 1h
    # costs: 🔥🔥🔥🔥🔥 has: 🔥🔥 pot: 16
    Blueprint(
        original=Card(
            name="Glowhare",
            power=2,
            health=1,
            costs_fire=5,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility],
        ),
        description="low powerhealth, expensive, costs a lot of fire, has shield and fertility skills, which represent its magical and elusive nature",
    ),
    # StormFalcon 🐭🧺🪁🐩 4p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 55
    Blueprint(
        original=Card(
            name="StormFalcon",
            power=4,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Fertility, skills.Packrat, skills.Soaring, skills.Underdog],
        ),
        description="high health, costs no fire, has fertility, packrat, soaring, and underdog skills, which suggest an agile and fast creature that can navigate through storms",
    ),
    # FlameFerret 💀🐭🧺 6p 3h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 37
    Blueprint(
        original=Card(
            name="FlameFerret",
            power=6,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Fertility, skills.Packrat],
        ),
        description="high health, low power, costs little fire, has instant death, fertility, and packrat skills, suggesting a cute and deceptive creature that can distract and surprise its opponents with its fiery personality",
    ),
    # Flamalope 🐭🔰 4p 1h
    # costs: 🔥🔥🔥🔥🔥 has: 👻👻👻👻👻 pot: 22
    Blueprint(
        original=Card(
            name="Flamalope",
            power=4,
            health=1,
            costs_fire=5,
            costs_spirits=0,
            has_spirits=5,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield],
        ),
        description='The name derives from the words "flame" and "antelope" to represent a fiery and fast animal with low health and high power, that can also give birth to another Flamalope thanks to the Fertility skill, and protect itself with the Shield skill',
    ),
    # Pheonixsis 🔰🐭🐩 2p 10h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Pheonixsis",
            power=2,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Shield, skills.Fertility, skills.Underdog],
        ),
        description='The name is a play on "Phoenix" and "sister," indicating a creature with two types of fire costs and a high health stat, that can also protect allies with skills like Shield and provide a boost to weaker cards with Underdog, similar to how a supportive sister would act',
    ),
    # Armora 💀 2p 2h
    # costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 11
    Blueprint(
        original=Card(
            name="Armora",
            power=2,
            health=2,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='Short for "Armor Armadillo," this name represents a creature with defensive skills like Shield and Instant Death, as well as a balanced powerhealth stat, making it a sturdy defensive card that can also deal with threats',
    ),
    # Chimeraff 🐭🐩💀🔰 7p 10h
    # costs: 👻 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Chimeraff",
            power=7,
            health=10,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=7,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Shield,
            ],
        ),
        description='A combination of "Chimera" and "giraffe," the name reflects a creature with a variety of skills like Fertility, Underdog, and Instant Death, as well as high stats in both fire and spirit elements Like a giraffe with its long neck that can spot danger from afar, this card can adapt to different situations and circumstances',
    ),
    # Packiyote 🐭🔰🧺💀🐩🪁 4p 5h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Packiyote",
            power=4,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Underdog,
                skills.Soaring,
            ],
        ),
        description='A mix of "pack" and "coyote," this name represents a card with a variety of skills such as Fertility, Shield, and Instant Death, as well as a balanced powerhealth stat With a high number of both fire and spirit elements, it can work well in a variety of decks, just like a pack of coyotes that can adapt to different environments',
    ),
    # Mythimic 🐭🧺💀 9p 7h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Mythimic",
            power=9,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="high power and health, expensive, Fertility, InstantDeath, Packrat",
    ),
    # Lyrafang 🐭 3p 9h
    # costs: 🔥 has: 👻 pot: 28
    Blueprint(
        original=Card(
            name="Lyrafang",
            power=3,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Fertility],
        ),
        description="high health, low fire, Fertility",
    ),
    # Inferni 💀🧺 4p 3h
    # costs: 🔥🔥 has: 🔥👻👻👻👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Inferni",
            power=4,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=6,
            has_fire=1,
            skills=[skills.InstantDeath, skills.Packrat],
        ),
        description="high spirit, low fire, InstantDeath, Packrat",
    ),
    # Pumaflare 🐭💀🍀🐩 2p 9h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Pumaflare",
            power=2,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.LuckyStrike,
                skills.Underdog,
            ],
        ),
        description="high health, high spirit, low power, Fertility, InstantDeath",
    ),
    # Doomhare 💀🐭🧺 8p 10h
    # costs: 🔥🔥🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Doomhare",
            power=8,
            health=10,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[skills.InstantDeath, skills.Fertility, skills.Packrat],
        ),
        description="related to the high powerhealth and Instant Death skill",
    ),
    # Thriffler 🧺🍀💀🐭🔰🐩 9p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Thriffler",
            power=9,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.LuckyStrike,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Underdog,
            ],
        ),
        description="related to the Packrat skill and low costs",
    ),
    # Soarowl 🐭💀🪁🔰🧺 3p 3h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Soarowl",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Soaring,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="related to the Soaring skill and having spirits",
    ),
    # Armadig 🐭💀🧺🔰 4p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 65
    Blueprint(
        original=Card(
            name="Armadig",
            power=4,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="related to the Armadillo from example, but now with skills and higher power",
    ),
    # Shroomwolf 🔰🧺💀🐭🐩🦔 7p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Shroomwolf",
            power=7,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="medium powerhealthcosts, packrat skill, fertile, underdog",
    ),
    # Viper 🧺💀 7p 5h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Viper",
            power=7,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Packrat, skills.InstantDeath],
        ),
        description="medium power, low health, costs fire, instant death",
    ),
    # Shieldmouse 🐭🔰🧺💀 3p 4h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Shieldmouse",
            power=3,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="low power, medium health, high spirits, various skills including shield and fertility",
    ),
    # Shadowkraken 🐩💀🧺🔰 7p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Shadowkraken",
            power=7,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
            ],
        ),
        description="high powerhealth, moderate costspiritsfire, underdog and instant death skills, and shield and packrat skills",
    ),
    # Thornporc 🦔 2p 6h
    # costs: 🔥🔥🔥🔥 has: 🔥👻👻 pot: 15
    Blueprint(
        original=Card(
            name="Thornporc",
            power=2,
            health=6,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description="low power, moderate health, high fire cost, moderate spirits, and spines skill",
    ),
    # Sproutox 🐭🧺 3p 6h
    # costs: 🔥 has: 👻👻👻 pot: 30
    Blueprint(
        original=Card(
            name="Sproutox",
            power=3,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=0,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="moderate powerhealth, low costspiritsfire, fertility and packrat skills",
    ),
    # Solarbear 🐭🐩🦔 5p 8h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Solarbear",
            power=5,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[skills.Fertility, skills.Underdog, skills.Spines],
        ),
        description="related to the high health and power, and also the high fire attribute, which aligns with the sun and fire fertility and spines skills require good survival and defense",
    ),
    # Reaperfox 🐭🐩🧺🦔💀 5p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Reaperfox",
            power=5,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.Packrat,
                skills.Spines,
                skills.InstantDeath,
            ],
        ),
        description="related to the high power and health, and also the multiple skills including InstantDeath the packrat skill shows that it is tricky like a fox",
    ),
    # Golemantis 🐭💀🧺 8p 2h
    # costs: 👻👻👻👻 has: 🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Golemantis",
            power=8,
            health=2,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath, skills.Packrat],
        ),
        description="related to the high spirit attribute and very low health fertility and instant death skills align with mutation and speedy attacks",
    ),
    # Geckoon 🐩🧺🐭 3p 9h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 39
    Blueprint(
        original=Card(
            name="Geckoon",
            power=3,
            health=9,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Underdog, skills.Packrat, skills.Fertility],
        ),
        description="related to the relatively balanced attributes and multiple skills including packrat the underdog skill highlights how the gecko is often underestimated for its small size",
    ),
    # Fireshrew  2p 1h
    # costs: 🔥🔥🔥🔥 has: 🔥🔥 pot: 3
    Blueprint(
        original=Card(
            name="Fireshrew",
            power=2,
            health=1,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[],
        ),
        description="related to the high fire attribute and low overall stats lacking any skills, the name aligns with the small and quick shrew that might have a fiery personality",
    ),
    # Magmarmot 🔰🧺🐩🐭💀 3p 4h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Magmarmot",
            power=3,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Underdog,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description="The card has moderate power and health, but low fire and spirit costs, implying a resilient creature This monarch of the underground keeps its power chiefly for defensive purposes, using multiple skills to protect itself from harm",
    ),
    # Fenghuang 🐭🔰🦔🍀🪁💀 9p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Fenghuang",
            power=9,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Spines,
                skills.LuckyStrike,
                skills.Soaring,
                skills.InstantDeath,
            ],
        ),
        description="A legendary creature of immense beauty, the phoenixlike Fenghuang fits the bill of a card that has high power and health, with moderate fire and spirit costs It has multiple highlevel skills that set it apart from other cards, ideal for strategizing",
    ),
    # Icefawn 🧺🐭🐩 6p 3h
    # costs: 🔥 has: 🔥🔥🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Icefawn",
            power=6,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Packrat, skills.Fertility, skills.Underdog],
        ),
        description="This elegant and majestic animal that bears antlers can be a great asset to a player in the later stages of the game With moderate power and low costs, it has several good skills that require careful use and aid in hitting enemies below the belt",
    ),
    # Gorgonack 🧺🔰🐭🦔💀 7p 6h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Gorgonack",
            power=7,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
                skills.Spines,
                skills.InstantDeath,
            ],
        ),
        description="The card is a symbol of power and strength, high on health, moderately powered and expensive to play Luxuriant with several good skills, it can turn the odds in favor of players in risky situations",
    ),
    # Dryor 🔰🐭🧺🐩 5p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Dryor",
            power=5,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=5,
            has_fire=3,
            skills=[skills.Shield, skills.Fertility, skills.Packrat, skills.Underdog],
        ),
        description="With high health and moderate power, this creature has low fire costs but high spirit costs, which implies there is something special about the animal's inner qualities Its shieldbased skill set keeps it from getting hurt like other cards",
    ),
    # Shadowpuma 💀🔰🐩🐭🦔 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Shadowpuma",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="high powerhealth, expensive, InstantDeath, Shield, Spines",
    ),
    # Silverdragon 🔰🧺🚀💀🐭 8p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Silverdragon",
            power=8,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Airdefense,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="high powerhealth, highly spirited, Shield, Packrat, Airdefense, InstantDeath, Fertility",
    ),
    # Ironrhino 💀🔰🐭🐩 7p 4h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Ironrhino",
            power=7,
            health=4,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="high power, decent health, expensive, Fire attribute, InstantDeath, Shield, Fertility, Underdog",
    ),
    # Frostfly  1p 1h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Frostfly",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[],
        ),
        description="With its icy blue wings and sleek body, this fantastical insect is always on the move and packs a small but effective punch with its freezing powers Its four spirit points represent its nimbleness in the face of threats",
    ),
    # Underwolf 🐩🔰💀 2p 3h
    # costs: 🔥🔥 has: - pot: 22
    Blueprint(
        original=Card(
            name="Underwolf",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Underdog, skills.Shield, skills.InstantDeath],
        ),
        description='With the skills of Underdog, Shield, and InstantDeath, this wolf is not to be underestimated Its low cost points and lack of elemental affiliation suggest it is a fierce and scrappy fighter, with high health for its power level And don\'t forget about that deadly "InstantDeath" skill',
    ),
    # Thornmole 🐭 2p 4h
    # costs: 🔥 has: 🔥👻👻 pot: 20
    Blueprint(
        original=Card(
            name="Thornmole",
            power=2,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="With a mix of low power and expensive fire cost, this armored mole is built for endurance It boasts Fertility in its arsenal, which already offers some clues to its play style Its spikes indicate an aggressive side hidden underneath its tanklike exterior",
    ),
    # Magmabear 🐩🧺🔰🐭 6p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Magmabear",
            power=6,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[skills.Underdog, skills.Packrat, skills.Shield, skills.Fertility],
        ),
        description="This card has high power and health, and costs just one fire to play It has skills like Underdog, Packrat, Shield, and Fertility The name Magmabear is related to its fire attribute and its toughness, making it a formidable opponent on the battlefield",
    ),
    # Nimblynx 🧺🐭💀🔰🦔🐩 2p 5h
    # costs: 🔥 has: 🔥🔥👻👻 pot: 46
    Blueprint(
        original=Card(
            name="Nimblynx",
            power=2,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Shield,
                skills.Spines,
                skills.Underdog,
            ],
        ),
        description="Nimblynx has low power and health but is very agile, represented by its high Spirit attribute It also has multiple skills, including Packrat, Fertility, and Spines The name Nimblynx suggests fast and nimble movements, highlighting this card's quick speed and agility",
    ),
    # Ghostfox 🐭🐩💀 3p 3h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 31
    Blueprint(
        original=Card(
            name="Ghostfox",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Fertility, skills.Underdog, skills.InstantDeath],
        ),
        description="This card has moderate power and health, and costs one fire to play Its skills include Fertility, Underdog, and InstantDeath The name Ghostfox relates to its Underdog skill, and its Spirit attribute, which could represent its ethereal or ghostlike appearance",
    ),
    # Deathwisp 🐭💀 0p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Deathwisp",
            power=0,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="The card has high cost, high health and low power and belongs to the spirit category The card has fertility and instantdeath skills, hence the name Deathwisp  also fitting the magical and fantastical theme of the game",
    ),
    # Spirithare 🐭 1p 2h
    # costs: 👻👻👻👻 has: 🔥 pot: 10
    Blueprint(
        original=Card(
            name="Spirithare",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=4,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="The card has low power and medium health, very low fire, and high spirit values The card has fertility skills, hence the name Spirithare  a magical rabbitlike creature that brings life and spirits to the battlefield",
    ),
    # Packraven 🐭🧺🔰🪁 0p 3h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 27
    Blueprint(
        original=Card(
            name="Packraven",
            power=0,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.Shield, skills.Soaring],
        ),
        description="The card has low power, high health, medium fire, and high spirit values The card has multiple skills including fertility, packrat, shield and soaring, hence the name Packraven  a bird known for being a pack animal, intelligent and able to soar and protect its pack",
    ),
    # Warwisp 🔰🐭💀 5p 6h
    # costs: - has: 🔥🔥🔥🔥👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Warwisp",
            power=5,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[skills.Shield, skills.Fertility, skills.InstantDeath],
        ),
        description="The name alludes to its high power and unhealthy skills, the Warwisp's goal is to instantly cause death in battle",
    ),
    # Skyherd 🔰🐩🪁🐭🧺💀 8p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 69
    Blueprint(
        original=Card(
            name="Skyherd",
            power=8,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Underdog,
                skills.Soaring,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="It is a high spirited, strong, and skilled card The name refers to its Soaring and Fertility abilities, as well as its Packrat feature",
    ),
    # Gloommite 🐭🚀 0p 2h
    # costs: 🔥🔥 has: - pot: 10
    Blueprint(
        original=Card(
            name="Gloommite",
            power=0,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility, skills.Airdefense],
        ),
        description="It's a dark, lowpowered card with resilience and air defense skills The name matches the card's defense abilities and low attributes",
    ),
    # Feymonster 🧺🪁🐭 3p 5h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Feymonster",
            power=3,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Packrat, skills.Soaring, skills.Fertility],
        ),
        description="It is a small card with Soaring and Packrat skills, with a fair amount of attack and defense skill levels The name fits the card's multiple skill levels",
    ),
    # Arschield 🔰💀 3p 2h
    # costs: - has: 🔥👻 pot: 31
    Blueprint(
        original=Card(
            name="Arschield",
            power=3,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Shield, skills.InstantDeath],
        ),
        description="The name's German homophone means shielded back The name relates to the Shield ability and high health feature while keeping in mind the low attack power",
    ),
    # Bramblefox 🐭🐩 3p 2h
    # costs: 🔥 has: 🔥👻 pot: 21
    Blueprint(
        original=Card(
            name="Bramblefox",
            power=3,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility, skills.Underdog],
        ),
        description="Bramblefox represents the card's skill and attribute, with bramble representing its underdog skill, allowing it to strike back especially when odds are against it, while fox represents its overall attributes, with high power and low health",
    ),
    # Shadowhawk 🐭 2p 3h
    # costs: - has: 🔥👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Shadowhawk",
            power=2,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="Shadowhawk represents the card's overall attribute, with the card having high spirits but no fire element for its costs, making it more covert and ethereal, like a shadow that swoops in for its attack Hawk is seen as a powerful bird of prey, making it a good fit for the card's high power",
    ),
    # Sproutmole  2p 2h
    # costs: 👻👻👻👻👻👻 has: 🔥🔥 pot: 3
    Blueprint(
        original=Card(
            name="Sproutmole",
            power=2,
            health=2,
            costs_fire=0,
            costs_spirits=6,
            has_spirits=0,
            has_fire=2,
            skills=[],
        ),
        description="Sproutmole represents the card's spirit attribute and low overall cost, with the attribute name being indicative of the card's ability to regenerate thanks to its high spirit, while mole represents its average power and health attributes",
    ),
    # Armoshield 🔰🐩🧺 5p 3h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥 pot: 32
    Blueprint(
        original=Card(
            name="Armoshield",
            power=5,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=5,
            skills=[skills.Shield, skills.Underdog, skills.Packrat],
        ),
        description="related to the Shield skill, high health, low spirit, high fire cost",
    ),
    # Rosefinch 🔰 3p 3h
    # costs: 🔥 has: 🔥👻👻 pot: 18
    Blueprint(
        original=Card(
            name="Rosefinch",
            power=3,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description="relates to Shield skill, modest powerhealth, modest spirit, modest fire cost",
    ),
    # Soarsphinx 🍀🔰🐭🧺🪁💀 9p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Soarsphinx",
            power=9,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.LuckyStrike,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
                skills.InstantDeath,
            ],
        ),
        description="related to the Soaring skill, very high powerhealth, moderately high spirit, moderately high fire",
    ),
    # Ferretore 🐭🧺🔰 4p 5h
    # costs: 🔥 has: 🔥🔥🔥👻👻 pot: 38
    Blueprint(
        original=Card(
            name="Ferretore",
            power=4,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="related to Fertility and Packrat skills, modest powerhealthcost, low spirit",
    ),
    # Sandcat  3p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 7
    Blueprint(
        original=Card(
            name="Sandcat",
            power=3,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="relates to low powerhealth, high fire cost, no skills",
    ),
    # Faepegasus 🪁🔰🐭🐩💀 6p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Faepegasus",
            power=6,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Soaring,
                skills.Shield,
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
            ],
        ),
        description="A fantastical animal that is known for its strength, speed, and grace With a high power and health, combined with skills like Soaring and Shield, this card is like an unstoppable flying force on the battlefield",
    ),
    # Thornechidna 🧺 5p 5h
    # costs: - has: 🔥👻 pot: 33
    Blueprint(
        original=Card(
            name="Thornechidna",
            power=5,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description='With high powerhealth and Packrat skill, this card is ready to fight Its name combines "thorn" referring to its tough exterior, and "echidna" referring to a spiny anteater, which fits in with the Spines skill',
    ),
    # Ferrocub 🐭🧺 2p 4h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 40
    Blueprint(
        original=Card(
            name="Ferrocub",
            power=2,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description='A fantastical name suggesting an animal that\'s powerful and sturdy, which fits with the card\'s high power and health attributes "Ferro" comes from the Latin word for iron and suggests toughness, while "cub" connects with the card\'s fertility skill',
    ),
    # Skyhare 🚀 1p 1h
    # costs: 🔥 has: 🔥👻👻 pot: 6
    Blueprint(
        original=Card(
            name="Skyhare",
            power=1,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Airdefense],
        ),
        description='This name evokes a nimble and elusive animal, fitting for a card with the air defense skill The "Sky" part highlights its agility and the "Hare" part relates to its low power and health attributes',
    ),
    # Phoenixdrag 💀🔰🐩🧺🐭 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Phoenixdrag",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="This name combines the mythical creatures of phoenix and dragon, which correspond with the card's very high power and health attributes Additionally, the \"drag\" part relates to the card's instant death skill",
    ),
    # Seaurchin 💀 1p 5h
    # costs: 🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Seaurchin",
            power=1,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='This name connects with the card\'s instant death skill, which is represented by the sharp spines of a sea urchin The "Sea" part relates to the card\'s low spirit and fire attribute costs and the "Urchin" part fits with its low power attribute',
    ),
    # Bristlepuma 🐭💀🐩🧺 7p 6h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Bristlepuma",
            power=7,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description='A name that corresponds with the card\'s ability to both cause instant death and have high fertility "Bristle" plays on its spiky abilities, such as fertility and instant death, while "Puma" connects with its high power and health attributes',
    ),
    # Shadowcat This name suits the card as it is quite powerful in terms of its power and health Additionally its skills allow it to defend itself Shield gather resources Packrat and cause destruction InstantDeath The name Shadowcat invokes the image of a stealthy powerful and ready 🔰🧺🐭💀🦔🐩 8p 8h
    # costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 70
    Blueprint(
        original=Card(
            name="Shadowcat This name suits the card as it is quite powerful in terms of its power and health Additionally its skills allow it to defend itself Shield gather resources Packrat and cause destruction InstantDeath The name Shadowcat invokes the image of a stealthy powerful and ready",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Spines,
                skills.Underdog,
            ],
        ),
        description="forbattle creature",
    ),
    # Serpenthorn 💀🔰🧺🪁🐭🐩 8p 8h
    # costs: 👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Serpenthorn",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Soaring,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="high powerhealth, high costs, multiple skills",
    ),
    # Underdogger 🧺🐩 3p 3h
    # costs: 🔥🔥 has: 🔥👻 pot: 19
    Blueprint(
        original=Card(
            name="Underdogger",
            power=3,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat, skills.Underdog],
        ),
        description="low powerhealth, high costfire, packrat and underdog skills",
    ),
    # Flutterbite 💀🐭 7p 3h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Flutterbite",
            power=7,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Fertility],
        ),
        description="high power, low health, hasspirits, instant death and fertility skills",
    ),
    # Armorspirit 🐩🔰🐭🧺💀 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Armorspirit",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
                skills.Packrat,
                skills.InstantDeath,
            ],
        ),
        description="very strong and resilient, high hasspirits, multiple skills",
    ),
    # Flamelet  1p 3h
    # costs: 🔥 has: 🔥🔥👻 pot: 8
    Blueprint(
        original=Card(
            name="Flamelet",
            power=1,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[],
        ),
        description="low power, low health, low costsfire",
    ),
    # Firegriffin 🐭🔰🪁🐩💀 7p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Firegriffin",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Soaring,
                skills.Underdog,
                skills.InstantDeath,
            ],
        ),
        description="With high power and health, this card is a force to be reckoned with The fiery attribute values suggest a strong, aggressive animal, while the skill set shows it is resilient, with the ability to both protect itself and attack fiercely",
    ),
    # Lightfawn 🐩🧺💀 10p 5h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻 pot: 44
    Blueprint(
        original=Card(
            name="Lightfawn",
            power=10,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=4,
            skills=[skills.Underdog, skills.Packrat, skills.InstantDeath],
        ),
        description='This card\'s high power and low health suggest a fast, attacking animal The skill set includes underdog, which implies that this card is underestimated but has a lot of potential The name "Lightfawn" suggests a young, agile animal, while the costsfire attribute suggests it has a fiery or energetic nature',
    ),
    # Fertiletoad 🐭🧺 5p 10h
    # costs: 🔥🔥 has: 🔥🔥👻👻 pot: 41
    Blueprint(
        original=Card(
            name="Fertiletoad",
            power=5,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description='This card has high health but relatively low power, suggesting an animal that is hard to kill but not very aggressive The skill set includes Fertility, implying that this is an animal that is good at reproducing and propagating itself The name "Fertiletoad" suggests a creature that is both gross and useful, and may even have supernatural abilities',
    ),
    # Thornpuma 🐭🧺 3p 3h
    # costs: - has: 🔥🔥👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Thornpuma",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=2,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="With high power and health but low resource costs, this card is a formidable force to be reckoned with Its unique skills of Packrat and Fertility are reminiscent of a puma who guards its territory fiercely and makes efficient use of available resources",
    ),
    # Turtelon 💀🔰🐭 5p 5h
    # costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Turtelon",
            power=5,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=2,
            skills=[skills.InstantDeath, skills.Shield, skills.Fertility],
        ),
        description="relates to moderate powerhealth, costsfire, and the Shield skill",
    ),
    # Phoenixpaw 🦔🪁💀🧺🔰🐭 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 76
    Blueprint(
        original=Card(
            name="Phoenixpaw",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Spines,
                skills.Soaring,
                skills.InstantDeath,
                skills.Packrat,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="relates to very high powerhealth, a combination of skills, and the high hasspirits value",
    ),
    # Featherfly 🪁 4p 2h
    # costs: 👻 has: 👻 pot: 12
    Blueprint(
        original=Card(
            name="Featherfly",
            power=4,
            health=2,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Soaring],
        ),
        description="relates to low powerhealth, costsspirits, and the Soaring skill",
    ),
    # Thornet thornet 🦔 2p 1h
    # costs: 🔥🔥🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Thornet thornet",
            power=2,
            health=1,
            costs_fire=4,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Spines],
        ),
        description='This name comes from the combination of "thorn" and "hornet" The card has spines and high costs to play and represents a small, but painful enemy to defeat',
    ),
    # Shieldox shield  fox 🔰 5p 2h
    # costs: 🔥 has: 🔥👻👻 pot: 20
    Blueprint(
        original=Card(
            name="Shieldox shield  fox",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield],
        ),
        description='A fox is known for its agility, and with the Shield skill, this card can defend itself well The name "Shieldox" represents both the foxlike nature and the protective skill of the card',
    ),
    # Manticora manticore  ora 🔰🐭💀🪁🐩🦔 6p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Manticora manticore  ora",
            power=6,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Soaring,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description="The name is a combination of two mythological creatures, Manticores and Chimeras, and represents the strength and versatility of the card",
    ),
    # Ursulon ursus  lion 🔰🧺🐭💀🐩🦔 8p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 72
    Blueprint(
        original=Card(
            name="Ursulon ursus  lion",
            power=8,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
                skills.Spines,
            ],
        ),
        description='A lion is known for its strength and bravery, and a bear is known for its resilience and toughness The name "Ursulon" represents both of these attributes, making the card a formidable opponent',
    ),
    # Emberkin ember  kin 🐭 8p 7h
    # costs: 🔥🔥 has: 🔥🔥👻 pot: 35
    Blueprint(
        original=Card(
            name="Emberkin ember  kin",
            power=8,
            health=7,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=2,
            skills=[skills.Fertility],
        ),
        description='The card has high power, but only medium health, and has the Fertility skill, which represents its ability to create more cards The name "Emberkin" symbolizes the card\'s fiery nature and its familial ties to other cards it can create',
    ),
    # Thornrhino 🔰🚀🧺🪁💀🐭 8p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Thornrhino",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Shield,
                skills.Airdefense,
                skills.Packrat,
                skills.Soaring,
                skills.InstantDeath,
                skills.Fertility,
            ],
        ),
        description="This name suits the card as it has high power and health, but no special skills other than Shield and Airdefense The name invokes the image of a powerful and dangerous creature, with thorny attributes to match",
    ),
    # Infernoant 🐭💀 1p 5h
    # costs: 🔥 has: 🔥👻👻👻👻 pot: 28
    Blueprint(
        original=Card(
            name="Infernoant",
            power=1,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="The card has low power and high health, but has the InstantDeath skill, making it a dangerous card to face The name Infernoant invokes the image of a small but fiery creature, with the ability to cause destruction",
    ),
    # Stoneturtle  2p 2h
    # costs: 🔥🔥🔥 has: 🔥👻 pot: 6
    Blueprint(
        original=Card(
            name="Stoneturtle",
            power=2,
            health=2,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="This name suits the card as it has low power and health, but high fire costs and no special skills The name Stoneturtle invokes the image of a slow and heavily armored creature, with a tough shell to match",
    ),
    # Thornmantle 🦔🧺💀🔰 5p 7h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 45
    Blueprint(
        original=Card(
            name="Thornmantle",
            power=5,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Spines, skills.Packrat, skills.InstantDeath, skills.Shield],
        ),
        description="a fantastical creature with spines and shieldlike protection, as suggested by the skills Shield and Spines",
    ),
    # Nixieweasel 🧺💀🐭🐩 0p 1h
    # costs: 🔥 has: 🔥 pot: 24
    Blueprint(
        original=Card(
            name="Nixieweasel",
            power=0,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
            ],
        ),
        description="a small, elusive creature known for its ability to dodge and escape danger, as suggested by the skill Underdog and Packrat ",
    ),
    # Loxijumper 🐭💀🐩 3p 1h
    # costs: 🔥🔥 has: - pot: 22
    Blueprint(
        original=Card(
            name="Loxijumper",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility, skills.InstantDeath, skills.Underdog],
        ),
        description="a nimble creature with powerful legs that can escape quickly and jump over obstacles, as suggested by the Skill Fertility and the high cost in fire and the absence thereof in spirits and fire in the card's attributes",
    ),
    # Ghostelk 💀🐩🔰🐭 8p 5h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Ghostelk",
            power=8,
            health=5,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="a spectral creature with high spirits and a strong presence that is hard to kill, as suggested by the skills InstantDeath and Shield",
    ),
    # Quillhog 🐭💀 1p 8h
    # costs: 🔥 has: 🔥 pot: 29
    Blueprint(
        original=Card(
            name="Quillhog",
            power=1,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="This card has high health and low power, resembling a hedgehog with more defense qualities The card has no spirit but has a fire which relates to a 'spiky' character themed name This card's skills involve Fertility and InstantDeath, so the name Quillhog relates to the card's spiky porcupinelike defense mechanisms and also the deadly attribute of instant death",
    ),
    # Dustwing 🐭🚀💀🧺 1p 1h
    # costs: - has: 👻👻👻👻 pot: 35
    Blueprint(
        original=Card(
            name="Dustwing",
            power=1,
            health=1,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=0,
            skills=[
                skills.Fertility,
                skills.Airdefense,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="This card has no fire but has high spirit and very low power and health, representing a fragile creature thats good at air defense capabilities The skills involve Fertility, Airdefense, InstantDeath, and Packrat The name Dustwing relates to the card's fragility, lightness, and speed, and its air defenserelated skills",
    ),
    # Kodiak 🧺🐩🐭 5p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Kodiak",
            power=5,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=3,
            skills=[skills.Packrat, skills.Underdog, skills.Fertility],
        ),
        description="This card has high power and health with decent fire and spirit but is expensive to use The skills involve Packrat, Underdog, and Fertility The name Kodiak relates to the card's bearlike characteristics and strength",
    ),
    # Thornback Rhino 🧺🦔🔰💀🚀🐭 10p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 73
    Blueprint(
        original=Card(
            name="Thornback Rhino",
            power=10,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=8,
            has_fire=6,
            skills=[
                skills.Packrat,
                skills.Spines,
                skills.Shield,
                skills.InstantDeath,
                skills.Airdefense,
                skills.Fertility,
            ],
        ),
        description="This card is very powerful, has high health, and has significant fire and spirit The skills involve Packrat, Spines, Shield, InstantDeath, Airdefense, and Fertility, meaning the card has a lot of attributes The name Thornback Rhino relates to the card's dangerouslooking spines, strength, and rhinolike appearance",
    ),
    # Armadillox 🐩🔰💀🧺 2p 4h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 32
    Blueprint(
        original=Card(
            name="Armadillox",
            power=2,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[
                skills.Underdog,
                skills.Shield,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="high health, low cost, shield, packrat",
    ),
    # Phoenixwolf 💀🪁🔰🐭 5p 8h
    # costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻👻👻👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Phoenixwolf",
            power=5,
            health=8,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=7,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Soaring,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="expensive, high spirits and fire, soaring",
    ),
    # Spinebear 🦔🧺💀🐭🐩🔰 7p 9h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 68
    Blueprint(
        original=Card(
            name="Spinebear",
            power=7,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.Spines,
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Underdog,
                skills.Shield,
            ],
        ),
        description="very strong, spines, packrat, underdog, shield, fertility",
    ),
    # Fertifax 🐭🧺💀 3p 6h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 53
    Blueprint(
        original=Card(
            name="Fertifax",
            power=3,
            health=6,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=4,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="related to fertility and packrat skills and high spiritfire presence",
    ),
    # Flamestoat 💀 2p 3h
    # costs: 🔥 has: 🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Flamestoat",
            power=2,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="related to fire, small size, and instant death skill",
    ),
    # Sunnix 🐭💀 3p 1h
    # costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Sunnix",
            power=3,
            health=1,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="related to sun and fire, low health, high fire presence, and fertility skill",
    ),
    # Embersprite  1p 2h
    # costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 7
    Blueprint(
        original=Card(
            name="Embersprite",
            power=1,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[],
        ),
        description="related to fire, small size, and mediumhigh presence of spiritsfire",
    ),
    # Shieldmantis 💀🐭🔰 7p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 50
    Blueprint(
        original=Card(
            name="Shieldmantis",
            power=7,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.InstantDeath, skills.Fertility, skills.Shield],
        ),
        description="related to shield and armor skills, high powerhealth, and high presence of spirits and fire",
    ),
    # Fertilitydrake 🐭🔰🧺🦔🚀💀 6p 10h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 77
    Blueprint(
        original=Card(
            name="Fertilitydrake",
            power=6,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
                skills.Spines,
                skills.Airdefense,
                skills.InstantDeath,
            ],
        ),
        description="The card has high power and health and skills like Fertility, Shield, and Packrat Fertilitydrake implies the fertility of its abilities, and drake represents its high power and health",
    ),
    # Shadowlynx  2p 3h
    # costs: 🔥🔥 has: 🔥🔥 pot: 8
    Blueprint(
        original=Card(
            name="Shadowlynx",
            power=2,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=2,
            skills=[],
        ),
        description="The lowcost fire attribute and moderate power and health make the name Shadowlynx appropriate Lynx represents the moderate power and health, and Shadow symbolizes the lowcost fire attribute",
    ),
    # Infernoowl  5p 2h
    # costs: 🔥 has: 🔥👻 pot: 13
    Blueprint(
        original=Card(
            name="Infernoowl",
            power=5,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[],
        ),
        description="The card has a high power attribute and a low health attribute The name Infernoowl reflects its high power with the Inferno prefix, and its low health is associated with the owl, which is a bird of prey known for its vulnerability",
    ),
    # Pygmyonx 🔰💀🦔🐭 3p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Pygmyonx",
            power=3,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.InstantDeath,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description='This name references the fact that the card has low power and high health, as pygmy refers to something small but also sturdy The "onx" part of the name is a nod to the fact that the card has a lot of fire and spirit elements, which could be likened to onyx stones',
    ),
    # Packlynx 💀🐩🔰🧺🦔🐭 7p 8h
    # costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Packlynx",
            power=7,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=7,
            has_fire=6,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Packrat,
                skills.Spines,
                skills.Fertility,
            ],
        ),
        description="This name plays off the fact that the card has a lot of skills related to pack mentality eg Packrat, Underdog The lynx part references the high power and health of the card, as lynxes are known for their stealth and strength",
    ),
    # Beetlekin 🔰🐩💀 0p 1h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Beetlekin",
            power=0,
            health=1,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Shield, skills.Underdog, skills.InstantDeath],
        ),
        description='This name references the fact that the card is small and weak but has defensive abilities like Shield and Underdog The "beetle" part of the name could also relate to the Fire cost of the card, as beetles have a hard exterior that could be likened to fire',
    ),
    # Soarbear 💀🪁🐭🔰 8p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 59
    Blueprint(
        original=Card(
            name="Soarbear",
            power=8,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Soaring,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description='This name references the fact that the card has a lot of skills related to flying and movement eg Soaring, and also that it has a lot of spirit elements which could be likened to soaring through the air The "bear" part of the name references the high power and health of the card',
    ),
    # Salamanderix 🧺 4p 2h
    # costs: 🔥🔥 has: 🔥 pot: 14
    Blueprint(
        original=Card(
            name="Salamanderix",
            power=4,
            health=2,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="The name Salamanderix relates to the card's fire attribute and its packs rats skill The card also has balanced power and health which relates to the idea of a salamander being able to adapt and survive in different environments",
    ),
    # Skyjaguar 🧺💀🐭🔰 3p 4h
    # costs: - has: 🔥🔥🔥🔥👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Skyjaguar",
            power=3,
            health=4,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.Packrat,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
            ],
        ),
        description="The name Skyjaguar incorporates the card's high fire attribute, as well as its agility instant death skill and packrat skill The reference to the sky also relates to the card's high cost of fire",
    ),
    # Shieldermade 🐭💀🔰 8p 8h
    # costs: - has: 🔥🔥🔥👻👻👻 pot: 62
    Blueprint(
        original=Card(
            name="Shieldermade",
            power=8,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[skills.Fertility, skills.InstantDeath, skills.Shield],
        ),
        description="The name Shieldermade relates to the card's high defense attributes shield skill and the idea of a creature made for battle The lowcost fire and spirit attribute aligns with the idea of a creature made for defense rather than offense",
    ),
    # Chimerafin 💀🐭🧺🪁 9p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Chimerafin",
            power=9,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
                skills.Soaring,
            ],
        ),
        description="The name Chimerafin incorporates the card's high power and health attributes, as well as its ability to soar soaring skill The card also has a balanced mix of fire and spirit, which relates to the idea of a chimera being a mix of different creatures The inclusion of the packrat skill refers to the card's resourcefulness and ability to collect valuable items",
    ),
    # Shieldowl 🐩🐭🧺🔰 3p 3h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻 pot: 49
    Blueprint(
        original=Card(
            name="Shieldowl",
            power=3,
            health=3,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[skills.Underdog, skills.Fertility, skills.Packrat, skills.Shield],
        ),
        description="This name fits the card as it has skills that allow it to shield itself and gather resources while it can also defend itself with its high health The name is inspired by the image of a wise and powerful owl that always has its shield up to protect its allies",
    ),
    # Spinepuma 💀🔰🧺🐩🐭🦔 6p 5h
    # costs: 👻👻👻 has: 🔥🔥🔥🔥👻👻👻 pot: 54
    Blueprint(
        original=Card(
            name="Spinepuma",
            power=6,
            health=5,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=3,
            has_fire=4,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Underdog,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="This name suits the card as it is very powerful in terms of its power and health while also having a skill that adds spines to its arsenal, making it a fearsome attacker The name invokes the image of a sleek and dangerous puma covered in sharp spines",
    ),
    # Faelion 🐭🧺🦔🔰🐩💀 8p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Faelion",
            power=8,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Spines,
                skills.Shield,
                skills.Underdog,
                skills.InstantDeath,
            ],
        ),
        description="This name fits the card as it has a very high power and health and a skillset that makes it more versatile both offensively and defensively The name is inspired by the image of a magical and otherworldly feline with a strong presence",
    ),
    # Fertileturtle 🐭 1p 4h
    # costs: 🔥 has: 🔥👻 pot: 17
    Blueprint(
        original=Card(
            name="Fertileturtle",
            power=1,
            health=4,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description="This name fits the card as it has a good amount of health and a skill that focuses on fertility, which allows it to gather resources and multiply The name invokes the image of a wise and slowmoving turtle that carries with it a spirit of fertility and growth",
    ),
    # Glitterrat 🧺🐭🔰💀 4p 4h
    # costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 47
    Blueprint(
        original=Card(
            name="Glitterrat",
            power=4,
            health=4,
            costs_fire=0,
            costs_spirits=1,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="This card has moderate power and health, along with the packrat, fertility, and shield skills The glitter element in the name suggests that this creature may have a hoarding instinct or collect shiny objects, like a rat",
    ),
    # Flametoad 💀 1p 5h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 17
    Blueprint(
        original=Card(
            name="Flametoad",
            power=1,
            health=5,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description="With low power and moderate health, this card has the instant death skill and a high fire cost The name suggests that this could be a toadlike creature with fiery abilities, but also fitting with its low power and susceptibility to instant death",
    ),
    # Spiritmole 🧺 1p 5h
    # costs: 👻👻 has: 🔥👻👻 pot: 16
    Blueprint(
        original=Card(
            name="Spiritmole",
            power=1,
            health=5,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Packrat],
        ),
        description="With low power and moderate health, this card has the packrat skill and a high spirit cost The name suggests an underground creature with a nose for treasures, like a mole",
    ),
    # Hedgehorn 🐩🐭🔰 3p 8h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 52
    Blueprint(
        original=Card(
            name="Hedgehorn",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[skills.Underdog, skills.Fertility, skills.Shield],
        ),
        description="With moderate power and health, this card has the underdog and fertility skills The name suggests a creature with a tough exterior that can defend against predators, but also capable of producing offspring, like a hedgehog",
    ),
    # Shadowspine 🦔 1p 9h
    # costs: 🔥 has: 👻👻 pot: 21
    Blueprint(
        original=Card(
            name="Shadowspine",
            power=1,
            health=9,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=0,
            skills=[skills.Spines],
        ),
        description="The card has low fire and high spirits, as well as the Spines skill The name suggests a small creature known for its spikey and stealthy nature",
    ),
    # Sparkwing 🪁🐭🔰💀 6p 7h
    # costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 60
    Blueprint(
        original=Card(
            name="Sparkwing",
            power=6,
            health=7,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Soaring,
                skills.Fertility,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="The creature is powerful and tough, with fire and spirits equally balanced It also has the skills Soaring, Fertility, Shield, and InstantDeath, suggesting a creature that can fly, reproduce, protect, and kill The name invokes an image of a majestic creature with a deadly touch",
    ),
    # Chimerapod 🐭🧺🔰💀 5p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 56
    Blueprint(
        original=Card(
            name="Chimerapod",
            power=5,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Fertility,
                skills.Packrat,
                skills.Shield,
                skills.InstantDeath,
            ],
        ),
        description="This name refers to the card's skills and its attributes A chimerapod has 'Fertility' and 'Packrat' skills, which can indicate the animal is able to carry and produce lots of things The high power and health stats, along with the shield skill, make it a formidable foe It also has the 'InstantDeath' skill, which makes it potentially deadly",
    ),
    # Pixieferret 🧺💀 1p 2h
    # costs: 👻👻 has: 🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Pixieferret",
            power=1,
            health=2,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=1,
            skills=[skills.Packrat, skills.InstantDeath],
        ),
        description="The card has moderate power and health stats, but the skills 'Packrat' and 'InstantDeath' hint at a nimble and tricky creature The 'Invisibility' and 'Illusion' skills of a pixie come to mind, and the card's 'Spirits' and 'Fire' compatibility can suggest a playful, yet dangerous nature",
    ),
    # Wyvernrider 🐩💀🐭🔰🧺 9p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 78
    Blueprint(
        original=Card(
            name="Wyvernrider",
            power=9,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Packrat,
            ],
        ),
        description="The name suggests that the animal is trained to be ridden and commanded It has high power and health stats, and the 'Underdog' skill implies that it can take a hit and come back stronger The 'Fertility' skill in combination with a name like 'Wyvernrider' can suggest that it is a mythic creature, perhaps even majestic",
    ),
    # Shieldtortoise 🔰🐭🧺 4p 4h
    # costs: 🔥🔥 has: 🔥👻👻 pot: 34
    Blueprint(
        original=Card(
            name="Shieldtortoise",
            power=4,
            health=4,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Shield, skills.Fertility, skills.Packrat],
        ),
        description="The name of the animal comes from its 'Shield' skill and high health stat The fact that it has low power but high defense fits the image and behavior of a tortoise It has 'Fertility' and 'Packrat' skills which suggest it is wellprotected, and the 'Fire' and 'Spirits' compatibility can hint at some kind of animistic or spiritual power",
    ),
    # Rampartkangaroo 💀🔰🧺🐭 6p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Rampartkangaroo",
            power=6,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=6,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="The name implies strength and defense a rampart is a protective wall around a fortress The 'Shield' and 'Packrat' skills fit well with the idea of a fortress, in this case, the kangaroo itself The card's 'InstantDeath' skill can suggest a powerful attack, and its high spirits make it quite energetic",
    ),
    # Thundercrab 💀🐩🔰🐭 2p 6h
    # costs: 🔥 has: 🔥 pot: 37
    Blueprint(
        original=Card(
            name="Thundercrab",
            power=2,
            health=6,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[
                skills.InstantDeath,
                skills.Underdog,
                skills.Shield,
                skills.Fertility,
            ],
        ),
        description="ThunderLow Fire, with skills that can do good damage to their opponents Crabs are known for their claws that pack some serious punch and thunder signifies a thunderous roar which can instill fear in the opponent",
    ),
    # Spiky Snail 🦔 0p 3h
    # costs: 🔥 has: 🔥👻👻 pot: 9
    Blueprint(
        original=Card(
            name="Spiky Snail",
            power=0,
            health=3,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Spines],
        ),
        description="SpinesHigh Spirit, Snails are known for their hard, protective shells, and adding spines to it make it a formidable opponent and high spirit implies it's stubborn and hard to defeat",
    ),
    # Fertilityrock 🐭 3p 1h
    # costs: 👻👻👻 has: 🔥👻👻 pot: 14
    Blueprint(
        original=Card(
            name="Fertilityrock",
            power=3,
            health=1,
            costs_fire=0,
            costs_spirits=3,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Fertility],
        ),
        description='SpiritFertility, with moderate power and low health "Fertility" hints at something that continually produces something, and in this case is producing spirit "Rock" implies it harder to take down It has moderate power which implies it needs time to build up, but it has low health since it\'s not meant to be the main attacker',
    ),
    # Fertileowl 🐭🧺 5p 2h
    # costs: - has: 🔥👻👻👻 pot: 37
    Blueprint(
        original=Card(
            name="Fertileowl",
            power=5,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=1,
            skills=[skills.Fertility, skills.Packrat],
        ),
        description="related to the high spirit value, Fertility skill, and sound association of owls with wisdom and magic",
    ),
    # Thorn Gecko 🐭🔰🧺🦔 2p 2h
    # costs: 🔥 has: - pot: 28
    Blueprint(
        original=Card(
            name="Thorn Gecko",
            power=2,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=0,
            has_fire=0,
            skills=[skills.Fertility, skills.Shield, skills.Packrat, skills.Spines],
        ),
        description="related to spines and the minuscule size and fragility of the gecko",
    ),
    # Water Dragon  7p 1h
    # costs: 👻👻 has: 🔥🔥🔥👻 pot: 15
    Blueprint(
        original=Card(
            name="Water Dragon",
            power=7,
            health=1,
            costs_fire=0,
            costs_spirits=2,
            has_spirits=1,
            has_fire=3,
            skills=[],
        ),
        description="related to high spirit values, a powerful card, and the skill costspirit",
    ),
    # Pumaquill 🐭🧺💀 4p 7h
    # costs: 🔥 has: 🔥🔥👻👻👻 pot: 42
    Blueprint(
        original=Card(
            name="Pumaquill",
            power=4,
            health=7,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=2,
            skills=[skills.Fertility, skills.Packrat, skills.InstantDeath],
        ),
        description="related to the combination of moderate powerhealth, Packrat skill and the quillspine from Spines skill",
    ),
    # Necrofly 💀🔰🐭🦔 4p 10h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
    Blueprint(
        original=Card(
            name="Necrofly",
            power=4,
            health=10,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=5,
            skills=[
                skills.InstantDeath,
                skills.Shield,
                skills.Fertility,
                skills.Spines,
            ],
        ),
        description="The high power and health, coupled with Instant Death, suggest a dark and deathly creature The Shield and Spines could be the result of its tough exterior, while Fertility might suggest its ability to control death and rebirth",
    ),
    # Dreamwing 🧺🐩💀🐭🔰🦔 7p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 67
    Blueprint(
        original=Card(
            name="Dreamwing",
            power=7,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=7,
            has_fire=5,
            skills=[
                skills.Packrat,
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Spines,
            ],
        ),
        description="The high spirit and power suggest a fantastic and dreamy creature, with the Spines skill hinting at the ability to defend itself Underdog represents its ability to surprise others, while Instant Death hints at its deadly nature The Fertility skill might suggest the creature can create illusions",
    ),
    # Stonehog  6p 2h
    # costs: - has: 🔥 pot: 23
    Blueprint(
        original=Card(
            name="Stonehog",
            power=6,
            health=2,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[],
        ),
        description="Low health with decent power, indicating a strong and possibly armored creature Lack of spirit resources with no skills might mean that it is solitary or unsociable Fire resources required might symbolize its hardiness in general",
    ),
    # Deathcrow 🐭💀 7p 3h
    # costs: 🔥🔥 has: 🔥 pot: 30
    Blueprint(
        original=Card(
            name="Deathcrow",
            power=7,
            health=3,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=0,
            has_fire=1,
            skills=[skills.Fertility, skills.InstantDeath],
        ),
        description="relates to InstantDeath, high power, low health",
    ),
    # Chaosdrake 🐭🐩💀🧺 9p 8h
    # costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 58
    Blueprint(
        original=Card(
            name="Chaosdrake",
            power=9,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Fertility,
                skills.Underdog,
                skills.InstantDeath,
                skills.Packrat,
            ],
        ),
        description="relates to high powerhealth, many skills, high fire and spirit costs",
    ),
    # Armorynx 🐩💀🐭🧺 9p 10h
    # costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Armorynx",
            power=9,
            health=10,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=4,
            has_fire=4,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Packrat,
            ],
        ),
        description="relates to high powerhealth, Underdog, Packrat, high costs of both fire and spirits",
    ),
    # Magmamite 🐭 3p 1h
    # costs: 🔥🔥 has: 🔥🔥🔥👻 pot: 16
    Blueprint(
        original=Card(
            name="Magmamite",
            power=3,
            health=1,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=1,
            has_fire=3,
            skills=[skills.Fertility],
        ),
        description="related to fire, fiery name, small and agile creature",
    ),
    # Viperoth 💀 1p 2h
    # costs: 🔥 has: 🔥👻 pot: 12
    Blueprint(
        original=Card(
            name="Viperoth",
            power=1,
            health=2,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=1,
            skills=[skills.InstantDeath],
        ),
        description='This card has an InstantDeath skill and is fairly weak in terms of power and health Viperoth is a combination of "viper" and "wraith" and reflects its lethal skill and fragile nature',
    ),
    # Carimagus 🐩🧺🐭💀 3p 8h
    # costs: - has: 🔥🔥🔥👻👻👻👻 pot: 57
    Blueprint(
        original=Card(
            name="Carimagus",
            power=3,
            health=8,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=4,
            has_fire=3,
            skills=[
                skills.Underdog,
                skills.Packrat,
                skills.Fertility,
                skills.InstantDeath,
            ],
        ),
        description='With high power, health, and spirits, Carimagus is a beastly combination of "caribou" and "magus" that represents its fierce nature and mystical abilities Its skills include a mix of underdog, packrat, and fertility',
    ),
    # Griffalcon 🔰🐭🪁🧺🐩 5p 8h
    # costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 51
    Blueprint(
        original=Card(
            name="Griffalcon",
            power=5,
            health=8,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.Soaring,
                skills.Packrat,
                skills.Underdog,
            ],
        ),
        description='This card has a mix of skills such as shield, soaring, packrat, underdog, and fertility It also has a high power and health value and costs  in fire Griffalcon is a rare combination of "griffin" and "falcon" and reflects its powerful yet swift nature',
    ),
    # Titansaur 🔰🐭💀🐩🧺 10p 10h
    # costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
    Blueprint(
        original=Card(
            name="Titansaur",
            power=10,
            health=10,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=5,
            has_fire=5,
            skills=[
                skills.Shield,
                skills.Fertility,
                skills.InstantDeath,
                skills.Underdog,
                skills.Packrat,
            ],
        ),
        description='With extremely high power , health, and an InstantDeath skill, the Titansaur is a force to be reckoned with As suggested by its name, it\'s a mix of "titan" and "dinosaur," representing its incredible strength and age',
    ),
    # Armishell 🐩💀🐭🔰🚀 3p 9h
    # costs: - has: 🔥🔥🔥🔥🔥👻👻👻 pot: 61
    Blueprint(
        original=Card(
            name="Armishell",
            power=3,
            health=9,
            costs_fire=0,
            costs_spirits=0,
            has_spirits=3,
            has_fire=5,
            skills=[
                skills.Underdog,
                skills.InstantDeath,
                skills.Fertility,
                skills.Shield,
                skills.Airdefense,
            ],
        ),
        description='With balanced stats and skills such as shield, underdog, and airdefense, Armishell is a defenseoriented card Its name is a fusion of "armadillo" and "shell," reflecting its ability to protect itself and its allies',
    ),
    # Stormlion 🧺🐭🔰 3p 5h
    # costs: 🔥🔥🔥 has: 🔥👻👻 pot: 33
    Blueprint(
        original=Card(
            name="Stormlion",
            power=3,
            health=5,
            costs_fire=3,
            costs_spirits=0,
            has_spirits=2,
            has_fire=1,
            skills=[skills.Packrat, skills.Fertility, skills.Shield],
        ),
        description="With high power, health, and costs fire, this card is reminiscent of a fearsome predator Its skills Packrat, Fertility, and Shield also speak to its strength and resilience The name Stormlion embodies power, strength, and ferocity",
    ),
    # Packratty 🐩🧺 1p 5h
    # costs: 🔥 has: 👻 pot: 19
    Blueprint(
        original=Card(
            name="Packratty",
            power=1,
            health=5,
            costs_fire=1,
            costs_spirits=0,
            has_spirits=1,
            has_fire=0,
            skills=[skills.Underdog, skills.Packrat],
        ),
        description="relates to cheapness, weak power and ability to stealspare resources",
    ),
    # Fertilego 💀🚀🧺🐭 6p 8h
    # costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 48
    Blueprint(
        original=Card(
            name="Fertilego",
            power=6,
            health=8,
            costs_fire=2,
            costs_spirits=0,
            has_spirits=3,
            has_fire=3,
            skills=[
                skills.InstantDeath,
                skills.Airdefense,
                skills.Packrat,
                skills.Fertility,
            ],
        ),
        description="relates to high spirits, fertility skills and powerful attributes",
    ),
]
