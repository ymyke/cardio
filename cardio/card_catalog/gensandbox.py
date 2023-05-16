#%%
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

minpot, maxpot, _ = Card.get_raw_potency_range()
for pot in range(max(minpot + 1, 0), maxpot):
    c = create_card(pot, exactly=True)
    print(c)

# c = create_card(55, exactly=True)
# print(c)

# %%
from cardio.card_catalog import create_noname_card, create_noname_cards
from cardio.card_catalog.query_openai import add_names_to_cards
cards = create_noname_cards([10, 20, 22], exactly=True)
add_names_to_cards(cards)
for c in cards:
    print(c)
    print()


#%%
from cardio.card_catalog.query_openai import query_openai
res = query_openai("""
Card(name='1', power=0, health=1, costs_fire=0, costs_spirits=0, has_spirits=1, has_fire=1, skills=[])
Card(name='2', power=1, health=2, costs_fire=1, costs_spirits=0, has_spirits=1, has_fire=1, skills=[skills.Spines]) 
Card(name='3', power=6, health=4, costs_fire=3, costs_spirits=0, has_spirits=1, has_fire=1, skills=[])
Card(name='4', power=1, health=4, costs_fire=2, costs_spirits=0, has_spirits=1, has_fire=1, skills=[])
Card(name='5', power=0, health=1, costs_fire=1, costs_spirits=0, has_spirits=10, has_fire=1, skills=[])
""")
print(res)

#%%
import re
from cardio.card_catalog import create_noname_cards
from cardio.card_catalog.query_openai import query_openai

cards = create_noname_cards([100, 100, 200, 200], exactly=False)
for i, c in enumerate(cards):
    c.name = str(i)
query = "\n".join(repr(c) for c in cards)
print(query)
print()

res = query_openai(query)
lines = res.split("\n")
for line in lines:
    i, rest = line.split(":")
    i = int(re.sub(r'[^\d]', '', i))
    name, rest = rest.split("[")
    name = name.strip()
    name = re.sub(r'[^A-Za-z ]', '', name)
    desc = rest.split("]")[0]
    desc = re.sub(r'[^A-Za-z ,"\']', '', desc)
    print(i, name, desc)
    cards[i].name = name
    cards[i]._openai_desc = desc
print()
for c in cards:
    print("{")
    s = "# " + "\n# ".join(str(c).split("\n"))
    print(s)
    print(f"'desc': '{c._openai_desc}',")
    print(f"'card': {repr(c)},")
    print("},")
    print()




# Need to register??
# # if not registered:
# add_name(card)
# # add card to register
# # else:
# #    look up card in register
# return card

# %%
