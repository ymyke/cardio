# %%
import logging
from cardio import Card, gg, GridPos
from cardio.tui.locations import tui
from cardio.computer_strategies import Round0OnlyStrategy

logging.basicConfig(level=logging.DEBUG)

gg.setup()

cs = Round0OnlyStrategy(
    grid=gg.grid,
    cards=[
        # type:ignore
        (GridPos(0, 1), Card("Steed", 1, 10, 1)),
        (GridPos(1, 0), Card("Dog", 1, 5, 1)),
        (GridPos(0, 0), Card("Mouse", 1, 1, 1)),
    ],
)

tv = tui.TUIFightVnC(debug=True, computerstrategy=cs, grid=gg.grid)
gg.vnc = tv
gg.humanplayer.spirits = 3
tv.handle_fight()
tv.close()
