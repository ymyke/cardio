from typing import NamedTuple
from cardio import session, Deck, GridPos
from cardio.card_blueprints import create_cards_from_blueprints
from asciimatics.screen import Screen
from .cards_renderer import draw_slot_in_grid

# FIXME Set up and close screen object when loading/unloading.

screen: Screen


def start_screen() -> None:
    global screen
    screen = Screen.open(unicode_aware=True)


def close_screen() -> None:
    global screen
    screen.close()


class Decks(NamedTuple):
    # QQ: Maybe unnecesary if I refactor decks implicitly via some `state` attribute in
    # the card.
    drawdeck: Deck
    hamsterdeck: Deck
    handdeck: Deck
    useddeck: Deck


def log_decks(decks: Decks):
    pass  # FIXME


def handle_round_of_fight(round_num, decks: Decks):
    log_decks(decks)

    # Play computer cards and animate how they appear:

    # Let human draw a card:
    # (Loop for keys ←, →, ↑)
    # And animate the card moving to the end of the hand deck.

    # Let human play card(s) from handdeck or items in his collection:
    # (Loop for keys ←, →, ↑, I, N)
    # (If placing cards: loop for ←, →, ↓, ESC)

    log_decks(decks)

    # Activate all cards:
    session.grid.activate_line(2)
    session.grid.activate_line(1)
    session.grid.prepare_line()
    session.view.update()  # FIXME

    if session.humanagent.has_lost_life():
        session.humanagent.update_lives_and_health_after_death()
        session.view.computer_wins_fight()
        return False
    if session.computeragent.has_lost_life():
        overflow = session.computeragent.update_lives_and_health_after_death()
        session.view.human_wins_fight()
        # FIXME Do something w overflow damage here -- maybe just store it in the
        # object right in the update_lives_and_health_after_death function but also
        # pass it to the view for some animation?
        return False
    if session.grid.is_empty():
        # QQ: Should this also break when the grid is "powerless", i.e., no cards
        # with >0 power?
        return False

    return True


def setup_decks() -> Decks:
    drawdeck = Deck()
    drawdeck.cards = session.humanagent.deck.cards
    drawdeck.shuffle()
    hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
    return Decks(drawdeck, hamsterdeck, Deck(), Deck())

# FIXME Add some border around the whole screen when the human presses "N" until he has
# to do something again?

def handle_fight():

    # Show empty grid:
    for linei in range(3):
        for sloti in range(4):
            draw_slot_in_grid(screen, GridPos(linei, sloti))
    
    # FIXME Some pause here?

    # Set up human's decks and show the hand deck:
    decks = setup_decks()

    for _ in range(3):
        card = decks.handdeck.draw_card()
        d_drawdeck_add_card(
            card, "hand"
        )  # FIXME Maybe implement differently in the future when cards have states: can use those states
        decks.handdeck.add_card(card)
    card = decks.hamsterdeck.draw_card()
    d_drawdeck_add_card(card, "hamster")
    decks.handdeck.add_card(card)

    # --- Run the fight ---
    fighting = True
    round_num = 0
    while fighting:
        fighting = handle_round_of_fight(round_num, decks)
        round_num += 1

    # --- Clean up after fight ---
    session.humanagent.deck.cards = [
        c
        for c in decks.useddeck.cards + decks.handdeck.cards + decks.drawdeck.cards
        if c.name != "Hamster"
    ]
    session.humanagent.deck.reset_cards()


# FIXME Check if anything should be taken over from handlers.
# FIXME Check if anything should be taken over from tui.
# FIXME Check if anything should be taken over from Fight.
