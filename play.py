import logging
import argparse
from cardio import gg, HumanPlayer
from cardio.run import Run
from cardio.tui.mapview import TUIMapView
from cardio.locations.location_directory import view_directory
from cardio.blueprints import thecatalog
from cardio import jason

logging.basicConfig(level=logging.DEBUG)


def create_new_player() -> HumanPlayer:
    hp = HumanPlayer(name="Schnuzgi", lives=1, spirits=3)
    # HUMAN_START_CARDS = ["Church Mouse", "Weasel", "Lynx", "Porcupine"]
    # startcards = thecatalog.find_by_names(HUMAN_START_CARDS).instantiate()
    startcards = thecatalog.find_by_potency_range(3, 4).instantiate()
    startcards = [c for c in startcards if c.costs_fire + c.costs_spirits <= 2]
    # FIXME ^ Better use net potency here too.
    hp.collection.cards = startcards
    return hp


# ----- command line arguments -----

parser = argparse.ArgumentParser()
parser.add_argument("--reset", action="store_true", help="Delete save files")
args = parser.parse_args()

if args.reset:
    jason.reset_all()

# ----- main -----

run = None

try:  # Existing game/player?
    gg.humanplayer, run = jason.load_all()
except FileNotFoundError:  # New game/player
    logging.debug("No save file found. Starting new game")
    gg.humanplayer = create_new_player()

while True:  # Forever start new runs:
    if not run or not run.is_on:
        run = Run()

    if run.current_rung == 0:  # Starting a new run:
        # Pick random cards from collection for the deck:
        gg.humanplayer.collection.shuffle()
        gg.humanplayer.deck.cards = gg.humanplayer.collection.draw_cards(4)

    jason.save_all(gg.humanplayer, run)
    mapview = TUIMapView(run, debug=True)

    while run.is_on:  # Visit locations in run:
        chosen_loc = mapview.get_next_location()
        mapview.move_to(chosen_loc)
        run.move_to(chosen_loc)
        view = view_directory[type(chosen_loc)]  # type: ignore
        run.is_on = chosen_loc.handle(view)
        jason.save_all(gg.humanplayer, run)

    # Run is over:
    # FIXME Maybe do some other stuff here, like saying something to the user, showing
    # run stats, somehow add run stats to player's history, etc.
    mapview.close()
    # Add deck back into collection:
    for card in gg.humanplayer.deck.cards:
        gg.humanplayer.collection.add_card(card)
    gg.humanplayer.deck.cards = []
