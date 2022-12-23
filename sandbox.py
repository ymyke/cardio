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

handlers.handle_fight()


#%% -------------------- Lifecycle of decks in a run --------------------
from cardio.card_blueprints import create_cards_from_blueprints, create_card_from_blueprint
from cardio.deck import Deck

# Starter deck is for an entire run.
starterdeck_names = ["Koala", "Weasel", "Lynx", "Porcupine"]

# Start of the run: Build maindeck out of starterdeck_names:
maindeck = Deck(create_cards_from_blueprints(starterdeck_names))

# During the run, more cards can get added to maindeck upon certain events on the map:
maindeck.add_card(create_card_from_blueprint("Weasel"))

# When a fight happens, 4 decks get created:
# - fightdeck: copy of maindeck
# - handdeck: the current hand, initially with 3(?) cards from the fight deck and 1 card
#   from the hamster deck
# - hamsterdeck: with all the helper cards
# - useddeck: with all the dead (or discarded?) cards (except cards from the
#   hamsterdeck)
fightdeck = Deck()
fightdeck.cards = maindeck.cards
fightdeck.shuffle()
hamsterdeck = Deck(create_cards_from_blueprints(["Hamster"]*10))
handdeck = Deck(fightdeck.draw_cards(3))
handdeck.add_card(hamsterdeck.draw_card())
useddeck = Deck()

# At the end of the fight, the decks get recombined to the maindeck and whatever card
# stats/statuses that need to get reset will get reset:
maindeck.cards = useddeck.cards + handdeck.cards + fightdeck.cards
maindeck.reset_cards()


#%%
from cardio import Agent
a = Agent("A", 1, 1, 1)
a = Agent("B", 1, 1, 1)
# FIXME Check if they share the same deck attribute or not

# %%
