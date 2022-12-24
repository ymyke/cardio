from typing import Optional
from . import session, Deck
from .card_blueprints import create_cards_from_blueprints
from .agent_strategies import AgentStrategy

# FIXME What exactly it the purpose of this module? Should the functions here be moved
# to session.py?


def handle_fight(
    computerstrategy: AgentStrategy, humanstrategy: Optional[AgentStrategy] = None
) -> None:

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
        # Computer plays cards:
        # (This can include more "world-style" cards such as trees or boulders etc.)
        # FIXME
        computerstrategy.play_cards(session.grid, turn_number)

        # Human draws card(s):
        # FIXME Need some view interaction here
        # FIXME And some strategy
        # drawncard = ...  # from fightdeck or hamsterdeck
        # handdeck.add_card(drawncard)

        # Human plays card(s):
        # FIXME Need some view interaction here
        # FIXME And some strategy
        if humanstrategy is not None:
            humanstrategy.play_cards(session.grid, turn_number)
        else:
            pass  # FIXME Need some interactive code here
        # FIXME ^ Should this thing also get the decks?

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
    session.humanagent.deck.cards = useddeck.cards + handdeck.cards + fightdeck.cards
    # FIXME Remove all the hamsters
    session.humanagent.deck.reset_cards()
