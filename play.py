import logging
import time
from cardio import gg, HumanPlayer
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.run import Run

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
game_on = True
current_rung = -1
while game_on:
    current_rung += 1
    # TODO Show map
    # TODO Let use choose location -> chosen_loc
    locs = run.get_locations(current_rung)
    chosen_loc = locs[0]
    # 👆 Simply taking the first one, should be chosen interactively TODO
    game_on = chosen_loc.handle()

### Game over:
###   ...
