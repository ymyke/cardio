from cardio import Card, skills
from .blueprint import Blueprint
all_blueprints = [
# Hamster  0p 1h
# costs: - has: 🔥👻 pot: 12
Blueprint(original=Card(name='Hamster', power=0, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description=''),
# Koala  1p 3h
# costs: 🔥 has: 🔥👻 pot: 7
Blueprint(original=Card(name='Koala', power=1, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description=''),
# Porcupine 🚀 1p 2h
# costs: 🔥 has: 🔥👻 pot: 7
Blueprint(original=Card(name='Porcupine', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Airdefense]), description=''),
# Lynx  3p 2h
# costs: 🔥🔥 has: 🔥👻 pot: 8
Blueprint(original=Card(name='Lynx', power=3, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description=''),
# Weasel  1p 1h
# costs: 👻👻 has: 🔥👻 pot: 3
Blueprint(original=Card(name='Weasel', power=1, health=1, costs_fire=0, costs_spirits=2, has_spirits=1, has_fire=1, skills=[]), description=''),
# Church Mouse 🐭 1p 1h
# costs: 🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Church Mouse', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description=''),
# Spikelet 🦔 1p 2h
# costs: 🔥🔥 has: 🔥👻👻👻👻 pot: 10
Blueprint(original=Card(name='Spikelet', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=1, skills=[skills.Spines]), description='referring to the spines and high cost in fire to play'),
# Badgeress 🧺 4p 5h
# costs: 🔥🔥 has: 👻 pot: 20
Blueprint(original=Card(name='Badgeress', power=4, health=5, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Packrat]), description='based on the strength and vitality of the badger, and the unique skill of collecting \"treasures\" a Packrat'),
# Bucklerog 🔰 3p 5h
# costs: 🔥 has: 🔥👻👻👻 pot: 22
Blueprint(original=Card(name='Bucklerog', power=3, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Shield]), description='a play on words with \"buckler\" a type of small shield and \"rog\" short for rogue, reflecting the skill of shielding and the medium power and health'),
# Falcon  3p 2h
# costs: 🔥 has: 🔥 pot: 8
Blueprint(original=Card(name='Falcon', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='fast and powerful, low health, fire is the only attribute, has no spirits'),
# Elephant  1p 6h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 11
Blueprint(original=Card(name='Elephant', power=1, health=6, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='strong and has high health, expensive, fire and spirits attributes'),
# Firefly 🐭 0p 2h
# costs: 🔥🔥🔥 has: 🔥🔥👻👻 pot: 12
Blueprint(original=Card(name='Firefly', power=0, health=2, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility]), description='weak, low fire attribute cost, high spirit attributes, has the Fertility skill'),
# Wolf  4p 2h
# costs: 🔥 has: 👻 pot: 10
Blueprint(original=Card(name='Wolf', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='strong and fast, but only fire attribute, low health'),
# Scorpion 💀 1p 2h
# costs: 🔥 has: 👻👻 pot: 12
Blueprint(original=Card(name='Scorpion', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.InstantDeath]), description='poisonous, low power and health, low fire attribute cost, high spirit attribute, has the InstantDeath skill'),
# Mole 🐩 1p 2h
# costs: 🔥 has: 🔥👻 pot: 9
Blueprint(original=Card(name='Mole', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Underdog]), description='weak, but has potential with the Underdog skill, balanced fire and spirits attributes'),
# Kangaroo  2p 2h
# costs: 🔥 has: 🔥🔥👻 pot: 8
Blueprint(original=Card(name='Kangaroo', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description='moderate power and health, high fire attribute, balanced overall'),
# Phoenix 🪁 2p 2h
# costs: 🔥🔥 has: 🔥👻 pot: 8
Blueprint(original=Card(name='Phoenix', power=2, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Soaring]), description='moderate power and health, medium fire attribute cost, has the Soaring skill'),
# Chameleon 🐩 2p 2h
# costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 8
Blueprint(original=Card(name='Chameleon', power=2, health=2, costs_fire=4, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Underdog]), description='moderate power and health, high fire attribute cost, has the Underdog skill, can adapt to different scenarios'),
# Turtle 🔰 2p 1h
# costs: 🔥🔥🔥 has: 👻 pot: 9
Blueprint(original=Card(name='Turtle', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Shield]), description='has a shield skill, low power and health, high fire attribute cost'),
# Jaguar  3p 4h
# costs: 🔥🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Jaguar', power=3, health=4, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a powerful and expensive animal, fits with high power and moderate health attributes'),
# Caterpillar  3p 8h
# costs: - has: 🔥 pot: 28
Blueprint(original=Card(name='Caterpillar', power=3, health=8, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='low in firepower, but high in health and regeneration, fits with the idea of a slow growing, sturdy creature'),
# Foxbat 🔰🧺🐭 2p 3h
# costs: - has: 🔥🔥👻👻 pot: 40
Blueprint(original=Card(name='Foxbat', power=2, health=3, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.Packrat, skills.Fertility]), description='a creature with both fiery and spiritual characteristics, with skills that include theft Packrat, deception and defense Shield'),
# Hydra 🐭🐩💀🔰🧺 2p 8h
# costs: 👻👻👻👻 has: 🔥🔥👻👻👻👻 pot: 48
Blueprint(original=Card(name='Hydra', power=2, health=8, costs_fire=0, costs_spirits=4, has_spirits=4, has_fire=2, skills=[skills.Fertility, skills.Underdog, skills.InstantDeath, skills.Shield, skills.Packrat]), description='a creature with high spiritual power that can resurrect even after instant death InstantDeath, and has fertility and defense skills Fertility, Shield'),
# Drakelet  1p 1h
# costs: 🔥 has: 🔥👻👻👻 pot: 6
Blueprint(original=Card(name='Drakelet', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[]), description='low powerhealth, low fire cost, but has a decent amount of spirits and no skills \"Drakelet\" is a small, baby dragon, which fits with the small size of the card'),
# Glimmer  1p 2h
# costs: 👻👻👻 has: 🔥 pot: 3
Blueprint(original=Card(name='Glimmer', power=1, health=2, costs_fire=0, costs_spirits=3, has_spirits=0, has_fire=1, skills=[]), description='low power, decent health, no fire cost, but high spirit cost \"Glimmer\" suggests something ethereal or magical which fits with the high spirits cost'),
# Ant  2p 1h
# costs: 🔥🔥 has: 👻 pot: 4
Blueprint(original=Card(name='Ant', power=2, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='decent power, low health, low fire cost, low spirit cost, no skills, but the low health and the small size could be compared to an ant'),
# Ferret  1p 2h
# costs: 🔥 has: 🔥👻 pot: 6
Blueprint(original=Card(name='Ferret', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='low power, decent health, low fire cost, low spirit cost, no skills, but the name suggests agility and speed which fits with the card\'s attributes'),
# Raccoon  2p 1h
# costs: 🔥🔥 has: 🔥👻 pot: 5
Blueprint(original=Card(name='Raccoon', power=2, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='decent power, low health, average fire cost, low spirit cost, no skills, The Raccoon is known for its mischievousness and resourcefulness, which could be applied to a card with decent power and average fire cost'),
# Gecko  0p 2h
# costs: 🔥 has: 🔥👻 pot: 4
Blueprint(original=Card(name='Gecko', power=0, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='low power, decent health, low fire cost, low spirit cost, no skills, but the ability to climb walls is associated with geckos, which fits with a card that has decent health'),
# Froglet  1p 1h
# costs: 🔥 has: 🔥👻👻 pot: 5
Blueprint(original=Card(name='Froglet', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='low powerhealth, low fire cost, low spirits, no skills, but has  spirits A froglet is a young frog and the name relates to the low powerhealth of the card'),
# Phoenixborn 🐩 0p 2h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 7
Blueprint(original=Card(name='Phoenixborn', power=0, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Underdog]), description='high fire costs, high fire value, and an Underdog skill This name suggests a powerful being that arises from fire and represents rebirth or transformation, fitting with the card\'s attributes and skill'),
# Nightwinged  2p 1h
# costs: 🔥 has: 🔥👻 pot: 6
Blueprint(original=Card(name='Nightwinged', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='low health, low fire costs, but quick and agile with high power A name that suggests a fast, stealthy, and fearsome creature of the night'),
# Lavalope  1p 2h
# costs: 🔥🔥 has: 🔥 pot: 4
Blueprint(original=Card(name='Lavalope', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='low spirits, high fire costs, but with both fire and mobility This name combines the elements of fire and the agility of a jackrabbit, fitting with the card\'s attributes'),
# Seraphwing  2p 1h
# costs: 🔥 has: 👻👻👻👻 pot: 7
Blueprint(original=Card(name='Seraphwing', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=0, skills=[]), description='low fire costs, high spirit, and the Healer skill This name suggests an angelic being capable of healing, fitting with the card\'s attributes and skill'),
# Infernorb  1p 2h
# costs: 🔥🔥🔥 has: 🔥👻👻 pot: 5
Blueprint(original=Card(name='Infernorb', power=1, health=2, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='high fire costs, average attributes, and no skills This name suggests a fiery creature that lacks any special abilities, fitting with the card\'s attributes '),
# Faeox Fairy Fox 🐩 1p 2h
# costs: 🔥 has: - pot: 7
Blueprint(original=Card(name='Faeox Fairy Fox', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Underdog]), description='Underdog, weak but with potential'),
# Spriggle Sprite Squirrel  1p 1h
# costs: 🔥 has: 👻👻👻👻 pot: 6
Blueprint(original=Card(name='Spriggle Sprite Squirrel', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=0, skills=[]), description='Small, but with high spirit power'),
# Shadowolf Shadow Wolf  2p 2h
# costs: 🔥🔥🔥 has: - pot: 4
Blueprint(original=Card(name='Shadowolf Shadow Wolf', power=2, health=2, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=0, skills=[]), description='Expensive, but very strong and powerful, with no magic abilities'),
# Griffox  3p 2h
# costs: 👻👻👻👻 has: 👻👻👻 pot: 7
Blueprint(original=Card(name='Griffox', power=3, health=2, costs_fire=0, costs_spirits=4, has_spirits=3, has_fire=0, skills=[]), description='powerful, spirited, moderately healthy, and requires some spirits to use'),
# Pythroar  1p 2h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 7
Blueprint(original=Card(name='Pythroar', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=3, skills=[]), description='firebased, fragile, fierce name for a creature with low health'),
# Underrawr 🐩 1p 1h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 7
Blueprint(original=Card(name='Underrawr', power=1, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Underdog]), description='a creature that can thrive with little, but its skills boost its performance'),
# Chimerex  4p 1h
# costs: 🔥🔥 has: 🔥👻👻 pot: 9
Blueprint(original=Card(name='Chimerex', power=4, health=1, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='powerful, practically invulnerable, but needs some spirits to use'),
# Skythorn  3p 2h
# costs: 🔥 has: 🔥👻 pot: 9
Blueprint(original=Card(name='Skythorn', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a fantasy creature with thorns on its wings and body The name relates to the power, cost, and fire element of the card'),
# Shieldcat 🔰 2p 1h
# costs: 👻👻👻👻👻👻 has: 🔥👻 pot: 7
Blueprint(original=Card(name='Shieldcat', power=2, health=1, costs_fire=0, costs_spirits=6, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='a catlike creature with a shield The name relates to the skills and high spirit cost of the card'),
# Treewhisper  1p 6h
# costs: 👻👻👻👻 has: 👻👻 pot: 10
Blueprint(original=Card(name='Treewhisper', power=1, health=6, costs_fire=0, costs_spirits=4, has_spirits=2, has_fire=0, skills=[]), description='a creature that speaks to trees and is tied to nature The name relates to the high health and spirit cost, as well as the absence of fire'),
# Glimmertail  2p 2h
# costs: 🔥 has: 🔥👻 pot: 7
Blueprint(original=Card(name='Glimmertail', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a creature with a shiny tail that distracts its opponents The name relates to the low power but presence of fire element'),
# Hellhound  2p 1h
# costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥🔥👻 pot: 8
Blueprint(original=Card(name='Hellhound', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=6, skills=[]), description='This card has high fire costs and low spirits, indicating a creature of the underworld With high power and low health, it\'s a fierce and dangerous creature that requires sacrifice to summon'),
# Pixiefox  2p 2h
# costs: 🔥 has: 🔥👻👻 pot: 8
Blueprint(original=Card(name='Pixiefox', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='With balanced stats and average costs, this creature is quick and nimble, able to easily dodge attacks It\'s a fantastical creature with foxlike features, but with mystical powers like a pixie'),
# Thunderbird  2p 2h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 7
Blueprint(original=Card(name='Thunderbird', power=2, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description='This card has high fire costs and high fire attribute, which suggest a creature born of fire With balanced stats, this birdlike creature is able to swiftly attack and evade'),
# Hedgebeast 🦔 2p 1h
# costs: 🔥 has: 🔥🔥👻👻 pot: 10
Blueprint(original=Card(name='Hedgebeast', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Spines]), description='This card has low health and high power, suggesting a creature that is a glass cannon With a spines skill, it can repel attacks, but it\'s not able to withstand many attacks It\'s a fantastical beast that\'s part hedgehog and part something else'),
# Furies  5p 1h
# costs: 🔥🔥 has: 👻👻 pot: 10
Blueprint(original=Card(name='Furies', power=5, health=1, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=0, skills=[]), description='This card has no fire attribute and high spirits, indicating a creature of the underworld With high power and low health, it\'s a dangerous creature that requires sacrifice to summon It has no skills, instead relying on its raw strength to take down its enemies The name Furies fits with the theme of creatures from the underworld and their vengeful nature'),
# Banshee 💀 1p 1h
# costs: 👻👻👻 has: 🔥👻 pot: 8
Blueprint(original=Card(name='Banshee', power=1, health=1, costs_fire=0, costs_spirits=3, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='instantly deadly, highly spiritual'),
# Basilisk  5p 1h
# costs: 🔥 has: - pot: 9
Blueprint(original=Card(name='Basilisk', power=5, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[]), description='strong and powerful, not reliant on elements, no skills'),
# Siren 🐭 0p 1h
# costs: 🔥 has: - pot: 8
Blueprint(original=Card(name='Siren', power=0, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Fertility]), description='alluring, has female connotations, fertility ability, fire costs'),
# Centaur 🐭 1p 2h
# costs: 🔥 has: - pot: 12
Blueprint(original=Card(name='Centaur', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Fertility]), description='balanced power and health, fertility ability, fire costs'),
# Pangolin 🔰 1p 2h
# costs: 🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Pangolin', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='shield ability, some spiritual elements, low power and health'),
# Chimera  3p 3h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 11
Blueprint(original=Card(name='Chimera', power=3, health=3, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description=' fire symbols, balanced power and health'),
# Seraphim 🔰 1p 1h
# costs: 🔥 has: 🔥🔥👻 pot: 11
Blueprint(original=Card(name='Seraphim', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Shield]), description='Fire element, Shield skill, low power and health'),
# Medusa 💀 1p 1h
# costs: 🔥 has: 🔥🔥👻 pot: 11
Blueprint(original=Card(name='Medusa', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.InstantDeath]), description='Instant Death skill, low fire cost, very low power and health'),
# Gorgon 🔰 3p 1h
# costs: 🔥🔥 has: 🔥👻 pot: 13
Blueprint(original=Card(name='Gorgon', power=3, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='Shield skill, high fire cost, low health and power'),
# Nightwing 🦔🪁🐭 1p 1h
# costs: 🔥🔥🔥 has: - pot: 13
Blueprint(original=Card(name='Nightwing', power=1, health=1, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Spines, skills.Soaring, skills.Fertility]), description='fits with soaring skill, has spines for defense, high fertility potential for breeding'),
# Thunderhoof  3p 2h
# costs: 🔥🔥🔥 has: 🔥🔥👻👻👻 pot: 10
Blueprint(original=Card(name='Thunderhoof', power=3, health=2, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=2, skills=[]), description='strong and fiery, balanced in spirits and fire, no standout skills'),
# Stormhare  4p 2h
# costs: 🔥🔥 has: 🔥👻 pot: 10
Blueprint(original=Card(name='Stormhare', power=4, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='quick and nimble, can handle fire, no skills'),
# Bansheebee 💀 0p 3h
# costs: 🔥🔥 has: 🔥👻👻 pot: 12
Blueprint(original=Card(name='Bansheebee', power=0, health=3, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath]), description='low power and fire, high spirits for a haunting wail of instant death'),
# Seedancer 🐭 0p 2h
# costs: 🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Seedancer', power=0, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='low fire, low spirits, high fertility potential for breeding'),
# Salamander 🔰🐩 1p 2h
# costs: 👻👻 has: 👻👻 pot: 14
Blueprint(original=Card(name='Salamander', power=1, health=2, costs_fire=0, costs_spirits=2, has_spirits=2, has_fire=0, skills=[skills.Shield, skills.Underdog]), description='a fireloving creature that fits with the card\'s firerelated costs and underdog skill, which relates to the card\'s low power and fire attribute values The shield skill also reinforces the card\'s inherent skill itself'),
# Firebird 🐭 2p 2h
# costs: 🔥🔥 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Firebird', power=2, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='costs  fire, has fire, has no spirits, and has a skill related to fertility'),
# Goblinbat 🐭 3p 1h
# costs: 🔥 has: - pot: 14
Blueprint(original=Card(name='Goblinbat', power=3, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Fertility]), description='low health, no spirits or fire, but high power and a skill related to fertility'),
# Minotaur 🔰 4p 1h
# costs: 🔥 has: 🔥 pot: 14
Blueprint(original=Card(name='Minotaur', power=4, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield]), description='high power, low health, has fire and a defensive skill, like a shield'),
# Kelpie 🐭 0p 5h
# costs: 👻👻👻👻👻👻 has: 🔥👻👻 pot: 14
Blueprint(original=Card(name='Kelpie', power=0, health=5, costs_fire=0, costs_spirits=6, has_spirits=2, has_fire=1, skills=[skills.Fertility]), description='high health, high spirits, fertility skill suggests a creature associated with growth and fertility, while the high spirit and low fire attributes reinforce a sense of otherworldliness and etherealness Kelpies are also water spirits with equine or humananimal hybrid features, which fits well with the Fertility skill implying a creature that somehow generates or enhances growth'),
# Dragonfly  3p 4h
# costs: 👻 has: 🔥🔥 pot: 13
Blueprint(original=Card(name='Dragonfly', power=3, health=4, costs_fire=0, costs_spirits=1, has_spirits=0, has_fire=2, skills=[]), description='moderate powerhealth, but with high fire attributes and low spirit attributes suggest a creature that is fast, nimble and fierce, with a fiery temper Dragonflies are brightly colored insects with iridescent wings, which give them a sense of speed and agility, and also suggest a fiery personality The high fire attributes reinforce this notion of a creature that is hotheaded and quick to act, while the low spirit attributes might suggest a lack of patience or foresight'),
# Rat king 🧺 2p 4h
# costs: 👻👻 has: 🔥🔥👻 pot: 16
Blueprint(original=Card(name='Rat king', power=2, health=4, costs_fire=0, costs_spirits=2, has_spirits=1, has_fire=2, skills=[skills.Packrat]), description='moderate powerhealth, with a skill that allows to hoard multiple items, paired with moderate spirit and fire attributes This card suggests a creature that is quick and dexterous, with an eye for useful items Rat kings are a real phenomenon in which several rats become entangled and live together This reinforces the idea of the Packrat skill that involves hoarding objects, however in this case, the Rat king combines the ability to collect with their fighting capabilities The moderate attributes in both spirit and fire suggest that the card is well balanced and capable in all aspects of the game'),
# Bloodhound  1p 7h
# costs: 🔥🔥 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Bloodhound', power=1, health=7, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='high health, medium power, costs fire, good for defense'),
# Gryphon 🔰 4p 2h
# costs: 🔥🔥 has: 🔥👻 pot: 16
Blueprint(original=Card(name='Gryphon', power=4, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='medium powerhealth, costs fire, has shield, mythical creature'),
# Dryad 🐭 1p 3h
# costs: 🔥 has: 🔥👻 pot: 15
Blueprint(original=Card(name='Dryad', power=1, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='low powerhealth, costs fire, has fertility skill, naturebased'),
# Fae Bunny 🐭 2p 2h
# costs: 👻👻 has: 🔥👻👻 pot: 15
Blueprint(original=Card(name='Fae Bunny', power=2, health=2, costs_fire=0, costs_spirits=2, has_spirits=2, has_fire=1, skills=[skills.Fertility]), description='This card has a high spirit value and the ability Fertility which relates to bunnies being known for their reproductive abilities The name \"Fae\" gives it a fantastical twist'),
# Demon Crow 💀 4p 2h
# costs: 🔥🔥 has: 🔥👻 pot: 16
Blueprint(original=Card(name='Demon Crow', power=4, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='The ability \"InstantDeath\" is associated with malevolent power, this card has high power and low health, the bird is a crow which is associated with the occult'),
# Pygmy Rhino 🔰🐩 2p 1h
# costs: 🔥 has: 🔥👻 pot: 15
Blueprint(original=Card(name='Pygmy Rhino', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Underdog]), description='This card has a shield ability and is an underdog card low power and health, the rhino has a shieldlike form and adding \"Pygmy\" gives it a fantastical twist fitting for the game'),
# Arctic Fox 🔰 3p 2h
# costs: 🔥 has: 🔥👻 pot: 15
Blueprint(original=Card(name='Arctic Fox', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='This card has a shield ability and is quite balanced with  power and  health The fox is known for its ability to adapt and survive harsh winter conditions, which fits well with the shield ability'),
# Goblin Rat 💀🧺 1p 3h
# costs: 🔥🔥🔥 has: 👻 pot: 16
Blueprint(original=Card(name='Goblin Rat', power=1, health=3, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath, skills.Packrat]), description='This card has the abilities \"InstantDeath\" and \"PackRat\" which align with goblins being known for their trickery and association with thievery The rat is an animal associated with scavenging and hoarding, fitting with the PackRat ability'),
# Dracoon 🔰 5p 2h
# costs: 🔥 has: 👻 pot: 18
Blueprint(original=Card(name='Dracoon', power=5, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Shield]), description='Combining a dragon and a raccoon, this card offers a good power value of , but relatively low health of  It has a fire cost of  and has only  spirit, meaning it can only use its shield skill once The name comes from the appearance of a raccoon mixed with a dragon, a creature with firebreathing abilities as well as being protective of its hoard'),
# Drachling 🔰🐩 4p 2h
# costs: 👻👻👻👻👻 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Drachling', power=4, health=2, costs_fire=0, costs_spirits=5, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Underdog]), description='With a high power, and shield and underdog skills, this dragonlike creature is small in health, but not easily defeated The high spirit cost suggests a magical creature'),
# Manticore 🚀🐭 1p 4h
# costs: 🔥🔥 has: 🔥 pot: 16
Blueprint(original=Card(name='Manticore', power=1, health=4, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Airdefense, skills.Fertility]), description='This mythical creature is known for its fierce and powerful defense mechanisms and air defense skill The fertility skill is also related to myths and legends The low spirit cost suggests it is a common creature in the game'),
# Flamehound  7p 2h
# costs: 🔥🔥 has: 🔥🔥🔥👻 pot: 17
Blueprint(original=Card(name='Flamehound', power=7, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=3, skills=[]), description='very strong, but expensive, costsfire, three hasfire, no skills'),
# Armordillo 🔰🧺 2p 1h
# costs: 🔥 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Armordillo', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Packrat]), description='moderate power, low health, Shield ability capable of minimizing damage taken, moderate costsfirecostsspirits'),
# Flameetle 🐭 4p 1h
# costs: 🔥 has: 🔥👻👻 pot: 18
Blueprint(original=Card(name='Flameetle', power=4, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility]), description='combines the words \'flame\' and \'beetle\', implying its fire attribute and insectlike appearance Its low health represents its fragility, while its power and Fertility skill suggest its ability to reproduce and quickly build up a swarm'),
# Shadowcat 🧺💀 3p 2h
# costs: 🔥 has: 🔥 pot: 20
Blueprint(original=Card(name='Shadowcat', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Packrat, skills.InstantDeath]), description='low health but high power combined with the Packrat skill suggest a sneaky, quick and efficient hunting animal, while the InstantDeath skill is the animal\'s deadly appearance, able to instantly neutralize any prey'),
# Trollsnake 🐩🐭 0p 4h
# costs: 🔥🔥🔥 has: 🔥👻👻 pot: 18
Blueprint(original=Card(name='Trollsnake', power=0, health=4, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Underdog, skills.Fertility]), description='high health with low power, this animal relies on its Underdog skill to defend itself as it grows Its Fertility skill represents its ability to quickly regrow any lost limbs or appendages'),
# Dragonet 🐭🔰 1p 2h
# costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 22
Blueprint(original=Card(name='Dragonet', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=4, skills=[skills.Fertility, skills.Shield]), description='This name is a nod to the dragon\'s firebreathing abilities, as well as its fertility skill The card\'s name also reflects its lower power and health values'),
# Shield Beetle 🔰 4p 4h
# costs: 👻 has: 🔥👻 pot: 21
Blueprint(original=Card(name='Shield Beetle', power=4, health=4, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='The name Shield Beetle is perfect for a creature with high health and a shield skill, fitting with its armorlike defenses'),
# Phoenix Cub 🐭 2p 3h
# costs: 🔥 has: 🔥🔥🔥👻 pot: 19
Blueprint(original=Card(name='Phoenix Cub', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=3, skills=[skills.Fertility]), description='The name fits the card\'s skills and attributes, being similar to Card  However, the cub has less fire power as it is still young and learning to control its abilities'),
# Sparkcat  5p 2h
# costs: - has: 🔥👻 pot: 22
Blueprint(original=Card(name='Sparkcat', power=5, health=2, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='relates to the card\'s high power and fire attribute, and the catlike qualities of agility and speed'),
# Tricksterat 🐭🧺💀 1p 1h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 24
Blueprint(original=Card(name='Tricksterat', power=1, health=1, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='a play on words for \"trickster rat\", relates to the card\'s packrat skill and the sly nature of rats'),
# Ironclaw 🔰💀 3p 2h
# costs: 🔥🔥 has: 👻 pot: 20
Blueprint(original=Card(name='Ironclaw', power=3, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Shield, skills.InstantDeath]), description='relates to the card\'s high defense skill and the clawlike qualities of shields'),
# Skywhip 🚀💀🐭 0p 5h
# costs: 🔥 has: 👻👻 pot: 24
Blueprint(original=Card(name='Skywhip', power=0, health=5, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Airdefense, skills.InstantDeath, skills.Fertility]), description='relates to the card\'s air defense skill and high spirits attribute, and the whiplike qualities of fertility'),
# Blazehorn 🔰 2p 5h
# costs: 🔥 has: 🔥🔥👻 pot: 20
Blueprint(original=Card(name='Blazehorn', power=2, health=5, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Shield]), description='relates to the card\'s high fire attribute and the hornlike qualities of shields'),
# Peryton 🐭 6p 1h
# costs: 🔥 has: 🔥👻 pot: 21
Blueprint(original=Card(name='Peryton', power=6, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='The Peryton represents a creature of eternal youth, fertility and divine grace The fertility skill suggests this name while the high power level represents the divine strength'),
# Wispwarden 🔰🧺💀 1p 3h
# costs: 🔥🔥 has: - pot: 22
Blueprint(original=Card(name='Wispwarden', power=1, health=3, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Shield, skills.Packrat, skills.InstantDeath]), description='name is a combination of \"wisp,\" which is a creature often associated with magic and ethereality, and \"warden,\" which implies protection The high health and shield skill make it seem like a protective creature that can take a lot of hits The instant death also adds to the idea of a powerful guardian'),
# Flamfuryx 🐭💀 3p 1h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 23
Blueprint(original=Card(name='Flamfuryx', power=3, health=1, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Fertility, skills.InstantDeath]), description='name is a combination of \"flame,\" referring to its high fire attribute, and \"fury,\" implying a powerful, aggressive creature The fertility skill adds a sense of reproduction and proliferation, making it a fiery and formidable creature that can easily overpower opponents'),
# Hydradon 🐭 3p 6h
# costs: 🔥 has: - pot: 22
Blueprint(original=Card(name='Hydradon', power=3, health=6, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Fertility]), description='name is a combination of \"hydra,\" a mythical creature with multiple heads, and \"don,\" meaning \"lord\" or \"master\" The high health and fertility skill make it seem like a dominating and resilient creature that can easily spawn other creatures The low fire attribute suggests that it may have a waterbased aspect, in line with the name'),
# Corruptorix 💀🐭 2p 3h
# costs: 🔥 has: 🔥👻 pot: 23
Blueprint(original=Card(name='Corruptorix', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Fertility]), description='name is a combination of \"corruption,\" which is in line with the instant death skill, and \"rix,\" which is a suffix denoting royalty or a highranking individual The high power and instant death skills suggest a powerful and malevolent creature that can easily take down opponents, with the fertility skill implying the ability to corrupt others and reproduce'),
# Ironhideon 🔰 2p 8h
# costs: 🔥 has: 🔥 pot: 23
Blueprint(original=Card(name='Ironhideon', power=2, health=8, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield]), description='name is a combination of \"ironhide,\" which implies incredible durability, and \"don,\" meaning \"lord\" or \"master\" The high health and shield skill make it seem like an imposing and nearly indestructible creature that can easily defend itself and others The low fire attribute adds to the idea of being tough and resilient '),
# Gremlin 💀🐩🧺🐭 2p 1h
# costs: 🔥🔥🔥 has: 🔥 pot: 26
Blueprint(original=Card(name='Gremlin', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.InstantDeath, skills.Underdog, skills.Packrat, skills.Fertility]), description='packrat skill, higher fire cost, low stats  mischievous creature that causes trouble'),
# Incubus 🐭🔰💀 2p 1h
# costs: 🔥 has: 🔥👻👻 pot: 27
Blueprint(original=Card(name='Incubus', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='spirit element, fertility skill, shield skill  seductive creature with supernatural abilities'),
# Gnome 🐩🔰🐭 1p 2h
# costs: 🔥 has: 🔥👻👻 pot: 24
Blueprint(original=Card(name='Gnome', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Underdog, skills.Shield, skills.Fertility]), description='small and weak with Underdog and Shield, but the Fertility skill hints at a magical or alchemical affinity, fitting for a gnome'),
# ReaperWolf 💀🐩 2p 8h
# costs: 🔥 has: 👻 pot: 27
Blueprint(original=Card(name='ReaperWolf', power=2, health=8, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath, skills.Underdog]), description='Instant Death, Underdog High health, low power, and no fire'),
# Thundercat 🐭 8p 2h
# costs: 🔥 has: 🔥 pot: 25
Blueprint(original=Card(name='Thundercat', power=8, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility]), description='High power, low health, strong fire, and Fertility skill'),
# PhoenixPup 🔰🐭 4p 2h
# costs: 🔥 has: 🔥👻 pot: 25
Blueprint(original=Card(name='PhoenixPup', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Fertility]), description='Shield, Fertility, and a good balance between power, health, and fire'),
# InfernoRat 🐩🔰💀🐭 2p 1h
# costs: 🔥🔥🔥 has: 🔥🔥 pot: 28
Blueprint(original=Card(name='InfernoRat', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=2, skills=[skills.Underdog, skills.Shield, skills.InstantDeath, skills.Fertility]), description='Instant Death, Shield, Underdog, and high fire cost for a relatively low power and health'),
# ThornyFox 🔰💀🦔🐩 2p 2h
# costs: 🔥 has: 🔥👻 pot: 26
Blueprint(original=Card(name='ThornyFox', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.InstantDeath, skills.Spines, skills.Underdog]), description='Shield, Instant Death, Spines, and a good balance between power, health, and spirits'),
# Drakeling 🔰🧺🦔🐭 0p 2h
# costs: 🔥 has: 🔥🔥 pot: 26
Blueprint(original=Card(name='Drakeling', power=0, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=2, skills=[skills.Shield, skills.Packrat, skills.Spines, skills.Fertility]), description='very fireoriented, strong shield, moderate powerhealth, spines, and packratting tendencies'),
# Titan 🐭 2p 8h
# costs: 🔥 has: 🔥👻 pot: 26
Blueprint(original=Card(name='Titan', power=2, health=8, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='very high health, no skills, but very low cost'),
# Griffin 🐩🧺🔰 3p 3h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 26
Blueprint(original=Card(name='Griffin', power=3, health=3, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Underdog, skills.Packrat, skills.Shield]), description='underdog, good powerhealth, strong shield, and packratting tendencies'),
# BlazeHare  9p 1h
# costs: - has: 🔥 pot: 27
Blueprint(original=Card(name='BlazeHare', power=9, health=1, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='relates to the high power and fire attribute and the low health attribute, while the \"Hare\" part suggests a fast but weak creature, befitting the card\'s high power and low health'),
# PackFalcon 🐭🔰🧺 3p 1h
# costs: 🔥 has: 🔥🔥🔥👻 pot: 28
Blueprint(original=Card(name='PackFalcon', power=3, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.Packrat]), description='relates to the packrat and shield skills, while \"Falcon\" sounds noble The high fire attribute and low spirits make this creature look less supernatural'),
# DeathDrake 🧺💀🐭🔰 2p 1h
# costs: 🔥🔥🔥🔥🔥🔥🔥 has: 🔥👻👻👻 pot: 28
Blueprint(original=Card(name='DeathDrake', power=2, health=1, costs_fire=7, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Packrat, skills.InstantDeath, skills.Fertility, skills.Shield]), description='relates to the instant death skill, while \"Drake\" sounds powerful and mythical The high fire cost suggests a creature that is difficult to summon, while the high spirit attribute supports its omenlike nature'),
# FertileAves 🪁🧺🔰🐭 2p 1h
# costs: 🔥 has: 🔥👻 pot: 27
Blueprint(original=Card(name='FertileAves', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Soaring, skills.Packrat, skills.Shield, skills.Fertility]), description='relates to the fertility skill, while \"Aves\" sounds dignified The card\'s low power and health and high spirits attribute suggest a spirit animal instead of a real one The low fire cost might reflect a creature that is easy to summon'),
# ShieldBug 🐩🔰 1p 3h
# costs: - has: 🔥👻👻👻👻 pot: 29
Blueprint(original=Card(name='ShieldBug', power=1, health=3, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=1, skills=[skills.Underdog, skills.Shield]), description='relates to the shield skill, while \"Bug\" sounds humble The high spirit attribute reflects the card\'s ability to function as an underdog The high health and low power suggest a creature that can absorb a lot of damage while dealing only little The absence of fire attribute suggests a creature that does not possess any innate magic power'),
# Kraken 🔰🐩💀 7p 1h
# costs: 👻👻👻👻 has: 🔥🔥 pot: 28
Blueprint(original=Card(name='Kraken', power=7, health=1, costs_fire=0, costs_spirits=4, has_spirits=0, has_fire=2, skills=[skills.Shield, skills.Underdog, skills.InstantDeath]), description='deadly, expensive, lacks spirits but has strong fire, can potentially kill instantly, underdog'),
# Sprite 🧺💀🐩 1p 1h
# costs: - has: 🔥👻 pot: 28
Blueprint(original=Card(name='Sprite', power=1, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat, skills.InstantDeath, skills.Underdog]), description='small, low powerhealth, cheap, has packrat tendencies and surprising skills up her sleeve'),
# Blaze Drake 🐭🔰💀 3p 2h
# costs: 🔥🔥 has: 🔥🔥🔥👻 pot: 30
Blueprint(original=Card(name='Blaze Drake', power=3, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='a dragonlike creature with firerelated abilities and instant death skill'),
# Moon Cat 🐭🧺 5p 4h
# costs: 🔥 has: 🔥👻👻 pot: 30
Blueprint(original=Card(name='Moon Cat', power=5, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.Packrat]), description='a magical cat with packrat skill and a high spirit count'),
# Mist Basilisk 💀 2p 6h
# costs: - has: 🔥👻 pot: 30
Blueprint(original=Card(name='Mist Basilisk', power=2, health=6, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='a snakelike creature that represents death and has no fire cost'),
# Thorned Puma 🧺💀🔰🦔 5p 1h
# costs: 🔥🔥 has: 🔥👻👻👻 pot: 32
Blueprint(original=Card(name='Thorned Puma', power=5, health=1, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Packrat, skills.InstantDeath, skills.Shield, skills.Spines]), description='a dangerous catlike creature with spines and instant death skills'),
# Flame Mongoose 🐭🧺 6p 3h
# costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 32
Blueprint(original=Card(name='Flame Mongoose', power=6, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=4, skills=[skills.Fertility, skills.Packrat]), description='a quick and cunning creature with packrat skill and high fire count'),
# Serpentine 🔰🧺🐭💀 7p 3h
# costs: 👻👻👻👻👻👻👻👻👻👻 has: - pot: 34
Blueprint(original=Card(name='Serpentine', power=7, health=3, costs_fire=0, costs_spirits=10, has_spirits=0, has_fire=0, skills=[skills.Shield, skills.Packrat, skills.Fertility, skills.InstantDeath]), description='referring to the high power and low health, as well as the shield skill which can protect the card like a snake\'s scales The packrat skill could reference their tendency to hoard treasure, and the fertility and instant death skills could allude to the card\'s ability to both generate and destroy life quickly'),
# Skylarkspur 🐭🪁🐩🔰 3p 2h
# costs: 👻 has: 🔥👻👻👻 pot: 30
Blueprint(original=Card(name='Skylarkspur', power=3, health=2, costs_fire=0, costs_spirits=1, has_spirits=3, has_fire=1, skills=[skills.Fertility, skills.Soaring, skills.Underdog, skills.Shield]), description='a combination of \"skylark\", which can symbolize freedom and soaring through the air fitting for the \"soaring\" skill, and \"spur\", which can symbolize an underdog rising to the challenge fitting for the \"underdog\" skill The fertility and shield skills could reference this creature\'s ability to protect and heal others'),
# Cephalipod 🧺🔰🐭 3p 4h
# costs: 🔥🔥 has: 👻 pot: 30
Blueprint(original=Card(name='Cephalipod', power=3, health=4, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='a reference to the card\'s tentacles similar in shape to the packrat skill icon, which are used for both defense and offense, and the high health as many cephalopods are renowned for their regenerative abilities The shield and fertility skills could also reference their nurturing and protective instincts'),
# Chrysophant 🧺🚀🐭 1p 9h
# costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 32
Blueprint(original=Card(name='Chrysophant', power=1, health=9, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Packrat, skills.Airdefense, skills.Fertility]), description='a reference to the card\'s high spirituality as \"chryso\" means \"gold\" and could represent spiritual purity, and its packrat and air defense skills with \"phant\" referencing the creature\'s defensive and strategic capabilities The fertility skill could also represent the creature\'s ability to create abundance and prosperity'),
# Pyropard 🧺💀🐭 2p 4h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 32
Blueprint(original=Card(name='Pyropard', power=2, health=4, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Packrat, skills.InstantDeath, skills.Fertility]), description='a combination of \"pyro\" referring to fire, fitting for the card\'s high fire attribute and \"leopard\" fitting for the card\'s agility and skill with the instant death ability The packrat and fertility skills might also reference this creature\'s cunning and resourcefulness in survival'),
# Wyvern 🐭💀🔰 3p 2h
# costs: 🔥 has: 🔥🔥👻👻 pot: 31
Blueprint(original=Card(name='Wyvern', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Shield]), description='powerful, firebased, some spirits, high health with a touch of fertility, and the defenses of shield and instant death'),
# Yeti 🐭🔰 9p 2h
# costs: 🔥🔥🔥🔥 has: 👻👻 pot: 31
Blueprint(original=Card(name='Yeti', power=9, health=2, costs_fire=4, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Fertility, skills.Shield]), description='the powerful aura aligns with its high power rating, hardly showing any fire as an element, but certainly a hard hitter'),
# Fyrewolf 🐭🧺🔰 2p 6h
# costs: 🔥 has: 🔥🔥👻 pot: 35
Blueprint(original=Card(name='Fyrewolf', power=2, health=6, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Fertility, skills.Packrat, skills.Shield]), description='combines \"fire\" and \"wolf\" to match the card\'s high fire attribute and attacking skills'),
# Dreamcat 🔰 1p 9h
# costs: - has: 🔥👻👻 pot: 35
Blueprint(original=Card(name='Dreamcat', power=1, health=9, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Shield]), description='combines \"dream\" and \"cat\" to match the card\'s high health and protective skills'),
# Pixiebat 🐭 1p 9h
# costs: - has: 🔥👻👻 pot: 36
Blueprint(original=Card(name='Pixiebat', power=1, health=9, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility]), description='combines \"pixie\" and \"bat\" to match the card\'s high spirits and fertility skills, as well as its low power'),
# Titanape 🐭🐩🔰 7p 2h
# costs: 🔥 has: 🔥👻 pot: 34
Blueprint(original=Card(name='Titanape', power=7, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.Underdog, skills.Shield]), description='combines \"titan\" and \"ape\" to match the card\'s high power and underdog skills, as well as its low health'),
# Infernowolf 💀🔰🧺🐭 4p 2h
# costs: 🔥 has: 👻 pot: 35
Blueprint(original=Card(name='Infernowolf', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath, skills.Shield, skills.Packrat, skills.Fertility]), description='With a high power and low health, this card is fiercely dangerous Its skills do not necessarily relate directly to its name, but packrat and fertility can hint at the card\'s fiery nature Shields are needed to counter its high damage output'),
# Phoenixbat 🧺🔰🐭🪁 0p 4h
# costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 33
Blueprint(original=Card(name='Phoenixbat', power=0, health=4, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=2, skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.Soaring]), description='With high health and spirit values, this card is difficult to take down and can soar over enemies with its skill of flight Its packrat skill means it can build up a powerful surge of attacks from its flaming aura attacks, and with fertility, it can rapidly reproduce'),
# Valkyrie 🐭💀🧺 6p 2h
# costs: 🔥 has: 🔥👻👻 pot: 35
Blueprint(original=Card(name='Valkyrie', power=6, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat]), description='a powerful and mystical female warrior, fitting for a card with high power and fertility abilities, but balanced with lower health and fire cost'),
# Hoarder 🧺🦔 2p 8h
# costs: - has: 👻👻👻 pot: 36
Blueprint(original=Card(name='Hoarder', power=2, health=8, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=0, skills=[skills.Packrat, skills.Spines]), description='this packrat is a creature with high health and a tendency to collect resources, reflected in its \"Packrat\" skill'),
# Narwal 🦔💀 7p 2h
# costs: - has: 🔥👻 pot: 35
Blueprint(original=Card(name='Narwal', power=7, health=2, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines, skills.InstantDeath]), description='a unicornlike creature with sharp tusks, reflected in its high power and \"Spines\" skill'),
# Tanuki 💀🐭🦔 7p 4h
# costs: 🔥 has: 🔥👻 pot: 36
Blueprint(original=Card(name='Tanuki', power=7, health=4, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Fertility, skills.Spines]), description='a mischievous shapeshifting animal in Japanese folklore known for playing deadly pranks on humans The high power and skills of Instant Death and spines fit this character, while Fertility adds to their craftiness overall'),
# Hippocampus 🔰🐭💀 1p 8h
# costs: 🔥 has: 🔥👻 pot: 36
Blueprint(original=Card(name='Hippocampus', power=1, health=8, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Fertility, skills.InstantDeath]), description='a creature from Greek mythology with the upper body of a horse and the lower body of a fish The high health and skills of Shield and Fertility suggest a resilient and prolific creature, while the skill of Instant Death hints at its potential for surprise attacks '),
# Nightfox 🧺💀🔰 10p 3h
# costs: 🔥 has: 🔥👻 pot: 41
Blueprint(original=Card(name='Nightfox', power=10, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat, skills.InstantDeath, skills.Shield]), description='The name Nightfox sounds powerful and the card has a high power value The skill InstantDeath adds to the power and the skill Packrat could represent the fox\'s cunning and resourcefulness, while the Shield skill could relate to the fox being elusive and hard to hit'),
# Sunhare 🧺🔰🐭 4p 4h
# costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 37
Blueprint(original=Card(name='Sunhare', power=4, health=4, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=5, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='The name Sunhare implies a quick and agile creature, which could represent the high fire value and Packrat skill The high health value could also come from the hare\'s wellknown ability to quickly regenerate The Fertility skill could represent the hare\'s ability to mate frequently and multiply'),
# Flamefalcon 🐭🧺💀 5p 4h
# costs: 🔥 has: 🔥🔥👻👻 pot: 37
Blueprint(original=Card(name='Flamefalcon', power=5, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='The name Flamefalcon is fitting for a card with high fire attribute and the skills InstantDeath and Fertility Falcons are known for their speed and agility, while the fire attribute and InstantDeath skill could represent the falcon\'s fiery and deadly nature The Fertility skill could represent the falcon\'s ability to mate frequently and raise large broods'),
# Spiritowl 🐩🔰🧺🐭 2p 5h
# costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 39
Blueprint(original=Card(name='Spiritowl', power=2, health=5, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=2, skills=[skills.Underdog, skills.Shield, skills.Packrat, skills.Fertility]), description='The name Spiritowl combines the card\'s high spirit attribute with the skill Packrat, which could represent the owl\'s wise and cunning nature The Shield skill could represent the owl\'s protective nature towards its young, while the Underdog skill could represent the owl\'s ability to outsmart its prey The high health value could also represent the owl\'s resilience and ability to endure'),
# Deathviper 💀🧺🐭🔰 3p 2h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 37
Blueprint(original=Card(name='Deathviper', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility, skills.Shield]), description='The name Deathviper represents a deadly and poisonous creature, fitting for a card with the InstantDeath skill The fire attribute and Fertility skill could represent the viper\'s ability to incubate its eggs, while the Packrat skill could represent the viper\'s cunning and ability to store venom for later use The relatively low health value could represent the viper\'s fragility despite its deadly nature'),
# DragonRock 🔰🐭💀 8p 3h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 41
Blueprint(original=Card(name='DragonRock', power=8, health=3, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.Fertility, skills.InstantDeath]), description='related to its high power and health, while the rock element reflects the high defense shield skill represented by the shield skill and the ability to stay alive after every attack fertility skill, and instant death which can be caused by its powerful attacks'),
# FireHound 🐭🧺🔰 7p 4h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='FireHound', power=7, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Fertility, skills.Packrat, skills.Shield]), description='related to the fire element represented by the cards\' ability to manipulate and use this element hasfire and costsfire, hound resembling the packrat skill, and that it\'s somewhat fragile due to its lower health'),
# SkyKraken 🪁💀🐩🐭 3p 7h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='SkyKraken', power=3, health=7, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Soaring, skills.InstantDeath, skills.Underdog, skills.Fertility]), description='related to the card\'s ability to fly soaring skill, high health, and the underdog skill which suggests that this creature is capable of defending itself from attacks Krakens are mythical creatures that have a reputation for being huge, strong, and hard to defeat'),
# ShieldTurtle 🔰🐩🐭💀 5p 3h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='ShieldTurtle', power=5, health=3, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.Underdog, skills.Fertility, skills.InstantDeath]), description='related to its high defense and ability to shield itself shield skill, high power but relatively low health, and ability to come back to life after being defeated thanks to its fertility skill'),
# ShadowCub 🐭💀🧺 2p 10h
# costs: 🔥 has: 🔥👻 pot: 41
Blueprint(original=Card(name='ShadowCub', power=2, health=10, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat]), description='related to its low power, high health its ability to survive, and its instant death skill sudden and stealthy like a shadow Cub reflects the fertility and packrat skills'),
# Dracotaur 🧺🔰 6p 3h
# costs: - has: 🔥🔥👻👻👻 pot: 40
Blueprint(original=Card(name='Dracotaur', power=6, health=3, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Packrat, skills.Shield]), description='combining \"dragon\" and \"centaur\", this name reflects the card\'s high power and skill combination of Packrat and Shield, as well as its moderate health and dual firespirit costs that balance out its strength'),
# Bramblewyrm 🐭🧺💀🦔 5p 5h
# costs: 🔥 has: 🔥👻👻👻 pot: 42
Blueprint(original=Card(name='Bramblewyrm', power=5, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath, skills.Spines]), description='combining \"bramble\" and \"wyrm\" a type of dragon, this name fits the spiked and sharptoothed card with high power and health, as well as its combination of Fertility and Packrat skills suggesting the ability to propagate and hoard resources, and Spines skill evoking the idea of brambles'),
# Frostfox 💀🔰🐭 2p 3h
# costs: - has: 🔥🔥👻👻 pot: 41
Blueprint(original=Card(name='Frostfox', power=2, health=3, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='suggesting a creature that is agile and elusive, this name fits the card\'s low power and health but high spirit and fire costs that suggest it is highly specialized and difficult to catch, and its skills of InstantDeath and Shield which further evoke the idea of a trickster that can slip past danger and defend itself when cornered'),
# Phoenixfire 🐭🐩🔰 3p 3h
# costs: - has: 🔥🔥🔥🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Phoenixfire', power=3, health=3, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=5, skills=[skills.Fertility, skills.Underdog, skills.Shield]), description='fits the attribute balance, with higher fire costs representing the bird\'s mythical fire element, along with above average stats and fertility, and the skills that suggest a rebirth in tough fights'),
# Glowworm 🐭🔰🐩 2p 4h
# costs: - has: 🔥🔥👻👻👻 pot: 41
Blueprint(original=Card(name='Glowworm', power=2, health=4, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.Underdog]), description='With decent power and health, this card has no attribute costs and moderate spiritfire costs It also has skills that protect it, making it a versatile and adaptable card that will light up any deck'),
# Unicorn 🧺🔰🐭 4p 7h
# costs: 👻👻 has: 🔥🔥🔥👻👻👻👻 pot: 42
Blueprint(original=Card(name='Unicorn', power=4, health=7, costs_fire=0, costs_spirits=2, has_spirits=4, has_fire=3, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='This name is already in use, but I would suggest it for this card as it has high spirit values and the skills Packrat and Fertility suggest it could have a magical and nurturing quality, like a unicorn in legends The high health value also reinforces the idea of a creature that is hard to harm'),
# Gorgonfly 🧺🔰🪁🦔 4p 4h
# costs: - has: 🔥🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Gorgonfly', power=4, health=4, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Packrat, skills.Shield, skills.Soaring, skills.Spines]), description='Combination of gorgon mythical creature with sharp teeth and claws and fly, which fits with the card\'s spines and ability to soar The powerhealth values are midrange, and the cost values are low, so the name should reflect that'),
# Phoenixowl 🪁🐭🧺💀🐩 2p 8h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 45
Blueprint(original=Card(name='Phoenixowl', power=2, health=8, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Soaring, skills.Fertility, skills.Packrat, skills.InstantDeath, skills.Underdog]), description='Combination of phoenix mythical bird that rises from the ashes and owl, which fits with the card\'s instant death and flying abilities The high health value suggests a strong creature, but its relatively low power means that it is better at surviving than attacking, which is reflected in the name'),
# Chimeraclaw 🐭🔰💀🧺🐩🦔 3p 3h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 45
Blueprint(original=Card(name='Chimeraclaw', power=3, health=3, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.InstantDeath, skills.Packrat, skills.Underdog, skills.Spines]), description='Combination of chimera mythical creature made of different animal parts and claw, which fits with the card\'s high number of skills The midrange values for powerhealth suggest a creature that is adaptable, which is reflected in the name'),
# Thunderpuma 🔰🐩💀 5p 3h
# costs: - has: 🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Thunderpuma', power=5, health=3, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.Underdog, skills.InstantDeath]), description='Combination of thunder powerful force of nature and puma, which fits with the card\'s high power value The midrange health value suggests a creature that can dish out damage but is also vulnerable, which is reflected in the name'),
# Infernewt 🐭🔰 7p 3h
# costs: - has: 🔥🔥🔥🔥👻👻 pot: 45
Blueprint(original=Card(name='Infernewt', power=7, health=3, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=4, skills=[skills.Fertility, skills.Shield]), description='it\'s a rare, fiery, and quite hot salamander that is able to shield against other coldblooded animals, yet it has a low spirit as it is still young, hence the high fire cost'),
# Gloomhound 🔰🐭🐩 8p 7h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 47
Blueprint(original=Card(name='Gloomhound', power=8, health=7, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Shield, skills.Fertility, skills.Underdog]), description='this fierce and gloomylooking canine enjoys being an underdog, will never run out of fire, and is quite fertile, making it a persistent hunter, and feared by its prey'),
# Spirit Wolf  1p 4h
# costs: 👻👻👻👻👻👻👻 has: 🔥👻 pot: 4
Blueprint(original=Card(name='Spirit Wolf', power=1, health=4, costs_fire=0, costs_spirits=7, has_spirits=1, has_fire=1, skills=[]), description='highly spiritual, with decent health and power'),
# Fire Drake 🍀 0p 2h
# costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 3
Blueprint(original=Card(name='Fire Drake', power=0, health=2, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.LuckyStrike]), description='high fire affinity with a lucky strike skill'),
# Storm Lion  1p 2h
# costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 3
Blueprint(original=Card(name='Storm Lion', power=1, health=2, costs_fire=4, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='expensive card with decent power and health'),
# Aqua Fox  0p 3h
# costs: 🔥 has: - pot: 4
Blueprint(original=Card(name='Aqua Fox', power=0, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[]), description='no fire or spirits but high health and agility'),
# Firecat  3p 1h
# costs: 👻👻👻👻 has: 🔥👻 pot: 5
Blueprint(original=Card(name='Firecat', power=3, health=1, costs_fire=0, costs_spirits=4, has_spirits=1, has_fire=1, skills=[]), description=' spirits,  power,  health,  fire,  skills'),
# Glimmerwing  2p 1h
# costs: 🔥 has: 🔥 pot: 5
Blueprint(original=Card(name='Glimmerwing', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description=' spirit,  power,  health,  fire,  skills'),
# Aquaconda  2p 3h
# costs: 🔥🔥 has: 👻👻 pot: 8
Blueprint(original=Card(name='Aquaconda', power=2, health=3, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=0, skills=[]), description=' spirits,  power,  health,  fire,  skills'),
# Pyrofox  0p 3h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 8
Blueprint(original=Card(name='Pyrofox', power=0, health=3, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[]), description=' spirits,  power,  health,  fire,  skills'),
# Shadowrat  2p 1h
# costs: 👻 has: 🔥 pot: 5
Blueprint(original=Card(name='Shadowrat', power=2, health=1, costs_fire=0, costs_spirits=1, has_spirits=0, has_fire=1, skills=[]), description=' spirit,  power,  health,  fire,  skills'),
# Harpy  3p 1h
# costs: 🔥 has: 🔥👻 pot: 7
Blueprint(original=Card(name='Harpy', power=3, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='moderately powered and healthy, low cost in fire, average spirits, no special skills'),
# Sylph  2p 4h
# costs: 👻👻👻👻 has: 🔥🔥👻👻 pot: 10
Blueprint(original=Card(name='Sylph', power=2, health=4, costs_fire=0, costs_spirits=4, has_spirits=2, has_fire=2, skills=[]), description='with an abundance of spirits, this card is light and airy but also powerful and durable, like a creature with wings'),
# Whelk  1p 2h
# costs: 🔥🔥 has: 🔥👻👻 pot: 6
Blueprint(original=Card(name='Whelk', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='this is a mollusk with a spiral shell, representing the card\'s spiraling up powertocost ratio The health is also relatively high for the cost'),
# Efreet  2p 1h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 9
Blueprint(original=Card(name='Efreet', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[]), description='this fierce fiery creature is strong but fragile, having low health, representing a dangerously balanced nature of this card'),
# Tortoise 🔰 0p 1h
# costs: 👻 has: 🔥🔥 pot: 8
Blueprint(original=Card(name='Tortoise', power=0, health=1, costs_fire=0, costs_spirits=1, has_spirits=0, has_fire=2, skills=[skills.Shield]), description='a creature known for its sturdiness and defense, especially its shell, the name represents the high defense and specifically the shield skill that the card holds'),
# Mermaid  1p 2h
# costs: 🔥 has: 👻👻👻 pot: 7
Blueprint(original=Card(name='Mermaid', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=0, skills=[]), description='low power and health, costly in terms of spirits, no fire element, no skills  Mermaids are mythical creatures associated with the ocean and often portrayed as being beautiful but dangerous'),
# Dragon  1p 3h
# costs: 🔥 has: 🔥🔥 pot: 7
Blueprint(original=Card(name='Dragon', power=1, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=2, skills=[]), description='low power, moderate health, costly in terms of fire, no spirits, high fire element, no skills  Dragons are mythical creatures often associated with fire and destruction'),
# Falconer 🪁 4p 2h
# costs: 🔥 has: 🔥 pot: 12
Blueprint(original=Card(name='Falconer', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Soaring]), description='The card\'s skill is Soaring, which suggests a bird, while the high power and low health suggest a bird handler rather than the bird itself In combination with the cost to play the card  fire, Falconer fits well'),
# Selkie  2p 2h
# costs: 👻👻 has: 🔥🔥👻👻 pot: 8
Blueprint(original=Card(name='Selkie', power=2, health=2, costs_fire=0, costs_spirits=2, has_spirits=2, has_fire=2, skills=[]), description='The card has an equal balance of spirits and fire, suggesting a creature related to water The cost to play the card  fire,  spirits suggests something that is elusive and only appears in certain conditions Selkies are mythical creatures that are said to live as seals in the sea but transform into humans on land'),
# Lemming  1p 3h
# costs: 🔥 has: 👻👻👻👻 pot: 9
Blueprint(original=Card(name='Lemming', power=1, health=3, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=0, skills=[]), description='The card has a high spirits attribute, suggesting a small creature that has a lot of energy The name Lemming fits with the game\'s animal theme, and also makes sense based on the low power and high health, as lemmings are known for their endurance'),
# Scorpatron 🔰 2p 1h
# costs: 🔥🔥🔥 has: 🔥 pot: 9
Blueprint(original=Card(name='Scorpatron', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield]), description='Scorpion  Patronus'),
# Sparkferret 🧺 2p 1h
# costs: 🔥 has: 👻👻 pot: 11
Blueprint(original=Card(name='Sparkferret', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Packrat]), description='A small, quick creature with a Packrat skill, this card has low health but agile movement, providing an excellent counter to larger and slower enemies Its fire cost is moderate, but its  power makes it a good investment'),
# Spikeback  4p 1h
# costs: 🔥 has: 🔥👻 pot: 9
Blueprint(original=Card(name='Spikeback', power=4, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='referring to the high power of  and the low health of , as well as the spike on the card, which indicates it is a defensive creature'),
# Skywhipper 🪁 2p 2h
# costs: 🔥 has: 🔥👻👻👻 pot: 11
Blueprint(original=Card(name='Skywhipper', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Soaring]), description='referring to the skill Soaring, combined with the moderate power and health values and the high spirit value that indicate it is a fast, agile creature'),
# Soulripper 💀 1p 3h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Soulripper', power=1, health=3, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='referring to the skill InstantDeath, combined with the low power and high health values and the high fire cost which suggest it can be a tricky, elusive adversary'),
# Packmouse 🧺 2p 1h
# costs: 🔥 has: - pot: 9
Blueprint(original=Card(name='Packmouse', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Packrat]), description='referring to the low attribute values and the presence of the skill Packrat that suggests it is a weak, but devious creature that relies on cunning rather than strength'),
# Flameclaw  3p 1h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 11
Blueprint(original=Card(name='Flameclaw', power=3, health=1, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=3, skills=[]), description='referring to the moderate power and low health values, combined with the high fire and spirit costs, as well as the presence of the keyword \"fire\" in the name which hints at the card\'s elemental affinity'),
# Fireflyer 🔰 1p 4h
# costs: 🔥 has: 👻 pot: 14
Blueprint(original=Card(name='Fireflyer', power=1, health=4, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Shield]), description='fast  health for  costfire, defensive Shield, fiery hasfire'),
# Moonwolf  5p 1h
# costs: 👻 has: 🔥👻 pot: 11
Blueprint(original=Card(name='Moonwolf', power=5, health=1, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[]), description='very spiritual hasspirits, costsspirits, swift attacker power, with no extra skills'),
# Starshell  2p 5h
# costs: 👻👻 has: 🔥🔥 pot: 12
Blueprint(original=Card(name='Starshell', power=2, health=5, costs_fire=0, costs_spirits=2, has_spirits=0, has_fire=2, skills=[]), description='dual element card  hasfire,  hasspirits, tough exterior  health, low attack  power'),
# Packbeast 🧺 5p 1h
# costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Packbeast', power=5, health=1, costs_fire=4, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='highly valued for carrying heavy loads, high power and low health with ability to steal cards'),
# Sunbird 🐭 1p 1h
# costs: 🔥 has: 👻👻 pot: 12
Blueprint(original=Card(name='Sunbird', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Fertility]), description='a bird that feeds on sunlight and has high spirit but low fire'),
# Pixie 🐭 1p 1h
# costs: 🔥🔥 has: 🔥👻 pot: 11
Blueprint(original=Card(name='Pixie', power=1, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='a small, mischievous creature that enhances fertility in other cards, low stats but useful skills'),
# Stormcrow 💀 2p 3h
# costs: 🔥🔥 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Stormcrow', power=2, health=3, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='This card\'s high health and power, combined with the InstantDeath skill, suggests a powerful and formidable bird of prey The name Stormcrow reflects its power and possible affinity with air elements'),
# Banshee InstantDeath 💀 2p 2h
# costs: 🔥 has: 👻 pot: 13
Blueprint(original=Card(name='Banshee InstantDeath', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath]), description='Banshees are mystical creatures known for their ability to induce instant death through their scream The high powerhealth and the skill align with their deadly reputation'),
# PhoenixDeath 💀 1p 2h
# costs: 🔥🔥 has: 🔥👻👻👻👻 pot: 14
Blueprint(original=Card(name='PhoenixDeath', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=1, skills=[skills.InstantDeath]), description='relates to the Instant Death skill and the high fire cost, suggesting a powerful, fiery creature'),
# GorgonWrath 💀 2p 1h
# costs: 🔥 has: 🔥👻👻 pot: 13
Blueprint(original=Card(name='GorgonWrath', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath]), description='relates to the Instant Death skill and high power, suggesting a dangerous, mythical creature'),
# Dragonflame 🐩 1p 3h
# costs: 🔥 has: 🔥🔥🔥 pot: 12
Blueprint(original=Card(name='Dragonflame', power=1, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=3, skills=[skills.Underdog]), description='relates to the high fire cost and the Underdog skill, suggesting a fierce and powerful creature with flames'),
# ChimeraStrength  2p 4h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 14
Blueprint(original=Card(name='ChimeraStrength', power=2, health=4, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[]), description='relates to the relatively high power and health values, and the mixed element cost, suggesting a mythical and powerful creature'),
# FairyFertility 🐭 1p 2h
# costs: 🔥 has: 🔥 pot: 13
Blueprint(original=Card(name='FairyFertility', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility]), description='relates to the Fertility skill and the low attribute values, suggesting a small and magical creature with the ability to enhance growth'),
# Gryphoness 🪁 5p 2h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 15
Blueprint(original=Card(name='Gryphoness', power=5, health=2, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Soaring]), description='a flying female creature with balanced fire and spirit costs, soaring ability, and decent powerhealth'),
# Warg  2p 5h
# costs: 🔥 has: 🔥👻 pot: 13
Blueprint(original=Card(name='Warg', power=2, health=5, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a wolflike hunter with moderate powerhealth, moderate fire and spirit costs, and no skills'),
# Leviathan  7p 2h
# costs: 🔥 has: 🔥 pot: 15
Blueprint(original=Card(name='Leviathan', power=7, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='high power, aquatic, fire element, no spirit element'),
# Enchantress 🐭💀 1p 1h
# costs: 🔥 has: 🔥👻 pot: 18
Blueprint(original=Card(name='Enchantress', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.InstantDeath]), description='low powerhealth, fertility skill, instant death skill, firealigned'),
# Pegasus  2p 6h
# costs: 🔥 has: 🔥👻👻👻👻👻👻 pot: 19
Blueprint(original=Card(name='Pegasus', power=2, health=6, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=1, skills=[]), description='very high health, high spirit, moderate power, no skills'),
# Deathbat 💀🧺 3p 1h
# costs: 🔥🔥 has: 🔥 pot: 17
Blueprint(original=Card(name='Deathbat', power=3, health=1, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.InstantDeath, skills.Packrat]), description='high power with InstantDeath skill, low health, and low spirit values, giving the card a dangerous and risky play style The name comes from a creature that is dark and deadly in nature, befitting of the card\'s attributes'),
# Gnomeleon  2p 3h
# costs: - has: 🔥👻 pot: 19
Blueprint(original=Card(name='Gnomeleon', power=2, health=3, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='very low power, decent health, no spirit cost, and no special skills but still has the fire attribute The name is a combination of Gnome and Chameleon, mythical creatures which are known for being elusive and deceptive, fitting with the card\'s low power and evasive capabilities'),
# Skyfin 🔰🧺🚀 0p 5h
# costs: 🔥🔥🔥🔥 has: 🔥👻👻 pot: 20
Blueprint(original=Card(name='Skyfin', power=0, health=5, costs_fire=4, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Shield, skills.Packrat, skills.Airdefense]), description='low power but high health, with a very high fire cost, and multiple skills like Shield, Packrat, and Airdefense The name combines \"Sky\" for the high cost of fire and \"Fin\" referring to fins or a shield giving this creature a tough exterior The skills add to this metaphor making it hard to take down quickly'),
# GhostCat 💀 4p 4h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 21
Blueprint(original=Card(name='GhostCat', power=4, health=4, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.InstantDeath]), description='With its high fire attribute, this card is ghostly and untouchable The instant death skill adds to its deadly nature'),
# ShadowFox 🦔🐭🧺🐩 0p 2h
# costs: 🔥🔥🔥🔥🔥 has: - pot: 18
Blueprint(original=Card(name='ShadowFox', power=0, health=2, costs_fire=5, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Spines, skills.Fertility, skills.Packrat, skills.Underdog]), description='With no fire or spirit attributes, this card is elusive like a shadow Its high health, paired with skills like spines and shield, make it a formidable opponent'),
# Flamehawk 🦔🔰 2p 4h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 18
Blueprint(original=Card(name='Flamehawk', power=2, health=4, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines, skills.Shield]), description='With balanced fire and spirit attributes, this card is a fierce predator that uses its spines and shield to defend itself and strike back at foes'),
# RatMage 🧺 2p 1h
# costs: - has: 🔥👻 pot: 21
Blueprint(original=Card(name='RatMage', power=2, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='With low power and health attributes, this card relies on its packrat skill to steal and hoard resources'),
# DreamLion 🐭💀 2p 1h
# costs: 🔥🔥🔥 has: 👻👻👻 pot: 19
Blueprint(original=Card(name='DreamLion', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=0, skills=[skills.Fertility, skills.InstantDeath]), description='With low fire and high spirit attributes, this card is dreamy and mysterious Its fertility skill allows it to rapidly reproduce, making it a difficult opponent to overcome'),
# Glitterfly  0p 1h
# costs: 🔥 has: 🔥👻👻 pot: 3
Blueprint(original=Card(name='Glitterfly', power=0, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='This creature has a high spirit pool, which is reflected in its ability to fly and burst its way to victory using its speed It\'s low on power, but boasts moderate health, making the Glitterfly a great closer when the opponent is low on cards The name pays homage to its bright and slightly mesmerizing glow, but don\'t let the beauty of the creature fool you'),
# ShadowCat  2p 2h
# costs: 🔥 has: 🔥 pot: 7
Blueprint(original=Card(name='ShadowCat', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='This card\'s attributes suggest a stealthy animal lurking in the shadows, ready to pounce on its prey The decent power and health, together with a relatively low fire cost make it a good contender for a balanced deck The lack of spirits could suggest a more solitary nature, fitting with a catlike creature'),
# FlameFox  2p 1h
# costs: 🔥 has: 👻 pot: 5
Blueprint(original=Card(name='FlameFox', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='This card has average health and low power, but the potential for high spirits and the absence of fire in its cost make it more of a spiritual fox than a firey one The alliteration in the name adds to the whimsy of the game, and the foxes\' cunning character could go well with some of the game\'s skill cards'),
# ThunderDrake  2p 2h
# costs: 🔥🔥🔥🔥 has: 👻👻 pot: 5
Blueprint(original=Card(name='ThunderDrake', power=2, health=2, costs_fire=4, costs_spirits=0, has_spirits=2, has_fire=0, skills=[]), description='The massive fire cost needed to bring out this card suggests a powerful creature indeed With decent attributes otherwise, the lightning name and dragonlike title suggest a fearsome creature dominating the arena The skills in the game should have some effect to show off this card\'s power'),
# Gorgonix  0p 4h
# costs: 🔥 has: - pot: 6
Blueprint(original=Card(name='Gorgonix', power=0, health=4, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[]), description='hulking, high health, armored'),
# Blinkfox  3p 2h
# costs: 🔥 has: 👻 pot: 8
Blueprint(original=Card(name='Blinkfox', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='nimble, fast, hard to catch, spiritpowered magic'),
# Skywhale 🪁 0p 5h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 9
Blueprint(original=Card(name='Skywhale', power=0, health=5, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Soaring]), description='massive health, aerial, soaring skill'),
# Phoenixfly  2p 3h
# costs: 🔥🔥🔥 has: 🔥 pot: 7
Blueprint(original=Card(name='Phoenixfly', power=2, health=3, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='very expensive, with high powerhealth, but no spirit attributes, fits with a hypothetical card that requires sacrifices to boost other cards'),
# Skykraken  2p 2h
# costs: 🔥 has: 👻 pot: 7
Blueprint(original=Card(name='Skykraken', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='Moderate card with balanced values, but high fire costs, implying that this creature is resilient where few else can dwell, eg higher altitudes, near volcanoes, etc'),
# Furion  3p 3h
# costs: 🔥 has: 👻 pot: 10
Blueprint(original=Card(name='Furion', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='relatively high health for its power, low fire costs, has no spiritual powers, implying that it is a feral creature with no ability to magically control elements, but is instead skilled in combat'),
# Iceling  3p 2h
# costs: 🔥🔥 has: 👻 pot: 7
Blueprint(original=Card(name='Iceling', power=3, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='Small creature with modest stats and a single skillless trait, but has a cold, almost icy exterior both in temperament and adaptation to cold environments'),
# Fire Lioness  0p 7h
# costs: 🔥🔥 has: 🔥 pot: 11
Blueprint(original=Card(name='Fire Lioness', power=0, health=7, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='high health, low cost due to no spirits, focused on fire element'),
# Sting Witch 💀🦔 1p 1h
# costs: 👻👻👻👻👻 has: 👻 pot: 8
Blueprint(original=Card(name='Sting Witch', power=1, health=1, costs_fire=0, costs_spirits=5, has_spirits=1, has_fire=0, skills=[skills.InstantDeath, skills.Spines]), description='low powerhealth, high cost due to spirits, focused on instakill and spines'),
# Inferno Chameleon  2p 1h
# costs: 🔥 has: 🔥🔥🔥🔥👻 pot: 8
Blueprint(original=Card(name='Inferno Chameleon', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=4, skills=[]), description='low health, versatile fire element, ability to adapt to different situations'),
# Ember Fox  1p 2h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻 pot: 8
Blueprint(original=Card(name='Ember Fox', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=4, skills=[]), description='low power, moderate health and spirits, focused on fire element'),
# Firewisp  2p 3h
# costs: 🔥 has: 🔥🔥👻 pot: 10
Blueprint(original=Card(name='Firewisp', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description='a quick, agile creature with a fiery disposition and the ability to manipulate flames'),
# Sunspear  1p 5h
# costs: 🔥 has: 🔥👻 pot: 11
Blueprint(original=Card(name='Sunspear', power=1, health=5, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a regal and noble creature that shines bright and emits warmth, reflecting its healing and protective abilities'),
# Pocketthief 🧺 1p 1h
# costs: 🔥 has: 🔥👻👻👻👻👻 pot: 13
Blueprint(original=Card(name='Pocketthief', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=1, skills=[skills.Packrat]), description='a mischievous and clever animal with a knack for hoarding and stealing resources'),
# Hellsbane 💀 3p 1h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Hellsbane', power=3, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='a fierce and fearsome beast that strikes with deadly precision, capable of dealing instant death to its foes'),
# Whisker 🧺 1p 3h
# costs: 🔥 has: 🔥👻 pot: 13
Blueprint(original=Card(name='Whisker', power=1, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='refers to the packrat skill, which involves stealing from opponents and hiding, like a small creature that keeps things hidden away Health is high but power is moderate, hence the name focuses on the skill rather than physical attributes'),
# Dryadling 🐭 1p 2h
# costs: 🔥 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Dryadling', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='With a power of , health of , and skill Fertility which suggests growth and propagation, the name Dryadling evokes the idea of a young, magical creature that is just beginning to grow into its powers'),
# Salamion  3p 2h
# costs: 🔥 has: 🔥🔥🔥🔥🔥 pot: 12
Blueprint(original=Card(name='Salamion', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=5, skills=[]), description='This card is heavy on fire hasfire and has a decent power and health The name Salamion relates to the heavy use of fire like a salamander and the overall strong, imposing character of the card'),
# Crustaceon 🔰 3p 1h
# costs: 👻 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Crustaceon', power=3, health=1, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='This card is low on spirit but has high defense skill Shield and  power The name Crustaceon relates to its ability to defend itself with its shell, like a crustacean, while still having enough power to attack'),
# Packrally 🧺 1p 4h
# costs: 🔥 has: 👻👻 pot: 14
Blueprint(original=Card(name='Packrally', power=1, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Packrat]), description='This card has good health and skill Packrat, which suggests hoarding and gathering resources The name Packrally evokes the idea of a group of creatures working together to gather resources and protect each other'),
# Aardvark  0p 7h
# costs: 🔥 has: 🔥👻 pot: 13
Blueprint(original=Card(name='Aardvark', power=0, health=7, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='long snout, strong defense high health, slow movement no fire ability'),
# Voodoo Bat 💀 1p 2h
# costs: 🔥 has: 🔥👻👻👻 pot: 14
Blueprint(original=Card(name='Voodoo Bat', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.InstantDeath]), description='Low power and health make this card seem harmless, but the Instant Death skill strikes terror into the hearts of opponents'),
# Imp 💀 2p 3h
# costs: 🔥 has: 👻 pot: 14
Blueprint(original=Card(name='Imp', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath]), description='This lowcost card with moderate power and health packs a punch with the Instant Death skill, making it a fearsome opponent despite its small presence The lack of fire and spirits suggests an impish creature from the underworld or magical realm'),
# Pyrogriffin 🐭 2p 1h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 14
Blueprint(original=Card(name='Pyrogriffin', power=2, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Fertility]), description='fire element, fertility skill, high costfire'),
# Packhound 🐩🧺 2p 3h
# costs: 🔥 has: 🔥 pot: 17
Blueprint(original=Card(name='Packhound', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Underdog, skills.Packrat]), description='With the population in the cards world being so geared towards solitary animals, the Underdog and Packrat skills fit a social canid'),
# Mandrake 💀 3p 2h
# costs: 🔥 has: 👻👻 pot: 15
Blueprint(original=Card(name='Mandrake', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.InstantDeath]), description='Mandrakes are known in legend for their deadly scream, which ties in with the Instant Death skill The low Spirit points suggest a magical creature that has difficulty existing in the real world'),
# Firebat 🔰 5p 2h
# costs: 🔥 has: 🔥 pot: 18
Blueprint(original=Card(name='Firebat', power=5, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield]), description='High strength with low health and a Shield skill suggests something that swoops in and charges, making a quick attack and then retreating for protection'),
# Spelunker 🧺 4p 3h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 16
Blueprint(original=Card(name='Spelunker', power=4, health=3, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='high fire and spirit cost, packrat skill, medium health and power'),
# Tree Nymph  3p 8h
# costs: 🔥🔥 has: 👻 pot: 18
Blueprint(original=Card(name='Tree Nymph', power=3, health=8, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='low fire presence, high spirit presence, high health, no skills'),
# Spritesong 🐭 3p 2h
# costs: 🔥 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Spritesong', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='low fire cost, fertility skill, low power, medium health'),
# Flamefox 🧺🔰 2p 1h
# costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻 pot: 18
Blueprint(original=Card(name='Flamefox', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Packrat, skills.Shield]), description='combining fire theme with fox, which suggest agility and quickness, plus the Shield and Packrat skills'),
# Chimerafly 💀🔰🐩 1p 2h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 20
Blueprint(original=Card(name='Chimerafly', power=1, health=2, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Shield, skills.Underdog]), description='a mythical creature that combines various animals, which fits with the card\'s skills, and fly represents the Underdog skill while chimera suggest deadly power'),
# Basiliskin 💀 5p 1h
# costs: 🔥 has: 🔥👻👻 pot: 18
Blueprint(original=Card(name='Basiliskin', power=5, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath]), description='combining the skills and attributes power and InstantDeath with the mythical creature Basilisk, and the \"kin\" ending suggests a smaller version of it'),
# Shieldturtle 🐩 1p 8h
# costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 19
Blueprint(original=Card(name='Shieldturtle', power=1, health=8, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Underdog]), description='a turtle represents high defense and health while the Shield skill supports this, and the name has a nice ring to it'),
# Spritelion 🔰🐭 1p 3h
# costs: 👻👻 has: 🔥🔥 pot: 21
Blueprint(original=Card(name='Spritelion', power=1, health=3, costs_fire=0, costs_spirits=2, has_spirits=0, has_fire=2, skills=[skills.Shield, skills.Fertility]), description='a playful and fantastical name combining spirit and fertility themes with the attributes of low power and high health, and the Shield skill'),
# Nymph 🐭 4p 2h
# costs: 👻 has: 🔥👻 pot: 19
Blueprint(original=Card(name='Nymph', power=4, health=2, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='spirited, with ability to boost fertility, spiritbased'),
# Ratsnake 🐭🧺 3p 1h
# costs: 🔥 has: 🔥 pot: 20
Blueprint(original=Card(name='Ratsnake', power=3, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility, skills.Packrat]), description='firebased, packratlike hoarder, with ability to boost fertility'),
# Shadehound 💀🧺 1p 4h
# costs: 🔥🔥 has: 🔥👻👻 pot: 21
Blueprint(original=Card(name='Shadehound', power=1, health=4, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath, skills.Packrat]), description='a doglike creature that can blend into shadows, Packrat skill represents their hoarding nature'),
# Treant  4p 7h
# costs: 🔥 has: 🔥👻 pot: 20
Blueprint(original=Card(name='Treant', power=4, health=7, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a powerful, ancient treelike creature with high health and moderate power'),
# Thornfox 🧺🦔 2p 5h
# costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 20
Blueprint(original=Card(name='Thornfox', power=2, health=5, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Packrat, skills.Spines]), description='combines the Spines and Packrat skills with a foxlike creature that is tough and cunning'),
# Skyguard 🐩🔰🪁 2p 5h
# costs: 🔥🔥 has: 🔥👻 pot: 23
Blueprint(original=Card(name='Skyguard', power=2, health=5, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Underdog, skills.Shield, skills.Soaring]), description='medium strength, good endurance, low flame cost, heartening, shielded, flying'),
# Spirit Tortoise 🔰🐭 4p 1h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 21
Blueprint(original=Card(name='Spirit Tortoise', power=4, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Fertility]), description='slow, with high defense, having the ability to breed rapidly'),
# Diamondback  2p 6h
# costs: - has: 👻 pot: 23
Blueprint(original=Card(name='Diamondback', power=2, health=6, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='very resilient, fastmoving, and adaptible, but with no special powers'),
# Gryphox 🔰🐭 1p 6h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 25
Blueprint(original=Card(name='Gryphox', power=1, health=6, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Fertility]), description='a majestic creature with a large health pool and a shield, and strong fertility powers, suggested by the skill name, and high fire costs'),
# Pyrolon 🐭 6p 1h
# costs: 🔥🔥 has: 🔥👻👻👻👻👻👻 pot: 24
Blueprint(original=Card(name='Pyrolon', power=6, health=1, costs_fire=2, costs_spirits=0, has_spirits=6, has_fire=1, skills=[skills.Fertility]), description='an explosive and fiery creature with high power and fire costs, suggested by the card\'s high power and fire attributes, and the Fertility skill, which could represent the ability to multiply'),
# Packrider 🧺💀 3p 3h
# costs: 🔥 has: 🔥👻 pot: 22
Blueprint(original=Card(name='Packrider', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat, skills.InstantDeath]), description='a quick and cunning animal with the ability to hoard resources and instant death powers, suggested by the Packrat and InstantDeath skills, and wellbalanced power and health attributes'),
# Flamefang 🧺🐭 4p 2h
# costs: 🔥🔥🔥 has: 🔥🔥 pot: 22
Blueprint(original=Card(name='Flamefang', power=4, health=2, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=2, skills=[skills.Packrat, skills.Fertility]), description='a fearsome and fiery predator with high fire attributes and strong packrat and fertility abilities, symbolized by the card\'s high power and fire costs, and the card\'s Packrat and Fertility skills'),
# Oxyhorn 🔰 7p 3h
# costs: 🔥 has: 🔥👻 pot: 24
Blueprint(original=Card(name='Oxyhorn', power=7, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='a tough and resilient animal with a high shield attribute and strong offensive powers, suggested by the card\'s high power and health attributes, the Shield skill, and the strong fire attribute'),
# Sylphidfox 🐩🐭 3p 5h
# costs: 👻👻👻👻 has: 🔥👻👻 pot: 24
Blueprint(original=Card(name='Sylphidfox', power=3, health=5, costs_fire=0, costs_spirits=4, has_spirits=2, has_fire=1, skills=[skills.Underdog, skills.Fertility]), description='The card\'s high health and spirit costs suggest an otherworldly creature, hence the Sylphid part of the name Fox fits with the Underdog and Fertility skills as a nimble and fertile animal with cunning ability to adapt and survive'),
# Dragonfire  10p 4h
# costs: 🔥🔥 has: 🔥🔥🔥 pot: 25
Blueprint(original=Card(name='Dragonfire', power=10, health=4, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=3, skills=[]), description='The high power and fire costs clearly suggest a dragon The relatively low health is balanced by its offensive power and the fact that it does not require spirits to summon'),
# Serenicorn 🐭 3p 9h
# costs: 🔥 has: - pot: 28
Blueprint(original=Card(name='Serenicorn', power=3, health=9, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Fertility]), description='A combination of serene and unicorn, the name reflects the card\'s high health and fertility skill The low power and fire costs are in line with a peaceful and mythical creature and the absence of fire and spirits suggest a pure and magical being'),
# Bloodclaw 🧺 8p 3h
# costs: 🔥 has: 👻 pot: 24
Blueprint(original=Card(name='Bloodclaw', power=8, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Packrat]), description='The powerful attack and relative lack of defense are reflected in the name The Packrat skill hints at a scavenger or predator that collects trophies of its hunting skills The single spirit requirement suggests a fierce and primal animal '),
# Skytalon 🐭🪁🔰 2p 2h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 26
Blueprint(original=Card(name='Skytalon', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Fertility, skills.Soaring, skills.Shield]), description='This name suggests a birdlike creature with talons, fitting with the skills \"Soaring\" and \"Shield\" The high fire cost and low spirits suggest a creature that is fiery and perhaps aggressive, while the balanced power and health suggest versatility The \"Fertility\" skill could suggest that the creature can mate and reproduce quickly, similar to many birds'),
# Vipernyx 💀 3p 1h
# costs: - has: 🔥🔥🔥👻 pot: 25
Blueprint(original=Card(name='Vipernyx', power=3, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=3, skills=[skills.InstantDeath]), description='This name combines the words \"viper\" and \"onyx,\" suggesting a creature with snakelike abilities and perhaps even a shiny, black appearance The high power and low health suggest a creature that is venomous and dangerous but also vulnerable The \"InstantDeath\" skill reinforces this idea The high fire cost suggests that the creature might be fiery or have a venom that causes a burning sensation'),
# Foxfire 🔰🐭 2p 2h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 27
Blueprint(original=Card(name='Foxfire', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=5, skills=[skills.Shield, skills.Fertility]), description='This name plays with the idea of foxes and fire, suggesting a fiery creature with perhaps a foxlike appearance The balanced power and health suggest a wellrounded creature, while the \"Shield\" skill and high fire cost suggest that it is difficult to defeat The \"Fertility\" skill suggests that the creature can reproduce quickly and perhaps has a large pack of offspring'),
# Darknova 🐭🔰💀 2p 2h
# costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 28
Blueprint(original=Card(name='Darknova', power=2, health=2, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='This name suggests a dark and powerful creature, fitting with the high fire cost and strong \"InstantDeath\" skill The balanced power and health suggest a versatile creature, while the \"Fertility\" skill could suggest that the creature can create a horde of offspring The low fire and high spirit costs could suggest that the creature is mysterious and perhaps magical'),
# Skerrow 🐭🧺💀 0p 3h
# costs: 🔥 has: 🔥👻👻👻👻👻 pot: 28
Blueprint(original=Card(name='Skerrow', power=0, health=3, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=1, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='This name suggests a small and crafty creature, fitting with the low power but high \"Packrat\" skill The high spirit cost and \"Fertility\" skill suggest that the creature is highly social and perhaps even communal The high health and low fire cost suggest that the creature may be difficult to defeat but not particularly aggressive or dangerous'),
# Armageddon  2p 8h
# costs: - has: 👻 pot: 27
Blueprint(original=Card(name='Armageddon', power=2, health=8, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='This card\'s high health and no fire attribute are represented by the name, which suggests a sense of being indestructible Its name also makes sense because the card has no skills, meaning it relies on its strength alone The fantasy element of the name fits with the game\'s theme'),
# Whiskerbat 🐭🔰🧺 4p 2h
# costs: 🔥 has: 🔥🔥👻 pot: 31
Blueprint(original=Card(name='Whiskerbat', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.Packrat]), description='This name is related to the Packrat skill and the high Fire attribute of the card The name also relates to the low Spirit attribute of the card as bats are commonly seen as spooky creatures'),
# Blossomoose 🧺 4p 10h
# costs: 🔥 has: 🔥👻 pot: 30
Blueprint(original=Card(name='Blossomoose', power=4, health=10, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='This name is fitting for the very high Health attribute of the card and the Packrat skill it possesses Blossomoose sounds like a gentle giant which is reflected in the low Power attribute'),
# Violephant 🧺🔰💀 3p 5h
# costs: 👻👻👻 has: 👻👻 pot: 30
Blueprint(original=Card(name='Violephant', power=3, health=5, costs_fire=0, costs_spirits=3, has_spirits=2, has_fire=0, skills=[skills.Packrat, skills.Shield, skills.InstantDeath]), description='This name relates to the high Spirit attribute and the fact that the card possesses two Shield skills, which makes it difficult for the opponent to damage you The name \"Violephant\" can be linked to the InstantDeath skill since Violephant flowers are known for their healing purposes'),
# Flametooth 🐭 9p 2h
# costs: 🔥 has: 🔥👻👻 pot: 28
Blueprint(original=Card(name='Flametooth', power=9, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility]), description='This name is linked to the Fire attribute and the Fertility skill The high Power attribute supports the name Flametooth since it evokes a powerful fiery image'),
# Gemshell 🐭🔰 1p 8h
# costs: 🔥🔥 has: 🔥👻 pot: 29
Blueprint(original=Card(name='Gemshell', power=1, health=8, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.Shield]), description='This name is linked to the Shield skill and high Health attribute The Fertility skill is also related to the name of the card since it represents the idea of being born from a shell, which in turn can have a shiny effect like a gem'),
# Spellturtle 🐭🔰 5p 4h
# costs: 🔥 has: 👻 pot: 29
Blueprint(original=Card(name='Spellturtle', power=5, health=4, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Fertility, skills.Shield]), description='Powerful with a defense mechanism and fertility Its turtlelike shell makes it a resilient and longlived creature Spellturtle has a strong correlation with magic that makes it highly sought after for its spellbound abilities'),
# Mysticfox 🐭💀🧺 2p 3h
# costs: 🔥🔥 has: 🔥👻👻👻 pot: 29
Blueprint(original=Card(name='Mysticfox', power=2, health=3, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat]), description='Quick and cunning, able to avoid danger instinctively It\'s known to hoard valuable magical objects and relics to be used when the situation gets dire'),
# Mantistaur 🐭💀 2p 7h
# costs: 🔥 has: 🔥👻 pot: 30
Blueprint(original=Card(name='Mantistaur', power=2, health=7, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.InstantDeath]), description='Symbiotically fierce creature born from the merging of a mantis with a bull, the Mantistaur is a skilful and agile fighter, able to decimate enemies with lightning speed, and grow twice his size in a few seconds for a powerful charge'),
# Swarmant 🐭 2p 3h
# costs: - has: 🔥👻👻👻👻 pot: 29
Blueprint(original=Card(name='Swarmant', power=2, health=3, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=1, skills=[skills.Fertility]), description='Born from a mating of two breeds of locust, Swarmant is the quintessential swarm creature, working as a single unit to attack and fend off the enemy Its ability to command other insects is its greatest strength'),
# Skyhound 🐩🪁🧺🐭 4p 3h
# costs: 🔥 has: 🔥👻👻👻 pot: 33
Blueprint(original=Card(name='Skyhound', power=4, health=3, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Underdog, skills.Soaring, skills.Packrat, skills.Fertility]), description='A creature that adapts to the change of the wind and moves with a flock, alert to danger and able to find which way the wind is blowing Skyhound is a packminded beast that loves to hoard precious items while traveling long distances with their trusted companions'),
# Goblin 🔰🐩🐭 3p 2h
# costs: - has: - pot: 35
Blueprint(original=Card(name='Goblin', power=3, health=2, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Shield, skills.Underdog, skills.Fertility]), description='low powerhealth, no fire or spirit cost, but skills like Underdog and Shield suggest a scrappy creature that can take bigger foes down with it'),
# Sableback 🐭🧺💀 4p 4h
# costs: 👻👻 has: 🔥🔥👻👻 pot: 35
Blueprint(original=Card(name='Sableback', power=4, health=4, costs_fire=0, costs_spirits=2, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='a creature with a strong backbone to support its high power and health Its skills provide a packratlike ability to gather resources instantly and even an instant death attack can take down tougher foes'),
# Skyfungus 💀🔰 4p 2h
# costs: - has: 🔥👻 pot: 33
Blueprint(original=Card(name='Skyfungus', power=4, health=2, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Shield]), description='a creature with high attack and one of the few with the Instant Death skill Its shield provides an extra layer of defense in tough situations'),
# Miragecat 🔰💀🧺 5p 6h
# costs: 👻👻👻 has: 👻 pot: 35
Blueprint(original=Card(name='Miragecat', power=5, health=6, costs_fire=0, costs_spirits=3, has_spirits=1, has_fire=0, skills=[skills.Shield, skills.InstantDeath, skills.Packrat]), description='a creature that represents how appearances can be deceiving Although it lacks fire, its skills can make it hard to hit and its high health and power make it a formidable opponent'),
# Starseer 🐭🧺 3p 3h
# costs: - has: 🔥👻👻👻 pot: 35
Blueprint(original=Card(name='Starseer', power=3, health=3, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Fertility, skills.Packrat]), description='a creature that can foresee the future, making it a great asset for any team With its fertility and packrat skills, it can gather resources and summon allies to help protect its high spirits'),
# Changeling 🐭💀🐩🔰 2p 3h
# costs: 👻 has: 🔥🔥👻👻 pot: 35
Blueprint(original=Card(name='Changeling', power=2, health=3, costs_fire=0, costs_spirits=1, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Underdog, skills.Shield]), description='balanced stats, but versatile skills including instant death and underdog, fits a creature capable of transformation and deception'),
# Rattlesnake 💀🔰🧺🦔 5p 2h
# costs: 🔥 has: 🔥👻👻 pot: 34
Blueprint(original=Card(name='Rattlesnake', power=5, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath, skills.Shield, skills.Packrat, skills.Spines]), description='powerful but weak health, spines indicate an animal with some defense mechanism, packrat skill fits a creature that hoards'),
# Ratscorn 🧺💀🐩🦔🐭 3p 2h
# costs: 🔥🔥🔥🔥 has: 🔥👻👻👻👻 pot: 35
Blueprint(original=Card(name='Ratscorn', power=3, health=2, costs_fire=4, costs_spirits=0, has_spirits=4, has_fire=1, skills=[skills.Packrat, skills.InstantDeath, skills.Underdog, skills.Spines, skills.Fertility]), description='This ferocious creature is a mix between a rat and a mythical beast, as represented by its many skills and high spirited nature The \"corn\" suffix in its name refers to its ability to collect and hoard items with the packrat skill, while \"rats\" represents its sneaky and underhanded nature'),
# Frostbite 💀🔰🐭 3p 7h
# costs: 🔥 has: 🔥👻👻 pot: 39
Blueprint(original=Card(name='Frostbite', power=3, health=7, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='With high HP and fertility skill, this fantastical yetilike creature is tough to beat in battle It has the ability to freeze enemies with its icy breath thanks to the \"instant death\" skill, represented in its name with \"frost\"'),
# Armoredillo 💀🐭🔰 2p 6h
# costs: 🔥 has: 🔥🔥👻👻 pot: 36
Blueprint(original=Card(name='Armoredillo', power=2, health=6, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Fertility, skills.Shield]), description='This armored creature has high health and the shield skill, making it tough to take down in battle Its \"instant death\" skill allows it to quickly dispatch enemies, while its name plays on the word \"armored\" and the animal \"armadillo\"'),
# Ferretix 🔰🐭🧺💀 3p 3h
# costs: 🔥 has: 🔥👻 pot: 36
Blueprint(original=Card(name='Ferretix', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Fertility, skills.Packrat, skills.InstantDeath]), description='A combination of the words ferret and matrix, suggesting its ability to store and protect resources skills packrat and shield and its adaptability skill fertility Its high power and moderate health make it a balanced opponent'),
# Scorpiora 🧺💀🔰 3p 8h
# costs: 🔥 has: 🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='Scorpiora', power=3, health=8, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Packrat, skills.InstantDeath, skills.Shield]), description='A combination of the words scorpion and aurora, suggesting its deadly stinger skill instant death and its luminous body hasspirits Its high health and moderate power make it a sturdy opponent, and the skills packrat and shield add to its defense'),
# Thundertusk 🔰🧺🐩 6p 5h
# costs: 🔥 has: 🔥👻👻👻 pot: 36
Blueprint(original=Card(name='Thundertusk', power=6, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Shield, skills.Packrat, skills.Underdog]), description='A combination of thunder and tusk, suggesting its powerful attacks skill underdog and its massive size high power and moderate health Its low costsfire, high hasspirits, and moderate hasfire further enforce its strength'),
# Phoenixie 🔰🐭 5p 6h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 37
Blueprint(original=Card(name='Phoenixie', power=5, health=6, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Shield, skills.Fertility]), description='A combination of phoenix and pixie, suggesting its ability to rise from the ashes skill fertility and its small, delicate appearance low power, moderate health Its high hasspirits and low costsfire hint at its magical nature, and the skills shield and fertility add to its defense and resurrection abilities'),
# Thunderox 💀🐭 3p 10h
# costs: 🔥 has: 🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='Thunderox', power=3, health=10, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Fertility]), description='This name reflects the high power maxed out at  and high health close to max at  of the card, as well as its abilities to instantly kill opponents InstantDeath and increase the fertility of allies Fertility'),
# Hummingjay 🐭🧺 2p 9h
# costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 37
Blueprint(original=Card(name='Hummingjay', power=2, health=9, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=2, skills=[skills.Fertility, skills.Packrat]), description='The relatively low power and health of this card are reflected in the name, as hummingbirds are small but agile creatures Its focus on increasing the fertility of allies Fertility and hoarding resources Packrat is reflected in the addition of \"jay,\" a bird known for its stash of acorns and other food in the fall'),
# Enchantigo 🐭🔰🍀🧺 2p 8h
# costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 39
Blueprint(original=Card(name='Enchantigo', power=2, health=8, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.LuckyStrike, skills.Packrat]), description='The name combines \"enchant\" and \"tango,\" reflecting the high value placed on spirits  and fire  to play this card, as well as its abilities to increase the luck of its allies LuckyStrike, shield them Shield, breed more creatures Fertility, and hoard resources Packrat \"Enchant\" also suggests an element of magic or charm, fitting for a fantastical creature'),
# Goldenhedge 💀🐭🔰🦔 4p 3h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='Goldenhedge', power=4, health=3, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=4, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Spines]), description='The card\'s high power  and low health  are reflected in the name, with \"gold\" connoting strength and \"hedge\" suggesting a prickly, defensive quality These attributes are matched by the card\'s abilities to destroy enemies InstantDeath, breed more creatures Fertility, shield itself Shield, and damage enemies Spines'),
# Driftwing 🐩🔰🐭🪁 4p 4h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 37
Blueprint(original=Card(name='Driftwing', power=4, health=4, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Underdog, skills.Shield, skills.Fertility, skills.Soaring]), description='The name reflects the card\'s abilities to fly Soaring and defend itself Shield, as well as its focus on supporting underdogs Underdog and breeding more creatures Fertility \"Drift\" carries connotations of floating or gliding, while \"wing\" suggests flight The name also fits with the card\'s values of high spirits  and fire '),
# Vampiricat 🐭💀🐩 5p 6h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 38
Blueprint(original=Card(name='Vampiricat', power=5, health=6, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Underdog]), description='the name suggests a powerful and undead feline, fitting for a card with high power and health The skills Fertility and Underdog suggest a cunning and dangerous creature, while InstantDeath hints at its vampiric nature'),
# Drakespine 🔰🦔🧺💀🚀🪁 4p 3h
# costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 41
Blueprint(original=Card(name='Drakespine', power=4, health=3, costs_fire=3, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Shield, skills.Spines, skills.Packrat, skills.InstantDeath, skills.Airdefense, skills.Soaring]), description='the name refers to a mythical creature with dragonlike features and defensive spines The skills Shield, Spines, Airdefense, and Soaring emphasize its defensive and aerial traits Costsfire and hasfire also align with the creature\'s draconic nature, while Packrat and InstantDeath show that it can be resourceful and dangerous'),
# Spiritsquirrel 🧺💀🐭 2p 7h
# costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 39
Blueprint(original=Card(name='Spiritsquirrel', power=2, health=7, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=2, skills=[skills.Packrat, skills.InstantDeath, skills.Fertility]), description='the name suggests a small and nimble creature, fitting for a card with moderate power and high health The skills Packrat and Fertility suggest a resourceful and multiplying animal, while InstantDeath shows its deadly side The high hasspirits value also aligns with the squirrel\'s mystical and otherworldly nature'),
# Infernofox 🔰💀🧺 7p 4h
# costs: 👻 has: 🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='Infernofox', power=7, health=4, costs_fire=0, costs_spirits=1, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.InstantDeath, skills.Packrat]), description='the name suggests a firebased creature with cunning and agility, fitting for a card with high power and moderate health The skills Shield and Packrat show its resourcefulness and defensive capabilities, while InstantDeath represents its cunning and deadly nature The costsspirits and hasfire values also align with its fiery and mystical nature'),
# Magpie 🔰🐭🧺 2p 10h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Magpie', power=2, health=10, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Shield, skills.Fertility, skills.Packrat]), description='The name suggests a crafty creature, fitting for a card with the Packrat skill Its Shield and Fertility skills suggest a protective yet fertile nature The balanced fire and spirit costs with low overall values suggest a quick and resourceful creature'),
# Jackalope 🐭🧺💀 4p 4h
# costs: - has: 🔥👻 pot: 43
Blueprint(original=Card(name='Jackalope', power=4, health=4, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='Jackalopes are mythical creatures that resemble rabbits with antlers The name is fitting for this card because it has average powerhealth, but with abilities like Fertility, Packrat, and InstantDeath it can surprise opponents'),
# Dracowl 🐩🔰🐭 6p 8h
# costs: 👻👻👻 has: 🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Dracowl', power=6, health=8, costs_fire=0, costs_spirits=3, has_spirits=3, has_fire=2, skills=[skills.Underdog, skills.Shield, skills.Fertility]), description='A powerful, highly spirited creature with three skills, including Shield and Fertility, indicating its resilience and ability to grow stronger over time The \'Drac\' in the name references its dragonlike powers and the \'owl\' references its high spirits and watchful nature'),
# Chimeralet 💀🐭 5p 10h
# costs: 👻👻👻 has: 🔥🔥👻👻 pot: 41
Blueprint(original=Card(name='Chimeralet', power=5, health=10, costs_fire=0, costs_spirits=3, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Fertility]), description='A slightly shorter variation of \"Chimera,\" this name represents the card\'s Instant Death skill, implying a fierce and deadly nature The \'let\' at the end is a diminutive, underscoring the card\'s smaller size compared to other Chimera creatures The Chimeralet\'s  power and  health, along with its Fertility skill, indicate a tenacious and strong creature'),
# Griffwisp 🐭🐩🔰 5p 8h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Griffwisp', power=5, health=8, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Fertility, skills.Underdog, skills.Shield]), description='A combination of \"Griffin\" and \"Willo\'thewisp,\" this name implies a strong, fantastical creature with fire affinity as well as the ability to guide and protect others referenced by its Shield and Underdog skills The Griffwisp\'s  power,  health, and  fire affinity suggest a creature that is both formidable and balanced'),
# Enchanthorn 🐭💀🐩 8p 5h
# costs: 👻👻👻 has: 🔥🔥👻👻 pot: 41
Blueprint(original=Card(name='Enchanthorn', power=8, health=5, costs_fire=0, costs_spirits=3, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Underdog]), description='An enchanting creature with Instant Death, Fertility, and Underdog skills, the Enchanthorn\'s  power and  health suggest a strong and dangerous character The \'thorn\' at the end of the name references its spiky, prickly abilities'),
# Phoenixhare 🐭🔰 9p 7h
# costs: 🔥 has: 🔥🔥👻👻 pot: 44
Blueprint(original=Card(name='Phoenixhare', power=9, health=7, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Shield]), description='A fiery creature with Shield and Fertility skills, the Phoenixhare embodies the concept of rebirth and regeneration referenced by the Phoenix name while also being nimble and quick referenced by the hare Its  power,  health, and  fire affinity suggest a strong creature that can both defend itself and deal damage'),
# Krakensaur 🔰💀🧺🦔🪁 2p 7h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
Blueprint(original=Card(name='Krakensaur', power=2, health=7, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Shield, skills.InstantDeath, skills.Packrat, skills.Spines, skills.Soaring]), description='This card has high health and moderate power, with a cost that is not too high The skills include packrat and instant death suggesting its ability to consume prey The name Krakensaur brings together the imagery of a dragonlike reptile and a powerful ocean creature which fits the card\'s attributes'),
# Starwhale 💀🔰🐭 5p 5h
# costs: 🔥🔥 has: 🔥🔥👻👻👻👻👻 pot: 42
Blueprint(original=Card(name='Starwhale', power=5, health=5, costs_fire=2, costs_spirits=0, has_spirits=5, has_fire=2, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='This card has a good balance of power and health, with a moderate cost to play The skills include instant death and shield, suggesting a formidable opponent Starwhale invokes the image of a massive, otherworldly creature that is aweinspiring and dangerous'),
# Griffowl 🧺🐭🦔 9p 5h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 44
Blueprint(original=Card(name='Griffowl', power=9, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Packrat, skills.Fertility, skills.Spines]), description='This card has high power and health, with a low cost to play The skills include packrat and spines, suggesting a powerful, predatory bird Griffowl combines the imagery of a griffin and an owl, which fits the card\'s profile perfectly'),
# Thunderhog 💀🐭🧺 4p 8h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 43
Blueprint(original=Card(name='Thunderhog', power=4, health=8, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.InstantDeath, skills.Fertility, skills.Packrat]), description='fits with the high power and health, and the InstantDeath skill, while also hinting at its association with fire and spirits as seen in the attribute values'),
# Pandragon 🐭🐩🔰💀 2p 6h
# costs: 👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻 pot: 44
Blueprint(original=Card(name='Pandragon', power=2, health=6, costs_fire=0, costs_spirits=1, has_spirits=3, has_fire=6, skills=[skills.Fertility, skills.Underdog, skills.Shield, skills.InstantDeath]), description='combines the ideas of pandas and dragons into a fantastical creature of high health and moderate power, with the skills Fertility and Shield having a nurturing and protective connotation, respectively'),
# Chimerafoe 🐭🐩💀 9p 5h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 43
Blueprint(original=Card(name='Chimerafoe', power=9, health=5, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Underdog, skills.InstantDeath]), description='a play on the mythical creature chimera, indicating a powerful and deadly creature that is also associated with fire and has the skill InstantDeath'),
# Shadowfox 🧺🐭💀 8p 5h
# costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 44
Blueprint(original=Card(name='Shadowfox', power=8, health=5, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Packrat, skills.Fertility, skills.InstantDeath]), description='a mysterious, elusive creature with strong spirits and fire, as well as the skills Packrat and Fertility, possibly indicating a cunning and resourceful nature'),
# Thorniclaw 🧺🔰🐭🦔 7p 5h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻 pot: 47
Blueprint(original=Card(name='Thorniclaw', power=7, health=5, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=4, skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.Spines]), description='a name that suggests the spines and high power, while also incorporating the Shield skill and the association with fire seen in the attribute values'),
# Blazefin 🐭💀🦔 5p 8h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 45
Blueprint(original=Card(name='Blazefin', power=5, health=8, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Fertility, skills.InstantDeath, skills.Spines]), description='referring to the high fire attribute and sharp spines, as well as the high power and health stats'),
# Swarmwing 🐭🧺💀 6p 6h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 45
Blueprint(original=Card(name='Swarmwing', power=6, health=6, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='relating to the Packrat skill and the multiple skills it has, as well as the balanced attributes'),
# Griffinix 🧺🐭🐩 5p 9h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 45
Blueprint(original=Card(name='Griffinix', power=5, health=9, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Packrat, skills.Fertility, skills.Underdog]), description='a mix between a griffin and a phoenix, as a reference to the high health and fire attributes and the packrat and fertility skills'),
# Deathfang 💀🧺🐭🐩 3p 8h
# costs: 🔥🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 46
Blueprint(original=Card(name='Deathfang', power=3, health=8, costs_fire=3, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility, skills.Underdog]), description='referring to the high instant death skill and the spines, as well as the relatively low power'),
# Armashield 🦔🔰💀🐭 4p 8h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 49
Blueprint(original=Card(name='Armashield', power=4, health=8, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Spines, skills.Shield, skills.InstantDeath, skills.Fertility]), description='a mix between an armadillo and a shield, referring to the high health and spines, as well as its shield and instant death skills'),
# Phoenixcat 💀🐭🔰 9p 4h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 48
Blueprint(original=Card(name='Phoenixcat', power=9, health=4, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.InstantDeath, skills.Fertility, skills.Shield]), description='With strong fire attributes and a shield ability, the Phoenixcat is hard to defeat Instant death and fertility powers only add to its danger, making it a true force to be reckoned with'),
# Nightshade 🐭🔰💀🐩 3p 3h
# costs: - has: 🔥🔥👻👻👻 pot: 47
Blueprint(original=Card(name='Nightshade', power=3, health=3, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.InstantDeath, skills.Underdog]), description='Refers to a plant that is poisonous, linking to InstantDeath skill, and its dark and mythical vibe fits with Shield and Underdog skills'),
# Shimmerwing 🧺🐭🐩🔰 5p 8h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 50
Blueprint(original=Card(name='Shimmerwing', power=5, health=8, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Packrat, skills.Fertility, skills.Underdog, skills.Shield]), description='an elegant creature with high health and power, but costly to summon the packrat and shield skills contribute to its resilience'),
# Starfrost 🧺🔰🐩🐭 4p 8h
# costs: 👻👻 has: 🔥🔥🔥👻👻👻👻 pot: 48
Blueprint(original=Card(name='Starfrost', power=4, health=8, costs_fire=0, costs_spirits=2, has_spirits=4, has_fire=3, skills=[skills.Packrat, skills.Shield, skills.Underdog, skills.Fertility]), description='a magical creature with a lot of spirit power and fertility, but weak against fire the underdog skill adds an element of surprise, while the shield skill protects it'),
# Thornbeast 🐭🦔🔰 7p 10h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 50
Blueprint(original=Card(name='Thornbeast', power=7, health=10, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Fertility, skills.Spines, skills.Shield]), description='a powerful, yet spiky creature with high health and low spirit cost the spines skill adds to its already dangerous physique, while the shield and fertility skills keep it going'),
# Aerialisk 🐭💀🧺🚀🐩 9p 4h
# costs: 🔥 has: 🔥🔥👻👻 pot: 49
Blueprint(original=Card(name='Aerialisk', power=9, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat, skills.Airdefense, skills.Underdog]), description='an airborne creature with a lot of power, but low health and spirit cost the packrat and underdog skills emphasize its ferocity, while the air defense skill makes it a formidable opponent against other flying creatures'),
# Draconic 🔰🐭💀🐩 3p 9h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 50
Blueprint(original=Card(name='Draconic', power=3, health=9, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Shield, skills.Fertility, skills.InstantDeath, skills.Underdog]), description='With high power and health, as well as the skills Shield and Underdog, this card inspires an image of a powerful, firebreathing dragon with an impenetrable shield The skills Fertility and InstantDeath add to the sense of awe and danger surrounding this creature'),
# Glaciate 🔰🦔🐭💀🧺 7p 4h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 52
Blueprint(original=Card(name='Glaciate', power=7, health=4, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Shield, skills.Spines, skills.Fertility, skills.InstantDeath, skills.Packrat]), description='The high power and spines of this card, combined with the Shield and Fertility skills, suggest a creature made of ice with sharp, dangerous spikes protruding from its body The Packrat skill adds an element of resourcefulness and cunning to the mix'),
# Etherion 🧺🐩🔰🐭 3p 10h
# costs: 👻 has: 🔥🔥🔥👻👻👻 pot: 50
Blueprint(original=Card(name='Etherion', power=3, health=10, costs_fire=0, costs_spirits=1, has_spirits=3, has_fire=3, skills=[skills.Packrat, skills.Underdog, skills.Shield, skills.Fertility]), description='With its high health and spirit values, this card brings to mind a mystical, otherworldly creature that can disappear into thin air The skills Packrat and Underdog also suggest an elusive, hardtocatch quality, while Shield and Fertility hint at an ethereal, protective nature'),
# Sirenade 🐭💀🧺 6p 4h
# costs: - has: 🔥🔥🔥👻👻👻 pot: 50
Blueprint(original=Card(name='Sirenade', power=6, health=4, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat]), description='The powerful, seductive allure of a siren is evoked by this card\'s Fertility skill, while the InstantDeath skill brings to mind the dangerous songs that can lure sailors to their doom The Packrat skill also suggests a creature that can accumulate treasures and resources, while its moderate power and health values suggest a challenging foe'),
# Vulpineer 🧺🔰🐭 3p 6h
# costs: - has: 🔥🔥🔥🔥👻👻👻 pot: 50
Blueprint(original=Card(name='Vulpineer', power=3, health=6, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='An intelligent and cunning creature, the Vulpineer is quick to adapt to its environment and make use of its resources  skills reflected in this card\'s Packrat and Fertility attributes The Shield skill suggests a defensive, tactical quality, while the moderate power and health values paint a picture of a creature that relies more on wit than brute force'),
# Necroturtle 💀🧺🐭🔰🐩 2p 3h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 42
Blueprint(original=Card(name='Necroturtle', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility, skills.Shield, skills.Underdog]), description='a turtlelike creature with the ability to inflict instant death, also a packrat, shielded, fertile, and an underdog'),
# Sunlioness 🐭🔰🐩 6p 8h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 47
Blueprint(original=Card(name='Sunlioness', power=6, health=8, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Fertility, skills.Shield, skills.Underdog]), description='a powerful lioness with high health and fire affinity, also fertile, shielded, and an underdog'),
# Phoenishark 🧺🔰🐭💀🐩 7p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
Blueprint(original=Card(name='Phoenishark', power=7, health=7, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.InstantDeath, skills.Underdog]), description='a fantastical creature with high powerhealth and water affinity, also a packrat, shielded, fertile, can inflict instant death, and is an underdog'),
# Mysticorn 🐭🧺💀🔰🐩 7p 9h
# costs: 👻👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
Blueprint(original=Card(name='Mysticorn', power=7, health=9, costs_fire=0, costs_spirits=2, has_spirits=6, has_fire=6, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath, skills.Shield, skills.Underdog]), description='a mystical unicorn with high powerhealth and spirit affinity, also shielded, fertile, a packrat, can inflict instant death, and an underdog'),
# Deathwing 💀🔰🐭 1p 2h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻 pot: 29
Blueprint(original=Card(name='Deathwing', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=5, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='With the skills Instant Death and Shield, this creature represents strength in both attack and defense The name reflects the instant death ability and powerful defense'),
# Packwolf 🧺🐩🔰🐭💀 9p 8h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 64
Blueprint(original=Card(name='Packwolf', power=9, health=8, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Packrat, skills.Underdog, skills.Shield, skills.Fertility, skills.InstantDeath]), description='This creature has the skills Packrat and Underdog, making it an ideal infiltrator and collector Its high power and health make it a threatening opponent Packwolf represents the creature\'s packrat abilities, as well as its wolflike strength and cunning'),
# Faeunicorn 🐭🧺💀 9p 7h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 51
Blueprint(original=Card(name='Faeunicorn', power=9, health=7, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='The high spirit score and Fertility skill of this card suggest a magical creature with healing abilities Its high power and health make it a formidable opponent The name Faeunicorn represents the creature\'s magical essence and physical toughness'),
# Shieldrhino 🐭💀🧺🔰 5p 7h
# costs: 🔥 has: 🔥🔥👻👻 pot: 49
Blueprint(original=Card(name='Shieldrhino', power=5, health=7, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat, skills.Shield]), description='This creature has the skills Shield and Packrat, indicating that it\'s an invincible collector The high health score and the rhinolike strength make it difficult to defeat Shieldrhino represents the creature\'s strength, protective qualities, and natural armor'),
# Firebug 💀🔰🐭 9p 4h
# costs: 👻👻👻👻👻 has: 🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Firebug', power=9, health=4, costs_fire=0, costs_spirits=5, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='The high spirit score and Fertility skill of this card suggest a creature with the ability to create life from fire Its high power and health make it a threatening opponent The name Firebug represents the creature\'s fiery nature and insectoid appearance'),
# Glimmbat 🔰🐩🐭 5p 3h
# costs: - has: 🔥🔥🔥🔥🔥👻👻 pot: 46
Blueprint(original=Card(name='Glimmbat', power=5, health=3, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=5, skills=[skills.Shield, skills.Underdog, skills.Fertility]), description='a small but tough creature with a shield ability and high fertility'),
# Thunderhare 🔰🐭🐩🧺💀🚀 9p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Thunderhare', power=9, health=8, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Shield, skills.Fertility, skills.Underdog, skills.Packrat, skills.InstantDeath, skills.Airdefense]), description='a fast and powerful rabbit with multiple skills, including air defense and instant death'),
# Thornoceros 🦔🔰 9p 7h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 38
Blueprint(original=Card(name='Thornoceros', power=9, health=7, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Spines, skills.Shield]), description='a spiny rhinoceroslike creature with strong shield and spine abilities'),
# Nebulion 🐭🚀💀🐩 8p 8h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 62
Blueprint(original=Card(name='Nebulion', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Fertility, skills.Airdefense, skills.InstantDeath, skills.Underdog]), description='a mystical creature with high fertility and the ability to defend against air attacks, perfect for a player with a focus on spirits'),
# Seedpup 🐭 3p 4h
# costs: 👻 has: 🔥🔥👻👻 pot: 22
Blueprint(original=Card(name='Seedpup', power=3, health=4, costs_fire=0, costs_spirits=1, has_spirits=2, has_fire=2, skills=[skills.Fertility]), description='a small but fertile and determined creature with fertility skills'),
# SkyDragon 🪁🦔🐭💀🔰🚀 7p 10h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 75
Blueprint(original=Card(name='SkyDragon', power=7, health=10, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.Soaring, skills.Spines, skills.Fertility, skills.InstantDeath, skills.Shield, skills.Airdefense]), description='high powerhealthspirits, fire cost, soaring, spines, fertility, instant death, shield, airdefense'),
# ViperHawk 🦔 8p 7h
# costs: 🔥 has: 🔥👻 pot: 29
Blueprint(original=Card(name='ViperHawk', power=8, health=7, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines]), description='high power, low health, fire cost, spines'),
# UnderRat 🐭🐩🧺 4p 2h
# costs: 🔥🔥 has: 🔥 pot: 26
Blueprint(original=Card(name='UnderRat', power=4, health=2, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility, skills.Underdog, skills.Packrat]), description='low powerhealth, high fire cost, packrat, underdog'),
# ShieldArmadillo 🧺🔰 4p 6h
# costs: 🔥🔥🔥 has: 👻👻 pot: 28
Blueprint(original=Card(name='ShieldArmadillo', power=4, health=6, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Packrat, skills.Shield]), description='low power, high health, high fire cost, packrat, shield'),
# Fungaloid 🧺🦔🔰🐭💀 8p 8h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 75
Blueprint(original=Card(name='Fungaloid', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=5, skills=[skills.Packrat, skills.Spines, skills.Shield, skills.Fertility, skills.InstantDeath]), description='The card has high spirits but requires high fire to use The name\'s relation to the card highlights its growth aspect, which has skills like Packrat and Fertility The spiky armor is reflected in its Spines and Shield skills, while its deadliness and fragility are reflected in InstantDeath'),
# Apexlion 🔰💀🪁 7p 4h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 50
Blueprint(original=Card(name='Apexlion', power=7, health=4, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Shield, skills.InstantDeath, skills.Soaring]), description='With high power, the name suits the card as the animal is seen as the ultimate predator The name\'s relation to the card highlights its strength with Shield and InstantDeath abilities The Soaring skill is related to the lions aspect of being a king of the skies'),
# Ferretora 🐭🧺 3p 5h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 43
Blueprint(original=Card(name='Ferretora', power=3, health=5, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Fertility, skills.Packrat]), description='The name relates to the card\'s animal theme, with the name being a fusion of ferret and tora Japanese for tiger The name\'s relation to the card highlights its balance of power and health, with skills like Fertility helping to keep it alive Its other skill, Packrat, is related to what real ferrets do'),
# Shadowsting 💀 3p 3h
# costs: 🔥 has: 👻 pot: 16
Blueprint(original=Card(name='Shadowsting', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath]), description='The name relates to the card\'s instant death ability, which is represented in its skills The animal theme is represented by a mysterious creature that lives in the shadows, while its fire requirement is reflected in its name'),
# Armorspike 🦔💀🧺🔰 6p 2h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 39
Blueprint(original=Card(name='Armorspike', power=6, health=2, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Spines, skills.InstantDeath, skills.Packrat, skills.Shield]), description='This card has high power, spines and instant death skill Suggesting a name that highlights its spiky armor, deadly capability, and formidable strength'),
# EnigmaMoth 🧺🐩🔰 3p 10h
# costs: - has: 🔥🔥🔥👻👻👻👻 pot: 52
Blueprint(original=Card(name='EnigmaMoth', power=3, health=10, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Packrat, skills.Underdog, skills.Shield]), description='An animal of myth has a high health value, shield and underdog skill which makes them unpredictable and hard to target The name is a nod to the creature\'s elusiveness and defensive abilities'),
# Furyphoenix 🧺🐭🐩💀 7p 6h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 52
Blueprint(original=Card(name='Furyphoenix', power=7, health=6, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=4, skills=[skills.Packrat, skills.Fertility, skills.Underdog, skills.InstantDeath]), description='This card has high power  hit points, fertility skill which means it can spawn other creatures, instant death and underdog skill Suggesting a name that highlights its fierce fire, ability to spawn other creatures, and strong defense when outnumbered'),
# Spirited Bear 🚀🦔🐭🪁💀🧺 10p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
Blueprint(original=Card(name='Spirited Bear', power=10, health=8, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.Airdefense, skills.Spines, skills.Fertility, skills.Soaring, skills.InstantDeath, skills.Packrat]), description='This card\'s high power and health values, and multiple skills including air defense and fertility make it a dominant force on the field The name reflects its high spirits and strength, while also nodding to its air defense abilities'),
# Fierceback 🦔💀🧺🔰🐭 7p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Fierceback', power=7, health=7, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Spines, skills.InstantDeath, skills.Packrat, skills.Shield, skills.Fertility]), description='This card has spines, instant death skill, high power and HP, and a packrat skill The name refers to its formidable weaponry, its determination to protect its brood and its ability to survive '),
# Flameleon 🧺 4p 2h
# costs: 🔥 has: 🔥🔥🔥🔥🔥 pot: 19
Blueprint(original=Card(name='Flameleon', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=5, skills=[skills.Packrat]), description='This card has high fire affinity, has the ability to store extra fire, and has a skill called Packrat, which fits well with the image of a small lizard that hoards flames and other treasures'),
# Phoenixcub 💀🐭🔰🧺 3p 10h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 53
Blueprint(original=Card(name='Phoenixcub', power=3, health=10, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Packrat]), description='With high health and many skills, this card is already strong and versatile, but as a young phoenix it also has great potential to grow stronger and evolve'),
# Undergnat 🐩 1p 2h
# costs: 🔥 has: 🔥🔥👻 pot: 10
Blueprint(original=Card(name='Undergnat', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Underdog]), description='This card has low power and health but the Underdog skill, which makes it stronger when it is outnumbered The name Undergnat plays on this theme of being small but able to annoy opponents, like a pesky little insect'),
# Shieldpup 💀🔰 2p 1h
# costs: 🔥🔥 has: 👻 pot: 16
Blueprint(original=Card(name='Shieldpup', power=2, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.InstantDeath, skills.Shield]), description='With a few defensive skills but low power and health, this card seems like a scrappy little puppy that can bark a lot but isn\'t too intimidating on its own The name Shieldpup reflects its resilience and potential to grow into a stronger protector'),
# Bansheeowl 💀🐭🐩 1p 1h
# costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 21
Blueprint(original=Card(name='Bansheeowl', power=1, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.InstantDeath, skills.Fertility, skills.Underdog]), description='relatively weak, but has InstantDeath skill and has  fire icons, making it deadly against other creatures'),
# Spriteling 🐭🔰 2p 1h
# costs: - has: 👻👻 pot: 29
Blueprint(original=Card(name='Spriteling', power=2, health=1, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=0, skills=[skills.Fertility, skills.Shield]), description='small, fast, and has the Fertility and Shield skills to help control the field and protect other creatures'),
# Chimerafang 🧺🔰💀🐭 4p 3h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 41
Blueprint(original=Card(name='Chimerafang', power=4, health=3, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Packrat, skills.Shield, skills.InstantDeath, skills.Fertility]), description='ferocious and skilled, with Packrat, Shield, InstantDeath, and Fertility skills and both fire and spirit requirements'),
# Firetortoise 🔰 1p 2h
# costs: 🔥🔥🔥 has: 🔥👻👻 pot: 11
Blueprint(original=Card(name='Firetortoise', power=1, health=2, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Shield]), description='slow and heavily costed, but with high defense and a powerful Shield skill to make it difficult to take down'),
# Pyrodillo 💀🐭🔰🐩🦔 9p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 72
Blueprint(original=Card(name='Pyrodillo', power=9, health=7, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=6, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Underdog, skills.Spines]), description='an armored creature with high power and health, and both fire and spirit requirements, as well as several versatile skills like InstantDeath, Fertility, Shield, Underdog, and Spines'),
# Gemmog 🔰🐭 2p 2h
# costs: 🔥 has: 🔥 pot: 21
Blueprint(original=Card(name='Gemmog', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield, skills.Fertility]), description='related to gems, as the card has Shield skill'),
# Fribbit 🐭💀🔰 4p 2h
# costs: 🔥 has: 🔥👻👻 pot: 32
Blueprint(original=Card(name='Fribbit', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.InstantDeath, skills.Shield]), description='related to frog, as the card has Fertility skill, and high power, but low health'),
# Pinelmink 🐭🔰🦔 3p 3h
# costs: 🔥 has: 🔥 pot: 27
Blueprint(original=Card(name='Pinelmink', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility, skills.Shield, skills.Spines]), description='related to pine martens, as the card has Spines skill, and is a balance between power and health'),
# Dragonsaur 🐭🧺🔰🐩💀🦔 6p 9h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
Blueprint(original=Card(name='Dragonsaur', power=6, health=9, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Fertility, skills.Packrat, skills.Shield, skills.Underdog, skills.InstantDeath, skills.Spines]), description='related to a dinosaur, as the card has many skills and a high cost and health'),
# Hedgemars 🐭 3p 1h
# costs: 🔥🔥 has: 👻👻👻 pot: 15
Blueprint(original=Card(name='Hedgemars', power=3, health=1, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=0, skills=[skills.Fertility]), description='related to hedgehogs and marsupials, as the card has Fertility skill and is lowcost, with high health'),
# Frostmoth 🐩 5p 2h
# costs: 👻👻👻 has: 👻👻 pot: 14
Blueprint(original=Card(name='Frostmoth', power=5, health=2, costs_fire=0, costs_spirits=3, has_spirits=2, has_fire=0, skills=[skills.Underdog]), description='a magical moth that lives in colder places, costs spirit, has a little fire, but is very frail'),
# Infernusaur  6p 2h
# costs: 👻 has: 🔥 pot: 14
Blueprint(original=Card(name='Infernusaur', power=6, health=2, costs_fire=0, costs_spirits=1, has_spirits=0, has_fire=1, skills=[]), description='powerful, fiery, low spirits cost, low spirits value, moderate health'),
# Luckythorn 🍀💀 1p 1h
# costs: 🔥 has: 🔥 pot: 9
Blueprint(original=Card(name='Luckythorn', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.LuckyStrike, skills.InstantDeath]), description='lucky and deadly, but weak, firebased, no spirits'),
# Flamegrizzly 🐭🔰💀 2p 2h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻 pot: 29
Blueprint(original=Card(name='Flamegrizzly', power=2, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=4, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='strong, high fire cost and fire value, can shield and procreate'),
# Shieldrex 💀🔰🐭 7p 6h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 48
Blueprint(original=Card(name='Shieldrex', power=7, health=6, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='highly protective, strong and enduring, high spirits value, high fire value'),
# Fertigore 💀🧺🐭 8p 8h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 51
Blueprint(original=Card(name='Fertigore', power=8, health=8, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility]), description='Fertile and has  power and health, with the skills InstantDeath and Packrat'),
# Coralynx  5p 1h
# costs: 🔥 has: 🔥👻 pot: 11
Blueprint(original=Card(name='Coralynx', power=5, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='A small but powerful creature, with  power and  health, and a fiery attribute'),
# Winglet 🐭🪁💀 4p 1h
# costs: 🔥 has: 👻 pot: 24
Blueprint(original=Card(name='Winglet', power=4, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Fertility, skills.Soaring, skills.InstantDeath]), description='Has a combination of abilities, with  power and  health, and can fly and be fertile'),
# Frostback 🔰🐭🦔🧺 4p 6h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
Blueprint(original=Card(name='Frostback', power=4, health=6, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.Shield, skills.Fertility, skills.Spines, skills.Packrat]), description='A snowloving creature with  power and  health, and the ability to defend itself with a shield, deal damage with spines and be fertile'),
# Flameknight  9p 3h
# costs: 🔥🔥🔥🔥🔥🔥 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Flameknight', power=9, health=3, costs_fire=6, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='A strong card with high power and moderate health, with an expensive cost in fire to play'),
# FertilitySage 🧺💀🔰🐩🐭 3p 5h
# costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 51
Blueprint(original=Card(name='FertilitySage', power=3, health=5, costs_fire=0, costs_spirits=2, has_spirits=7, has_fire=5, skills=[skills.Packrat, skills.InstantDeath, skills.Shield, skills.Underdog, skills.Fertility]), description='This card has a high health and spirit cost and specializes in increasing the fertility of other cards Its packrat skill helps keep it supplied with enough spirits, and its instant death skill can neutralize a powerful enemy The name \"FertilitySage\" fits its nurturing nature and speciality in providing support to other cards'),
# ThornedLynx 💀🐭🔰🦔 4p 6h
# costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 42
Blueprint(original=Card(name='ThornedLynx', power=4, health=6, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Spines]), description='This card has spines and high power and health, plus a moderate fire cost Its instant death and shield skills and moderate spirit cost emphasize its fighting abilities Its name \"ThornedLynx\" reflects its powerful nature and sharp spines'),
# SpinyImp 🦔 6p 1h
# costs: - has: 🔥👻 pot: 25
Blueprint(original=Card(name='SpinyImp', power=6, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines]), description='This cheap card has high power and low health, plus useful spines and moderate fire and spirit costs Its name \"SpinyImp\" represents its mischievous and spiky nature, with the ability to inflict damage'),
# ShieldedBasilisk 🧺💀🔰🐭 5p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 61
Blueprint(original=Card(name='ShieldedBasilisk', power=5, health=6, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Packrat, skills.InstantDeath, skills.Shield, skills.Fertility]), description='This card has moderate stats overall, with high fire and spirit costs and shield, instant death, packrat, and fertility skills Its name \"ShieldedBasilisk\" emphasizes its defensive capabilities, and the instant death skill represents its dangerous nature'),
# ArmoredRhino 💀🧺🐭🔰 8p 3h
# costs: 🔥 has: 🔥🔥👻👻 pot: 47
Blueprint(original=Card(name='ArmoredRhino', power=8, health=3, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility, skills.Shield]), description='This powerful card has high stats across the board and a moderate fire cost Its skills include instant death, packrat, fertility, and shield Its name \"ArmoredRhino\" reflects its thick skin, and the instant death skill represents its deadly nature'),
# Voidragon 🔰🐭🦔🧺💀 6p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 62
Blueprint(original=Card(name='Voidragon', power=6, health=8, costs_fire=1, costs_spirits=0, has_spirits=7, has_fire=5, skills=[skills.Shield, skills.Fertility, skills.Spines, skills.Packrat, skills.InstantDeath]), description='The name relates to the card\'s high power and health, as well as its attribute of having a lot of spirits and being very costly  in comparison to the Grizzly Bear The card\'s skills add to its fierce and mystical character, and the name \"Voidragon\" implies a powerful and almost mystical creature'),
# Starhound 💀🦔🐭🪁🧺🐩 9p 9h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Starhound', power=9, health=9, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.InstantDeath, skills.Spines, skills.Fertility, skills.Soaring, skills.Packrat, skills.Underdog]), description='The name \"Starhound\" relates to the card\'s high power and health values and the fact that it has no costs in fire or spirits, making it a very versatile card The skills also make it a fierce Hunter creature, which makes the name even more fitting'),
# Windrider 💀🚀🐭🧺🔰 8p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Windrider', power=8, health=7, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.InstantDeath, skills.Airdefense, skills.Fertility, skills.Packrat, skills.Shield]), description='The name \"Windrider\" relates to the card\'s high power and health values especially when looked at its price, as well as its low fire and spirits costs, which are indicated in the card The skills also make it a speedy and agile creature, which makes the name even more fitting'),
# Skulker 💀 10p 4h
# costs: 🔥 has: 🔥👻👻 pot: 32
Blueprint(original=Card(name='Skulker', power=10, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath]), description='The name \"Skulker\" implies a creature that is powerful and sneaky, which relates to the card\'s high power value and its skill \"InstantDeath\" The card\'s low health values, as well as its low fire and spirit costs, are also taken into account when coming up with this name'),
# Burrower 🧺🐭 3p 1h
# costs: 🔥 has: 🔥👻👻 pot: 21
Blueprint(original=Card(name='Burrower', power=3, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Packrat, skills.Fertility]), description='The name \"Burrower\" suggests a creature that is underground, which relates to the card\'s skill set The card has low power and health values but high spirit cost, which are all taken into account when suggesting this name The name also implies that this card type is best for supporting other creature types'),
# Faewolf 🔰💀🐭 3p 3h
# costs: 👻👻👻👻👻 has: 🔥👻 pot: 28
Blueprint(original=Card(name='Faewolf', power=3, health=3, costs_fire=0, costs_spirits=5, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.InstantDeath, skills.Fertility]), description='has high spirit cost, animal name relates to fertility skill, average powerhealth, and has defensive skills'),
# Inferna  4p 1h
# costs: 🔥🔥🔥 has: 🔥 pot: 7
Blueprint(original=Card(name='Inferna', power=4, health=1, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='high fire cost, high power, low health, no skills, and name relates to fire'),
# Packturtle 🔰🧺💀 4p 10h
# costs: 🔥🔥🔥 has: 🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Packturtle', power=4, health=10, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Shield, skills.Packrat, skills.InstantDeath]), description='high health, lots of firespirit, defensive skills, and name relates to defensive skill and animal combination'),
# FertilityFox 🐭 1p 2h
# costs: 🔥 has: 👻 pot: 13
Blueprint(original=Card(name='FertilityFox', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Fertility]), description='low powerhealth, minimal fire, one fertility skill, and animal name relates to skill'),
# Spiritox 🐭🧺💀 5p 10h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 50
Blueprint(original=Card(name='Spiritox', power=5, health=10, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath]), description='a powerful creature with high health and strength but requires a lot of fire and spirit to summon and maintain Skills such as fertility and packrat make it a fearsome enemy The \'tox\' part of the name indicates it is venomous and dangerous, while \'spirit\' references its magical abilities'),
# Blinkcat 🐭 3p 4h
# costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 20
Blueprint(original=Card(name='Blinkcat', power=3, health=4, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Fertility]), description='a quick and agile feline that is somewhat expensive and difficult to summon due to the high fire cost Its fertility skill references its ability to rapidly reproduce, while its low health indicates it can be taken down just as quickly'),
# Airviper  3p 1h
# costs: 🔥🔥🔥 has: 👻👻 pot: 6
Blueprint(original=Card(name='Airviper', power=3, health=1, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=0, skills=[]), description='a dangerous reptilian creature that requires spirit to summon and is quite fragile Despite this, its flight skills make it difficult to attack Its name references both its ability to fly and its venomous bite'),
# ShieldBear 🦔🪁🔰🐭🧺🐩 6p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 66
Blueprint(original=Card(name='ShieldBear', power=6, health=7, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Spines, skills.Soaring, skills.Shield, skills.Fertility, skills.Packrat, skills.Underdog]), description='a massive creature with high health and strength but no fire cost Its skills, particularly shield and underdog, indicate a tanklike role Its name references its ability to protect other creatures and take heavy hits'),
# Featherbat 🪁 2p 2h
# costs: 🔥 has: 🔥👻👻👻👻👻 pot: 13
Blueprint(original=Card(name='Featherbat', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=1, skills=[skills.Soaring]), description='a flying creature with medium powerhealth and moderate fire cost Its soaring skill makes it difficult to attack, while its name references its feathered wings and its batlike appearance'),
# Shieldbear 🐭🔰💀 3p 9h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Shieldbear', power=3, health=9, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='The card has high health and is equipped with several shield skills The name Shieldbear indicates a sturdy, armored creature that is tough to take down'),
# Faeferret 🐭 1p 2h
# costs: 🔥🔥 has: 🔥🔥👻👻 pot: 14
Blueprint(original=Card(name='Faeferret', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility]), description='The card is small low power, low health, but has high spirit and fire attributes, and a fertility skill The name Faeferret has a magical and playful quality to it, which fits with the card\'s attributes'),
# Firefox 🐭 1p 2h
# costs: 🔥 has: 🔥🔥👻 pot: 14
Blueprint(original=Card(name='Firefox', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Fertility]), description='The card is a lowcost card with relatively low power and health, but has high fire attribute and a fertility skill The name Firefox evokes the element of fire and the animal\'s agility and swiftness'),
# Shellback 🔰🐩 2p 2h
# costs: 🔥 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Shellback', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Underdog]), description='The card has average power and health, but is equipped with shield and underdog skills The name Shellback indicates a tough, protective creature'),
# Archelion 🐭🔰🧺 7p 4h
# costs: 🔥 has: 🔥🔥👻👻 pot: 41
Blueprint(original=Card(name='Archelion', power=7, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.Packrat]), description='related to the powerhealth ratio and the skill packrat'),
# Dreamweaver 🦔💀🚀🔰🐭 7p 9h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 71
Blueprint(original=Card(name='Dreamweaver', power=7, health=9, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Spines, skills.InstantDeath, skills.Airdefense, skills.Shield, skills.Fertility]), description='high spirited, high health, diverse set of skills'),
# Chrysalis 🔰🧺🐭💀🚀 8p 8h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 72
Blueprint(original=Card(name='Chrysalis', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Shield, skills.Packrat, skills.Fertility, skills.InstantDeath, skills.Airdefense]), description='related to the protective skills and the equally balanced attributes'),
# Packratle 🧺🔰💀 2p 3h
# costs: - has: 🔥🔥👻👻👻 pot: 39
Blueprint(original=Card(name='Packratle', power=2, health=3, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Packrat, skills.Shield, skills.InstantDeath]), description='related to the packrat skill and the name similarity to Armadillo'),
# Thunderhorn 🐭💀🧺🐩🦔🔰 8p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Thunderhorn', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat, skills.Underdog, skills.Spines, skills.Shield]), description='with high values in power and health, and the skills InstantDeath and Shield, this card is both mighty and hard to defeat The name suggests a powerful and dangerous creature, with a fierce horn that strikes like thunder'),
# Skylynx 💀🔰🪁🐭 2p 2h
# costs: 🔥 has: 🔥👻👻👻 pot: 31
Blueprint(original=Card(name='Skylynx', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.InstantDeath, skills.Shield, skills.Soaring, skills.Fertility]), description='with decent power and health stats, and the skills Soaring and Shield, this card can hold its own The name suggests a majestic and swift creature that can traverse the skies with grace and ease'),
# Firehoof 💀🐭🐩 8p 3h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
Blueprint(original=Card(name='Firehoof', power=8, health=3, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.InstantDeath, skills.Fertility, skills.Underdog]), description='with high power but low health, this card is risky to play However, the skill InstantDeath can help it take down even the strongest enemies The name suggests a creature with hooves that are infused with fire, giving it a dangerous and fiery kick'),
# Whispup 💀🪁🐭🧺 2p 1h
# costs: 🔥 has: 🔥👻 pot: 27
Blueprint(original=Card(name='Whispup', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Soaring, skills.Fertility, skills.Packrat]), description='with low power and health, this card seems weak However, the skills Soaring and Fertility suggest a creature that can grow and strengthen quickly The name suggests a small, wispy creature that can flutter and dance in the wind, but has the potential to become much more than it appears'),
# Armorgator 🐩💀🔰🧺🐭🦔 8p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Armorgator', power=8, health=7, costs_fire=0, costs_spirits=0, has_spirits=8, has_fire=6, skills=[skills.Underdog, skills.InstantDeath, skills.Shield, skills.Packrat, skills.Fertility, skills.Spines]), description='with high power and health, this card is a formidable opponent The skills Shield and Packrat make it even harder to take down The name suggests a creature with scaly armor that protects its vulnerable spots, and a tenacious fighter that doesn\'t give up easily'),
# Mysticboar 🐭🐩🔰 6p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 53
Blueprint(original=Card(name='Mysticboar', power=6, health=10, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=6, skills=[skills.Fertility, skills.Underdog, skills.Shield]), description='high power and health, some fire and spirits, fertility and shield skills, related to the boar\'s fighting abilities and mystical attribute'),
# Solarlynx 🐭🔰💀 9p 5h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 50
Blueprint(original=Card(name='Solarlynx', power=9, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='high power, low health, some fire and spirits, fertility, shield and instant death skills, related to the lynx\'s hunting and nocturnal abilities'),
# Spindlecat 🐩💀🐭🔰🧺 10p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 72
Blueprint(original=Card(name='Spindlecat', power=10, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Underdog, skills.InstantDeath, skills.Fertility, skills.Shield, skills.Packrat]), description='high power and health, some fire and spirits, fertility, shield, instant death, underdog and packrat skills, related to the cat\'s agility, survival and collection abilities'),
# Scalemouse 🔰💀🐭🐩 4p 5h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Scalemouse', power=4, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Shield, skills.InstantDeath, skills.Fertility, skills.Underdog]), description='low power and health, some fire and spirits, fertility, shield, underdog and instant death skills, related to the mouse\'s small size, armor and defensive qualities'),
# Flametick 🐭🔰💀 2p 5h
# costs: 🔥 has: 🔥👻👻 pot: 34
Blueprint(original=Card(name='Flametick', power=2, health=5, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='low power, high health, some fire and spirits, fertility, shield and instant death skills, related to the tick\'s parasitic nature and fire attribute'),
# Thunderstag 🧺🐭💀🐩🪁🔰 7p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 69
Blueprint(original=Card(name='Thunderstag', power=7, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Packrat, skills.Fertility, skills.InstantDeath, skills.Underdog, skills.Soaring, skills.Shield]), description='high power and health, expensive to use, shielded, able to store resources, deadly, has potential to turn around a losing battle'),
# Vipertaur 💀🐭🐩🦔🔰 9p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Vipertaur', power=9, health=6, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.InstantDeath, skills.Fertility, skills.Underdog, skills.Spines, skills.Shield]), description='high power and low health, able to cause instant death, fertile, shielded, spiny and underdog fighter'),
# Crystanther 🔰 3p 5h
# costs: 👻👻👻👻👻 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Crystanther', power=3, health=5, costs_fire=0, costs_spirits=5, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='low power and health, expensive in spirits, highly spirited, shielded'),
# Netchimera 💀🐭🦔 5p 1h
# costs: 🔥 has: 🔥👻 pot: 28
Blueprint(original=Card(name='Netchimera', power=5, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Fertility, skills.Spines]), description='moderate power, low health, causes instant death and fertility, spiny, not expensive to use'),
# Spiketale 🧺💀🪁 2p 7h
# costs: 🔥🔥 has: 🔥👻👻 pot: 29
Blueprint(original=Card(name='Spiketale', power=2, health=7, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Packrat, skills.InstantDeath, skills.Soaring]), description='moderate power and high health, expensive in fire, packrat and soaring abilities, able to cause instant death'),
# Mysticore 🐩🔰💀🦔🧺 10p 6h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 58
Blueprint(original=Card(name='Mysticore', power=10, health=6, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=4, skills=[skills.Underdog, skills.Shield, skills.InstantDeath, skills.Spines, skills.Packrat]), description='a magical creature with high power and health, costs a bit of fire and spirits, and has both fire and spirit attributes It is also skilled with underdog, shield, instant death, spines, and packrat'),
# Gryphonfly 🐭🚀🔰 8p 3h
# costs: 🔥 has: 🔥👻 pot: 35
Blueprint(original=Card(name='Gryphonfly', power=8, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.Airdefense, skills.Shield]), description='a mythical creature that can fly and has air defense skill, and can create an impact with high power despite its smaller size He has moderate health and lower fire attribute, and costs a bit of fire to cast'),
# Ratking 💀🐩🧺 1p 6h
# costs: 🔥 has: 🔥🔥👻👻 pot: 29
Blueprint(original=Card(name='Ratking', power=1, health=6, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Underdog, skills.Packrat]), description='a fierce leader of underground armies, with low power and average health but an expert at underdog and packrat skills He costs a bit of fire but has a good spirit supply'),
# Fertilebacks 🐭🔰 1p 2h
# costs: 🔥🔥🔥 has: 👻 pot: 17
Blueprint(original=Card(name='Fertilebacks', power=1, health=2, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Fertility, skills.Shield]), description='a creature skilled at fertility and has shield skill, meaning it can protect itself and its pack with a good health supply He has a higher cost of fire to summon and no fire attribute, but still a valuable addition to a deck'),
# Flowhound 🐭 1p 5h
# costs: 🔥🔥 has: 🔥👻 pot: 18
Blueprint(original=Card(name='Flowhound', power=1, health=5, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='medium power, high health, expensive, fertility'),
# Timberwolf 🧺 4p 2h
# costs: - has: 🔥👻👻 pot: 27
Blueprint(original=Card(name='Timberwolf', power=4, health=2, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Packrat]), description='high power, low health, high spirits and packrat skill'),
# Thornycat 🦔🧺💀🐭 9p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
Blueprint(original=Card(name='Thornycat', power=9, health=8, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Spines, skills.Packrat, skills.InstantDeath, skills.Fertility]), description='very high powerhealth, expensive, fireskillheavy'),
# Mistfrog  3p 1h
# costs: 👻👻 has: 👻 pot: 6
Blueprint(original=Card(name='Mistfrog', power=3, health=1, costs_fire=0, costs_spirits=2, has_spirits=1, has_fire=0, skills=[]), description='low powerhealth, expensive, high spirit and spiritcost'),
# Beetleback 🧺 2p 2h
# costs: 👻👻 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Beetleback', power=2, health=2, costs_fire=0, costs_spirits=2, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='lowmedium powerhealth, lowcost spirit, packrat skill'),
# Constrictor 💀🧺🦔🐭 8p 9h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 57
Blueprint(original=Card(name='Constrictor', power=8, health=9, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.InstantDeath, skills.Packrat, skills.Spines, skills.Fertility]), description='a large and powerful snake with instant death capability and strong packrat skills'),
# Skylark 🐭🔰🚀🪁 5p 9h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 58
Blueprint(original=Card(name='Skylark', power=5, health=9, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Fertility, skills.Shield, skills.Airdefense, skills.Soaring]), description='a bird that soars high and has air defense and soaring skills, with decent health stats'),
# Thornbird 🐭💀🦔 3p 9h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 42
Blueprint(original=Card(name='Thornbird', power=3, health=9, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Fertility, skills.InstantDeath, skills.Spines]), description='a small and spiky bird with instant death and spines skills, with high health stats'),
# Blazebeetle 🦔🔰🐭💀 7p 5h
# costs: 🔥🔥🔥 has: 🔥🔥👻👻 pot: 44
Blueprint(original=Card(name='Blazebeetle', power=7, health=5, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Spines, skills.Shield, skills.Fertility, skills.InstantDeath]), description='a fiery bug with spines and shield skills, with high power and low health stats'),
# Spinefury 🦔 6p 3h
# costs: - has: 🔥👻👻👻 pot: 30
Blueprint(original=Card(name='Spinefury', power=6, health=3, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Spines]), description='This creature has relatively low power and health stats, but it does have Spines, which suggests a certain level of defensiveness Its spirits and fire stats are both relatively low, so the name should reflect that \"Spinefury\" plays off the \"spines\" skill, while also conveying a sense of urgency and intensity'),
# Flame 🔰 5p 5h
# costs: 🔥 has: 👻👻👻 pot: 25
Blueprint(original=Card(name='Flame', power=5, health=5, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=0, skills=[skills.Shield]), description='turtle  This creature has moderate power and health, but its strength lies mainly in its defensive abilities  specifically, its Shield skill Given its fire stats, a name that plays off \"flame\" could be fitting \"Flameturtle\" suggests a creature that is both slow and steady, but also protected by a fiery shell'),
# Packthorn 🧺🐭🐩💀🦔🔰 7p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
Blueprint(original=Card(name='Packthorn', power=7, health=7, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.Packrat, skills.Fertility, skills.Underdog, skills.InstantDeath, skills.Spines, skills.Shield]), description='With high power and health, Packthorn is definitely a threat on the battlefield It also has a range of skills, including Packrat, Fertility, and Underdog, that suggest a certain level of resourcefulness and adaptability The \"thorn\" in its name reinforces its power and danger, while the \"pack\" suggests a creature that works well with others'),
# Phoenixwing 🦔🪁🧺💀🐭🔰 9p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Phoenixwing', power=9, health=8, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Spines, skills.Soaring, skills.Packrat, skills.InstantDeath, skills.Fertility, skills.Shield]), description='With power and health at their maximums, this card is a force to be reckoned with The name ties in nicely with the two fire and spirit attributes at the top range of their allowed values, as well as the skills \"Soaring\" and \"Fertility\", which are reminiscent of a mythical bird reborn from its ashes, spreading its wings and rising above all competition'),
# Goatoble 🪁🐭💀🧺 9p 6h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻 pot: 51
Blueprint(original=Card(name='Goatoble', power=9, health=6, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=4, skills=[skills.Soaring, skills.Fertility, skills.InstantDeath, skills.Packrat]), description='This card has high power, a decent health score and some skills, but it\'s hampered by its aboveaverage cost yellow fire number and uneven spirit score The name adequately reflects its ramlike disposition, while the \"Instant Death\" and \"Fertility\" skills are reminiscent of the oftenduplicitous nature of goats'),
# Zoomba 🚀💀🐩 3p 1h
# costs: 🔥🔥 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Zoomba', power=3, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Airdefense, skills.InstantDeath, skills.Underdog]), description='This tiny chihuahua of a card brings little power, limited health, and a couple of tricks to the table, all at an aboveaverage cost As it turns out, the two fire cost makes it faster than it looks, and \"Airdefense\" and \"Underdog\" skill names are reflected in the name choice'),
# Bullpharoah 🔰🐭💀🦔🧺 8p 8h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 73
Blueprint(original=Card(name='Bullpharoah', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Shield, skills.Fertility, skills.InstantDeath, skills.Spines, skills.Packrat]), description='With a formidable score and a couple of defensive skills, this card is a leader on the battlefield however, it comes at a cost It has balanced spirit and fire attributes, although a bit shy of what\'s allowed, and a reasonable cost to both The name choice reflects its status as a powerful leader, with obvious references to the bull, and a nod to its powerful defense, evocative of pharaohs'),
# Blazepig 🔰🧺🐭🦔💀🚀 10p 6h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 65
Blueprint(original=Card(name='Blazepig', power=10, health=6, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=6, skills=[skills.Shield, skills.Packrat, skills.Fertility, skills.Spines, skills.InstantDeath, skills.Airdefense]), description='High power and less impressive health are the theme of this piggy card, with a cost that sits nicely in the middle The skill set is quite impressive, however, including Spines, Shield, Packrat, and Airdefense abilities The name is intended to reflect the spikes and the flame components, but also to lean somewhat into its piggish nature'),
# Luckfinch 🍀🔰 0p 1h
# costs: 🔥 has: 🔥👻👻👻👻👻 pot: 12
Blueprint(original=Card(name='Luckfinch', power=0, health=1, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=1, skills=[skills.LuckyStrike, skills.Shield]), description='low power, low health, high spirits, regenerative shield, a small, lucky bird'),
# Sky Guardian 🪁 8p 3h
# costs: - has: 🔥 pot: 30
Blueprint(original=Card(name='Sky Guardian', power=8, health=3, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Soaring]), description='very powerful, low cost, flying'),
# Inferno Crab  2p 1h
# costs: 🔥🔥🔥 has: 🔥👻👻👻 pot: 6
Blueprint(original=Card(name='Inferno Crab', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=1, skills=[]), description='low power, low health, high fire costs, moderate spirits, no skills'),
# Shell Shield 🔰 1p 3h
# costs: 👻 has: 🔥👻 pot: 14
Blueprint(original=Card(name='Shell Shield', power=1, health=3, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='low power, moderate health, no fire cost, high spirits, defensive skills'),
# Blossomice 🐭🔰💀🧺 10p 5h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 59
Blueprint(original=Card(name='Blossomice', power=10, health=5, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Fertility, skills.Shield, skills.InstantDeath, skills.Packrat]), description='relates to its high Fertility skill The card has moderate power and health and requires little Fire or Spirits to play, making it readily accessible It also has a Shield skill, adding to the card\'s survivability The name \'Blossomice\' is a play on words combining animal and nature elements'),
# Chimerafox 🐩🧺🐭🔰💀 5p 9h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
Blueprint(original=Card(name='Chimerafox', power=5, health=9, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Underdog, skills.Packrat, skills.Fertility, skills.Shield, skills.InstantDeath]), description='relates to a fox with a combination of skills, including Fertility, Shield, and Packrat The card has high health and moderate power and requires little Fire or Spirits to play The Chimera is a hybrid creature of various animals, fit for this combination of skills The alliteration of both words creates a unique and memorable name'),
# Tortoistra 🔰 3p 2h
# costs: - has: 🔥 pot: 24
Blueprint(original=Card(name='Tortoistra', power=3, health=2, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield]), description='a combination of Tortoise and Maestro, relates to the shield attribute which indicates survival and the skill Shield The card has low power and health but also requires no Spirits to play, making it an easy and enduring lategame card The composer reference in the name adds some intelligence to the card'),
# DemonBull 💀 9p 4h
# costs: 👻👻👻 has: 🔥🔥👻 pot: 28
Blueprint(original=Card(name='DemonBull', power=9, health=4, costs_fire=0, costs_spirits=3, has_spirits=1, has_fire=2, skills=[skills.InstantDeath]), description='relates to the high power attribute and the skill InstantDeath, which adds a demonic association to the bull theme The card requires some Spirits, making it more of a mid to lategame card, but it has Fire as its primary cost, which is cheap and easily accessible'),
# Armorsaur 🐭🐩🧺🦔🔰💀 9p 9h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 73
Blueprint(original=Card(name='Armorsaur', power=9, health=9, costs_fire=1, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.Fertility, skills.Underdog, skills.Packrat, skills.Spines, skills.Shield, skills.InstantDeath]), description='relates to a dinosaur theme with high health and power, and the skills, Shield, Packrat, and Fertility, adding to its survivability and growth The card requires little Spirits to play, making it easily accessible, and Fire as a primary cost indicates its strength'),
# Krakenling 🐭💀🦔🐩🧺🔰 4p 5h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 53
Blueprint(original=Card(name='Krakenling', power=4, health=5, costs_fire=2, costs_spirits=0, has_spirits=5, has_fire=4, skills=[skills.Fertility, skills.InstantDeath, skills.Spines, skills.Underdog, skills.Packrat, skills.Shield]), description='high health and packrat skills, yet balanced by the low fire and spirits cost The spines skill adds an ability to attack adjacent cards, as if a small, squishy tentacle were sticking out'),
# Spritelark 🦔🔰💀🧺🐭 4p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 62
Blueprint(original=Card(name='Spritelark', power=4, health=6, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Spines, skills.Shield, skills.InstantDeath, skills.Packrat, skills.Fertility]), description='a mix between a sprite and a lark, very spirited, with some protection skills, yet with low fire and spirits costs A card that can fly and has a complex songlike attack, hitting all adjacent cards in a melodylike way'),
# Vipervox 🐩🦔 5p 3h
# costs: 🔥🔥 has: 👻 pot: 19
Blueprint(original=Card(name='Vipervox', power=5, health=3, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Underdog, skills.Spines]), description='a sneaky, lowcost card with high power and spiny defense A small snake creature with the skill to surpriseattack with a barklike sound and retreat quickly, leaving the defender with spines'),
# Thornfury 🐩🧺🐭🔰 7p 4h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 46
Blueprint(original=Card(name='Thornfury', power=7, health=4, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Underdog, skills.Packrat, skills.Fertility, skills.Shield]), description='a highly spirited card with a high power, highcost and protective skills It has the added ability to attack two times in a turn, at the cost of damaging itself'),
# Moltenbeak 💀🔰🚀🦔🧺🐭 9p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Moltenbeak', power=9, health=8, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.InstantDeath, skills.Shield, skills.Airdefense, skills.Spines, skills.Packrat, skills.Fertility]), description='a highly offensive, high health, and nocost card with various skills The name incorporates a reference to the fire and skills for air defense, and a powerful beak attack'),
# FertilityCat 🔰🐭💀 2p 1h
# costs: 🔥 has: 🔥👻👻👻 pot: 28
Blueprint(original=Card(name='FertilityCat', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Shield, skills.Fertility, skills.InstantDeath]), description='a card with average health and decent attack power, capable of breeding new cards and populating the field with multiple units to overpower opponents, also has the ability to instantly kill opposing cards'),
# PackWyvern 🐭💀🧺🔰 7p 8h
# costs: 🔥🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
Blueprint(original=Card(name='PackWyvern', power=7, health=8, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=6, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat, skills.Shield]), description='a formidable card with high health and strong attack, also has several skills like Fertility, InstantDeath and Shield that makes it the leader of the pack, symbolizing a loyal and powerful dragon'),
# AirSpine 🐭💀🚀🦔 8p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 52
Blueprint(original=Card(name='AirSpine', power=8, health=8, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Fertility, skills.InstantDeath, skills.Airdefense, skills.Spines]), description='a versatile card with high attack and defense power, has skills that can make it a powerful flying force on the battlefield, yet spines that provide great defense when under attack, symbolizing a deadly air defense unit'),
# Packratling 💀🧺🐭 4p 3h
# costs: 👻 has: 🔥👻 pot: 32
Blueprint(original=Card(name='Packratling', power=4, health=3, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility]), description='a small card with low power but decent health and skills like Fertility and Packrat, that allows it to breed and store greater units, symbolizing a sneaky and resourceful creature'),
# Furylynx 🧺💀🔰🦔🐭 7p 5h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 66
Blueprint(original=Card(name='Furylynx', power=7, health=5, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Packrat, skills.InstantDeath, skills.Shield, skills.Spines, skills.Fertility]), description='This card has high power and health, as well as multiple skills to take down opponents The name combines \"fury\" to represent its high power and \"lynx\" to represent its agility and skill'),
# Sproutfox 🐭 4p 1h
# costs: 👻 has: 🔥🔥👻👻 pot: 19
Blueprint(original=Card(name='Sproutfox', power=4, health=1, costs_fire=0, costs_spirits=1, has_spirits=2, has_fire=2, skills=[skills.Fertility]), description='This card has moderate power, low health, and only one skill, but it has high spirit and low fire costs The name combines \"sprout\" to represent its low cost and \"fox\" to represent its agility'),
# Deathscreech 💀 4p 5h
# costs: 👻👻👻 has: 🔥🔥👻 pot: 21
Blueprint(original=Card(name='Deathscreech', power=4, health=5, costs_fire=0, costs_spirits=3, has_spirits=1, has_fire=2, skills=[skills.InstantDeath]), description='This card has moderate power and high health, with a high spirit cost and a single skill to take out opponents The name combines \"death\" to represent its instant death skill and \"screech\" to represent its ferocity'),
# Shieldedspine 🐭🔰🐩🦔🧺💀 5p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 61
Blueprint(original=Card(name='Shieldedspine', power=5, health=8, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Fertility, skills.Shield, skills.Underdog, skills.Spines, skills.Packrat, skills.InstantDeath]), description='This card has high power and health, moderate fire costs, and multiple skills to protect itself and take down opponents The name combines \"shielded\" to represent its skills to protect itself and \"spine\" to represent its spines skill and general toughness'),
# Armogator 🧺 6p 4h
# costs: 🔥🔥 has: 🔥👻 pot: 22
Blueprint(original=Card(name='Armogator', power=6, health=4, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='This card has high power and moderate health, with a moderate fire cost and a single skill to protect itself The name combines \"armor\" to represent its protection and \"gator\" to represent its toughness'),
# Flamebug 🔰 2p 1h
# costs: 🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Flamebug', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='This card has moderate power and low health, costs low fire resource and has a skill Shield, so it feels like an offensive card that has a defense mechanism The name Flamebug is related to its fire attribute and small size, making it more likely for players to underestimate its potential'),
# Fertilecat 🐭 5p 4h
# costs: 🔥 has: 🔥👻 pot: 24
Blueprint(original=Card(name='Fertilecat', power=5, health=4, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='This card has high power and health, costs low fire resource, and has a Fertility skill, which suggests it fights together with more allies The name Fertilecat plays into the high health and strength of the card, while the cat part suggests that it\'s a fastmoving and aggressive card'),
# Nightox 🐭🔰🐩🍀🧺🪁 9p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 74
Blueprint(original=Card(name='Nightox', power=9, health=8, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.Fertility, skills.Shield, skills.Underdog, skills.LuckyStrike, skills.Packrat, skills.Soaring]), description='high powerhealth, highly spirited, skillful and lucky'),
# Thornlynx 🐭🔰🦔💀 2p 4h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻 pot: 38
Blueprint(original=Card(name='Thornlynx', power=2, health=4, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.Spines, skills.InstantDeath]), description='low power but spines, balanced health, spirited'),
# Flamegorilla 💀🧺🐭🔰 4p 10h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 55
Blueprint(original=Card(name='Flamegorilla', power=4, health=10, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility, skills.Shield]), description='high health, moderately high power, somewhat costly, elusive'),
# Skybear 🔰🐭🪁🦔 6p 9h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 54
Blueprint(original=Card(name='Skybear', power=6, health=9, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Shield, skills.Fertility, skills.Soaring, skills.Spines]), description='strong and spirited, great for defense, able to soar'),
# Shadowarmadillo 🔰🧺💀🐭 0p 4h
# costs: 🔥🔥 has: 🔥👻👻 pot: 33
Blueprint(original=Card(name='Shadowarmadillo', power=0, health=4, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Shield, skills.Packrat, skills.InstantDeath, skills.Fertility]), description='low power and health, shielded and sneaky'),
# Fangedrake 🧺🔰🐭💀🦔 9p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Fangedrake', power=9, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.InstantDeath, skills.Spines]), description='powerful, high health, spines, pack rat, shield, fertility, instant death'),
# Embersnail 🔰🧺💀🐭 2p 2h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 31
Blueprint(original=Card(name='Embersnail', power=2, health=2, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield, skills.Packrat, skills.InstantDeath, skills.Fertility]), description='low powerhealth, expensive fire cost, no spirits, shield, pack rat, instant death, fertility'),
# Thunderwolf 💀🧺🔰🦔🐭🍀 8p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 76
Blueprint(original=Card(name='Thunderwolf', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.InstantDeath, skills.Packrat, skills.Shield, skills.Spines, skills.Fertility, skills.LuckyStrike]), description='very strong, high spirits and fire, pack rat, shield, spines, fertility, instant death, lucky strike'),
# Cloudcat 🐩🐭🔰🪁 7p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 58
Blueprint(original=Card(name='Cloudcat', power=7, health=6, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Underdog, skills.Fertility, skills.Shield, skills.Soaring]), description='related to its high fire and spirit cost, with soaring skill and an underdog skill, this catlike creature could be a rare breed that lives on clouds'),
# Serpentowl 💀🦔🔰🐭🧺🪁 7p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Serpentowl', power=7, health=10, costs_fire=1, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.InstantDeath, skills.Spines, skills.Shield, skills.Fertility, skills.Packrat, skills.Soaring]), description='a creature with high health and power, instant death and spines skills, that resembles an owl with serpentlike features'),
# Driftoad 🧺💀🔰 8p 2h
# costs: 👻👻👻 has: 👻 pot: 33
Blueprint(original=Card(name='Driftoad', power=8, health=2, costs_fire=0, costs_spirits=3, has_spirits=1, has_fire=0, skills=[skills.Packrat, skills.InstantDeath, skills.Shield]), description='a small creature with just enough spirit power for some packrat and shield skills, that can drift with the wind, but becomes quite weak without the spirits'),
# Flametalon 💀🧺🔰🐭🪁🐩 10p 8h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 81
Blueprint(original=Card(name='Flametalon', power=10, health=8, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.InstantDeath, skills.Packrat, skills.Shield, skills.Fertility, skills.Soaring, skills.Underdog]), description='a very strong creature with high attack and health, fiery in both its appearance and skills, and with some incredible agility in the air'),
# Soulshark 🔰🧺💀🐩🦔🐭 8p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
Blueprint(original=Card(name='Soulshark', power=8, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Shield, skills.Packrat, skills.InstantDeath, skills.Underdog, skills.Spines, skills.Fertility]), description='powerful, high health, highly spirited, defensive skills'),
# Faejaguar 🐭🧺💀🔰🪁 6p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 68
Blueprint(original=Card(name='Faejaguar', power=6, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath, skills.Shield, skills.Soaring]), description='powerful, high health, highly spirited, fertility, soaring'),
# Ironant  2p 1h
# costs: 🔥🔥🔥 has: 🔥🔥🔥👻 pot: 6
Blueprint(original=Card(name='Ironant', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=3, skills=[]), description='low powerhealth, costly, firebased, no skills'),
# Gorgontaur 🧺🐭🔰💀 7p 9h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 60
Blueprint(original=Card(name='Gorgontaur', power=7, health=9, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Packrat, skills.Fertility, skills.Shield, skills.InstantDeath]), description='powerful, high health, medium cost, packrat, defensive skills'),
# Shadowstag 🔰🐭💀🧺🪁🦔 9p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 69
Blueprint(original=Card(name='Shadowstag', power=9, health=8, costs_fire=1, costs_spirits=0, has_spirits=7, has_fire=5, skills=[skills.Shield, skills.Fertility, skills.InstantDeath, skills.Packrat, skills.Soaring, skills.Spines]), description='The card\'s high power and health make it a formidable foe, while its skills Shield, Fertility, Packrat create a versatile, capable opponent The name Shadowstag reflects its combination of power and stealth, making it an elusive and dangerous creature'),
# Boltbat 🐭💀🦔🔰🧺 4p 4h
# costs: 🔥 has: 🔥🔥👻👻 pot: 44
Blueprint(original=Card(name='Boltbat', power=4, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Spines, skills.Shield, skills.Packrat]), description='The card\'s moderate stats and skills Fertility, Instant Death, Spines, Shield, Packrat make it a good allaround choice The name Boltbat reflects both its lightningquick attacks and its ability to strike fear into its prey, fitting for a creature with such versatile skills'),
# Vortexowl 🐭🔰 7p 3h
# costs: 🔥 has: 🔥👻👻 pot: 33
Blueprint(original=Card(name='Vortexowl', power=7, health=3, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.Shield]), description='The card\'s high power and low health, combined with skills in Fertility and Shield, suggest a creature that is more strategic than allout berserker The name Vortexowl implies a bird of prey that can use gusts of wind to its advantage, while also having a wise and strategic mind'),
# Flametortoise  1p 7h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 14
Blueprint(original=Card(name='Flametortoise', power=1, health=7, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description='With low power and high health, the flametortoise is a defensive creature The card\'s skills are quite limited and the cost of fire is relatively high, but the health of the flametortoise makes it durable The name Flametortoise suggests a creature that is hotheaded and battlehardened, able to withstand flames and continue the fight'),
# Thornferret 🐭🦔 3p 2h
# costs: 🔥 has: 🔥👻 pot: 20
Blueprint(original=Card(name='Thornferret', power=3, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.Spines]), description='The card\'s relatively low power and health, combined with skills in Fertility and Spines, suggest a quick and nimble creature that relies on its agility and cunning The name Thornferret evokes a small creature that is both ferocious and sneaky, a perfect fit for this card\'s ability to deal damage from unexpected angles'),
# Fatesteed 💀🧺🐭 5p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 54
Blueprint(original=Card(name='Fatesteed', power=5, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility]), description='mix of fieryspritely, high powerhealth'),
# Runehound 🧺🐭💀 3p 3h
# costs: 🔥 has: 🔥👻👻👻👻👻👻👻👻 pot: 36
Blueprint(original=Card(name='Runehound', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=8, has_fire=1, skills=[skills.Packrat, skills.Fertility, skills.InstantDeath]), description='fast and versatile, packratlike abilities, mid powerhealth'),
# Armoredrake 💀🐭🧺🔰🦔 5p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 66
Blueprint(original=Card(name='Armoredrake', power=5, health=7, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.InstantDeath, skills.Fertility, skills.Packrat, skills.Shield, skills.Spines]), description='high healthspines, shield skill, expensive'),
# Infernafox 🐭🔰💀 7p 5h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 47
Blueprint(original=Card(name='Infernafox', power=7, health=5, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.InstantDeath]), description='high power, fiery abilities, mid health'),
# Furyfer 💀🐭🔰🧺🐩🦔 9p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
Blueprint(original=Card(name='Furyfer', power=9, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Packrat, skills.Underdog, skills.Spines]), description='powerful, spirited, skilled'),
# Spiritcat 🐭🧺🔰💀🦔 10p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 76
Blueprint(original=Card(name='Spiritcat', power=10, health=7, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=6, skills=[skills.Fertility, skills.Packrat, skills.Shield, skills.InstantDeath, skills.Spines]), description='powerful, low health, very skilled'),
# Wingfox 🐭 4p 2h
# costs: 🔥 has: 🔥👻 pot: 19
Blueprint(original=Card(name='Wingfox', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='low powerhealth, flight ability'),
# Underdogon 🐭🐩💀🚀🧺 2p 10h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 48
Blueprint(original=Card(name='Underdogon', power=2, health=10, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Fertility, skills.Underdog, skills.InstantDeath, skills.Airdefense, skills.Packrat]), description='high health, low power, underdog ability'),
# Armorphant 🔰🐩💀🐭 5p 5h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 58
Blueprint(original=Card(name='Armorphant', power=5, health=5, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.Shield, skills.Underdog, skills.InstantDeath, skills.Fertility]), description='balanced, defensive, underdog ability'),
# Thundercow 💀🐭🔰 1p 7h
# costs: 🔥🔥🔥 has: 🔥👻👻 pot: 34
Blueprint(original=Card(name='Thundercow', power=1, health=7, costs_fire=3, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath, skills.Fertility, skills.Shield]), description='high health, high costs, Shield'),
# Arcticowl  1p 2h
# costs: 🔥 has: 🔥👻👻👻 pot: 7
Blueprint(original=Card(name='Arcticowl', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=1, skills=[]), description='low powerhealth, high spirits, ice attribute'),
# Deathmoth 💀 1p 2h
# costs: 👻 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Deathmoth', power=1, health=2, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.InstantDeath]), description='low costs, InstantDeath skill'),
# Spiritpack 💀🔰🐭🧺 8p 9h
# costs: 🔥🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 61
Blueprint(original=Card(name='Spiritpack', power=8, health=9, costs_fire=3, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.InstantDeath, skills.Shield, skills.Fertility, skills.Packrat]), description='high powerhealth, high cost, Packrat skill'),
# Flamehorn 🧺🐭💀🔰🦔 10p 10h
# costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
Blueprint(original=Card(name='Flamehorn', power=10, health=10, costs_fire=0, costs_spirits=1, has_spirits=5, has_fire=5, skills=[skills.Packrat, skills.Fertility, skills.InstantDeath, skills.Shield, skills.Spines]), description='very strong, high powerhealth, no ice attribute, Spines skill'),
# Skywyrm 🪁💀🔰🐭🧺 9p 8h
# costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
Blueprint(original=Card(name='Skywyrm', power=9, health=8, costs_fire=0, costs_spirits=2, has_spirits=5, has_fire=5, skills=[skills.Soaring, skills.InstantDeath, skills.Shield, skills.Fertility, skills.Packrat]), description='Skywyrms are known to have high health and power, and the ability to fly through the air with ease Soaring skill The InstantDeath skill implies a dangerous aspect, which we can relate with the fire attribute that this card does not have, and the fire and spirits abilities for costavailability can indicate it\'s a creature that\'s difficult to obtain and control, similar to a dragon'),
# Emberlynx 🐭 5p 5h
# costs: 🔥 has: 🔥👻👻 pot: 27
Blueprint(original=Card(name='Emberlynx', power=5, health=5, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility]), description='The balance of the health and power stats of this card is reflected in a name that captures both aspects The Fertility skill suggests the creature is quick to breed, so bring lots of little ones with them  Fire and  Spirit cost'),
# Shieldonix 🔰🧺💀🐭 5p 6h
# costs: 🔥 has: 🔥🔥🔥👻👻👻 pot: 49
Blueprint(original=Card(name='Shieldonix', power=5, health=6, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Shield, skills.Packrat, skills.InstantDeath, skills.Fertility]), description='The Shield skill is an important characteristic for this card, and as a creature with high health and power, it can be related to a shield being solid and sturdy The Packrat skill refers to a tendency to hoard items or resources, and as such, Shieldonix should be related to an armadillo or a creature with armor scales'),
# Grimshark 💀🔰🧺🐭 9p 9h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 64
Blueprint(original=Card(name='Grimshark', power=9, health=9, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.InstantDeath, skills.Shield, skills.Packrat, skills.Fertility]), description='Grimshark is a creature known to have very high power and health, which makes it a formidable beast InstantDeath and Shield skills are related to a defensive creature that can also deal a lot of damage The cost and availability of this card will be higher than average, so a name that implies rarity, and menacing qualities can fit well here'),
# Thornhog 🧺🔰🐭 6p 9h
# costs: 🔥🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 48
Blueprint(original=Card(name='Thornhog', power=6, health=9, costs_fire=3, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='With its high health and the Packrat, Shield and Fertility skills, Thornhog is a tough creature with spiky attributes that produces offspring quickly and enjoys collecting items The  Fire cost suggests an animal that is more imbued with fire attributes'),
# Spiritcrag 🐩🔰🧺💀🐭🦔 7p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Spiritcrag', power=7, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Underdog, skills.Shield, skills.Packrat, skills.InstantDeath, skills.Fertility, skills.Spines]), description='high powerhealthspiritfire, multiple skills'),
# Sunweasel 💀 1p 2h
# costs: 🔥🔥 has: 🔥👻👻 pot: 12
Blueprint(original=Card(name='Sunweasel', power=1, health=2, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.InstantDeath]), description='low powerhealth, high fire cost, instant death skill'),
# Thornsprite 🦔 2p 2h
# costs: 🔥 has: 🔥👻 pot: 10
Blueprint(original=Card(name='Thornsprite', power=2, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines]), description='low powerhealth, low cost, spines skill'),
# Phoenixspark 🐩🪁💀🔰🐭🧺 8p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 76
Blueprint(original=Card(name='Phoenixspark', power=8, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Underdog, skills.Soaring, skills.InstantDeath, skills.Shield, skills.Fertility, skills.Packrat]), description='very strong, high spiritfire, multiple skills'),
# Lifedrake 🐭🔰🧺💀 7p 7h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
Blueprint(original=Card(name='Lifedrake', power=7, health=7, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.Fertility, skills.Shield, skills.Packrat, skills.InstantDeath]), description='A fierce, strong and valuable dragon with high power and health attributes It is costly to put on the board and requires both fire and spirits, denoted by its attribute values The many skills it possesses give it additional advantages, like Packrat and InstantDeath, both of which suggest its power to amass items and wipe out opponents'),
# Glimmerlynx 💀🔰🧺🐭 5p 4h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 47
Blueprint(original=Card(name='Glimmerlynx', power=5, health=4, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=5, skills=[skills.InstantDeath, skills.Shield, skills.Packrat, skills.Fertility]), description='A fantastical lynx with a coat that glimmers in various colors Its power and health attributes are above average, denoted by its attribute values, and are complemented by a variety of skills Its inclusion of InstantDeath and Shield skills speaks to its overall cleverness and fighting prowess in battle'),
# Soaringphoenix 🪁💀🔰🐭🐩 9p 10h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 77
Blueprint(original=Card(name='Soaringphoenix', power=9, health=10, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Soaring, skills.InstantDeath, skills.Shield, skills.Fertility, skills.Underdog]), description='A majestic and highly valuable bird that costs no fire to put on the board and has high spirit requirements Its power and health attributes are very strong and suggest the bird\'s overall strength, making it hard to defeat Its multiple skills, including Soaring, suggest its ability to rise above opponents and avoid attacks while delivering powerful blows'),
# Fertilemole 🐭💀🧺 2p 6h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 36
Blueprint(original=Card(name='Fertilemole', power=2, health=6, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat]), description='A cute and furry animal that has very low offensive attributes but high health, denoting it is harder to defeat It requires few resources to put on the board and has skills that suggest its value in creating new allies Fertility, while still possessing enough defensive capabilities to be a useful ally in battle with its InstantDeath and Packrat skills'),
# Flamebeast 💀🐭🪁🐩🔰 5p 10h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 69
Blueprint(original=Card(name='Flamebeast', power=5, health=10, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.InstantDeath, skills.Fertility, skills.Soaring, skills.Underdog, skills.Shield]), description='A fearsome, firebased creature that has high health and aboveaverage power It has a range of highpowered skills that make it a tough opponent, such as InstantDeath and Soaring, as well as Underdog which suggests it can still fight well even if its power or health is reduced The lack of fire cost to play this card and the high spirits requirement suggest that it is not only powerful but highly valuable'),
# Gorgonite 💀🧺 8p 2h
# costs: 🔥 has: 🔥👻 pot: 29
Blueprint(original=Card(name='Gorgonite', power=8, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.InstantDeath, skills.Packrat]), description='very powerful, but low health Instant Death and Packrat skills suggest an almost mythical warriorassassinlike persona'),
# Dream Ferret  0p 2h
# costs: 🔥 has: 🔥👻👻 pot: 5
Blueprint(original=Card(name='Dream Ferret', power=0, health=2, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[]), description='weak and cheap, but highly spirited The name is a nod to the magical or ethereal quality of the card'),
# Skitterbat 🐭💀🔰 2p 1h
# costs: 🔥🔥 has: 🔥 pot: 24
Blueprint(original=Card(name='Skitterbat', power=2, health=1, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility, skills.InstantDeath, skills.Shield]), description='low power and health, only has fire The Fertility, Instant Death and Shield skills suggest a creature with a lot of personality and agility'),
# Luminorm 🧺💀🐭🔰 4p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 63
Blueprint(original=Card(name='Luminorm', power=4, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Packrat, skills.InstantDeath, skills.Fertility, skills.Shield]), description='strong, with high spirits and fire but no spirit costs The Packrat, Instant Death, Fertility and Shield skills suggest a creature with a lot of skills and adaptability The name is a nod to the bright and shimmering quality of the card'),
# Mystique 🔰🐭 4p 5h
# costs: - has: 🔥🔥👻 pot: 41
Blueprint(original=Card(name='Mystique', power=4, health=5, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Shield, skills.Fertility]), description='mysterious, high health, protective and fertile'),
# Thunderclaw 🧺🔰🚀 7p 5h
# costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 37
Blueprint(original=Card(name='Thunderclaw', power=7, health=5, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=2, skills=[skills.Packrat, skills.Shield, skills.Airdefense]), description='powerful, highly spirited, pack animal, air defender'),
# Spikewhip 🧺🔰🐭💀 3p 5h
# costs: - has: 🔥🔥🔥👻👻👻👻 pot: 54
Blueprint(original=Card(name='Spikewhip', power=3, health=5, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.InstantDeath]), description='dangerous, spikey, spiny, instant killer'),
# Thornback 🧺🔰🦔🐩 3p 4h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 47
Blueprint(original=Card(name='Thornback', power=3, health=4, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.Packrat, skills.Shield, skills.Spines, skills.Underdog]), description='spiny underdog, high spirited, shielded, nimble'),
# Hellfire 🐩💀🔰 5p 1h
# costs: 🔥🔥🔥🔥 has: 🔥 pot: 23
Blueprint(original=Card(name='Hellfire', power=5, health=1, costs_fire=4, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Underdog, skills.InstantDeath, skills.Shield]), description='expensive, low health, fiery, underdog'),
# Cragbison 🔰🧺🐭 3p 6h
# costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 40
Blueprint(original=Card(name='Cragbison', power=3, health=6, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=2, skills=[skills.Shield, skills.Packrat, skills.Fertility]), description='a powerful, tough animal with a shield skill and fertility power'),
# Fateserpent 💀🐭🔰🧺 8p 7h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 60
Blueprint(original=Card(name='Fateserpent', power=8, health=7, costs_fire=2, costs_spirits=0, has_spirits=8, has_fire=4, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Packrat]), description='a strong creature with instantdeath and protection skills'),
# Soarspine 🐭🪁💀🦔🔰🧺 6p 8h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 71
Blueprint(original=Card(name='Soarspine', power=6, health=8, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Fertility, skills.Soaring, skills.InstantDeath, skills.Spines, skills.Shield, skills.Packrat]), description='an animal with a very high health, soaring, and spines skills'),
# Voodoomonkey 🐭💀 6p 5h
# costs: - has: 🔥🔥👻👻👻👻👻👻👻 pot: 50
Blueprint(original=Card(name='Voodoomonkey', power=6, health=5, costs_fire=0, costs_spirits=0, has_spirits=7, has_fire=2, skills=[skills.Fertility, skills.InstantDeath]), description='has a fertility skill to summon minions and instantdeath skill to eliminate enemies'),
# Wraithound 🧺🔰💀 2p 2h
# costs: - has: 🔥👻 pot: 35
Blueprint(original=Card(name='Wraithound', power=2, health=2, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat, skills.Shield, skills.InstantDeath]), description='a combination of \"wraith\" instant death skill and \"hound\" packrat and shield skills that represents this card with all these skills'),
# Rockrhino  3p 5h
# costs: 🔥🔥🔥🔥 has: 🔥👻 pot: 12
Blueprint(original=Card(name='Rockrhino', power=3, health=5, costs_fire=4, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='a rhino that is big and tough, with high defense against attacks Hence, \"rock\" represents its sturdiness and unyielding nature'),
# Glimmagecko 🐭💀🧺🔰 8p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 62
Blueprint(original=Card(name='Glimmagecko', power=8, health=8, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Fertility, skills.InstantDeath, skills.Packrat, skills.Shield]), description='a mix of \"glimmer\" referring to Fertility, Instant Death, and Packrat skills and \"gecko\" relevant because of the high spirit attribute, representing a small, but cunning creature with solid abilities'),
# Glimmertusk 🚀🧺 3p 5h
# costs: 🔥 has: - pot: 19
Blueprint(original=Card(name='Glimmertusk', power=3, health=5, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Airdefense, skills.Packrat]), description='A fantastical creature with tough, glittering skin, able to defend itself from air attacks and carry treasure'),
# Solarhare 🐭🔰🐩 8p 6h
# costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 46
Blueprint(original=Card(name='Solarhare', power=8, health=6, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.Underdog]), description='A rabbitlike creature that draws on the power of the sun and has the ability to create shields, particularly deadly to larger creatures with the underdog skill'),
# Pyroboa 💀🔰🐭 3p 5h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻 pot: 39
Blueprint(original=Card(name='Pyroboa', power=3, health=5, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=5, skills=[skills.InstantDeath, skills.Shield, skills.Fertility]), description='A fiery, snakelike creature that can bring instant death and increase fertility'),
# Fabledox 🐩🐭🔰 8p 2h
# costs: 👻👻 has: 🔥👻👻 pot: 35
Blueprint(original=Card(name='Fabledox', power=8, health=2, costs_fire=0, costs_spirits=2, has_spirits=2, has_fire=1, skills=[skills.Underdog, skills.Fertility, skills.Shield]), description='A small but powerful creature with a mix of fire and spirit attributes, skilled in underdog attacks and shielded by its high health'),
# Glimmershrew 🧺🔰🐭 3p 4h
# costs: 🔥 has: 🔥🔥👻 pot: 33
Blueprint(original=Card(name='Glimmershrew', power=3, health=4, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='A small, nimble creature with glimmering fur that reflects its low costs and packs a lot of skills The name \'shrew\' also reflects its low health'),
# Thunderbeast 💀🦔🧺🐭🔰🚀 9p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 76
Blueprint(original=Card(name='Thunderbeast', power=9, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.InstantDeath, skills.Spines, skills.Packrat, skills.Fertility, skills.Shield, skills.Airdefense]), description='A powerful creature with high power and health, and a skillset that strikes fear into opponents The name reflects its thunderous nature and beastly abilities'),
# Emberdillo 🔰 4p 3h
# costs: 🔥 has: 🔥👻 pot: 19
Blueprint(original=Card(name='Emberdillo', power=4, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='A resilient creature with a skill that shields it from attacks Its name reflects its association with fire, as well as its armored nature'),
# Wisptail 🐭🧺🔰 4p 8h
# costs: 👻👻👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 45
Blueprint(original=Card(name='Wisptail', power=4, health=8, costs_fire=0, costs_spirits=4, has_spirits=5, has_fire=5, skills=[skills.Fertility, skills.Packrat, skills.Shield]), description='A highly spirited creature with a skillset that focuses on packbuilding and defense The name reflects its intangible nature and the agility of its tail'),
# Thornhorn 🔰 5p 1h
# costs: 👻 has: 🔥👻 pot: 17
Blueprint(original=Card(name='Thornhorn', power=5, health=1, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='A creature with high power but low health, and a skill that shields it from attacks Its name reflects its tough, pointy exterior'),
# Glacibear 🐭🧺 8p 4h
# costs: 🔥 has: 🔥👻👻 pot: 35
Blueprint(original=Card(name='Glacibear', power=8, health=4, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Fertility, skills.Packrat]), description='the name comes from \"glacier\" and \"bear\", which suggests a powerful and resilient animal, fitting for a card with high power and health'),
# Sylphwing 🧺🐭🔰💀🐩 7p 10h
# costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 68
Blueprint(original=Card(name='Sylphwing', power=7, health=10, costs_fire=0, costs_spirits=1, has_spirits=7, has_fire=5, skills=[skills.Packrat, skills.Fertility, skills.Shield, skills.InstantDeath, skills.Underdog]), description='the name comes from \"sylph\", a nimble and airy creature, and \"wing\", which suggests freedom and power These qualities evoke the high spirits and health of this card, as well as useful skills like Fertility and Shield'),
# Nymphox 🐭 0p 1h
# costs: 👻👻👻 has: 🔥🔥👻👻 pot: 10
Blueprint(original=Card(name='Nymphox', power=0, health=1, costs_fire=0, costs_spirits=3, has_spirits=2, has_fire=2, skills=[skills.Fertility]), description='high spirit, low health, fertility skill'),
# Phoenixrat 🔰🧺🐭 2p 5h
# costs: 🔥🔥 has: 🔥👻👻 pot: 32
Blueprint(original=Card(name='Phoenixrat', power=2, health=5, costs_fire=2, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Shield, skills.Packrat, skills.Fertility]), description='medium powerhealth, low cost of fire, packrat skill'),
# Skywyvern 🐭🚀💀🔰🐩 9p 9h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 64
Blueprint(original=Card(name='Skywyvern', power=9, health=9, costs_fire=2, costs_spirits=0, has_spirits=8, has_fire=4, skills=[skills.Fertility, skills.Airdefense, skills.InstantDeath, skills.Shield, skills.Underdog]), description='very strong, high spiritfire, air defense and instant death skill'),
# Shadowpan 🐭🦔🔰💀🐩 6p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 65
Blueprint(original=Card(name='Shadowpan', power=6, health=6, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Fertility, skills.Spines, skills.Shield, skills.InstantDeath, skills.Underdog]), description='related to the high power and multiple skills, evoking an image of a dark, powerful beast'),
# Faefer 💀🐭🔰🧺🐩 9p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Faefer', power=9, health=10, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.InstantDeath, skills.Fertility, skills.Shield, skills.Packrat, skills.Underdog]), description='a combination of \"fae\" related to the skill \"Fertility\" and \"ferret\" related to the small, quick, skilled character of the card'),
# Flametle 🧺🐭🔰 4p 3h
# costs: 🔥 has: 🔥🔥👻👻 pot: 34
Blueprint(original=Card(name='Flametle', power=4, health=3, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Packrat, skills.Fertility, skills.Shield]), description='a combination of \"flame\" related to the fire attributes and \"beetle\" related to the shield skill, evoking an image of a small but fiery and resilient creature'),
# Phoenixogre 🔰🐩💀🐭🦔 6p 5h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻 pot: 61
Blueprint(original=Card(name='Phoenixogre', power=6, health=5, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Shield, skills.Underdog, skills.InstantDeath, skills.Fertility, skills.Spines]), description='This card has high stats across the board, making it a powerful play The skills it possesses are Shield, Underdog, InstantDeath, Fertility, and Spines The name Phoenixogre combines two mythical creatures known for their strength and resilience, suggesting a card that is both powerful and resilient'),
# Pixiecat 🐩 3p 2h
# costs: - has: 🔥👻 pot: 22
Blueprint(original=Card(name='Pixiecat', power=3, health=2, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Underdog]), description='This card has moderate stats but possesses the Underdog skill, making it a capable fighter The Pixie part of the name speaks to the card\'s skill, which implies that it can pull off unexpected victories The cat part is a nod to the animal theme of the game'),
# Mermaidon 🔰💀 4p 7h
# costs: 👻👻 has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 37
Blueprint(original=Card(name='Mermaidon', power=4, health=7, costs_fire=0, costs_spirits=2, has_spirits=4, has_fire=5, skills=[skills.Shield, skills.InstantDeath]), description='This card has relatively low stats but possesses the skills Shield and InstantDeath The name Mermaidon combines two words, Mermaid and Don, a nod to the card\'s defensive nature since mermaids are associated with water and water generally puts out fire and its ability to get rid of an opponent\'s card instantly since a don is a university professor and often seen as an authority figure'),
# Flamemongoose 💀🧺🐭🔰 4p 8h
# costs: 🔥🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 53
Blueprint(original=Card(name='Flamemongoose', power=4, health=8, costs_fire=2, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.InstantDeath, skills.Packrat, skills.Fertility, skills.Shield]), description='This card has strong attack stats and skills that include InstantDeath, Packrat, Fertility, and Shield The name Flamemongoose combines two seemingly conflicting elements  fire and an animal that lives predominantly underground  to create a sense of unexpectedness and surprise, which matches the different skills on the card'),
# Glimmerturtle 🐭🧺🔰 2p 3h
# costs: - has: 🔥🔥🔥👻👻👻 pot: 42
Blueprint(original=Card(name='Glimmerturtle', power=2, health=3, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Fertility, skills.Packrat, skills.Shield]), description='This card has decent stats all around but is particularly balanced, with the same amount of spirits and fire Its skills include Fertility, Packrat, and Shield, which can help it play a supportive role on the battlefield The name Glimmerturtle reflects its balanced nature and also hints at its ability to shield and gather resources'),
# Sunmouse  1p 1h
# costs: 🔥 has: 👻👻 pot: 4
Blueprint(original=Card(name='Sunmouse', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=0, skills=[]), description='This card has a low power and health, but is cheap to summon and only requires one fire to do so It also has a couple of slots for skills The name Sunmouse reflects its fiery attribute and also hints at its small size and agility'),
# Sunbear 🐭 10p 8h
# costs: 👻👻 has: 🔥🔥👻 pot: 40
Blueprint(original=Card(name='Sunbear', power=10, health=8, costs_fire=0, costs_spirits=2, has_spirits=1, has_fire=2, skills=[skills.Fertility]), description='With a power of  and health of , this bear is a strong performer for a low cost Its fiery attribute combined with the \"Fertility\" skill led to the creation of a bear that is associated with the warmth and energy of the sun'),
# Molemite  1p 1h
# costs: 🔥 has: 🔥👻 pot: 4
Blueprint(original=Card(name='Molemite', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='With its small size and average attributes, this card is a basic mole creature with no skills The card was named after a combination of the words \"mole\" and \"dynamite\" to give it a more memorable and unique name that fits its explosive potential'),
# Shieldfin 🐩🦔🐭🔰🧺💀 10p 9h
# costs: 👻 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
Blueprint(original=Card(name='Shieldfin', power=10, health=9, costs_fire=0, costs_spirits=1, has_spirits=6, has_fire=6, skills=[skills.Underdog, skills.Spines, skills.Fertility, skills.Shield, skills.Packrat, skills.InstantDeath]), description='With a high spirit attribute and multiple skills, this card has a variety of unique abilities It is named for its physical appearance, which resembles a fish with armor plating that can defend itself against attacks Its high spirit score further emphasizes its powerful defense'),
# Flamelete 🐭🧺💀🔰 2p 1h
# costs: 👻 has: 🔥👻 pot: 31
Blueprint(original=Card(name='Flamelete', power=2, health=1, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=1, skills=[skills.Fertility, skills.Packrat, skills.InstantDeath, skills.Shield]), description='With both \"Fertility\" and \"InstantDeath\" skills and attributes that lean heavily towards the element of fire, the name Flamelete came naturally The card represents a small but powerful creature with the potential to explode at any moment, making it a dangerous opponent for any player'),
# Windwyrm 🧺🚀🪁 10p 9h
# costs: 👻 has: 🔥🔥🔥👻👻 pot: 44
Blueprint(original=Card(name='Windwyrm', power=10, health=9, costs_fire=0, costs_spirits=1, has_spirits=2, has_fire=3, skills=[skills.Packrat, skills.Airdefense, skills.Soaring]), description='With high power and health, but low spirit and fire, this card\'s name captures its dominance over the skies and its agility in battle thanks to its Air Defense and Soaring skills, making it hard to bring down'),
# Furyfox  6p 1h
# costs: 🔥🔥 has: 🔥🔥👻 pot: 13
Blueprint(original=Card(name='Furyfox', power=6, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description='This animal name fits well with the card\'s high power and low health, but is also associated with agility and quick attacks The card\'s fire cost and fire property is also reflected in the fox\'s fiery nature'),
# Shieldserpent 🐭🧺🔰🚀💀🐩 7p 8h
# costs: 👻 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 65
Blueprint(original=Card(name='Shieldserpent', power=7, health=8, costs_fire=0, costs_spirits=1, has_spirits=7, has_fire=5, skills=[skills.Fertility, skills.Packrat, skills.Shield, skills.Airdefense, skills.InstantDeath, skills.Underdog]), description='This animal name combines the card\'s high power, low spirit and high health, which is reflective of the serpent\'s strong and tough nature Its Shield and Underdog skills also make it particularly hard to defeat'),
# Krystaur 💀🐭 3p 2h
# costs: 👻👻 has: 🔥🔥👻 pot: 23
Blueprint(original=Card(name='Krystaur', power=3, health=2, costs_fire=0, costs_spirits=2, has_spirits=1, has_fire=2, skills=[skills.InstantDeath, skills.Fertility]), description='related to crystal, spiritual, costly, deadly'),
# Packdragon 🐭🧺🪁💀🦔🔰 10p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 74
Blueprint(original=Card(name='Packdragon', power=10, health=10, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Fertility, skills.Packrat, skills.Soaring, skills.InstantDeath, skills.Spines, skills.Shield]), description='powerful, expensive, versatile, many skills'),
# Shieldwolf 🔰🐩💀🧺🐭 4p 3h
# costs: 🔥🔥 has: 🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Shieldwolf', power=4, health=3, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.Shield, skills.Underdog, skills.InstantDeath, skills.Packrat, skills.Fertility]), description='defensive, affordable, skilled, underdog'),
# Ratwizard  2p 2h
# costs: 🔥🔥🔥 has: 🔥🔥👻 pot: 7
Blueprint(original=Card(name='Ratwizard', power=2, health=2, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=2, skills=[]), description='low powerhealth and high cost with no skills, but with a trick up the sleeve'),
# Phoenixfury 🔰🐩🧺💀🐭 10p 8h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 70
Blueprint(original=Card(name='Phoenixfury', power=10, health=8, costs_fire=1, costs_spirits=0, has_spirits=7, has_fire=5, skills=[skills.Shield, skills.Underdog, skills.Packrat, skills.InstantDeath, skills.Fertility]), description='The card has high power and health, making it almost unbeatable It also has some of the most valuable and expensive attributes, namely fire and spirits The card has a range of skills including Shield and Packrat that enhance and protect its abilities and InstantDeath that makes it a formidable opponent All these attributes combined create an almost indestructible creature, mythical in power and terror, hence the name Phoenixfury'),
# Thornosaur 🧺🦔💀🐭 7p 1h
# costs: 🔥🔥 has: 🔥👻 pot: 35
Blueprint(original=Card(name='Thornosaur', power=7, health=1, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat, skills.Spines, skills.InstantDeath, skills.Fertility]), description='The card has a midrange power and low health, but high fire cost and low spirit cost It has a few skills including Spines and InstantDeath, which go well with the name Overall, the card feels like a creature cobbled together from various mythical beasts dinosaur, thorny dragon, able to rapidly kill enemies with its spikes'),
# Snowtress 💀🐩🐭🧺 4p 3h
# costs: 🔥 has: 🔥🔥👻👻👻 pot: 38
Blueprint(original=Card(name='Snowtress', power=4, health=3, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=2, skills=[skills.InstantDeath, skills.Underdog, skills.Fertility, skills.Packrat]), description='The card has a moderately low power and health, but is relatively cheap and has a decent amount of spirits and fire It has a range of skills, notably InstantDeath, Underdog, and Fertility The name Snowtress comes from the idea of a graceful and mystical creature with a cold and ruthless heart, capable of defending and attacking with equal ferocity'),
# Moonhare 🐭 2p 5h
# costs: 🔥 has: 🔥🔥👻 pot: 21
Blueprint(original=Card(name='Moonhare', power=2, health=5, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Fertility]), description='high health, slightly costly, fertility skill'),
# Scuttler 🧺 1p 1h
# costs: 🔥 has: 🔥👻👻👻👻 pot: 12
Blueprint(original=Card(name='Scuttler', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=1, skills=[skills.Packrat]), description='low powerhealth, packrat skill, spirited'),
# Skywing 🪁 3p 2h
# costs: - has: 🔥👻 pot: 21
Blueprint(original=Card(name='Skywing', power=3, health=2, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Soaring]), description='soaring skill, fire attribute, lowcost'),
# Spikemander 🦔🐭 2p 6h
# costs: - has: 🔥👻 pot: 35
Blueprint(original=Card(name='Spikemander', power=2, health=6, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines, skills.Fertility]), description='high health, spines skill, slightly costly'),
# Nightowl 🐭🐩 2p 4h
# costs: - has: 👻👻👻👻👻 pot: 35
Blueprint(original=Card(name='Nightowl', power=2, health=4, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=0, skills=[skills.Fertility, skills.Underdog]), description='a creature of the night, with medium power and health, and the skills Fertility and Underdog fitting for an underrated creature'),
# Mantistar 🐭🔰🧺💀 2p 3h
# costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 38
Blueprint(original=Card(name='Mantistar', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=2, skills=[skills.Fertility, skills.Shield, skills.Packrat, skills.InstantDeath]), description='a small creature with medium health and power, but unique skills Shield, Fertility, InstantDeath that give it a distinguishing character the name relates to its mix of different skills'),
# Spiketusk 🦔💀🐭 3p 8h
# costs: - has: 🔥🔥🔥👻👻👻👻 pot: 50
Blueprint(original=Card(name='Spiketusk', power=3, health=8, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Spines, skills.InstantDeath, skills.Fertility]), description='a strong and spiky creature with high health and the skills Spines and Fertility the name relates to its spiky appearance'),
# Shieldox 🐭🔰🧺🦔 4p 7h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻👻👻 pot: 45
Blueprint(original=Card(name='Shieldox', power=4, health=7, costs_fire=2, costs_spirits=0, has_spirits=4, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.Packrat, skills.Spines]), description='a defensive card with average power and high health, and powerful skills such as Shield and Packrat the name relates to its strong defense capabilities'),
# Springhare 🐭 1p 1h
# costs: 🔥 has: 👻 pot: 11
Blueprint(original=Card(name='Springhare', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=0, skills=[skills.Fertility]), description='this card has attributes that make it a support card with the skill Fertility, a cost structure that is inexpensive, and fairly balanced powerhealth points'),
# Hedgewisp 🐭🔰🦔🧺 4p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 56
Blueprint(original=Card(name='Hedgewisp', power=4, health=6, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Fertility, skills.Shield, skills.Spines, skills.Packrat]), description='this card has balanced attributes and cost structure, but a range of skills that make it not only hard to kill, but able to support its allies while attacking'),
# Thunderfury 🐭💀🦔🐩🧺🔰 6p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 73
Blueprint(original=Card(name='Thunderfury', power=6, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Fertility, skills.InstantDeath, skills.Spines, skills.Underdog, skills.Packrat, skills.Shield]), description='this card is a strong allaround character with multiple skills, fairly high cost, and highly balanced attributes'),
# Shieldagon 🔰 3p 7h
# costs: - has: 🔥👻 pot: 34
Blueprint(original=Card(name='Shieldagon', power=3, health=7, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Shield]), description='this card\'s strong shield and health can make it exceptionally difficult to attack in battle, and the name \'Shieldagon\' plays up this concept of a shieldlike creature'),
# Baneviper 🔰🐭💀 2p 4h
# costs: - has: 🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Baneviper', power=2, health=4, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.Fertility, skills.InstantDeath]), description='relatively high power and health, instant death skill, relatively high fire and spirits, no costs'),
# Thunderhawk 💀🐭🔰 9p 4h
# costs: 🔥 has: 🔥🔥👻👻👻👻 pot: 47
Blueprint(original=Card(name='Thunderhawk', power=9, health=4, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=2, skills=[skills.InstantDeath, skills.Fertility, skills.Shield]), description='high power, relatively high spirits, instant death skill, fire cost'),
# Shadowwolf 🐩🔰💀🐭 5p 7h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻 pot: 61
Blueprint(original=Card(name='Shadowwolf', power=5, health=7, costs_fire=0, costs_spirits=0, has_spirits=4, has_fire=5, skills=[skills.Underdog, skills.Shield, skills.InstantDeath, skills.Fertility]), description='relatively high health, shield skill, underdog skill, relatively high fire and spirits, no fire cost'),
# Blazeferret 🐭🧺🪁 9p 3h
# costs: 👻 has: 🔥🔥👻👻👻 pot: 39
Blueprint(original=Card(name='Blazeferret', power=9, health=3, costs_fire=0, costs_spirits=1, has_spirits=3, has_fire=2, skills=[skills.Fertility, skills.Packrat, skills.Soaring]), description='This name combines \"blaze\" to represent the strong attack power and \"ferret\" to represent the small, quick nature of the card'),
# Skyrider 🔰🧺 1p 2h
# costs: - has: 🔥👻👻👻 pot: 28
Blueprint(original=Card(name='Skyrider', power=1, health=2, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Shield, skills.Packrat]), description='\"Sky\" represents the card\'s fire attribute and the fact that it has no spirit costs, while \"rider\" suggests that the card accompanies and defends its owner'),
# Tombat  1p 3h
# costs: - has: 🔥 pot: 16
Blueprint(original=Card(name='Tombat', power=1, health=3, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=1, skills=[]), description='This name fuses \"tom\" from \"tomcat\" with \"bat\" to suggest the card\'s low stats and lack of skills'),
# Earthwing 🧺🔰🐭 4p 2h
# costs: 🔥 has: 👻👻👻 pot: 31
Blueprint(original=Card(name='Earthwing', power=4, health=2, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=0, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='With a balance of power and health, Earthwing is a strong and versatile creature Its packrat like tendencies make it a valuable addition to any deck, and its shield gives it an added layer of defense However, its fertility skill means it must be approached with caution, as it can quickly multiply and overwhelm opponents'),
# Empressbee 🔰🐭💀 4p 7h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 57
Blueprint(original=Card(name='Empressbee', power=4, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.Shield, skills.Fertility, skills.InstantDeath]), description='high power and health, no fire cost, lots of spirits, skills related to shielding, fertility, and instant death Empressbee suggests a powerful and regal queen of the bees, with the ability to protect and nurture her hive while also wielding deadly stingers'),
# Wyverngoose 🐩💀🐭🧺 5p 10h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 56
Blueprint(original=Card(name='Wyverngoose', power=5, health=10, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=4, skills=[skills.Underdog, skills.InstantDeath, skills.Fertility, skills.Packrat]), description='very high power and health, moderate fire cost, lots of spirits, skills related to being an underdog, instant death, fertility, and packratting Wyverngoose sounds like a formidable and unusual creature, with the strength and cunning to overcome even the toughest of opponents'),
# Grasshopper 🐩🧺 2p 1h
# costs: 🔥 has: 🔥👻👻 pot: 15
Blueprint(original=Card(name='Grasshopper', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=1, skills=[skills.Underdog, skills.Packrat]), description='low power and health, low fire cost, moderate spirits, skills related to being an underdog and packratting Grasshopper suggests a nimble and agile creature that can hop quickly out of danger and gather resources efficiently'),
# Mysticbear 🧺🐭🐩🔰 3p 8h
# costs: 🔥 has: 🔥🔥🔥👻👻 pot: 45
Blueprint(original=Card(name='Mysticbear', power=3, health=8, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=3, skills=[skills.Packrat, skills.Fertility, skills.Underdog, skills.Shield]), description='strong health and power, high fire cost, medium spirit cost, abilities suggest paranormal attributes'),
# Faeblin 🧺 0p 3h
# costs: 🔥🔥 has: 🔥👻👻👻 pot: 12
Blueprint(original=Card(name='Faeblin', power=0, health=3, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=1, skills=[skills.Packrat]), description='low powerhealth, high fire cost, medium spirit cost, Packrat skill suggests small stature and love for gathering'),
# Thornmaw 🐭🐩🔰🧺🦔 10p 9h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 67
Blueprint(original=Card(name='Thornmaw', power=10, health=9, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=5, skills=[skills.Fertility, skills.Underdog, skills.Shield, skills.Packrat, skills.Spines]), description='very strong, high fire cost, medium spirit cost, multiple skills including Spines suggest a dangerous animal with threatening looks'),
# Flarepup 🐭 2p 1h
# costs: 🔥 has: 🔥🔥🔥👻 pot: 15
Blueprint(original=Card(name='Flarepup', power=2, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=3, skills=[skills.Fertility]), description='low powerhealth, low fire cost, low spirit cost, Fertility skill suggests animal traits of high reproductive abilities andor nurturing aspects, while fire cost and name suggest a powerfulenergetic aspect'),
# Armospire 🐭 2p 6h
# costs: 🔥 has: 🔥👻 pot: 22
Blueprint(original=Card(name='Armospire', power=2, health=6, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='medium powerhealth, low fire cost, low spirit cost, Fertility skill suggests protective abilities, the name suggests a creature with armorlike attributes, spire also implies some type of ability to act as a lookout or sentry'),
# Quickfox 🔰💀🐭🧺 2p 3h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 40
Blueprint(original=Card(name='Quickfox', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=5, skills=[skills.Shield, skills.InstantDeath, skills.Fertility, skills.Packrat]), description='relatively balanced stats, multiple skills including Shield and InstantDeath'),
# Fatesprite 🔰💀🧺🐭 10p 7h
# costs: 👻👻👻 has: 🔥🔥🔥🔥👻👻👻👻 pot: 59
Blueprint(original=Card(name='Fatesprite', power=10, health=7, costs_fire=0, costs_spirits=3, has_spirits=4, has_fire=4, skills=[skills.Shield, skills.InstantDeath, skills.Packrat, skills.Fertility]), description='high stats and skills, including Fertility and InstantDeath'),
# Phoenixlet 🪁🔰 1p 1h
# costs: 🔥 has: 🔥🔥👻 pot: 13
Blueprint(original=Card(name='Phoenixlet', power=1, health=1, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=2, skills=[skills.Soaring, skills.Shield]), description='low powerhealth, moderate fire attribute, Soaring and Shield skills'),
# Spikegnat 💀🐭🧺🪁🔰🐩 3p 1h
# costs: 🔥 has: 🔥🔥👻👻 pot: 40
Blueprint(original=Card(name='Spikegnat', power=3, health=1, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Fertility, skills.Packrat, skills.Soaring, skills.Shield, skills.Underdog]), description='high power, low health, multiple skills including InstantDeath and Fertility'),
# Dragonlord 🔰🐭💀 3p 9h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 47
Blueprint(original=Card(name='Dragonlord', power=3, health=9, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=3, skills=[skills.Shield, skills.Fertility, skills.InstantDeath]), description='This card is powerful and has high health, making it fit to be a dragon and to be a lord of all dragons Its high spirit and fire costs have also made it quite exclusive to obtain The Shield skill is fitting given that it is a lord leading its pack Fertility and InstantDeath are also fitting skills, as a dragon is typically very long lived and capable of great destruction'),
# Hexfire 🔰🧺💀🐭 3p 3h
# costs: 🔥 has: 🔥🔥👻👻 pot: 38
Blueprint(original=Card(name='Hexfire', power=3, health=3, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Shield, skills.Packrat, skills.InstantDeath, skills.Fertility]), description='This animal would contain the idea of fire and danger The Shield skill would also help draw out that imagery, conjuring an air of both danger and protection around the creature Packrat is skillfull, because Hexfire could be seen as hoarding its symbolical fire, given that this card has relatively low spirit and fire costs, despite its power Black cats are often considered unlucky and hexed, making the fantasy creature\'s name befitting a very clever and dangerous animal'),
# Flametusk 🔰🪁🐭🧺💀 9p 10h
# costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 67
Blueprint(original=Card(name='Flametusk', power=9, health=10, costs_fire=2, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Shield, skills.Soaring, skills.Fertility, skills.Packrat, skills.InstantDeath]), description='This animal would be a fiery one, as it has a high fire cost and has Shield as well as Packrat skills The name implies it would be a strong animal, like an elephant, which is fitting with its high power and health The Flame part of its name adds to that, but \"tusk\" hints that it has some sort of physical defense with its tusks, fitting with the Shield ability Soaring skill could work well with that as it implies it is a large and heavy creature that can only fly for a short amount of time'),
# Soulwing 🪁🔰💀 3p 5h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻 pot: 43
Blueprint(original=Card(name='Soulwing', power=3, health=5, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=5, skills=[skills.Soaring, skills.Shield, skills.InstantDeath]), description='related to the high spirits and has fire attributes, also the skill Soaring'),
# FertilityBat 🐭💀 4p 4h
# costs: 🔥🔥 has: 🔥 pot: 27
Blueprint(original=Card(name='FertilityBat', power=4, health=4, costs_fire=2, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility, skills.InstantDeath]), description='relates to the Fertility skill, also has fire attribute'),
# Hoarderhorn 🔰💀🧺🐭 4p 6h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻 pot: 49
Blueprint(original=Card(name='Hoarderhorn', power=4, health=6, costs_fire=1, costs_spirits=0, has_spirits=3, has_fire=5, skills=[skills.Shield, skills.InstantDeath, skills.Packrat, skills.Fertility]), description='relates to the Packrat skill, has both fire and spirits attributes, also has Shield skill'),
# Packleader 🧺🐭🔰 3p 7h
# costs: 🔥 has: 🔥🔥🔥👻👻👻👻👻 pot: 42
Blueprint(original=Card(name='Packleader', power=3, health=7, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=3, skills=[skills.Packrat, skills.Fertility, skills.Shield]), description='relates to Packrat and Fertility skills, and has high health, spirits and Packrat skill'),
# Spikebackula 🧺🔰🐭💀🦔🪁 7p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 73
Blueprint(original=Card(name='Spikebackula', power=7, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Packrat, skills.Shield, skills.Fertility, skills.InstantDeath, skills.Spines, skills.Soaring]), description='relates to the Spines skill and high power, health, spirits, and fire attributes'),
# Homunculus 🧺 2p 1h
# costs: 🔥🔥🔥 has: 🔥👻 pot: 9
Blueprint(original=Card(name='Homunculus', power=2, health=1, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Packrat]), description='A miniature, artificially created humanoid, representing the low health and cost of the card The skill Packrat, implying a hoarder or collector, fits with the idea of a crafted creature collecting and keeping things'),
# Pyrothorax 🐭🔰💀🧺 6p 4h
# costs: 🔥🔥 has: 🔥🔥🔥👻👻👻 pot: 46
Blueprint(original=Card(name='Pyrothorax', power=6, health=4, costs_fire=2, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Fertility, skills.Shield, skills.InstantDeath, skills.Packrat]), description='A creature that combines a fiery nature being associated with the element fire, with a high power and spirit cost, but also quite strong in the presence of spirits or fire Shield, Fertility, and Packrat fit the idea of a creature that hoards and protects valuable resources, like burning embers or flammable materials Instant Death, however, implies a quick end, which could work with the idea that a burning creature doesn\'t last long if extinguished'),
# Dreamhare  2p 2h
# costs: 🔥🔥 has: 👻 pot: 6
Blueprint(original=Card(name='Dreamhare', power=2, health=2, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=0, skills=[]), description='balanced, fantastical, fits with other fantastical animal names in game'),
# Soarhawk 🧺🪁🐭🔰💀 6p 8h
# costs: - has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 68
Blueprint(original=Card(name='Soarhawk', power=6, health=8, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=4, skills=[skills.Packrat, skills.Soaring, skills.Fertility, skills.Shield, skills.InstantDeath]), description='high spirits, strong fire, flying skills'),
# Krakenix 🦔🧺🔰🐩🐭💀 9p 7h
# costs: - has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻 pot: 78
Blueprint(original=Card(name='Krakenix', power=9, health=7, costs_fire=0, costs_spirits=0, has_spirits=6, has_fire=6, skills=[skills.Spines, skills.Packrat, skills.Shield, skills.Underdog, skills.Fertility, skills.InstantDeath]), description='skillful, balanced, aquatic'),
# Runebull 🧺🐭🔰💀🦔🐩 10p 10h
# costs: 🔥 has: 🔥🔥🔥🔥🔥🔥👻👻👻👻👻👻👻 pot: 77
Blueprint(original=Card(name='Runebull', power=10, health=10, costs_fire=1, costs_spirits=0, has_spirits=7, has_fire=6, skills=[skills.Packrat, skills.Fertility, skills.Shield, skills.InstantDeath, skills.Spines, skills.Underdog]), description='strong, earthy, skilled'),
# Flamebugle 🔰🧺🦔🐭 8p 6h
# costs: - has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 64
Blueprint(original=Card(name='Flamebugle', power=8, health=6, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Shield, skills.Packrat, skills.Spines, skills.Fertility]), description='firerelated, shielded, low costs'),
# Mysticcat 🐭💀 2p 7h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻 pot: 34
Blueprint(original=Card(name='Mysticcat', power=2, health=7, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=4, skills=[skills.Fertility, skills.InstantDeath]), description='high health, wellbalanced stats, instant death and fertility skills'),
# Ghostlynx 🐭 6p 3h
# costs: 🔥 has: 🔥 pot: 23
Blueprint(original=Card(name='Ghostlynx', power=6, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Fertility]), description='high power, low health, strong fertility skill'),
# Stormdrake 💀🪁 10p 8h
# costs: 🔥 has: 🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Stormdrake', power=10, health=8, costs_fire=1, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.InstantDeath, skills.Soaring]), description='very high power and health, moderate cost, instant death and soaring skills'),
# Gorgontail 🦔💀🔰🍀🪁 5p 10h
# costs: - has: 🔥🔥🔥👻👻👻 pot: 57
Blueprint(original=Card(name='Gorgontail', power=5, health=10, costs_fire=0, costs_spirits=0, has_spirits=3, has_fire=3, skills=[skills.Spines, skills.InstantDeath, skills.Shield, skills.LuckyStrike, skills.Soaring]), description='very high health, multiple skills including spines and shields'),
# Quickarmad  2p 10h
# costs: 🔥 has: 🔥👻 pot: 21
Blueprint(original=Card(name='Quickarmad', power=2, health=10, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[]), description='high health, low power, no skills'),
# Stingersaur 🦔 4p 5h
# costs: - has: 🔥👻👻👻👻👻 pot: 32
Blueprint(original=Card(name='Stingersaur', power=4, health=5, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=1, skills=[skills.Spines]), description='With high power and health and the Spines skill, this card\'s name relates to its deadly nature, evoking the image of a dinosaur with sharp, poisonous spines'),
# Firebirdie 🐭🦔 2p 9h
# costs: - has: 🔥🔥👻👻 pot: 42
Blueprint(original=Card(name='Firebirdie', power=2, health=9, costs_fire=0, costs_spirits=0, has_spirits=2, has_fire=2, skills=[skills.Fertility, skills.Spines]), description='This card has balanced attributes, both for spirits and fire, and the Fertility and Spines skills The name invokes the idea of a small but potent bird, with flaming feathers and spiky defense mechanisms'),
# Shieldratle 🔰🧺🦔 1p 4h
# costs: - has: 🔥 pot: 32
Blueprint(original=Card(name='Shieldratle', power=1, health=4, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=1, skills=[skills.Shield, skills.Packrat, skills.Spines]), description='With low spirits but spiky skills, this card evokes the image of a small, tough rodent with an armadillolike defense mechanism The name hints at both its spines and its shielding ability'),
# Fertilebear 🔰🐭🦔 7p 3h
# costs: 🔥 has: 🔥🔥👻👻👻👻👻 pot: 39
Blueprint(original=Card(name='Fertilebear', power=7, health=3, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=2, skills=[skills.Shield, skills.Fertility, skills.Spines]), description='With high spirits and fire costs, this card is both strong and expensive Its name references not only its fertility skill but also its strength and bearlike attributes'),
# Infernodillo 🐩🐭🔰 3p 5h
# costs: 🔥🔥🔥 has: - pot: 28
Blueprint(original=Card(name='Infernodillo', power=3, health=5, costs_fire=3, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Underdog, skills.Fertility, skills.Shield]), description='This card is quite balanced overall, with a focus on fire costs and the Underdog skill Its name evokes the image of an armored armadillo that can withstand intense heat and fire, fitting for a card with these kinds of attributes'),
# Faeox 🐭 7p 3h
# costs: 🔥 has: 🔥👻 pot: 26
Blueprint(original=Card(name='Faeox', power=7, health=3, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Fertility]), description='This name suggests a supernatural creature that is both beautiful and mysterious, fitting for a card with moderate power and low health values The relatively low fire cost only  and high spirit cost reflect the Faeox\'s mystical nature, and their sole skill of Fertility hints at their ability to bring magical life to any situation'),
# Deathwhale 🧺🐭💀 8p 8h
# costs: - has: 🔥🔥🔥👻👻👻👻👻 pot: 63
Blueprint(original=Card(name='Deathwhale', power=8, health=8, costs_fire=0, costs_spirits=0, has_spirits=5, has_fire=3, skills=[skills.Packrat, skills.Fertility, skills.InstantDeath]), description='very strong, very expensive, even though it has no fire or spirit powers, it\'s highly spirited, it\'s pack rat, fertility, and instant death skills give it a dangerous edge'),
# Fireborn 🧺🐭💀🔰🐩🦔 7p 10h
# costs: 🔥🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻 pot: 68
Blueprint(original=Card(name='Fireborn', power=7, health=10, costs_fire=2, costs_spirits=0, has_spirits=5, has_fire=5, skills=[skills.Packrat, skills.Fertility, skills.InstantDeath, skills.Shield, skills.Underdog, skills.Spines]), description='strong, wellrounded, especially useful against underdog skills, and with great health, even though it\'s quite expensive'),
# Shieldhog 🔰🐭💀🧺 6p 9h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻 pot: 57
Blueprint(original=Card(name='Shieldhog', power=6, health=9, costs_fire=1, costs_spirits=0, has_spirits=4, has_fire=4, skills=[skills.Shield, skills.Fertility, skills.InstantDeath, skills.Packrat]), description='exceptionally good defense, OK offense, low cost, and with good health, armored with shield, instant death, and packrat skills, making it useful in a lot of situations'),
# Embermoose 🐭💀 7p 4h
# costs: 👻 has: 👻 pot: 33
Blueprint(original=Card(name='Embermoose', power=7, health=4, costs_fire=0, costs_spirits=1, has_spirits=1, has_fire=0, skills=[skills.Fertility, skills.InstantDeath]), description='high power, low spirit, low cost, with fertility and instant death skills, good for early play and against deck builders'),
# Shadowbear 💀🐭🧺🔰 8p 8h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻 pot: 60
Blueprint(original=Card(name='Shadowbear', power=8, health=8, costs_fire=1, costs_spirits=0, has_spirits=5, has_fire=4, skills=[skills.InstantDeath, skills.Fertility, skills.Packrat, skills.Shield]), description='This card has high power and health, but also high costs in fire and spirits The skills InstantDeath and Shield suggest a bear that is hard to take down, perhaps even a little menacing The name \"Shadowbear\" relates to this by suggesting a bear that lurks in the shadows, ready to pounce on its prey'),
# Rainguard 🧺🔰🐭 2p 3h
# costs: 🔥 has: - pot: 27
Blueprint(original=Card(name='Rainguard', power=2, health=3, costs_fire=1, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Packrat, skills.Shield, skills.Fertility]), description='With moderate power and health, no fire or spirit cost, and skills like Packrat and Shield, this card seems like a protector The name \"Rainguard\" relates to this by suggesting a creature that shields and protects others from the elements'),
# Nightdrake 🐭🔰🧺💀 8p 9h
# costs: 🔥 has: 🔥🔥🔥🔥👻👻👻👻👻👻 pot: 63
Blueprint(original=Card(name='Nightdrake', power=8, health=9, costs_fire=1, costs_spirits=0, has_spirits=6, has_fire=4, skills=[skills.Fertility, skills.Shield, skills.Packrat, skills.InstantDeath]), description='A card with high power, high health, and skills like Fertility and Packrat suggests a dragonlike creature The name \"Nightdrake\" relates to this by suggesting a fierce dragon that hunts in the darkness'),
# Dirtmole 🧺 5p 2h
# costs: - has: - pot: 26
Blueprint(original=Card(name='Dirtmole', power=5, health=2, costs_fire=0, costs_spirits=0, has_spirits=0, has_fire=0, skills=[skills.Packrat]), description='With low power, moderate health, and only packrat skills, this card seems like a simple mole that burrows underground The name \"Dirtmole\" relates to this by suggesting a creature that lives and thrives in dirt and tunnels'),
# Blazebug 🧺💀🐭🔰🪁 10p 9h
# costs: 🔥 has: 🔥🔥🔥🔥🔥👻👻👻👻👻👻👻👻 pot: 71
Blueprint(original=Card(name='Blazebug', power=10, health=9, costs_fire=1, costs_spirits=0, has_spirits=8, has_fire=5, skills=[skills.Packrat, skills.InstantDeath, skills.Fertility, skills.Shield, skills.Soaring]), description='This card has high power and health, as well as skills like InstantDeath and Shield, suggesting a creature that is hard to bring down The high fire cost and the name \"Blazebug\" both relate to this by suggesting a creature that is hot and fiery, and perhaps even explosive'),
]
