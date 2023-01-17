# Grid
↓↓↓↓  <- 0/computer
☐☐☐☐  <- 1/computer
☐☐☐☐  <- 2/human
- PP: The grid controls the cards. The cards don't control themselves. The grid knows
  where each card is. A card does not know where it is.(?) [QQ: What about a skill that
  affects cards/slots surrounding it???]

# Card Slots??
- Have some Slot class, which would enable to do something like `slot.is_empty()`
  instead of checking for `None`?

# Cards
- have meta information for curation, likes etc. -- maybe also stats?
- Bones!!!
- Blood / cost!!!
- Tribes???

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
    - lives -- usually just 1, but bosses have 2, almost more like levels in actuality
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

# Money / Gems
- QQ: What should be the metaphor for money? 💎?

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

# Random ideas
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
- Can there be shops where you can buy stuff, including additional lives?