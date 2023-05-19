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
]
