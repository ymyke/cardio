First up:
- 1 fight between 2 cards.

Grid, e.g.:
↓↓↓↓
☐☐☐☐
☐☐☐☐
- But can be flexible
- Needs update function
- PP: The grid controls the cards. The cards don't control themselves. The grid knows
  where each card is. A card does not know where it is.(?) [QQ: What about a sigil that
  affects cards/slots surrounding it???]

Card Slots
- or similar?
- Have some Slot class, which would enable to do something like `slot.is_empty()`
  instead of checking for `None`?


Cards
- can be drawn, played, moved, can attack, ...
- have scores, values, sigils, etc.
- have meta information for curation, likes etc. -- maybe also stats?
- Are sigils best modeled as something like side effects or similar? -- Also for stuff like overflow damage etc.?
- Sigils:
  - can evolve! I.e., need to track their own states as to when played etc.

Card Blueprints
- Used to instantiate concrete cards from. -- Are those templates or rather subclasses?
  -- I think superclasses. 

Decks
- Player
  - Draw
    - Main
    - Squirrels etc.
  - Hand
- Enemy
  - Draw vs hand

BasePlayer
- PlayerPlayer or OpponentPlayer

OpponentPlayerBehavior
- When he brings which cards into play.
- Maybe also when he does other things, e.g., if he also has items available.

Map

Locations

Items
- also things like the totem? Or are they something else?
