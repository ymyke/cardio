import logging
from typing import Literal
from . import session, Card, Deck, Grid, GridPos
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

    def card_died(self, card: Card, pos:GridPos) -> None:
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
        pass

    # --- Controller-related ---

    def show_empty_grid(self, grid_width: int) -> None:
        pass

    def show_drawdecks(self, drawdeck: Deck, hamsterdeck: Deck) -> None:
        pass

    def show_card_to_handdeck(
        self, handdeck: Deck, card: Card, whichdeck: Literal["draw", "hamster"]
    ) -> None:
        pass

    def show_computer_plays_card(self, card: Card, to: GridPos) -> None:
        """Play a computer card to `to`, which can be in line 0 or 1."""
        pass

    def show_human_places_card(self, card: Card, from_slot: int, to_slot: int) -> None:
        """Place a human card from the hand (`from_slot`) to the grid (`to_slot`). Line
        is implicitly always 2.
        """
        pass

    def show_agents_state(self) -> None:
        """Show agent information, damage, spirits, lives, etc."""
        # FIXME Must be called if: damage diff changes, spirits change, lives change,
        # items added, items used, ... -- make sure this is the case
        pass

    def handle_human_draws_new_card(self) -> None:
        pass

    def handle_human_plays_card(self) -> None:
        pass

    def handle_damage(self, howmuch: int, source: Card) -> None:
        assert source.get_linei() in (1, 2)
        if source.get_linei() == 1:
            self.damagestate.damage_human(howmuch)
        else:
            self.damagestate.damage_computer(howmuch)
        # FIXME Add some animation for for damage
        self.show_agents_state()

    # --- Misc ---

    def human_wins_fight(self) -> None:
        # FIXME Still necessary?
        pass

    def computer_wins_fight(self) -> None:
        # FIXME Still necessary?
        # QQ: Boss fights will work differently.
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
        self.show_card_to_handdeck(self.decks.handdeck, card, from_name)
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
        self.handle_human_draws_new_card()

        # Let human play card(s) from handdeck or items in his collection:
        self.handle_human_plays_card()

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
        self.show_empty_grid(self.grid.width)
        self.show_agents_state()

        # Set up the 4 decks for the fight:
        drawdeck = Deck()
        drawdeck.cards = session.humanplayer.deck.cards
        drawdeck.shuffle()
        hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
        self.decks = Decks(drawdeck, hamsterdeck, Deck(), Deck())

        # Draw the decks and show how the first cards get drawn:
        self.show_drawdecks(self.decks.drawdeck, self.decks.hamsterdeck)
        for _ in range(3):
            self._safe_draw_card_to_deck(self.decks.drawdeck, "draw")
        self._safe_draw_card_to_deck(self.decks.hamsterdeck, "hamster")
        # Redraw because size of decks changed:
        self.show_drawdecks(self.decks.drawdeck, self.decks.hamsterdeck)

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
            # FIXME Animate overflow damage that turns into gems
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
