First up:
- 1 fight between 2 cards.

Grid, e.g.:
↓↓↓↓  <- prepper
☐☐☐☐  <- opponent -- better computer? because opponent has a different meaning already?
☐☐☐☐  <- player -- better human?  
// ^ FIXME Need to rename these?
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
- Important: A card in a deck is also something like a blueprint for a card that is on
  the grid. Once it leaves the grid, the original values need to be restored!
- Bones!!!

Sigils
- can evolve! I.e., need to track their own states as to when played etc. (???)
- how to implement?
  - callback hooks and sigil handlers?
  - mixins?
  - ...?


Special behaviors
- "Note that some cards have symbols in place of their Power, which represent a variable
  number. For instance, the Worker Ant and Ant Queen have Ants power, which changes
  depending on the number of ants in play. These symbols are defined as special
  behaviours and not sigils."

Card Blueprints
- Used to instantiate concrete cards from. -- Are those templates or rather subclasses?
  -- I think subclasses. 

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
- Or BaseAgent & PlayerAgent & OpponentAgent?
- Or playeragent and computeragent?

OpponentPlayerBehavior
- When he brings which cards into play.
- Maybe also when he does other things, e.g., if he also has items available.

Map

Locations

Items
- also things like the totem? Or are they something else?
