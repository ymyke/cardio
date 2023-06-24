"""Skills

Checklist when adding a new skill:

- Implement its logic. There are 3 implenetation styles:
  - Fully self-contained ⭐: The skill is implemented in its own class and only uses
    hooks from the base class `Skill`. Example: Regenerate. -- This is the preferred
    style.
  - Fully dependent: The skill is implemented with specific code in `FightCard` and/or
    `FightVnC`. The skill class serves only as a container for the skill's basic
    attributes. Examples: InstantDeath, Fertility, Spines, Soaring, Airdefense.
  - Hybrid: The skill uses specific code outside its class but also some logic in the
    class (as well as maybe some state to be tracked). Examples: LuckyStrike, Shield,
    Weakness. 
- Check for possible interdependencies with other skills and address those in the code
  accordingly.
- Add tests for skill and all interdependencies.
- Does the skill add any kind of state to the card (or other cards or other parts of the
  world) that would need to be set or reset in any of the hooks (e.g., `pre_attack`
  etc.)?
- Any new hooks needed? (E.g., because the skill needs to be (re)set at other points in
  time such as before or after preparing a card.)
- Does the skill need any new view animation that needs to be implemented and called?
- Anything that needs to be saved in the game state (i.e., module `jason`)?
- Create new blueprints with this skill and add them to the catalog. (Use the
  `fix_skill` variable in `gen_skills`. Generate an amount of blueprints with that skill
  that is reasonable in the overall catalog, cf `blueprint_stats.ipynb`.)
"""
from __future__ import annotations
from typing import List, Optional, Type, Union, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
import logging
import random

if TYPE_CHECKING:
    from cardio import FightCard


# QQ: Better implement this simply as a directory of names with specs and a factory?


class ForWhom(Enum):
    """Who can use a skill?"""

    HUMAN = auto()
    COMPUTER = auto()
    BOTH = auto()


@dataclass
class Skill:
    """Skill base class.

    Skills can have hooks that will be called at certain points in time during the
    fight. Examples: `pre_attack`, `post_round`, etc. Hooks will be called with a
    `carrier` argument, which is the card that has the skill. This hook can be used to
    access the card's attributes. (Or if necessary to access the fight state, the grid,
    or other objects/information.)
    """

    name: str
    symbol: str
    description: str
    potency: int  # [-10, 10], usually [0, 10]
    forwhom: ForWhom = ForWhom.BOTH

    def __post_init__(self) -> None:
        self.pre_fight(None)
        # TODO ^ Not nice. Why not get rid of this and use post_init where necessary?

    def pre_fight(self, carrier: FightCard) -> None:
        """Called before the fight starts. Use this to set up a pristine state in skills
        that have state.
        """
        pass

    def pre_attack(self, carrier: FightCard) -> None:
        pass

    def post_attack(self, carrier: FightCard) -> None:
        pass

    def post_round(self, carrier: FightCard) -> None:
        """Called after each round of fight, iff the card is still alive."""
        pass


SkillType = Type[Skill]
SkillOrSkillType = Union[Skill, SkillType]
ListOfSkillsOrSkillTypes = List[SkillOrSkillType]


def get_skilltypes() -> List[SkillType]:
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

    def copy(self) -> SkillSet:
        return SkillSet(self.get_types())

    def call(self, method_name: str, *args, **kwargs):
        """Call a method on all skills. E.g., `skillset.call('pre_fight')`."""
        for skill in self.skills:
            getattr(skill, method_name)(*args, **kwargs)

    def __repr__(self) -> str:
        return f"SkillSet({self.skills})"

    def __iter__(self):
        return iter(self.skills)

    def __contains__(self, skill):
        return self.has(skill)

    def __eq__(self, other: SkillSet) -> bool:
        return isinstance(other, SkillSet) and (
            set(self.get_types()) == set(other.get_types())
        )


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
    forwhom: ForWhom = ForWhom.HUMAN


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
    name: str = "Shield"
    symbol: str = "🔰"  # 🛡️ (doesn't work in asciimatics)
    description: str = (
        "The Shield on a card absorbs 1 (the first) damage the card receives per turn."
        # (OR: The first x damage per fight. OR: All damage of the first damage dealt.)
    )
    potency: int = 7
    # Keep track of which turn the shield was used in:
    _turns_used: List[int] = field(default_factory=list)

    def pre_fight(self, carrier: FightCard):
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
    description: str = "A card with Underdog gains +1 power when opposed by a card with higher power. A card with power 0 will also gain 1 power and start attacking when it has Underdog."
    potency: int = 5
    # (QQ: Underdog (and maybe some other skills) could also be implemented by
    # implementing a power property on FightCard that returns the power after applying
    # all skill-related modifiers.)


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

    def is_lucky(self) -> bool:
        assert self._is_lucky is not None
        return self._is_lucky

    def pre_attack(self, carrier: FightCard) -> None:
        self._is_lucky = random.random() <= 0.5
        logging.debug("% is lucky: %s", self.name, self._is_lucky)

    def post_attack(self, carrier: FightCard) -> None:
        self._is_lucky = None

    def power_up_against_agent(self, power: int) -> int:
        assert self.is_lucky()
        return power * 2


@dataclass
class Regenerate(Skill):
    name: str = "Regenerate"
    symbol: str = "🩹"
    description: str = (
        "A card with Regenerate will heal 1 damage at the end of each fight round."
    )
    potency: int = 5

    def post_round(self, carrier: FightCard) -> None:
        carrier.heal_damage(1)
        logging.debug("%s heals 1D", self.name)


@dataclass
class Weakness(Skill):
    name: str = "Weakness"
    symbol: str = "🤕"
    description: str = "A card with Weakness will deal 1 less damage when it attacks."
    potency: int = -4

    def modify_damage(self, damage: int) -> int:
        return max(damage - 1, 0)


# ----- Sanity checks -----

assert all(abs(cls.potency) <= 10 for cls in get_skilltypes())
