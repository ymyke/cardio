import logging
from cardio import gg, HumanPlayer
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.run import Run
from cardio.tui.mapview import TUIMapView
from cardio.locations.location_directory import view_directory

logging.basicConfig(level=logging.DEBUG)

### Start menu: Create new or load existing player | start new run

### If create new player:
humanplayer = HumanPlayer(name="Schnuzgi", lives=1, spirits=3)
HUMAN_START_CARDS = ["Church Mouse", "Weasel", "Lynx", "Porcupine"]
humanplayer.deck.cards = create_cards_from_blueprints(HUMAN_START_CARDS)
gg.humanplayer = humanplayer

### If load player:
# (Load and just use the main deck the player has.)

### Start new run:
run = Run()  # <- This generates a new seed
# (or load seed + current location + player state if existing game is being continued)


### While not game over:
mapview = TUIMapView(run, debug=True)
game_on = True
while game_on:
    chosen_loc = mapview.get_next_location()
    mapview.move_to(chosen_loc)
    run.move_to(chosen_loc)
    view = view_directory[type(chosen_loc)]  # type: ignore
    game_on = chosen_loc.handle(view)


### Game over:
###   ...
