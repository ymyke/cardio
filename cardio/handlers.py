from typing import Optional, List
import logging
from . import session, Deck
from .card_blueprints import create_cards_from_blueprints
from .agent_strategies import AgentStrategy, HumanAgentStrategy

# FIXME What exactly it the purpose of this module? Should the functions here be moved
# to session.py?


def log_decks(decks: List[Deck]):
    """Assumes decks to be passed in order of Hand, Fight, Hamster, Used."""
    for deck, name in zip(decks, ["Hand", "Fight", "Hamster", "Used"]):
        logging.debug(
            "%sdeck size: %s (%s)",
            name,
            len(deck.cards),
            ",".join([c.name for c in deck.cards]),
        )


def handle_fight(
    computerstrategy: AgentStrategy, humanstrategy: Optional[HumanAgentStrategy] = None
) -> None:

    # FIXME Which of the code in here should be elsewhere? E.g., in a model or in a
    # view? E.g., the code around decks should maybe be in a model?

    # --- Prepare the decks ---
    # When a fight happens, 4 decks get created:
    # - fightdeck: copy of maindeck
    # - handdeck: the current hand, initially with 3(?) cards from the fight deck and 1
    #   card from the hamster deck
    # - hamsterdeck: with all the helper cards
    # - useddeck: with all the dead (or discarded?) cards (except cards from the
    #   hamsterdeck)
    fightdeck = Deck()
    fightdeck.cards = session.humanagent.deck.cards
    fightdeck.shuffle()
    hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
    handdeck = Deck(fightdeck.draw_cards(3))
    handdeck.add_card(hamsterdeck.draw_card())
    useddeck = Deck()

    # FIXME:
    # AND/OR: Should any played card be moved from the handdeck to the useddeck anyway
    # and then nothing additional is needed? It simply gets removed from the grid when
    # it is killed and that's it? -- What about hards that can re-occur in the handdeck?
    #
    #  Options:
    # - Add these to the agent.
    # - Add them to the session.
    # - Have some Fight object? <= doesn't help, I believe
    # - Have handle_turn as a function within this function?
    # - Also see the disucssions in README about this.

    # --- Run the fight ---
    fighting = True
    turn_number = 0
    while fighting:
        log_decks([handdeck, fightdeck, hamsterdeck, useddeck])

        # Computer plays cards:
        # (This can include more "world-style" cards such as trees or boulders etc.)
        # FIXME
        computerstrategy.play_cards(session.grid, turn_number)

        # Human draws card(s):
        # FIXME Need some view interaction here
        # FIXME And some strategy
        # drawncard = ...  # from fightdeck or hamsterdeck
        # handdeck.add_card(drawncard)

        # FIXME The human strategy should return the same thing the interactive
        # functions would return, i.e.: 1) the deck to draw from, 2) which card from the
        # handdeck to play where.

        # Human plays card(s):
        # FIXME Need some view interaction here
        if humanstrategy is not None:
            humanstrategy.add_decks(fightdeck, hamsterdeck, handdeck, useddeck)
            whichdeck = humanstrategy.deck_to_draw_from(turn_number)
            if not whichdeck.is_empty():
                card = whichdeck.draw_card()
                handdeck.add_card(card)
                logging.debug("Human draws %s", card.name)
            # FIXME View needs to update with new card moving to handdeck
            posandcard = humanstrategy.card_to_play_from_hand(turn_number)
            if posandcard is not None:
                pos, card = posandcard
                session.grid[pos.line][pos.slot] = card
                useddeck.add_card(card)
                logging.debug("Human plays %s on %s", card.name, pos)
            else:
                logging.debug("Human plays no card.")
        else:
            # FIXME Need some interactive code here
            # FIXME And when playing a card -- need to check if handdeck is empty?
            # FIXME Move played cards to useddeck -- at least for human player.
            whichdeck = ...  # whichdeck needs to be set
            # View needs to update with new card moving to handdeck
            # Need some code that:
            # - Player picks card from handdeck
            # - If card has cost: Player picks cards on grid to sacrifice until cost is paid
            # - Player plays the new card to a certain grid position
            # - Player can exit process and pick different card at any time

        # Post condition: 0-n new cards have been placed on the grid & player has
        # decided to end his turn.
        # FIXME Need some interaction to end turn

        log_decks([handdeck, fightdeck, hamsterdeck, useddeck])

        # Activate all cards:
        session.grid.playerline.activate()
        session.grid.opponentline.activate()
        session.grid.prepline.prepare()
        session.view.update()

        if session.humanagent.has_lost_life():
            session.humanagent.update_lives_and_health_after_death()
            session.view.computer_wins_fight()
            fighting = False
        if session.computeragent.has_lost_life():
            overflow = session.computeragent.update_lives_and_health_after_death()
            session.view.human_wins_fight()
            # FIXME Do something w overflow damage here -- maybe just store it in the
            # object right in the update_lives_and_health_after_death function but also
            # pass it to the view for some animation?
            fighting = False
        if session.grid.is_empty():
            # QQ: Should this also break when the grid is "powerless", i.e., no cards
            # with >0 power?
            fighting = False

        turn_number += 1

    # --- Clean up after fight ---
    session.humanagent.deck.cards = [
        c
        for c in useddeck.cards + handdeck.cards + fightdeck.cards
        if c.name != "Hamster"
    ]
    session.humanagent.deck.reset_cards()
