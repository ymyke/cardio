import logging
from typing import NamedTuple
from cardio import Deck


class Decks(NamedTuple):
    # QQ DECK: Maybe unnecesary if I refactor decks implicitly via some `state` attribute in
    # the card.
    drawdeck: Deck
    hamsterdeck: Deck
    handdeck: Deck
    useddeck: Deck

    def log(self):
        for deck, name in zip(
            [self.handdeck, self.drawdeck, self.hamsterdeck, self.useddeck],
            ["Hand", "Fight", "Hamster", "Used"],
        ):
            logging.debug(
                "%sdeck size: %s (%s)",
                name,
                len(deck.cards),
                ",".join([c.name for c in deck.cards]),
            )
