# %%
import logging
from cardio import Card, session, GridPos
from cardio.tui import tui
from cardio.computer_strategies import Round0OnlyStrategy

logging.basicConfig(level=logging.DEBUG)

session.setup()

cs = Round0OnlyStrategy(
    grid=session.grid,
    cards=[
        # type:ignore
        (GridPos(0, 1), Card(name="Steed", initial_power=1, initial_health=10)),
        (GridPos(1, 0), Card(name="Dog", initial_power=1, initial_health=5)),
    ],
)

tv = tui.TUIViewAndController(debug=True, grid=session.grid)
session.view = tv
tv.handle_fight(computerstrategy=cs)
tv.close()
