# %%
import logging
from cardio import Card, Sigil, handlers, session
logging.basicConfig(level=logging.DEBUG)

session.setup()
# session.view.non_blocking = True

# Add some stuff:
session.grid[0][1] = Card(name="Steed", initial_power=2, initial_health=10)
session.grid[2][0] = Card(
    name="Cat",
    initial_power=1,
    initial_health=3,
    sigils=[Sigil.INSTANTDEATH, Sigil.SOARING],
)
session.grid[1][0] = Card(name="Dog", initial_power=2, initial_health=5)

handlers.play_game()
