# Grid
↓↓↓↓  <- 0/computer
☐☐☐☐  <- 1/computer
☐☐☐☐  <- 2/human

# Card Slots??
- QQ: Have some Slot class, which would enable to do something like `slot.is_empty()`
  instead of checking for `None`?

# Cards
- Attributes: power, health, (inner) fire, spirits (what they leave implicitly)
- Cost: number of fires or spirits
- have meta information for curation, likes etc. -- maybe also stats?
- QQ: Tribes?

# Card Blueprints
- Used to instantiate concrete cards from.

# Skills

# Decks

# Special behaviors
- "Note that some cards have symbols in place of their Power, which represent a variable
  number. For instance, the Worker Ant and Ant Queen have Ants power, which changes
  depending on the number of ants in play. These symbols are defined as special
  behaviours and not sigils."

# Agents
- Computer player &  human player -- QQ: Maybe only humanplayer in the future and call
  it simply player? Because in the meantime, the human and computer players are very
  different.
- The agents behind:
  - Computer: 
    - name -- can be a global constant / hardcoded
    - ~~no lives -- human either makes it to the end or not~~
    - ~~no damage~~
    - ~~no deck~~
  - Human:
    - name
    - lives -- number of fights he can lose until game is over
    - ~~no damage -- only relevant in fights~~
    - score & stats...
    - gems
    - deck
    - items
    - card archive(?) -- all cards she has ever discovered
- During a fight:
  - Computer:
    - name -- can be different, esp. for boss fights
    - lives -- usually just 1, but bosses have 2, although more like levels in actuality
    - damage (see separate discussion below)
  - Human:
    - damage (see separate discussion below)
    - 4 fight card decks -- they're currently in FightVnC directly...

# Damage
option 1: both agents track:
- computer.damage - human.damage > 5 -> human wins
- human.damage - computer.damage > 5 -> computer wins
- => need access to the other agent to determine state
- overflow damage anything beyond 5

option 2: only human tracks: 
- human.damage > 5 -> computer wins
- human.damage < -5 -> human wins

option 3: one common game state w/o agents in FightVnC: <- Favorite! ⭐
- human_damage: >5 => human lost; <-5 => human won

# Gems
- 💎

# Boss fights
- Need a different model in Fight.handle_round_of_fight -- surely also elsewhere, e.g.
  in Agent or so.

# ComputerStrategy
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

# Run
- One run through the game.
- Runs are fully predetermined based on some seed, i.e., they don't adapt based on the
  player's behavior in any way.
- Runs are indefinite. A player gets as far as she gets.
  - How to meaure how far a player came? Simply by number of locations pased? Or
    something more clever?

# Map
- The map contains all the locations and paths in a run.
- Naturally, the game only shows the map segment that currently fits on the screen. 
- After the player has visited a location, she can chose the next location on the map.
  The map always shows the maximum information, i.e., with each visited location the
  next paths and locations are added to the map and shown to the player.

# Location
- One Location on the map. Contains everything it needs to handle that location.
- E.g., FightLocation:
  - ComputerStrategy including cards
  - Computer player initial values
- A location has a seed and a distance (steps from the start) attribute, which are used
  to generate the location. The seed is derived from an original seed for the entire
  run.

# Items
- also things like the totem? Or are they something else?

# Achievements / Badges
- for the human player

# Misc
- Upgrading the game should invalidate all running/saved runs.