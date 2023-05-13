from __future__ import annotations
from typing import List, Optional, Tuple, TYPE_CHECKING
import copy
from . import gg
from .skills import ListOfSkillsOrSkillTypes, SkillSet, get_skilltypes

if TYPE_CHECKING:
    from .fightcard import FightCard


class Card:
    """Card class

    Principles for `has_*` and `costs_*`:
    - `costs_fire` & `costs_spirits`:
        - Exactly one is > 0.
    - `has_fire` & `has_spirits`:
        - Typically both are == 1.
        - Max one is > 1.
        - Neither is == 0, "0-ness" is indicated via some skill such as bloodless or
          inert or so. (A card with bloodless should always have both `has_*` == 1.)
        - The preceding two bullets are design decisions to keep things simple(r) so a
          player can rely on default information even if not all information is always
          displayed.
        - (QQ: Possible variant: `has_spirits` is always == 1; this would simplify
          things further. But the current philosophy could easily be adapted to such a
          rule.)

    QQ: Turn `has_*` and `costs_*` into properties to enforce the above rules?
    """

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

    def is_human(self) -> bool:
        return self in gg.humanplayer.get_all_human_cards()
        # FIXME Not nice, rethink the `is_human` test.

    def is_skilled(self) -> bool:
        return self.skills.count() > 0

    @property
    def raw_potency(self) -> int:
        """Return the raw potency number of this card. Simply add a number of
        attributes, where power and health are weighted more heavily. Add a bonus for
        cards with no costs.
        """
        strengths = (
            self.power * 2
            + self.health * 2
            + self.has_fire
            + self.has_spirits
            + sum(s.potency for s in self.skills)
        )
        costs = self.costs_fire + self.costs_spirits
        costs_bonus = 10 if costs == 0 else 0  # Bonus for cards with no costs at all
        return strengths - costs + costs_bonus

    @property
    def potency(self) -> int:
        """Return this card's potency, its raw potency number normalized to [0, 100].
        (Note that it can actually also be <0, but usually isn't.)
        """
        return int(self.raw_potency / self.get_raw_potency_range()[1] * 100)

    def copy(self) -> Card:
        cp = copy.copy(self)
        cp.skills = self.skills.copy()
        return cp

    @classmethod
    def get_raw_potency_range(cls) -> Tuple[int, int, int]:
        """Return the current potency range: (min, max, theoretical max)."""
        skills = sorted(
            get_skilltypes(implemented_only=False),
            key=lambda s: s.potency,
            reverse=True,
        )
        mincard = Card(
            name="Min",
            power=0,
            health=0,
            costs_fire=10,
            skills=[s for s in skills[-Card.MAX_SKILLS :] if s.potency < 0],
            costs_spirits=0,  # 0, bc we can't have both types of costs in a card
            has_spirits=0,
            has_fire=0,
        )
        curmaxcard = Card(
            name="Max",
            power=Card.MAX_ATTR,
            health=Card.MAX_ATTR,
            costs_fire=0,
            skills=skills[: Card.MAX_SKILLS],  # type: ignore (why is this necessary?)
            costs_spirits=0,
            has_spirits=Card.MAX_ATTR,
            has_fire=Card.MAX_ATTR,
        )
        theorymaxcard = curmaxcard.copy()
        theorymaxcard.skills = []
        return (
            mincard.raw_potency,
            curmaxcard.raw_potency,
            theorymaxcard.raw_potency + Card.MAX_SKILLS * 10,
        )


# ----- Types -----

CardList = List[Card]
