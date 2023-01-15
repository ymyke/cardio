import logging
from typing import Literal, Optional
from . import session, Card, Deck, Grid, GridPos
from .computer_strategies import ComputerStrategy
from .card_blueprints import create_cards_from_blueprints
from .tui.decks import Decks  # FIXME tui should not be known here


class FightVnC:
    """
    - All the `card_` methods should be able to rely on the precondition that the `card`
      is still in the grid when the method is called.
    """

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.states_log = ""
        # FIXME Should we also set the computerstrategy here?

    # --- Called by Card class ---

    def card_about_to_die(self, card: Card) -> None:
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

    def handle_human_draws_new_card(self) -> None:
        pass

    def handle_human_plays_card(self) -> None:
        pass

    # --- Misc ---

    def human_wins_fight(self) -> None:
        # FIXME Still necessary?
        pass

    def computer_wins_fight(self) -> None:
        # FIXME Still necessary?
        # QQ: Boss fights will work differently.
        pass

    def update_states_log(self) -> None:
        def card2str(card: Optional[Card]) -> str:
            if card is None:
                return "-"
            symbols = "".join([s.value.symbol for s in card.skills])
            return f"{card.name[0]}p{card.power}h{card.health}{symbols}"

        s = f"{self.round_num}:\n"
        for line in range(3):
            s += "|"
            for slot in range(self.grid.width):
                card = self.grid[line][slot]
                s += f" {card2str(card):12s}|"
            s += "\n"
        for deck, name in [
            (self.decks.handdeck, "Hand"),
            (self.decks.useddeck, "Used"),
            (self.decks.drawdeck, "Draw"),
            (self.decks.hamsterdeck, "Hamster"),
        ]:
            s += f"{name}: " + " ".join([card2str(c) for c in deck.cards]) + "\n"
        s += "\n"
        # FIXME Add human and computer damage, lives, maybe items, ...
        self.states_log += s

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

    def handle_round_of_fight(self) -> bool:
        logging.debug("----- Start of round %s -----", self.round_num)
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
        self.grid.activate_line(1)
        self.grid.prepare_line()

        self.grid.log()
        self.update_states_log()
        logging.debug("----- End of round %s -----", self.round_num)

        # FIXME Still some things missing below:
        if session.humanagent.has_lost_life():
            session.humanagent.update_lives_and_health_after_death()
            self.computer_wins_fight()
            return False
        if session.computeragent.has_lost_life():
            overflow = session.computeragent.update_lives_and_health_after_death()
            self.human_wins_fight()
            # FIXME Do something w overflow damage here -- maybe just store it in the
            # object right in the update_lives_and_health_after_death function but also
            # pass it to the view for some animation?
            return False
        if self.grid.is_empty():
            # QQ: Should this also break when the grid is "powerless", i.e., no cards
            # with >0 power?
            return False

        return True

    def handle_fight(self, computerstrategy: ComputerStrategy) -> None:
        self.computerstrategy = computerstrategy
        # ^ FIXME Should this be in __init__? And/or the entire ComputerAgent object,
        # which could contain the computerstrategy? It will be used for one fight only
        # anyway...
        self.show_empty_grid(self.grid.width)

        # Set up the 4 decks for the fight:
        drawdeck = Deck()
        drawdeck.cards = session.humanagent.deck.cards
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
        fighting = True
        self.round_num = 0
        while fighting:
            fighting = self.handle_round_of_fight()
            self.round_num += 1

        # Reset human deck after the fight:
        session.humanagent.deck.cards = [
            c
            for c in self.decks.useddeck.cards
            + self.decks.handdeck.cards
            + self.decks.drawdeck.cards
            if c.name != "Hamster"
        ]
        session.humanagent.deck.reset_cards()
