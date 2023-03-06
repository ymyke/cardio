from __future__ import annotations
import logging
import copy
from dataclasses import dataclass, field, fields
from typing import Optional, List, TYPE_CHECKING
from .skills import Skill, SkillList
from . import session

if TYPE_CHECKING:
    from . import GridPos


# QQ: This class in its current implementation is geared fully on being used during
# fights: accessing the grid, updating humanplayer, ... -- What will be necessary in the
# future when cards are also used outside of fights? -- Maybe it's ok since fights are
# at the very center of the game and everything else is surrounding stuff.


@dataclass
class Card:
    name: str
    initial_power: int  # 💪
    initial_health: int  # 💓
    costs_fire: int  # How much fire 🔥 needed

    # Optional attributes:
    skills: SkillList = field(default_factory=list)
    costs_spirits: int = 0  # How many spirits 👻 needed
    has_spirits: int = 1  # How many spirits this card generates upon death 👻
    has_fire: int = 1  # How much fire this card is worth when sacrificed 🔥

    # post_init attributes:
    power: int = 0
    health: int = 0

    def __post_init__(self) -> None:
        assert all(
            getattr(self, f.name) >= 0 for f in fields(self) if f.type == "int"
        ), "No negative numbers please"
        assert self.costs_fire * self.costs_spirits == 0, (
            "Either fire or spirit costs must be 0. "
            "Hybrids are not supported at this time."
            # QQ: Will we ever have cards that can have both cost_fire and cost_spirits?
            # If so, would that be AND or OR? Note that such hybrids would add
            # considerable complexity to the UI, since the player would have to be able
            # to choose how much of either to use (unless specified algorithmically).
        )
        if self.power == 0 or self.health == 0:
            # (This test allows to explicitly set power and health, e.g., for tests.)
            self.reset()

    def reset(self) -> None:
        self.power = self.initial_power
        self.health = self.initial_health

    def is_human(self) -> bool:
        def is_in(what: object, inlist: list) -> bool:
            """We want to use `is` instead of `==` equality here."""
            return any(x is what for x in inlist)

        # QQ: In the future: What should be the invariant? Maybe that a card is always
        # in session.humanplayer.deck.cards?
        # FIXME Should be improved/simplified once we have a new architecture for deck
        # in place. // Maybe just add an `owner` attribute to the object and simply use
        # that? (On could ask whether we should then just use some subclass but an owner
        # might make things more straightforward.)
        # FIXME Add test for this method.
        return (
            is_in(self, session.humanplayer.deck.cards)
            # (Note that the above test does not suffice bc new cards could be created
            # (e.g., via fertility) during a fight which are added to one of the decks
            # below but not yet to a player's deck (which gets recreated only after a
            # fight).)
            or (
                getattr(session.view, "decks", None)
                # (Testing for the `decks` attribute first mostly to enable various
                # tests where we don't want to set up the entire fight environment
                # first.)
                and any(
                    is_in(self, d.cards)
                    for d in [
                        session.view.decks.drawdeck,
                        session.view.decks.hamsterdeck,
                        session.view.decks.handdeck,
                        session.view.decks.useddeck,
                    ]
                )
            )
            or is_in(self, session.grid.lines[2])
        )

    def get_grid_pos(self) -> GridPos:
        pos = session.grid.find_card(self)
        assert pos is not None, "Cards calling `get_grid_pos` must be on the grid"
        return pos

    def duplicate(self) -> Card:
        return copy.deepcopy(self)

    def get_prep_card(self) -> Optional[Card]:
        """Get the card from the prepline of this cards slot."""
        return session.grid.get_card(self.get_grid_pos()._replace(line=0))

    def _die_silently(self) -> None:
        self.health = 0
        session.humanplayer.spirits += self.has_spirits 
        # TODO This is wrong! Will lead to computer cards that die also adding to
        # human's spirits. => fix and add a test case.
        # TODO Add card to useddeck if it is a human card
        # TODO How does a card know whether it is human or not? -> Subclasses?
        session.grid.remove_card(self)

    def die(self) -> None:
        logging.debug("%s dies.", self.name)
        pos = self.get_grid_pos()
        self._die_silently()
        session.view.card_died(self, pos)

    def sacrifice(self) -> None:
        self._die_silently()

    def lose_health(self, howmuch: int) -> int:
        assert howmuch > 0
        if howmuch >= self.health:
            howmuch = self.health
            self.die()
        else:
            self.health -= howmuch
            session.view.card_lost_health(self)
            logging.debug("%s new health: %s", self.name, self.health)
        return howmuch

    def get_attacked(self, opponent: Card) -> None:
        logging.debug("%s gets attacked by %s", self.name, opponent.name)

        if Skill.SPINES in self.skills:
            # FIXME Should maybe be moved further down once we have an animation in
            # place for this because otherwise the animations will happen in the wrong
            # order.
            logging.debug(
                "%s causes 1 damage on %s with Spines", self.name, opponent.name
            )
            opponent.lose_health(1)

        prepcard = self.get_prep_card() if self.get_grid_pos().line == 1 else None
        # (Prep cards only relevant if computer is being attacked.)
        session.view.card_getting_attacked(self, opponent)
        # (Needs to happen before the call to `lose_health` below, bc the card could
        # die/vanish during that call, leading to a `None` reference on the grid and an
        # error in the view update call.)
        howmuch = self.lose_health(opponent.power)
        if opponent.power > howmuch and prepcard is not None:
            logging.debug(
                "%s gets overflow damage of %s", prepcard.name, opponent.power - howmuch
            )
            prepcard.lose_health(opponent.power - howmuch)

    # QQ: Fight logic is distributed between Card and FightVNC. Can this be streamlined?
    # (One could argue that all the places where the card module needs to call a view
    # method should rather belong somewhere else?)

    def attack(self, opponent: Optional[Card]) -> None:
        if self.power == 0:
            logging.debug("%s would attack but has 0 power, so doesn't", self.name)
            return

        if opponent is None:
            session.view.handle_player_damage(self.power, self)
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
                session.view.handle_player_damage(self.power, self)
            return

        if Skill.INSTANTDEATH in self.skills:
            opponent.die()
            return

        opponent.get_attacked(self)

    def activate(self) -> None:
        logging.debug("%s becomes active", self.name)
        opponent = session.grid.get_opposing_card(self)
        pos = self.get_grid_pos()
        session.view.card_activate(self)
        self.attack(opponent)
        session.view.pos_card_deactivate(pos)

    def prepare(self) -> None:
        pos = self.get_grid_pos()
        assert pos is not None and pos.line == 0
        to_pos = pos._replace(line=1)
        prep_to = session.grid.get_card(to_pos)
        if prep_to is not None:
            logging.debug(
                "Preparing %s but the prep-to space is occupied by %s",
                self.name,
                prep_to.name,
            )
            return
        logging.debug("Preparing %s, moving to computer line", self.name)
        session.view.card_prepare(self)
        session.grid.move_card(self, to_pos=to_pos)
        self.activate()


# ----- Types -----

CardList = List[Card]
