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
        (GridPos(0, 1), Card("Steed", 1, 10, 1)),
        (GridPos(1, 0), Card("Dog", 1, 5, 1)),
        (GridPos(0, 0), Card("Mouse", 1, 1, 1)),
    ],
)

tv = tui.TUIFightVnC(debug=True, grid=session.grid)
session.view = tv
session.humanplayer.spirits = 3
tv.handle_fight(computerstrategy=cs)
tv.close()
