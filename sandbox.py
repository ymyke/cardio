#%% Print potency stats:
from cardio.potency_utils import print_potency_stats

print_potency_stats()

"""
- Simplify? 
- Use only raw potency?
"""

#%%
from cardio.blueprints import thecatalog
from cardio import Card
x=thecatalog.find_by_potency_range(3,3)
x[0]._original.pot.gross_normd
# %%
for b in x:
    print(b._original)

#%%
from cardio import Card
Card.get_raw_potency_range()
Card.get_min_max()

# %% Net potency of cards:
from cardio import Card
from cardio.blueprints import thecatalog

mincard, maxcard = Card.get_min_max()

for b in thecatalog.find_by_potency_range(4,4):
    print(b._original)
    print(f"Old calc: {b._original.potency}")
    # print(b._original.raw_potency, b._original.pot.gross_raw)
    print(f"New normd net: {b._original.pot.net_normd} gross: {b._original.pot.gross_normd}")
    print(f"New raw net: {b._original.pot.net_raw} gross: {b._original.pot.gross_raw}")
    print(f"Net normd2gross: {b._original.pot.net_normd2gross}")
    print(f"Net range: [{mincard.pot.net_raw}, {maxcard.pot.net_raw}], gross range: [{mincard.pot.gross_raw}, {maxcard.pot.gross_raw}]")
    print()

# Ex 1:
# Luckicat 🍀 1p 3h
# costs: 🔥🔥🔥🔥🔥 has: 🔥👻 pot: 4
# Old calc: 4
# New normd net: 10 gross: 12   => ⚡
# New raw net: 8 gross: 5       => makes sense

# Ex 2: -- same
# Mermancer  1p 2h
# costs: 👻👻👻👻 has: 🔥🔥👻 pot: 4
# Old calc: 4
# New normd net: 7 gross: 12
# New raw net: 6 gross: 5

# Ex 3: -- same
# Firefawn  1p 3h
# costs: 👻👻👻 has: - pot: 4
# Old calc: 4
# New normd net: 10 gross: 12
# New raw net: 8 gross: 5

# Ex 4: -- ok
# Molemite  1p 1h
# costs: 🔥 has: 🔥👻 pot: 4
# Old calc: 4
# New normd net: 5 gross: 12
# New raw net: 4 gross: 5



# %%
# Let's look at some weaker blueprints:
from cardio import Card
from cardio.blueprints import thecatalog

for b in thecatalog._blueprints:
    c = b._original
    # if c.pot.net_normd < 10 or c.pot.gross_normd < 10:
    if  c.pot.gross_normd < 10:
        print(c)
        print(f"Net normd: {c.pot.net_normd} gross normd: {c.pot.gross_normd}")
        print()