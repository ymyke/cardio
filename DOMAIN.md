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
  where each card is. A card does not know where it is.(?) [QQ: What about a skill that
  affects cards/slots surrounding it???]

Card Slots
- or similar?
- Have some Slot class, which would enable to do something like `slot.is_empty()`
  instead of checking for `None`?


Cards
- have meta information for curation, likes etc. -- maybe also stats?
- Important: A card in a deck is also something like a blueprint for a card that is on
  the grid. Once it leaves the grid, the original values need to be restored!
- Bones!!!
- Blood / cost!!!
- Tribes???

Skills

Special behaviors
- "Note that some cards have symbols in place of their Power, which represent a variable
  number. For instance, the Worker Ant and Ant Queen have Ants power, which changes
  depending on the number of ants in play. These symbols are defined as special
  behaviours and not sigils."

Card Blueprints
- Used to instantiate concrete cards from. -- Are those templates or rather subclasses?
  -- I think templates. 

Decks
- Player
  - Draw
    - Main
    - Squirrels etc.
  - Hand
- Enemy
  - Draw vs hand
- Idea: What about if the human player had 2 decks he could build as he saw fit? So
  whenever he got a new card he could chose whether to add it his A or his B deck. Then
  he could build a squirell deck vs the rest on his own accord or go with some other
  strategy.

Agents

Boss fights
- Need a different model in Fight.handle_round_of_fight -- surely also elsewhere, e.g.
  in Agent or so.

ComputerPlayerBehavior or -Strategy
- When he brings which cards into play.
- Maybe also when he does other things, e.g., if he also has items available.
- A strategy could take some input parameters (initial deck, current grid, turn number,
  ...) and return which cards will be played to which slot. Then the strategy can be as
  constrained or free as necessary:
  - Completely random strategy
  - Adhering to rules or not (i.e., able to place any card anywhere)
  - Needing to work with an initial deck
  - Needing to adhere to placement rules such as blood sacrifices etc.
  - ...

Map

Locations

Items
- also things like the totem? Or are they something else?

Achievements / Badges
- for the human player

Random ideas
- could cards gain experience with fights and other things and evolve over time (stats
  would be permanent) but also die for real?
- Have a location that allows me to create new cards, combining health, power and
  skills, and give them a name and keep them. -- Or some other mechanism to create new
  cards?
- New concepts even for health and power?
- Terrain and weather conditions etc. that affect the cards?
- Maybe you can lose cards for good in a run -- in a fight? Or as a downside risk when
  going for a particularly strong upgrade? E.g., the stronger the upgrade the higher the
  likelihood to lose the card? -- Then, a save game and game progress score would
  somehow take into account a hash over the entire game to make sure the game has not
  been tampered with? Then only authoritative scores are allowed in leaderboards etc.
  Can the TSM be used somehow to that end?
- Corveaux special ability/animal? Can consume ghosts/souls/spirits and release them as
  blood/energy/...?
- Have floor tiles with special effects? I.e., more strength if a create is on it?