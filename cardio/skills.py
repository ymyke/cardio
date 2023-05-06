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
from dataclasses import dataclass, field
from enum import Enum, auto
import logging
import random
from typing import List, Optional, Type, Union


# TODO Implement this simply as a directory of names -> specs and a factory?


class ForWhom(Enum):
    """Who can use a skill?"""

    # TODO Use this where relevant
    HUMAN = auto()
    COMPUTER = auto()
    BOTH = auto()


@dataclass
class Skill:
    name: str
    symbol: str
    description: str
    potency: int  # [-10, 10], usually [0, 10]
    forwhom: ForWhom = ForWhom.BOTH
    under_construction: bool = False

    def reset(self) -> None:
        pass

    def pre_attack(self) -> None:
        pass

    def post_attack(self) -> None:
        pass


SkillType = Type[Skill]
SkillOrSkillType = Union[Skill, SkillType]
ListOfSkillsOrSkillTypes = List[SkillOrSkillType]


def get_skilltypes(implemented_only: bool = True) -> List[SkillType]:
    if implemented_only:
        return [s for s in Skill.__subclasses__() if not s.under_construction]
    return Skill.__subclasses__()


class SkillSet:
    """A collection of skills.

    All methods that take a skill are flexible in that they accept both a skill instance
    and a skill type (i.e., the class itself), hence the `SkillOrSkillType` type. So,
    e.g., both `a_skillist.add(Spines)` and `a_skillist.add(Spines())` are valid.
    """

    def __init__(self, skills: Optional[ListOfSkillsOrSkillTypes] = None) -> None:
        skills = skills or []
        self.skills: List[skill] = [s() if isinstance(s, type) else s for s in skills]  # type: ignore

    def has(self, skill: SkillOrSkillType) -> bool:
        return skill in self.skills or skill in [type(s) for s in self.skills]

    def get(self, skill: SkillOrSkillType) -> Skill:
        if skill in self.skills:
            assert isinstance(skill, Skill)
            return skill
        elif skill in [type(s) for s in self.skills]:
            return [s for s in self.skills if type(s) == skill][0]
        raise AttributeError(f"Skill {skill} not found in {self.skills}")

    def get_types(self) -> List[SkillType]:
        return [type(s) for s in self.skills]

    def count(self) -> int:
        return len(self.skills)

    def add(self, skill: SkillOrSkillType) -> None:
        assert not self.has(skill), "Skill stacking is not supported."
        # QQ: Should certain or all (or none?) skills be stackable? What does that mean?
        # where does it make sense?
        self.skills.append(skill() if isinstance(skill, type) else skill)  # type: ignore

    def remove(self, skill: SkillOrSkillType) -> None:
        assert self.has(skill)
        if isinstance(skill, type):
            self.skills = [s for s in self.skills if not isinstance(s, skill)]
        else:
            self.skills.remove(skill)

    def remove_all(self) -> None:
        self.skills = []

    def __repr__(self) -> str:
        return f"SkillSet({self.skills})"

    def __iter__(self):
        return iter(self.skills)

    def __contains__(self, skill):
        return self.has(skill)


# TODO Which skills will need some state and how will we save that state?

# FIXME Need more skills in the 1-4 range.


# ----- Individual skills -----


@dataclass
class InstantDeath(Skill):
    name: str = "Instant Death"
    symbol: str = "💀"
    description: str = "A card with Instant Death will instantly kill any card it damages. If the attack strikes the opposing agent directly, the skill has no effect, and the attack will deal damage according to its power. If a card has 0 power, it will not attack, and this skill will have no effect."
    potency: int = 7
    # QQ: Alternative names: One-Shot🎯, Killer Instinct, Exterminator, Terminator
    # FIXME What if the attack is blocked, e.g. by a shield? I think they can't be
    # blocked. (Maybe the shield gets destroyed?)


@dataclass
class Fertility(Skill):
    name: str = "Fertility"
    symbol: str = "🐭"
    description: str = (
        "A fertile card creates a copy of itself in your hand when it is played."
    )
    potency: int = 9
    # FIXME: Maybe FERTILITY only makes sense for cards that use spirits as costs? Or
    # that cost more than 1 fire? Otherwise you can create infinite spirits with them?
    # OR: The cards go to the draw deck instead of the hand? QQ: Should copies of this
    # lose their fertility skill? OR: Cards with fertility do not produce spirits, no
    # matter what.  TODO: This was a bug in how sacrifice works. Sacrificed cards must
    # not produce spirits.
    # QQ: BTW, for such restrictions, we could use a "restriction" attribute/function here
    # that gets the card and evaluates whether the skill can be added or not. [1]


@dataclass
class Soaring(Skill):
    name: str = "Soaring"
    symbol: str = "🪁"
    description: str = (
        "A Soaring card will ignore opposing cards and strike an opponent directly."
    )
    potency: int = 2
    # Or: Jump 🐇🦘


@dataclass
class Spines(Skill):
    name: str = "Spines"
    symbol: str = "🦔"
    description: str = (
        "After a card with Spines is attacked, the attacker receives 1 damage."
    )
    potency: int = 3


@dataclass
class Airdefense(Skill):
    name: str = "Air Defense"
    symbol: str = "🚀"
    description: str = "A card with Air Defense will block attacks from Soaring cards."
    potency: int = 1
    # QQ: Maybe REACHHIGH instead of AIRDEFENSE? With an arm symbol? Or
    # LONGNECK/HEADHIGH/... and the girafe emoji? Or: Sky Shield? ☁️


@dataclass
class Shield(Skill):
    # TODO Shields introduce deadlock potential!!
    name: str = "Shield"
    symbol: str = "🔰"  # 🛡️ (doesn't work in asciimatics)
    description: str = (
        "The Shield on a card absorbs 1 (the first) damage the card receives per turn."
        # (OR: The first x damage per fight. OR: All damage of the first damage dealt.)
    )
    potency: int = 7
    # Keep track of which turn the shield was used in:
    _turns_used: List[int] = field(default_factory=list)

    def reset(self):
        self._turns_used: List[int] = []

    def absorbed_damage(self, damage_left: int, fight_round: int) -> int:
        if damage_left == 0:
            logging.debug("%s absorbs 0D (no damage to absorb)", self.name)
            return 0
        if fight_round not in self._turns_used:
            self._turns_used.append(fight_round)
            logging.debug("%s absorbs 1D", self.name)
            return 1

        logging.debug("%s absorbs 0D (already used this turn)", self.name)
        return 0

    # QQ: Will a shield be destroyed by INSTANTDEATH? And maybe LUCKYSTRIKE? If so,
    # mention in their descriptions.


@dataclass
class Underdog(Skill):
    name: str = "Underdog"
    symbol: str = "🐩"
    description: str = "A card with Underdog gains additional strength when opposed by a card with higher power."
    potency: int = 4


@dataclass
class Packrat(Skill):
    name: str = "Packrat"
    symbol: str = "🧺"
    description: str = "A card with Packrat will draw another card to the player's hand when it is played."
    potency: int = 6
    forwhom: ForWhom = ForWhom.HUMAN


@dataclass
class LuckyStrike(Skill):
    name: str = "Lucky Strike"
    symbol: str = "🍀"
    description: str = "A card with Lucky Strike has a 50-50 chance to either kill the opponent or the card itself instantly. If the attack strikes the opposing agent directly and is lucky, it strikes with doubled power. If a card has 0 power, it will not attack, and this skill will have no effect. (Lucky Strike has precedence over Instant Death.)"
    potency: int = 0
    _is_lucky: Optional[bool] = False
    # QQ: What if the attack is blocked, e.g. by a shield? I think they can't be
    # blocked. (Maybe the shield gets destroyed?)
    # QQ: Or maybe better: 1/3 chance to kill the opponent, 1/3 chance to kill itself,
    # 1/3 chance to attack as usual.

    def is_lucky(self) -> bool:
        assert self._is_lucky is not None
        return self._is_lucky

    def pre_attack(self) -> None:
        self._is_lucky = random.random() <= 0.5
        logging.debug("% is lucky: %s", self.name, self._is_lucky)

    def post_attack(self) -> None:
        self._is_lucky = None

    def power_up_against_agent(self, power: int) -> int:
        assert self.is_lucky()
        return power * 2


# ----- Under construction -----


@dataclass
class Inhibit(Skill):
    # FIXME This is not easy. Maybe need some kind of precondition filter code that
    # gets executed for each skill? See also [1] above -> Skills would have an
    # assign-filter and an activate-filter. The activate-filter for INHIBIT would
    # not be with the INHIBIT skill but with EVERY skill.
    # QQ: What if INHIBIT and INHIBIT oppose each other?
    name: str = "Inhibit"
    symbol: str = "🚧"
    description: str = (
        "A card with Inhibit will disable all skills of the opposing card."
    )
    potency: int = 2
    under_construction: bool = True


@dataclass
class Amnesia(Skill):
    name: str = "Amnesia"
    symbol: str = "🤷‍♂️"
    description: str = "A card with Amnesia will forget all its other skills. They remain on the card, but they will not be activated as long as Amnesia is on the card."
    potency: int = -3
    under_construction: bool = True
    # Similar to INHIBIT. See notes there.


@dataclass
class Fragile(Skill):
    name: str = "Fragile"
    symbol: str = "🥚"
    description: str = "A card with Fragile takes 1 more damage from every successful (e.g., non-blocked) attack by an opponent."
    potency: int = -4
    under_construction: bool = True
    # FIXME Make sure this works properly once we have a way to block attacks, shields
    # etc. ⭐


@dataclass
class Trample(Skill):
    name: str = "Trample"
    symbol: str = "🦏"
    description: str = "A card with Trample will deal the equal amount of damage to the opposing player as it deals to the opposing card."
    potency: int = 7
    under_construction: bool = True


@dataclass
class Regenerate(Skill):
    name: str = "Regenerate"
    symbol: str = "🩹"
    description: str = (
        "A card with Regenerate will heal 1 damage at the end of each turn."
    )
    potency: int = 5
    under_construction: bool = True
    # ⭐


@dataclass
class Healer(Skill):
    name: str = "Healer"  # Medic
    symbol: str = "🚑"
    description: str = "A card with Healer will heal 1 damage of its neighboring cards at the end of each turn."
    potency: int = 6
    under_construction: bool = True
    # ⭐


@dataclass
class Overload(Skill):
    name: str = "Overload"
    symbol: str = "🔌"  # 🔋
    description: str = (
        "A card with Overload will deal 1 damage to itself when it attacks."
    )
    potency: int = -5
    under_construction: bool = True
    # ⭐
    # Maybe there will be ways to prevent cards from attacking in a turn (e.g.,
    # through an item?), in which case this skill would become more strategic and
    # controllable by the player.


@dataclass
class Weakness(Skill):
    name: str = "Weakness"
    symbol: str = "🤕"
    description: str = "A card with Weakness will deal 1 less damage when it attacks."
    potency: int = -4
    under_construction: bool = True
    # ⭐
    # TODO Is this the same as reducing its power by 1?


@dataclass
class Bully(Skill):
    name: str = "Bully"
    symbol: str = "🥊"
    description: str = "A card with Bully will always attack the weakest opposing card (in the entire row), but never its directly opposing card."
    potency: int = 6
    under_construction: bool = True


@dataclass
class Empty(Skill):
    name: str = "Empty"  # Bloodless / Pale / Inert / Extinguished
    symbol: str = "📭"
    description: str = "A card with Empty will not provide any fire or spirits. This also means the card cannot be sacrificed."
    potency: int = -3
    under_construction: bool = True
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


@dataclass
class Doublestrike(Skill):
    name: str = "Double Strike"
    symbol: str = "✌️"
    description: str = "A card with Double Strike will attack twice. Afterwards, it will lose 1 power (for the rest of the fight)."
    potency: int = 6
    under_construction: bool = True
    # ⭐


@dataclass
class Finalblow(Skill):
    name: str = "Final Blow"
    symbol: str = "🏁"
    description: str = (
        "A card with Final Blow will attack one last time just before dying."
    )
    potency: int = 6
    under_construction: bool = True


@dataclass
class Berserk(Skill):
    name: str = "Berserk"
    symbol: str = "🪓"
    description: str = "A card with Berserk gains 1 power each time it is attacked (until the end of the fight)."
    potency: int = 8
    under_construction: bool = True


@dataclass
class Mixer(Skill):
    name: str = "Mixer"
    symbol: str = "🔀"
    description: str = "When a card with Mixer is played, it swaps one random card from the player's hand with another one from the draw deck."
    potency: int = 0
    under_construction: bool = True
    # FIXME humanonly


@dataclass
class Hamsterwheel(Skill):
    name: str = "Hamster Wheel"
    symbol: str = "🎡"
    description: str = "When a card with Hamster Wheel is played, it swaps one random card from the player's hand with another one from the draw deck (same as Mixer). In addition, the player draws a hamster card."
    potency: int = 5
    under_construction: bool = True
    # FIXME humanonly


# ----- Sanity checks -----

assert all(abs(cls.potency) <= 10 for cls in get_skilltypes())


# ----- Ideas for more skills ----- High prio -----


# ----- Ideas for more skills ----- Medium prio -----

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


# ----- Ideas for more skills ----- Low prio -----
# (Low prio and/or high complexity and/or only applicable to human's cards)

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
