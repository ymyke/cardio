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
]
