import logging
from .fightvnc import FightVnC
from . import Deck


class HumanStrategyVnC(FightVnC):
    def handle_human_choose_deck_to_draw_from(self) -> Deck:
        """Simply alternate between drawdeck and hamsterdeck."""
        if self.decks.drawdeck.is_empty() or self.round_num % 2 == 0:
            return self.decks.hamsterdeck
        else:
            return self.decks.drawdeck

    def handle_human_plays_card(self) -> None:
        """Simply play the first card in the handdeck to the first empty slot in the
        grid line.
        """
        # TODO Can we simplify this too after incorporating the BZL stuff into the base
        # class?
        # TODO Either way, this needs to be adapted if handle_human_plays_card returns
        # some value in the future.
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
