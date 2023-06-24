from __future__ import annotations
from typing import List, Literal, Optional, TYPE_CHECKING
import copy
from .skills import ListOfSkillsOrSkillTypes, SkillSet, ForWhom
from cardio.whichplayer import WhichPlayer

if TYPE_CHECKING:
    from .fightcard import FightCard


class Card:
    """Card class"""

    MAX_ATTR = 10  # Max value per attribute (power, health, ...)
    MAX_SKILLS = 6  # Max number of skills a card can have
    # FIXME ^ These are not enforced yet. Should be. Not only in the initializer but
    # whenever something changes to affect these values.

    _fc: FightCard

    def __init__(
        self,
        # Mandatory:
        name: str,
        power: int,  # 💪
        health: int,  # 💓
        costs_fire: int,  # How much fire 🔥 needed
        # Optional:
        skills: Optional[ListOfSkillsOrSkillTypes] = None,
        costs_spirits: int = 0,  # How many spirits 👻 needed
        has_spirits: int = 1,  # How many spirits this card generates upon death 👻
        has_fire: int = 1,  # How much fire this card is worth when sacrificed 🔥
    ) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.costs_fire = costs_fire
        self.skills = SkillSet(skills or [])
        self.costs_spirits = costs_spirits
        self.has_spirits = has_spirits
        self.has_fire = has_fire

        # Sanity checks:
        assert all(
            getattr(self, a) >= 0 for a in dir(self) if isinstance(a, int)
        ), "No negative numbers please"
        assert costs_fire * costs_spirits == 0, (
            "Either fire or spirit costs must be 0. "
            "Hybrids are not supported at this time."
            # (Will we ever have cards that can have both cost_fire and cost_spirits? If
            # so, would that be AND or OR? Note that such hybrids would add considerable
            # complexity to the UI, since the player would have to be able to choose how
            # much of either to use (unless specified algorithmically).)
        )

    def xname(self) -> str:
        skillstr = "".join(s.symbol for s in self.skills)
        skillstr += " " if skillstr else ""
        return f"{self.name} {skillstr}{self.power}p {self.health}h"

    def __str__(self) -> str:
        coststr = "🔥" * self.costs_fire + "👻" * self.costs_spirits
        hasstr = "🔥" * self.has_fire + "👻" * self.has_spirits
        s = self.xname() + "\n"
        s += f"costs: {coststr or '-'} has: {hasstr or '-'} "
        s += f"pot: {self.potency('human')}/{self.potency('computer')}"
        return s

    def __repr__(self) -> str:
        skillstr = ", ".join("skills." + t.__name__ for t in self.skills.get_types())
        return (
            f"Card(name='{self.name}', power={self.power}, health={self.health}, "
            f"costs_fire={self.costs_fire}, costs_spirits={self.costs_spirits}, "
            f"has_spirits={self.has_spirits}, has_fire={self.has_fire}, "
            f"skills=[{skillstr}])"
        )

    def is_gameplay_equal(self, other: Card) -> bool:
        """Return whether this card is gameplay-wise equal to `other`. That is, whether
        they have the same values for all non-cosmetic attributes.
        """
        return (
            self.power == other.power
            and self.health == other.health
            and self.costs_fire == other.costs_fire
            and self.costs_spirits == other.costs_spirits
            and self.has_fire == other.has_fire
            and self.has_spirits == other.has_spirits
            and self.skills == other.skills
        )

    def is_skilled(self) -> bool:
        return self.skills.count() > 0

    def copy(self) -> Card:
        cp = copy.copy(self)
        cp.skills = self.skills.copy()
        return cp

    def potency(self, which: WhichPlayer = "human") -> int:
        """Card's potency, i.e., its value for the player."""
        core = self.power * 2 + self.health * 2
        if which == "human":
            # Potency for human player will take into account everything, including all
            # human-relevant skills.
            skills = sum(
                s.potency for s in self.skills if not s.forwhom == ForWhom.COMPUTER
            )
            has = self.has_fire + self.has_spirits
            costs = self.costs_fire + self.costs_spirits
            costs_bonus = 10 if costs == 0 else 0  # Cards with 0 costs are strong
            return core + skills + has - costs + costs_bonus
        elif which == "computer":
            # Potency for computer player will leave out everything
            # fire-/spirit-related, because the computer doesn't have to "pay" for
            # cards. Also, we only use computer-relevant skills here.
            skills = sum(
                s.potency for s in self.skills if not s.forwhom == ForWhom.HUMAN
            )
            return core + skills
        else:
            raise ValueError(f"Unknown potency type {which}")


# ----- Types -----

CardList = List[Card]
