import logging
from .fightvnc import FightVnC


class HumanStrategyVnC(FightVnC):
    def handle_human_draws_new_card(self) -> None:
        """Simply alternate between drawdeck and hamsterdeck."""
        if self.decks.drawdeck.is_empty() or self.round_num % 2 == 0:
            whichdeck = self.decks.hamsterdeck
        else:
            whichdeck = self.decks.drawdeck
        if whichdeck.is_empty():
            return
        card = whichdeck.draw_card()
        self.decks.handdeck.add_card(card)
        logging.debug("Human draws %s", card.name)

    def handle_human_plays_card(self) -> None:
        """Simply play the first card in the handdeck to the first empty slot in the
        grid line.
        """
        if self.decks.handdeck.is_empty():
            return None
        for slot in range(self.grid.width):
            if self.grid[2][slot] is None:
                card = self.decks.handdeck.draw_card()
                self.grid[2][slot] = card
                self.decks.useddeck.add_card(card)
                logging.debug("Human plays %s on %s", card.name, slot)
                return
        logging.debug("Human plays no card.")
