import logging
from typing import NamedTuple
from cardio import Deck, session
from cardio.card_blueprints import create_cards_from_blueprints


class Decks(NamedTuple):
    # QQ: Maybe unnecesary if I refactor decks implicitly via some `state` attribute in
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


def setup_decks() -> Decks:
    drawdeck = Deck()
    drawdeck.cards = session.humanagent.deck.cards
    drawdeck.shuffle()
    hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
    return Decks(drawdeck, hamsterdeck, Deck(), Deck())
