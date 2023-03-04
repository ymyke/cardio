import logging
from typing import Callable, List, Optional
from . import Deck, GridPos, Grid
from .fightvnc import FightVnC
from .placement_manager import PlacementManager


class HumanStrategyVnC(FightVnC):
    def handle_human_choose_deck_to_draw_from(self) -> Deck:
        """Simply alternate between drawdeck and hamsterdeck."""
        if self.decks.drawdeck.is_empty() or self.round_num % 2 == 0:
            return self.decks.hamsterdeck
        else:
            return self.decks.drawdeck

    def handle_human_plays_cards(self, place_card_callback: Callable) -> None:
        """Simply play the first card in the handdeck to the first empty slot in the
        grid line.
        """
        # TODO Can we simplify this too after incorporating the BZL stuff into the base
        # class? -- I.e., place the cards implicitly via place_card_callback rather than
        # explicitly here, ignoring the callback.
        if self.decks.handdeck.is_empty():
            return
        for slot in range(self.grid.width):
            if self.grid[2][slot] is None:
                card = self.decks.handdeck.draw_card()
                self.grid[2][slot] = card
                self.decks.useddeck.add_card(card)
                logging.debug("Human plays %s on %s", card.name, slot)
                return
        logging.debug("Human plays no card.")


class ProperlyPlacingHumanStrategyVnC(HumanStrategyVnC):
    def __init__(
        self, grid: Grid, whichrounds: Optional[List[int]] = None, *args, **kwargs
    ) -> None:  # TODO Can I this w/o the grid here?
        """Use `whichrounds` to only become active in specific fight rounds."""
        super().__init__(grid, *args, **kwargs)
        self.whichrounds = whichrounds

    def handle_human_plays_cards(self, place_card_callback: Callable) -> None:
        if self.whichrounds and not self.round_num in self.whichrounds:
            return
        if self.decks.handdeck.is_empty():
            return
        for slot in range(self.grid.width):
            pos = GridPos(2, slot)
            if self.grid.get_card(pos) is None:
                card = self.decks.handdeck.cards[0]
                card.costs_fire = 0
                card.costs_spirits = 0
                p = PlacementManager(self.grid, 0, card)
                p.target_card = card  # TODO Add these to initializer
                p.placement_position = pos  # TODO Rename to target_position
                place_card_callback(p, 0)
                return
        logging.debug("Human plays no card.")
