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
    under_construction: bool = False


# TODO Which skills will need some state and how will we save that state? Need to have
# some skill representation that is not frozen? Maybe some skills are subclasses of
# SkillSpec?

# FIXME Need more skills in the 1-4 range.


class Skill(Enum):
    INSTANTDEATH = SkillSpec(
        name="Instant Death",
        symbol="💀",
        description="A card with Instant Death will instantly kill any card it damages. If the attack strikes the opposing agent directly, the skill has no effect, and the attack will deal damage according to its power. If a card has 0 power, it will not attack, and this skill will have no effect.",
        potency=7,
        # QQ: Alternative names: One-Shot🎯, Killer Instinct, Exterminator, Terminator
        # FIXME What if the attack is blocked, e.g. by a shield? I think they can't be
        # blocked. (Maybe the shield gets destroyed?)
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
        # that gets the card and evaluates whether the skill can be added or not. [1]
    )
    SOARING = SkillSpec(
        name="Soaring",
        symbol="🪁",
        description="A Soaring card will ignore opposing cards and strike an opponent directly.",
        potency=2,
        # Or: Jump 🐇🦘
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
    INHIBIT = SkillSpec(
        # FIXME This is not easy. Maybe need some kind of precondition filter code that
        # gets executed for each skill? See also [1] above -> Skills would have an
        # assign-filter and an activate-filter. The activate-filter for INHIBIT would
        # not be with the INHIBIT skill but with EVERY skill.
        # QQ: What if INHIBIT and INHIBIT oppose each other?
        name="Inhibit",
        symbol="🚧",
        description="A card with Inhibit will disable all skills of the opposing card.",
        potency=2,
        under_construction=True,
    )
    AMNESIA = SkillSpec(
        name="Amnesia",
        symbol="🤷‍♂️",
        description="A card with Amnesia will forget all its other skills. They remain on the card, but they will not be activated as long as Amnesia is on the card.",
        potency=-3,
        under_construction=True,
        # Similar to INHIBIT. See notes there.
    )
    FRAGILE = SkillSpec(
        name="Fragile",
        symbol="🥚",
        description="A card with Fragile takes 1 more damage from every successful (e.g., non-blocked) attack by an opponent.",
        potency=-4,
        under_construction=True,
        # FIXME Make sure this works properly once we have a way to block attacks, shields
        # etc. ⭐
    )
    LUCKYSTRIKE = SkillSpec(
        name="Lucky Strike",
        symbol="🍀",
        description="A card with Lucky Strike has a 50-50 chance to either kill the opponent or the card itself instantly. If the attack strikes the opposing agent directly, the skill has no effect, and the attack will deal damage according to its power. If a card has 0 power, it will not attack, and this skill will have no effect.",
        potency=0,
        under_construction=True,
        # QQ: What if the attack is blocked, e.g. by a shield? I think they can't be
        # blocked. (Maybe the shield gets destroyed?)
    )
    TRAMPLE = SkillSpec(
        name="Trample",
        symbol="🦏",
        description="A card with Trample will deal the equal amount of damage to the opposing player as it deals to the opposing card.",
        potency=7,
        under_construction=True,
    )
    REGENERATE = SkillSpec(
        name="Regenerate",
        symbol="🩹",  # 💊🌡️
        description="A card with Regenerate will heal 1 damage at the end of each turn.",
        potency=5,
        under_construction=True,
        # ⭐
    )
    HEALER = SkillSpec(
        name="Healer",  # Medic?
        symbol="🚑",  # 🩺⚕️
        description="A card with Healer will heal 1 damage of its neighboring cards at the end of each turn.",
        potency=6,
        under_construction=True,
        # ⭐
    )
    UNDERDOG = SkillSpec(
        name="Underdog",
        symbol="🐩",
        description="A card with Underdog gains additional strength when opposed by a card with higher power.",
        potency=4,
        under_construction=True,
        # ⭐
    )
    OVERLOAD = SkillSpec(
        name="Overload",
        symbol="🔌",  # 🔋
        description="A card with Overload will deal 1 damage to itself when it attacks.",
        potency=-5,
        under_construction=True,
        # ⭐
        # Maybe there will be ways to prevent cards from attacking in a turn (e.g.,
        # through an item?), in which case this skill would become more strategic and
        # controllable by the player.
    )
    WEAKNESS = SkillSpec(
        name="Weakness",
        symbol="🤕",
        description="A card with Weakness will deal 1 less damage when it attacks.",
        potency=-4,
        under_construction=True,
        # ⭐
        # TODO Is this the same as reducing its power by 1?
    )
    PACKRAT = SkillSpec(
        name="Packrat",
        symbol="🧺",
        description="A card with Packrat will draw another card to the player's hand when it is played.",
        potency=6,
        under_construction=True,
        # ⭐
        # FIXME This one is also only applicable to human player's cards. Should there
        # be a flag to differentiate the two types?
    )
    BULLY = SkillSpec(
        name="Bully",
        symbol="🥊",
        description="A card with Bully will always attack the weakest opposing card (in the entire row), but never its directly opposing card.",
        potency=6,
        under_construction=True,
    )
    EMPTY = SkillSpec(
        name="Empty",  # Bloodless / Pale / Inert / Extinguished 🧯
        symbol="📭",
        description="A card with Empty will not provide any fire or spirits. This also means the card cannot be sacrificed.",
        potency=-3,
        under_construction=True,
        # TODO What is the basic philosophy? a) A card with EMPTY keeps all its stats
        # (esp. has_*) and the code does special handling to check for cards with this
        # skill wherever appropriate (e.g., card placement). b) A card keeps its
        # _original_ stats and adjusts its stats as it gets (and loses, in which case
        # the original stats will be restored) a skill such as EMPTY. That way, the code
        # does not need to identify and handle special cases. -- Seems to me that a is
        # the more consistent approach that can apply to all skills. -- One way to make
        # things easier is to turn the attributes in the Card class into properties that
        # handle all these special cases such as EMPTY etc.
        #
        # → QQ: How many other skills are relevant to this question?
    )
    SHIELD = SkillSpec(
        name="Shield",
        symbol="🛡️",
        description="The Shield on a card absorbs 1 damage per attack the card receives.",
        potency=7,
        under_construction=True,
        # ⭐
        # FIXME Will be destroyed by INSTANTDEATH? And maybe LUCKYSTRIKE? If so, mention
        # in their descriptions.
    )
    DOUBLESTRIKE = SkillSpec(
        name="Double Strike",
        symbol="✌️",
        description="A card with Double Strike will attack twice. Afterwards, it will lose 1 power (for the rest of the fight).",
        potency=6,
        under_construction=True,
        # ⭐
    )
    FINALBLOW = SkillSpec(
        name="Final Blow",
        symbol="🏁",
        description="A card with Final Blow will attack one last time just before dying.",
        potency=6,
        under_construction=True,
    )
    BERSERK = SkillSpec(
        name="Berserk",
        symbol="🪓",
        description="A card with Berserk gains 1 power each time it is attacked (until the end of the fight).",
        potency=8,
        under_construction=True,
    )
    MIXER = SkillSpec(
        name="Mixer",
        symbol="🔀",
        description="When a card with Mixer is played, it swaps one random card from the player's hand with another one from the draw deck. In addition, the player draws a hamster card.",
        potency=0,
        under_construction=True,
        # FIXME humanonly
    )
    HAMSTERWHEEL = SkillSpec(
        name="Hamster Wheel",
        symbol="🎡",
        description="When a card with Hamster Wheel is played, it swaps one random card from the player's hand with another one from the draw deck (same as Mixer). In addition, the player draws a hamster card.",
        potency=5,
        under_construction=True,
        # FIXME humanonly
    )


SkillList = List[Skill]

# Sanity check:
assert all(abs(s.value.potency) <= 10 for s in Skill)


# ----- Ideas for more skills -----

# ----- High prio -----


# ----- Medium prio -----

# - Overrun 🏃‍♂️ -- A card with Overrun will apply surplus damage to the prep line card
#   instead of the opposing player. (Caveat: This would have no effect for computer
#   player cards.)
# - Longrange 🏹 -- A card with Longrange will attack the prep line card instead of the
#   front line card. (Caveat: Makes only sense for human player's cards.)
# - Rampage -- A card with Rampage will become stronger with every opponent it kills.
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
# - Terminator 🤖 -- Destroys a card for good. Not just for this fight but for the
#   entire game. (Only makes sense against the human player maybe?)


# ----- Low prio and/or high complexity and/or only applicable to human's cards -----

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
# - Wither 💀 -- A card with Wither deals damage to itself at the end of each turn. (Too
#   similar to Overload?)
