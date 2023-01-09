import logging
import sys
import time
import atexit
import copy
from typing import NamedTuple, Optional
from cardio import session, Deck, GridPos, Card
from cardio.agent_strategies import AgentStrategy
from cardio.card_blueprints import create_cards_from_blueprints
from asciimatics.screen import Screen
from asciimatics.paths import Path
from asciimatics.event import KeyboardEvent
from .cards_renderer import (
    draw_slot_in_grid,
    draw_drawdecks,
    draw_screen_resolution,
    draw_drawdeck_highlights,
    draw_handdeck_highlight,
    highlight_card_in_grid,
    gridpos2dpos,
    clear_card_in_grid,
    flash_card_in_grid,
    shake_card_in_grid,
    redraw_card_in_grid,
    activate_card_in_grid,
    burn_card_in_grid,
    BOX_HEIGHT,  # FIXME
    BOX_WIDTH,  # FIXME
)
from . import cards_renderer

# FIXME Todos:
# - Finish fight, e.g. cards that die, ...
# - Add other elements:
#   - separator between grid and hand deck
#   - Switch agent health to agent damage where the difference between the two must be
#     visualized and indicates loss/win if it exceeds 5.
#   - score/health between human and computer
#   - agent state
# - useddeck?
# - More animations needed for Spine and maybe other skills?

# FIXME How would a HumanAgentStrategy (aka automated human) be implemented here?

screen: Screen
# FIXME Should there be some viewsession module or something, which contains the screen
# and maybe other important stuff and can get imported by all the view modules? So we
# don't have to pass around screen...


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
    for deck, name in zip(
        [decks.handdeck, decks.drawdeck, decks.hamsterdeck, decks.useddeck],
        ["Hand", "Fight", "Hamster", "Used"],
    ):
        logging.debug(
            "%sdeck size: %s (%s)",
            name,
            len(deck.cards),
            ",".join([c.name for c in deck.cards]),
        )


def log_grid(grid):
    for line in range(3):
        logging.debug("Grid line %s: %s", line, ", ".join([str(c) for c in grid[line]]))


def d_card_lost_health(card: Card) -> None:
    redraw_card_in_grid(screen, card, session.grid.find_card(card))


def d_card_dies(card: Card) -> None:
    pos = session.grid.find_card(card)
    assert pos is not None, "Trying to burn a card that is not in the grid"
    burn_card_in_grid(screen, card, pos)


def d_prepare_card(card: Card) -> None:
    pos = session.grid.find_card(card)
    assert pos is not None, "Trying to prepare a card that is not in the grid"
    assert pos.line == 0, "Calling prepare on card that is not in prep line"
    startpos = gridpos2dpos(GridPos(0, pos.slot))
    targetpos = gridpos2dpos(GridPos(1, pos.slot))

    clear_card_in_grid(screen, pos)
    draw_slot_in_grid(screen, pos)
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    p = Path()
    p.jump_to(x=startpos.x, y=startpos.y + 1)
    p.move_straight_to(x=targetpos.x, y=targetpos.y, steps=10)
    for x, y in p._steps:
        screen._buffer._double_buffer = copy.deepcopy(buffer)
        screen.refresh()
        cards_renderer.show_effects(
            screen, cards_renderer.render_card_at(screen, card, x, y)
        )


def d_activate_card(card: Card) -> None:
    logging.debug("d_activate_card %s", card.name)
    pos = session.grid.find_card(card)
    assert pos is not None, (
        f"{card.name} gets gets activated and "
        "needs a view update but has no position on the grid"
    )
    activate_card_in_grid(screen, card, pos)


def d_deactivate_card(card: Card) -> None:
    pos = session.grid.find_card(card)
    assert pos is not None, (
        f"{card.name} gets gets deactivated and "
        "needs a view update but has no position on the grid"
    )
    activate_card_in_grid(screen, card, pos, deactivate=True)
    # FIXME: This will break if the card dies between being activated and being
    # deactivated. E.g. due to spine. Furthermore, this will break visually if a card is
    # moved in between. Possible solutions: a) Contect mgr, b) return pos in
    # d_activate_card and pass that pos to the call to d_deactivate_card (and rename to
    # d_deactivate_card_in_gridpos or so?), ...? c) Maybe the little pause we have in
    # d_activate_card is enough and there is no need for d_deactivate_card after all?


def d_card_gets_attacked(target: Card, attacker: Card) -> None:
    pos = session.grid.find_card(target)
    assert pos is not None, (
        f"{target.name} gets attacked by {attacker.name} and "
        "needs a view update but has no position on the grid"
    )
    shake_card_in_grid(screen, target, pos, "h")
    # redraw_card_in_grid(screen, target, pos)


def d_play_computer_card(card: Card, to_pos: GridPos):
    starty = -5
    startx = 50  # FIXME Calc middle of the grid
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    cards_renderer.show_effects(
        screen, cards_renderer.render_card_at(screen, card, x=startx, y=starty)
    )
    p = Path()
    p.jump_to(x=startx, y=starty)
    to_pos = cards_renderer.gridpos2dpos(to_pos)
    p.move_straight_to(x=to_pos.x, y=to_pos.y, steps=5)
    for x, y in p._steps:
        screen._buffer._double_buffer = copy.deepcopy(buffer)
        cards_renderer.show_effects(
            screen, cards_renderer.render_card_at(screen, card, x, y)
        )


def get_keycode(screen) -> Optional[int]:
    """Ignore all mouse events. Return key code."""
    event = screen.get_event()
    if not isinstance(event, KeyboardEvent):
        return None
    if event.key_code == ord("$"):
        sys.exit(0)
    return event.key_code
    # FIXME Add a tiny sleep here (and some do_pause parameter) in case there is no key
    # so the while loops don't load CPU that much?


def handle_human_draws_new_card(decks: Decks) -> None:
    if not decks.drawdeck.is_empty():
        highlights = [True, False]
    elif not decks.hamsterdeck.is_empty():
        highlights = [False, True]
    else:  # both empty
        return

    while True:
        draw_drawdeck_highlights(screen, highlights)
        keycode = get_keycode(screen)
        if keycode == Screen.KEY_LEFT and not decks.drawdeck.is_empty():
            highlights = [True, False]
        elif keycode == Screen.KEY_RIGHT and not decks.hamsterdeck.is_empty():
            highlights = [False, True]
        elif keycode == screen.KEY_UP:
            if highlights[0]:
                card = decks.drawdeck.draw_card()
                d_draw_card_to_handdeck(decks.handdeck, card, "draw")
            else:
                card = decks.hamsterdeck.draw_card()
                d_draw_card_to_handdeck(decks.handdeck, card, "hamster")
            decks.handdeck.add_card(card)
            draw_drawdecks(screen, [decks.drawdeck.size(), decks.hamsterdeck.size()])
            return


def d_place_human_card(card: Card, from_slot: int, to_slot: int):
    startpos = gridpos2dpos(GridPos(4, from_slot))
    targetpos = gridpos2dpos(GridPos(2, to_slot))

    buffer = copy.deepcopy(screen._buffer._double_buffer)
    cards_renderer.show_effects(
        screen, cards_renderer.render_card_at(screen, card, x=startpos.x, y=startpos.y)
    )
    p = Path()
    p.jump_to(x=startpos.x, y=startpos.y)
    p.move_straight_to(x=targetpos.x, y=targetpos.y, steps=10)
    for x, y in p._steps:
        screen._buffer._double_buffer = copy.deepcopy(buffer)
        screen.refresh()
        cards_renderer.show_effects(
            screen, cards_renderer.render_card_at(screen, card, x, y)
        )
    # FIXME Refactor with other move functions
    # FIXME Make a small buffercontroller object


def handle_human_places_card(decks: Decks, grid, card: Card, from_slot: int) -> bool:
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    cursor = 0
    while True:
        screen._buffer._double_buffer = copy.deepcopy(buffer)
        highlight_card_in_grid(screen, GridPos(2, cursor))

        keycode = get_keycode(screen)
        if keycode == Screen.KEY_LEFT:
            cursor = max(0, cursor - 1)
        elif keycode == Screen.KEY_RIGHT:
            cursor = min(grid.width - 1, cursor + 1)
        elif keycode == Screen.KEY_DOWN:
            # FIXME Check if card can be placed at all
            grid[2][cursor] = card
            d_place_human_card(card, from_slot=from_slot, to_slot=cursor)
            decks.useddeck.add_card(card)
            logging.debug("Human plays %s in %s", card.name, cursor)
            # screen._buffer._double_buffer = copy.deepcopy(buffer)
            return True
        elif keycode == Screen.KEY_ESCAPE:
            screen._buffer._double_buffer = copy.deepcopy(buffer)
            return False


def handle_human_plays_card(decks: Decks) -> None:
    # FIXME What if hand is empty?
    buffer = copy.deepcopy(screen._buffer._double_buffer)
    cursor = 0
    while True:
        screen._buffer._double_buffer = copy.deepcopy(buffer)
        if not decks.handdeck.is_empty():
            draw_handdeck_highlight(screen, cursor)

        keycode = get_keycode(screen)
        if keycode == Screen.KEY_LEFT:
            cursor = max(0, cursor - 1)
        elif keycode == Screen.KEY_RIGHT:
            cursor = min(decks.handdeck.size() - 1, cursor + 1)
        elif keycode == Screen.KEY_UP:
            # FIXME Check if card is playable at all
            # Don't pick the card yet (i.e., don't remove it from the deck yet) because
            # the player might still abort the placing  of the card:
            card = decks.handdeck.cards[cursor]
            res = handle_human_places_card(decks, session.grid, card, cursor)
            if res:
                decks.handdeck.pick_card(cursor)
                cursor = min(decks.handdeck.size() - 1, cursor)
                d_redraw_handdeck(decks.handdeck, cursor)
                buffer = copy.deepcopy(screen._buffer._double_buffer)
            else:
                # Otherwise, we return bc the process was aborted by the user and won't
                # update the cursor.
                # FIXME Implement this w an exception rather than the True/False
                # mechanics?
                pass
            # FIXME ^ Use some update_buffer method here once we have the
            # buffercontroller object.
            cursor = min(decks.handdeck.size() - 1, cursor)
        elif keycode in (ord("i"), ord("I")):
            pass  # FIXME Inventory!
        elif keycode in (ord("c"), ord("C")):
            screen._buffer._double_buffer = copy.deepcopy(buffer)
            return


def handle_round_of_fight(round_num, decks: Decks, computerstrategy: AgentStrategy):
    log_decks(decks)

    # Play computer cards and animate how they appear:
    for pos, card in computerstrategy.cards_to_be_played(session.grid, round_num):
        print(pos, card)
        d_play_computer_card(card, pos)
    # Now also place them in the model:
    computerstrategy.play_cards(session.grid, round_num)  

    # Let human draw a card:
    handle_human_draws_new_card(decks)

    # Let human play card(s) from handdeck or items in his collection:
    handle_human_plays_card(decks)

    log_decks(decks)
    log_grid(session.grid)

    # Activate all cards:
    session.grid.activate_line(2)
    session.grid.activate_line(1)
    session.grid.prepare_line()
    # session.view.update()  # FIXME

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

    log_grid(session.grid)
    return True


def setup_decks() -> Decks:
    drawdeck = Deck()
    drawdeck.cards = session.humanagent.deck.cards
    drawdeck.shuffle()
    hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"] * 10))
    return Decks(drawdeck, hamsterdeck, Deck(), Deck())


# FIXME Add some border around the whole screen when the human presses "N" until he has
# to do something again?


def d_redraw_handdeck(handdeck: Deck, from_index: int):
    pos = gridpos2dpos(GridPos(4, from_index))
    screen.clear_buffer(
        Screen.COLOUR_WHITE,
        0,
        0,
        x=pos.x,
        y=pos.y,
        w=screen.width - pos.x,
        h=BOX_HEIGHT,
    )
    for i, card in list(enumerate(handdeck.cards))[from_index:]:
        cards_renderer.show_effects(
            screen, cards_renderer.render_card_in_grid(screen, card, GridPos(4, i))
        )
    screen.refresh()


def d_draw_card_to_handdeck(handdeck: Deck, card: Card, whichdeck: str):
    # FIXME Maybe implement differently in the future when cards have states: can use
    # those states for `whichdeck`.

    starty = cards_renderer.DRAW_DECKS_Y - 2
    # FIXME ^ When we put `-1` here, there will be a leftover `-` on the screen after
    # moving the cards. How to get rid of that?
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
        screen.refresh()
        cards_renderer.show_effects(
            screen, cards_renderer.render_card_at(screen, card, x, y)
        )


def handle_fight(computerstrategy: AgentStrategy):

    # --- Prepare the fight ---
    # Show empty grid:
    for linei in range(3):
        for sloti in range(4):
            draw_slot_in_grid(screen, GridPos(linei, sloti))

    # FIXME Some pause here?

    # Set up human's decks and show the hand deck:
    decks = setup_decks()
    draw_drawdecks(screen, [len(decks.drawdeck.cards), len(decks.hamsterdeck.cards)])
    for _ in range(3):
        card = decks.drawdeck.draw_card()
        d_draw_card_to_handdeck(decks.handdeck, card, "draw")
        decks.handdeck.add_card(card)

    card = decks.hamsterdeck.draw_card()
    d_draw_card_to_handdeck(decks.handdeck, card, "hamster")
    decks.handdeck.add_card(card)
    draw_drawdecks(screen, [len(decks.drawdeck.cards), len(decks.hamsterdeck.cards)])

    # --- Run the fight ---
    fighting = True
    round_num = 0
    while fighting:
        fighting = handle_round_of_fight(
            round_num, decks, computerstrategy=computerstrategy
        )
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
# FIXME Use something like the Fight class with calls to a view object -- similar to how
# it is/was done in the Card class, e.g., when activating a class?
