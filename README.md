
# Architectural considerations

- Add some draw_strategy param to the fight handler so the humanagent can be automated
  for tests? -- That way it would be warranted for both agents types to have
  strategties.
- Get rid of the `Line`s.
- Get rid of the grid (or most of it) and track positions in the cards directly?
- Get rid of the decks and track the decks as states in the cards. Then there would just
  be a CardCollection with each agent. Card states would be: maindeck, hamsterdeck,
  hand, used or so. At the end of the fight, all hamster cards would be removed. (QQ:
  Where would the hamster cards come from?) (Also, there would be no shuffle method any
  longer but just a draw method which would draw random card(s) from a specific deck.)
- Dependency chaos?
  - Draw all modules and their dependencies and think about them.
  - Should cards have a game attribute which they use to query the world (e.g., who the
    opposing agent is) and to update the world (instead of the view directly)?

# Todo

- Implement some skills that have an influence on the decks (e.g., fertility, Ouroboros,
  unkillable, ...) and see if they work well with the current deck implementation.
- Write tests for all existing classes and all card characteristics and sigils.

# Curses

- https://inventwithpython.com/pygcurse/tutorial/

# Game related

- https://inscryption.fandom.com/wiki/Cards
- https://inscryption.fandom.com/wiki/Sigils