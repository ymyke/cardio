import logging
from typing import Callable, List, Optional
from . import Deck, GridPos
from .fightvnc import FightVnC
from .placement_manager import PlacementManager


class HumanStrategyVnC(FightVnC):
    def __init__(
        self, whichrounds: Optional[List[int]] = None, *args, **kwargs
    ) -> None:
        """Use `whichrounds` to only become active in specific fight rounds."""
        super().__init__(*args, **kwargs)
        self.whichrounds = whichrounds

    def handle_human_choose_deck_to_draw_from(self) -> Optional[Deck]:
        """Simply alternate between drawdeck and hamsterdeck."""
        if self.decks.draw.is_empty() and self.decks.hamster.is_empty():
            return None
        if self.decks.draw.is_empty() or self.round_num % 2 == 0:
            return self.decks.hamster
        return self.decks.draw

    def handle_human_plays_cards(self, place_card_callback: Callable) -> None:
        """Simply play the first card in the handdeck to the first empty slot in the
        grid line. Uses the `place_card_callback` in order to invoke all the relevant
        code.

        Note that both costs will be set to 0 before placing each card so cards get
        placed regardless of the current state of the human player.
        """
        if self.whichrounds and not self.round_num in self.whichrounds:
            return
        if self.decks.hand.is_empty():
            return
        for slot in range(self.grid.width):
            pos = GridPos(2, slot)
            if self.grid.get_card(pos) is None:
                card = self.decks.hand.cards[0]
                card.costs_fire = 0
                card.costs_spirits = 0
                p = PlacementManager(self.grid, 0, card, placement_position=pos)
                place_card_callback(p, 0)
                return
        logging.debug("Human plays no card.")
