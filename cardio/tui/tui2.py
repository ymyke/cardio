import time
import atexit
import copy
from typing import NamedTuple
from cardio import session, Deck, GridPos, Card
from cardio.card_blueprints import create_cards_from_blueprints
from asciimatics.screen import Screen
from asciimatics.paths import Path
from .cards_renderer import draw_slot_in_grid, draw_drawdecks, draw_screen_resolution
from . import cards_renderer


screen: Screen


def start_screen(debug: bool = False) -> None:
    global screen
    screen = Screen.open(unicode_aware=True)
    if debug:
        draw_screen_resolution(screen)
    atexit.register(close_screen)


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


def d_draw_card_to_handdeck(handdeck: Deck, card: Card, whichdeck: str):
    # FIXME Maybe implement differently in the future when cards have states: can use
    # those states for `whichdeck`.

    starty = cards_renderer.DRAW_DECKS_Y
    if whichdeck == "draw":
        startx = cards_renderer.DRAW_DECKS_X
    else:
        startx = cards_renderer.DRAW_DECKS_X + cards_renderer.BOX_WIDTH + 2
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    cards_renderer.show_effects(
        screen, cards_renderer.render_card_at(screen, card, x=startx, y=starty)
    )
    p = Path()
    p.jump_to(x=startx, y=starty)
    to_pos = cards_renderer.gridpos2dpos(GridPos(4, len(handdeck.cards)))
    p.move_straight_to(x=to_pos.x, y=to_pos.y, steps=5)
    for x, y in p._steps:
        screen._buffer._double_buffer = copy.deepcopy(buffer)
        cards_renderer.show_effects(
            screen, cards_renderer.render_card_at(screen, card, x, y)
        )


def handle_fight():

    # --- Prepare the fight ---
    # Show empty grid:
    for linei in range(3):
        for sloti in range(4):
            draw_slot_in_grid(screen, GridPos(linei, sloti))

    # FIXME Some pause here?

    # Set up human's decks and show the hand deck:
    decks = setup_decks()
    draw_drawdecks(screen)
    for _ in range(3):
        card = decks.drawdeck.draw_card()
        d_draw_card_to_handdeck(decks.handdeck, card, "draw")
        decks.handdeck.add_card(card)
    card = decks.hamsterdeck.draw_card()
    d_draw_card_to_handdeck(decks.handdeck, card, "hamster")
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
