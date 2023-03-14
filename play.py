import logging
import time
from cardio import gg, HumanPlayer
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.location import FightLocation

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

### Generate new seed
# (or load seed + current location + player state if existing game is being continued)

# TODO Need some seed handling in the Run class. Should generate seed from root seed
# based on distance. Should maybe also store some history information (either the entire
# map or the seed + current commit hash) and the path taken by the user.

# TODO Also need some code that decides which kind of location will be generated at each
# step. (Maybe Locations have a fixed probability weight and register themselves with
# some location factory or with the run that then chooses among all registered
# locations?)

### While not game over:
###   Display map (create new locations if necessary to fill map segment)
###   Choose path => next location
###   Handle location

### If fight:
# (cs = run.current_location.get_computerstrategy() or something -- or maybe better:
# run.current_location.handle() where current_location is a Location object and in case
# of a fight a FightLocation object with a computerstrategy attribute.)
# TODO Implement Run and Location classes next?

game_on = True
distance = -1
while game_on:
    distance += 1
    l = FightLocation(time.time_ns(), distance, 0)
    game_on = l.handle()

### Game over:
###   ...
