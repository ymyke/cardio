import logging
from cardio import gg, HumanPlayer
from cardio.run import Run
from cardio.tui.mapview import TUIMapView
from cardio.locations.location_directory import view_directory
from cardio.blueprints import thecatalog
from cardio import jason

logging.basicConfig(level=logging.DEBUG)


def create_new_player() -> HumanPlayer:
    HUMAN_START_CARDS = ["Church Mouse", "Weasel", "Lynx", "Porcupine"]
    hp = HumanPlayer(name="Schnuzgi", lives=1, spirits=3)
    hp.deck.cards = thecatalog.find_by_names(HUMAN_START_CARDS).instantiate()
    return hp


# ----- main -----

try:  # Existing game/player?
    gg.humanplayer, run = jason.load_all()
except FileNotFoundError:  # New game/player
    logging.debug("No save file found. Starting new game")
    gg.humanplayer = create_new_player()
    run = Run()
    jason.save_all(gg.humanplayer, run)

mapview = TUIMapView(run, debug=True)
while True:  # Forever start new runs:
    run_on = True
    while run_on:  # Visit locations in run:
        chosen_loc = mapview.get_next_location()
        mapview.move_to(chosen_loc)
        run.move_to(chosen_loc)
        view = view_directory[type(chosen_loc)]  # type: ignore
        run_on = chosen_loc.handle(view)
        jason.save_all(gg.humanplayer, run)

    # Run is over:
    # FIXME Maybe do some other stuff here, like saying something to the user, showing
    # run stats, somehow add run stats to player's history, etc.
    run = Run()
    jason.save_all(gg.humanplayer, run)
