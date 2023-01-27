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
- Computer player &  human player
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

# Map

# Locations

# Items
- also things like the totem? Or are they something else?

# Achievements / Badges
- for the human player
