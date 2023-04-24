"""Skills

Checklist when adding a new skill:
- Implement its logic in `Card` (and elsewhere, if necessary).
- Check for possible interdependencies with other skills and address those in the code
  accordingly.
- Add tests for skill and all interdependencies.
- Does the skill add any kind of state to the card (or other cards or other parts of the
  world) that would need to be reset (e.g., in `Card.reset`)?
- Does the skill need any new view animation that needs to be implemented and called?
- Anything that needs to be saved?
"""
from dataclasses import dataclass
from enum import Enum
from typing import List

# QQ: Maybe use a subclass such as TemporarySkill to implement things like temporary
# buffs like the power buff thanks to the Leader skill.

# FIXME: Should certain or all (or none?) skills be stackable? What does that mean?
# where does it make sense?


@dataclass(frozen=True)
class SkillSpec:
    name: str
    symbol: str
    description: str
    potency: int  # [-10, 10], usually [0, 10]


class Skill(Enum):
    INSTANTDEATH = SkillSpec(
        name="Instant Death",
        symbol="💀",
        description="A card with Instant Death will instantly kill any card it damages. If the attack strikes the opponent directly, the skill has no effect, and the attack will deal damage according to its power. If a card has 0 power, it will not attack, and this skill will have no effect.",
        potency=7,
        # QQ: Alternative names: One-Shot🎯, Killer Instinct, Exterminator, Terminator
    )
    FERTILITY = SkillSpec(
        name="Fertility",
        symbol="🐭",
        description="A fertile card creates a copy of itself in your hand when it is played.",
        potency=9,
        # FIXME: Maybe FERTILITY only makes sense for cards that use spirits as costs?
        # Or that cost more than 1 fire? Otherwise you can create infinite spirits with
        # them? OR: The cards go to the draw deck instead of the hand? QQ: Should copies
        # of this lose their fertility skill? OR: Cards with fertility do not produce
        # spirits, no matter what.
        # QQ: BTW, for such restrictions, we could use a "restriction" attribute/function here
        # that gets the card and evaluates whether the skill can be added or not.
    )
    SOARING = SkillSpec(
        name="Soaring",
        symbol="🪁",
        description="A Soaring card will ignore opposing cards and strike an opponent directly.",
        potency=2,
        # Or: Jump 🐇
    )
    SPINES = SkillSpec(
        name="Spines",
        symbol="🦔",
        description="After a card with Spines is attacked, the attacker receives 1 damage.",
        potency=3,
    )
    AIRDEFENSE = SkillSpec(
        name="Air Defense",
        symbol="🚀",
        description="A card with Air Defense will block attacks from Soaring cards.",
        potency=1,
        # QQ: Maybe REACHHIGH instead of AIRDEFENSE? With an arm symbol? Or
        # LONGNECK/HEADHIGH/... and the girafe emoji? Or: Sky Shield? ☁️
    )


SkillList = List[Skill]

# Sanity check:
assert all(s.value.potency >= 0 and s.value.potency <= 10 for s in Skill)


# ----- Ideas for more skills -----

# ----- High prio -----

# - Healing / Regeneration 💉 -- Itself or others around it? A card with Regeneration
#   will heal 1 damage at the end of each turn.
# - Shield 🛡️ -- Blocks the first attack? Or absorbs 1 damage per attack? Or absorbs
#   the first x damage?
# - Berserk 💢 -- A card with Berserk gains increased strength when it has taken damage.
# - Underdog 🐩 -- A card with Underdog gains additional strength when fighting against
#   cards with higher power.
# - Mixer 🔀 -- A card with Mixer swaps one random card from your hand with another one
#   from your draw deck. (Maybe also gives me an additional hamster?)
# - Persevering / Final Blow 💥 -- Hits one more time in dying.
# - Quick ⚡ / Double strike -- Attacks twice.
# - Bloodless / Pale/ Inert / Extinguished 🧯 -- Will not provide any fire or spirits
#   (has_*). That also means the card cannot be sacrificed.
# - Overload 🔌 -- A card with Overload will deal 1 damage to itself when it attacks.
# - Weakness 🤕 -- A card with Weakness will deal 1 less damage when it attacks.
# - Bully 🤼 -- A card with Bully will always attack the weakest opponent (in the entire
#   row or opponent + 2 neighbors).
# - Hoarder -- Draw another card when this card is played.
# - Longrange 🏹 -- A card with Longrange will attack the prep line card instead of the
#   front line card.
# - Trample – A card with Trample will deal the equal amount of damage to the computer
#   player as it deals to the opposing card.
# - Lucky Strike 🍀 -- Either kills the opponent or deals 1 damage to itself.
# - Annihilator 💔 -- Destroys a card for good. Not just for this fight but for the
#   entire game. (Only makes sense against the human player maybe?)
# - Vulnerable 🎯 -- A card with Vulnerable takes increased damage from attacks.
# - Wither 💀 -- A card with Wither deals damage to itself at the end of each turn.
# - Amnesiac 🤔 -- A card with Amnesiac will forget all its other skills.
# - Inhibit 🚧 -- A card with Inhibit will disable all skills of the opponent's card.


# ----- Medium prio -----

# - Confused 😵 -- A card with Confused will occasionally attack its own allies instead
#   of the opponent.
# - Pregnant -- One-time (per fight) fertility?
# - Firefighter 🚒🧯🧑‍🚒 -- A card with Firefighter will reduce its neighbors' fire to
#   0.
# - Parry -- A card with Parry has a chance to deflect an opponent's attack back at
#   them.
# - Drain 💉 -- A card with Drain can steal health from an opponent's cards.
# - Eternal / Persistent / Resilient -- A card with Persistent will be returned to its
#   owner's deck when it dies.
# - Echolot 🔍 -- Pick a specific card from the deck.
# - Summon 🤝 -- A card with Summon can bring other cards from your deck into play.
# - Yell 🗣️ -- A card with Yell will deal 1 more damage when it attacks.
# - Poisonous 🐍💊 / Noxious 🌿 -- Opponent (player or card?) gets poisoned and loses 1
#   health each round.
# - Radiant 🌞 -- A card with Radiant creates 1 more spirit each time it gets brought
#   into play.
# - Glutton 🍔 or Insatiable 🍕 -- A card with Glutton becomes 1 unit more costly each
#   time it gets brought into play.
# - Slow 🐢 -- A card with Slow will attack only every other round.
# - Slow II -- A card with Slow II will attack at the end of the round instead of at its
#   usual turn. (Can be both an advantage or a disadvantage for the human.)
# - Stun 🥊 -- A card with Stun will stun an attacked card with a successful attack. A
#   stunned card will not attack next round.
# - Leader 👑 -- A card with Leader can buff other cards.
# - Recruit 👥 -- Recruit one of the opponent's cards that you killed at the end of the
#   fight.


# ----- Low prio and/or high complexity -----

# - Corbeaux / Corvus Corax -- Can consume spirits and release them as fire.
# - Viral -- Like poisonous, but spreads?
# - Crazy -– A card with Crazy randomly attacks either the opponent's cards or the
#   player's own cards, creating unpredictable and potentially chaotic gameplay.
# - Wildcard 🃏 -- In each round, gets a random skill from the list of all skills.
# - Blowfish 💣 -- A card with Blowfish can explode, dealing damage to opponent and its
#   2 neighbors. Or to opponent and its prep line. But then it dies.
# - Confuse 😵 -- A card with Confuse can confuse an opponent's cards, causing them to
#   attack each other.
# - Hunter / Kidnapper -- A card with Hunter will grab the opposing card to the player's
#   side (for the duration of the fight), pushing the Hunter-card to the prep line
#   (computer) or the player's (human) hand.
# - Bloodsucker 🩸 -- A card with Bloodsucker will have comparatively high fire cost but
#   can use opponent's cards as well for sacrifice.
# - "Allesfresser" -- can use fire _or_ spirit (or a mix) to be placed.
# - Hotblooded -- Can be played at any time. (Doesn't really fit the basic gameplay
#   model but might be a fun "real-time" element where you either press a key in time to
#   interrupt the game flow or you missed it.)
