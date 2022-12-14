#%%
import logging
logging.basicConfig(level=logging.DEBUG)
from cardio.card import *

a = Card("Steed", 2, 10)
b = Card("Cat", 1, 5)


#%%
b.attack(a)
a.attack(b)
# %%

import logging
logging.basicConfig(level=logging.DEBUG)
from cardio.grid import Grid, GridController, SimpleView
from cardio.card import Card

g = Grid(4)
g[0][1] = Card("Steed", 2, 10)
g[2][0] = Card("Cat", 1, 3)
g[1][0] = Card("Dog", 2, 5)
gv = SimpleView()
gc = GridController(g, gv)


#%%
x = [[1, 2], [3, 4]]
# %%
