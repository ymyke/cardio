"""FightVnC

Implements or orchestrates all the game-logic related code and anything that changes the
model. There is also some fight-related logic in the `Card` class.
"""

import logging
from typing import Callable, Literal, Optional

from cardio.tui.placement_manager import (
    PlacementManager,
)  # TODO move placement_manager to cardio instead of tui
from . import session, Card, Deck, Grid, GridPos, Skill
from .agent_damage_state import AgentDamageState
from .computer_strategies import ComputerStrategy
from .card_blueprints import create_cards_from_blueprints
from .tui.decks import Decks  # FIXME tui should not be known here
from .states_logger import StatesLogger


class EndOfFightException(Exception):
    pass


class FightVnC:
    """
    - All the `card_` methods should be able to rely on the precondition that the `card`
      is still in the grid when the method is called.
    """

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.damagestate = AgentDamageState()
        self.stateslogger = StatesLogger(self)
        # FIXME Should we also set the computerstrategy here?

    # --- Called by Card class ---

    def card_died(self, card: Card, pos: GridPos) -> None:
        pass

    def card_lost_health(self, card: Card) -> None:
        pass

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pass

    def card_activate(self, card: Card) -> None:
        pass

    def card_prepare(self, card: Card) -> None:
        pass

    def pos_card_deactivate(self, pos: GridPos) -> None:
        """Uses a position instead of a card because it could be that the card has died
        and been removed from the grid between being activated and deactivated. In this
        case, `pos` should point to where the card used to be before being removed.
        """
        pass

    # --- Controller-related ---

    def show_human_draws_new_card(
        self, handdeck: Deck, card: Card, whichdeck: Deck
    ) -> None:
        pass

    def show_human_receives_card_from_grid(self, card: Card, from_slot: int) -> None:
        pass

    def show_computer_plays_card(self, card: Card, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        pass

    def show_human_places_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        pass

    def handle_human_choose_deck_to_draw_from(self) -> Optional[Deck]:
        return None

    def handle_human_plays_cards(self, place_card_callback: Callable) -> None:
        pass

    def handle_player_damage(self, howmuch: int, source: Card) -> None:
        source_line = source.get_grid_pos().line
        assert source_line in (1, 2)
        if source_line == 1:
            self.damagestate.damage_human(howmuch)
        else:
            self.damagestate.damage_computer(howmuch)
        # FIXME Add some animation for for damage
        self.redraw_view()

    # --- Misc ---

    def redraw_view(self) -> None:
        # TODO Which category does this belong to?
        pass

    def human_wins_fight(self) -> None:
        # FIXME Still necessary?
        pass

    def computer_wins_fight(self) -> None:
        # FIXME Still necessary?
        pass

    # --- Controller ---

    def _safe_draw_card_to_deck(
        self, draw_from: Deck, from_name: Literal["draw", "hamster"]
    ) -> None:
        """Safe way to draw a card from a deck that doesn't break when the deck is
        empty. Important for tests.
        """
        try:
            card = draw_from.draw_card()
        except IndexError:
            return
        self.show_human_draws_new_card(self.decks.handdeck, card, from_name)
        self.decks.handdeck.add_card(card)

    def _has_computer_won(self) -> bool:
        return self.damagestate.has_computer_won() or not any(
            c.power > 0
            for c in self.grid.lines[2]
            + self.decks.handdeck.cards
            + self.decks.drawdeck.cards
            + self.decks.hamsterdeck.cards
            if c is not None
        )
        # FIXME The above is not fully correct yet. There could also be a case there is
        # a card in the hand with power > 0 but that is not playable, e.g., because the
        # necessary sacrifice is not possible. That should be taken into account in the
        # test. Moreover, items that can have a relevant effect should be taken into
        # account as well. Also skills that have a relevant effect such as spines or
        # skills that increase the power of other cards etc. So this test could become
        # very complex in the end. -- Maybe these more complex cases should be handled
        # differently in the UI or at least explained?

    def _has_human_won(self) -> bool:
        return self.damagestate.has_human_won()

    def _check_for_end_of_fight(self) -> None:
        if self._has_computer_won() or self._has_human_won():
            raise EndOfFightException

    def _place_card(self, pmgr: PlacementManager, from_slot: int) -> None:
        for sacrifice_pos in pmgr.get_marked_positions():
            card = self.grid.get_card(sacrifice_pos)
            if card is not None:
                session.humanplayer.spirits += (
                    card.has_spirits
                )  # TODO should this rather be card.die()?
        self.redraw_view()
        pmgr.do_place()
        session.humanplayer.spirits -= pmgr.target_card.costs_spirits
        to_slot = pmgr.get_placement_position().slot
        self.show_human_places_card(pmgr.target_card, from_slot, to_slot)
        self.decks.useddeck.add_card(pmgr.target_card)
        self.decks.handdeck.pick_card(from_slot)

        if Skill.FERTILITY in pmgr.target_card.skills:
            new_card = pmgr.target_card.duplicate()
            new_card.reset()
            self.redraw_view()
            self.decks.handdeck.add_card(new_card)
            self.show_human_receives_card_from_grid(new_card, from_slot=to_slot)

        self.redraw_view()
        logging.debug("Human plays %s in %s", pmgr.target_card.name, to_slot)

    def handle_round_of_fight(self) -> None:  # FIXME Should be private
        logging.debug("----- Start of round %s -----", self.round_num)
        self.stateslogger.log_current_state()
        self.decks.log()

        # Play computer cards and animate how they appear:
        for pos, card in self.computerstrategy.cards_to_be_played(self.round_num):
            self.show_computer_plays_card(card, pos)
        # Now also place them in the model:
        self.computerstrategy.play_cards(self.round_num)

        # Let human draw a card:
        deck = self.handle_human_choose_deck_to_draw_from()
        if deck is not None:
            card = deck.draw_card()
            self.show_human_draws_new_card(self.decks.handdeck, card, deck)
            self.decks.handdeck.add_card(card)

        # Let human play card(s) from handdeck or items in his collection:
        self.handle_human_plays_cards(place_card_callback=self._place_card)
        # TODO Send _place_card along as a callback
        # TODO How to move the BZL to the base class in this case? -- Maybe w a callback
        # for the inventory call (bc maybe in the future the TUIFightVnC is no longer a
        # subclass of FightVnC but split into TUIController und TUIAnimator?)

        self.decks.log()
        self.grid.log()

        # Activate all cards:
        self.grid.activate_line(2)
        self._check_for_end_of_fight()
        self.grid.activate_line(1)
        self._check_for_end_of_fight()
        self.grid.prepare_line()
        self._check_for_end_of_fight()

        self.grid.log()
        logging.debug("----- End of round %s -----", self.round_num)

    def handle_fight(self, computerstrategy: ComputerStrategy) -> None:
        self.computerstrategy = computerstrategy
        # ^ FIXME Should this be in __init__? And/or the entire ComputerAgent object,
        # which could contain the computerstrategy? It will be used for one fight only
        # anyway...

        # Set up the 4 decks for the fight:
        drawdeck = Deck()
        drawdeck.cards = session.humanplayer.deck.cards
        drawdeck.shuffle()
        hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
        self.decks = Decks(drawdeck, hamsterdeck, Deck(), Deck())

        # Draw the decks and show how the first cards get drawn:
        self.redraw_view()
        for _ in range(3):
            self._safe_draw_card_to_deck(self.decks.drawdeck, "draw")
        self._safe_draw_card_to_deck(self.decks.hamsterdeck, "hamster")

        # Run the fight:
        self.round_num = 0
        while True:
            try:
                self.handle_round_of_fight()
            except EndOfFightException:
                break
            self.round_num += 1
        self.stateslogger.log_current_state(final=True)

        # Handle win/lose conditions:
        if self._has_computer_won():
            self.computer_wins_fight()
            session.humanplayer.lives -= 1
            # FIXME Check for game over here or later on
        if self._has_human_won():
            session.humanplayer.gems += self.damagestate.get_overflow()
            # LIXME Animate overflow damage that turns into gems
            self.human_wins_fight()

        # Reset human deck after the fight:
        session.humanplayer.deck.cards = [
            c
            for c in self.decks.useddeck.cards
            + self.decks.handdeck.cards
            + self.decks.drawdeck.cards
            if c.name != "Hamster"
        ]
        session.humanplayer.deck.reset_cards()
