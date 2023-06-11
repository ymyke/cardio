"""FightVnC

Implements or orchestrates all the game-logic related code and anything that changes the
model. There is also some fight-related logic in the `Card` class.
"""

import logging
from typing import Callable, Optional
from . import gg, FightCard, Deck, FightDecks, Grid, GridPos, skills
from .placement_manager import PlacementManager
from .agent_damage_state import AgentDamageState
from .computer_strategies import ComputerStrategy
from .states_logger import StatesLogger


class EndOfFightException(Exception):
    pass


class FightVnC:
    """
    - All the `card_` methods should be able to rely on the precondition that the `card`
      is still in the grid when the method is called.
    """

    def __init__(self, grid: Grid, computerstrategy: ComputerStrategy) -> None:
        self.grid = grid
        self.damagestate = AgentDamageState()
        self.stateslogger = StatesLogger(self)
        FightCard.init_fight(self, self.grid)
        self.computerstrategy = computerstrategy

    # --- Called by FightCard class ---

    def card_died(self, card: FightCard, pos: GridPos) -> None:
        pass

    def card_lost_health(self, card: FightCard) -> None:
        pass

    def card_getting_attacked(self, target: FightCard, attacker: FightCard) -> None:
        pass

    def card_activate(self, card: FightCard) -> None:
        pass

    def card_prepare(self, card: FightCard) -> None:
        pass

    def card_deactivate(self, card: FightCard) -> None:
        """Note that the card might have died and been removed from the grid before this
        method gets called.
        """
        pass

    # --- Controller-related ---

    def show_human_draws_new_card(
        self, draw_to: Deck, card: FightCard, draw_from: Deck
    ) -> None:
        pass

    def show_human_receives_card_from_grid(
        self, card: FightCard, from_slot: int
    ) -> None:
        pass

    def show_computer_plays_card(self, card: FightCard, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        pass

    def show_human_places_card(
        self, card: FightCard, from_slot: int, to_slot: int
    ) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        pass

    def handle_human_choose_deck_to_draw_from(self) -> Optional[Deck]:
        return None

    def handle_human_plays_cards(self, place_card_callback: Callable) -> None:
        pass

    def handle_agent_damage(self, to_computer: bool, howmuch: int) -> None:
        """Handle `howmuch` damage to the agent. `to_computer` indicates whether the
        damage is to the computer or the human.
        """
        if to_computer:
            self.damagestate.damage_computer(howmuch)
        else:
            self.damagestate.damage_human(howmuch)
        self.redraw_view()

    # --- Misc ---

    def redraw_view(self) -> None:
        pass

    def human_wins_fight(self) -> None:
        # QQ: Still necessary?
        pass

    def computer_wins_fight(self) -> None:
        # QQ: Still necessary?
        pass

    # --- Controller ---

    def _safe_draw_card_to_deck(self, draw_from: Deck) -> None:
        """Safe way to draw a card from a deck that doesn't break when the deck is
        empty. Important for tests.
        """
        try:
            card = draw_from.draw_card()
        except IndexError:
            return
        self.show_human_draws_new_card(self.decks.hand, card, draw_from)
        self.decks.hand.add_card(card)

    # TODO simplify the following 3 methods into 1?
    # TODO use WhichPlayer type here too?

    def _has_computer_won(self) -> bool:
        return self.damagestate.has_computer_won()

    def _has_human_won(self) -> bool:
        return self.damagestate.has_human_won()

    def _check_for_end_of_fight(self) -> None:
        if self._has_computer_won() or self._has_human_won():
            raise EndOfFightException

    def _place_card(self, pmgr: PlacementManager, from_slot: int) -> None:
        # Update model:
        for sacrifice_pos in pmgr.get_marked_positions():
            card = self.grid.get_card(sacrifice_pos)
            assert card is not None
            card.sacrifice()
        gg.humanplayer.spirits -= pmgr.target_card.costs_spirits
        self.grid.set_card(pmgr.placement_position, pmgr.target_card)  # type:ignore

        # Update view:
        to_slot = pmgr.get_placement_position().slot
        self.show_human_places_card(pmgr.target_card, from_slot, to_slot)
        self.decks.hand.pick_card(from_slot)

        if skills.Fertility in pmgr.target_card.skills:
            new_card = pmgr.target_card.copy()
            self.redraw_view()
            self.decks.hand.add_card(new_card)
            self.show_human_receives_card_from_grid(new_card, from_slot=to_slot)
            logging.debug("Human copies %s via Fertility", new_card.name)

        self.redraw_view()

        if skills.Packrat in pmgr.target_card.skills:
            if not self.decks.draw.is_empty():
                new_card = self.decks.draw.draw_card()
                self.show_human_draws_new_card(
                    self.decks.hand, new_card, self.decks.draw
                )
                self.decks.hand.add_card(new_card)
                logging.debug("Human draws %s via Packrat", new_card.name)

        self.redraw_view()
        logging.debug("Human plays %s in %s", pmgr.target_card.name, to_slot)

    def handle_round_of_fight(self) -> None:  # QQ: Should be private?
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
            self.show_human_draws_new_card(self.decks.hand, card, deck)
            self.decks.hand.add_card(card)

        # Let human play card(s) from handdeck or items in his collection:
        self.handle_human_plays_cards(place_card_callback=self._place_card)

        self.decks.log()
        self.grid.log()

        # Activate all cards line by line:
        for line in [2, 1, 0]:
            for card in (c for c in self.grid.lines[line] if c is not None):
                if line == 0:
                    if not card.prepare():
                        continue  # Do not attack, if not prepared successfully
                card.attack(gg.grid.get_opposing_card(card))
            self._check_for_end_of_fight()
            # QQ: Here, we check end-of-fight conditions after each line. Should this
            # rather be at the end of the fight? Or after each card?

        self.damagestate.add_to_history(self.round_num)
        self._check_for_end_of_fight()

        self.grid.log()
        logging.debug("----- End of round %s -----", self.round_num)

    def handle_fight(self) -> None:
        assert self.computerstrategy is not None

        # Set up the decks for the fight:
        self.decks = FightDecks()
        self.decks.draw.cards = FightCard.from_cards(gg.humanplayer.deck.cards)
        hamster_cards = [
            gg.humanplayer.hamster_blueprint.instantiate() for _ in range(10)
        ]
        self.decks.hamster.cards = FightCard.from_cards(hamster_cards)
        self.decks.draw.shuffle()

        # Initialize all skills:
        for card in self.decks.draw.cards + self.decks.hamster.cards:
            card.skills.call("pre_fight")

        # Draw the decks and show how the first cards get drawn:
        self.redraw_view()
        for _ in range(3):
            self._safe_draw_card_to_deck(self.decks.draw)
        self._safe_draw_card_to_deck(self.decks.hamster)

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
            gg.humanplayer.lives -= 1
            # FIXME Check for game over here or later on
        if self._has_human_won():
            gg.humanplayer.gems += self.damagestate.get_overflow()
            # LIXME Animate overflow damage that turns into gems
            self.human_wins_fight()
