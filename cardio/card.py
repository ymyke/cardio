from __future__ import annotations
import logging
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from .skills import Skill, SkillList
from . import session

if TYPE_CHECKING:
    # To prevent circular imports. Should maybe be fixed somehow at some point.
    from . import Agent


@dataclass
class Card:
    name: str
    # QQ: Could cards have an icon that gets displayed, e.g., top right of the card?
    # QQ: Then only pick animal (and plant?) types that have an emoji?
    initial_power: int
    initial_health: int
    # FIXME How much blood needed?
    # FIXME Bones...

    # Derived attributes:
    power: int = 0
    health: int = 0
    skills: SkillList = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.power == 0 or self.health == 0:
            # (This test allows to explicitly set power and health, e.g., for tests.)
            self.reset()

    def reset(self) -> None:
        self.power = self.initial_power
        self.health = self.initial_health

    def get_sloti(self) -> int:
        pos = session.grid.find_card(self)
        if pos is None:
            raise RuntimeError("Trying to get sloti for card that is not on the grid.")
        return pos.slot

    def get_linei(self) -> int:
        pos = session.grid.find_card(self)
        if pos is None:
            raise RuntimeError("Trying to get linei for card that is not on the grid.")
        return pos.line

    def get_prep_card(self) -> Optional[Card]:
        """Get the card from the prepline of this cards slot."""
        return session.grid[0][self.get_sloti()]

    def get_opposing_agent(self) -> Agent:
        return session.computeragent if self.get_linei() == 2 else session.humanagent
        # QQ: Use enums or something instead of 0, 1, 2 for the lines?
        # QQ: Should this be a grid function? (Also some of the other methods?)

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        self.health = 0
        session.grid.remove_card(self)
        # FIXME Card must also be moved to a different deck? (This is done elsewhere, I
        # believe. But if I ever refacator to cards knowing their states and their
        # position in the grid, it might make sense to do this here.)

    def lose_health(self, howmuch: int) -> int:
        assert howmuch > 0
        if howmuch >= self.health:
            howmuch = self.health
            # FIXME
            from cardio.tui import tui2 
            tui2.d_card_dies(self)  
            # FIXME Why is the view update done here and not in the `die` method?
            self.die()
        else:
            self.health -= howmuch
            # FIXME
            from cardio.tui import tui2
            tui2.d_card_lost_health(self)
            logging.debug("%s new health: %s", self.name, self.health)
        return howmuch

    def get_attacked(self, opponent: Card) -> None:
        logging.debug("%s gets attacked by %s", self.name, opponent.name)

        if Skill.SPINES in self.skills:
            logging.debug(
                "%s causes 1 damage on %s with Spines", self.name, opponent.name
            )
            opponent.lose_health(1)

        prep = self.get_prep_card()
        # session.view.get_attacked(self, opponent)
        # FIXME  -- breaks tests
        from cardio.tui import tui2
        tui2.d_card_gets_attacked(self, opponent)
        # (Needs to happen before the call to `lose_health` below, bc the card could
        # die/vanish during that call, leading to a `None` reference on the grid and an
        # error in the view update call.) 
        howmuch = self.lose_health(opponent.power)
        if opponent.power > howmuch and prep is not None:
            logging.debug(
                "%s gets overflow damage of %s", prep.name, opponent.power - howmuch
            )
            prep.lose_health(opponent.power - howmuch)

    def attack(self, opponent: Card) -> None:
        if self.power == 0:
            logging.debug("%s would attack but has 0 power, so doesn't", self.name)
            return

        logging.debug(
            "%s%s attacks %s %s",
            self.name,
            "".join(s.value.symbol for s in self.skills),
            opponent.name,
            "".join(s.value.symbol for s in opponent.skills),
        )

        if Skill.SOARING in self.skills:
            if Skill.AIRDEFENSE in opponent.skills:
                if Skill.INSTANTDEATH in self.skills:
                    opponent.die()
                else:
                    opponent.get_attacked(self)
            else:
                self.get_opposing_agent().lose_health(self.power)
            return

        if Skill.INSTANTDEATH in self.skills:
            opponent.die()
            return

        opponent.get_attacked(self)

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.get_opposing_card(self)
        # session.view.activate_card(self)
        # FIXME -- breaks tests
        from cardio.tui import tui2
        tui2.d_activate_card(self)
        # FIXME ^ Should the view be an object again in the future or how should this
        # work? 
        if opponent is not None:
            self.attack(opponent)
        elif self.power > 0:
            self.get_opposing_agent().lose_health(self.power)
            # ^ FIXME should this be in attack after all?
        tui2.d_deactivate_card(self)

    def prepare(self) -> None:
        pos = session.grid.find_card(self)
        assert pos is not None and pos.line == 0
        prep_to_card = session.grid[1][pos.slot]
        # ^ QQ: Should this be a method like get_card() or something?
        if prep_to_card is not None:
            logging.debug(
                "Preparing %s but the prep-to space is occupied by %s",
                self.name,
                prep_to_card.name,
            )
            return
        logging.debug("Preparing %s, moving to computer line", self.name)
        # FIXME
        from cardio.tui import tui2
        tui2.d_prepare_card(self)
        session.grid.move_card(self, to_pos=(1, pos.slot))
        self.activate()


# ----- Types -----

CardList = List[Card]
