import logging
from cardio import Card, session, GridPos, HumanPlayer, Grid
from cardio.card_blueprints import create_cards_from_blueprints
from cardio.tui import tui
from cardio.computer_strategies import Round0OnlyStrategy

logging.basicConfig(level=logging.DEBUG)

### Start menu: Create new or load existing player | start new run

### If create new player:
humanplayer = HumanPlayer(name="Schnuzgi", lives=1, spirits=3)
HUMAN_START_CARDS = ["Church Mouse", "Weasel", "Lynx", "Porcupine"]
humanplayer.deck.cards = create_cards_from_blueprints(HUMAN_START_CARDS)
session.humanplayer = humanplayer

### If load player:
# (Load and just use the main deck the player has.)

### Start new run:

### Generate new run/map (or load old map if existing game is being continued)
# (Also creates/chooses a computer strategy for each fight.)

### While not game over:
###   Display map
###   Choose path => next location
###   Handle location

### If fight:
# (cs = run.current_location.get_computerstrategy() or something -- or maybe better:
# run.current_location.handle() where current_location is a Location object and in case
# of a fight a FightLocation object with a computerstrategy attribute.)
# TODO Implement Run and Location classes next?
grid = Grid(4)
cs = Round0OnlyStrategy(
    grid=grid,
    cards=[
        # type:ignore
        (GridPos(0, 1), Card("Steed", 1, 10, 1)),
        (GridPos(1, 0), Card("Dog", 1, 5, 1)),
        (GridPos(0, 0), Card("Mouse", 1, 1, 1)),
    ],
)
vnc = tui.TUIFightVnC(debug=True, computerstrategy=cs, grid=grid)

# Stick information into session:
session.vnc = vnc
session.grid = grid  # TODO Maybe have this only in the vnc (and computerstrategy) and not separately?

vnc.handle_fight()
vnc.close()

# ----- End of fight -----

### Game over:
###   ...
