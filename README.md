# In this branch


# Next up

- Add more cards
- Add more skills.
- Scoring and difficulty progress:
  - Should there be additional scores in addition to the rung? Something that better
    reflects the difficulty mastered by that run? E.g., number of fights? Or should
    there be a score per fight (maybe something that reflects how hard the fight is)?
  - Refine FightLocation and Computerstrategy so the game becomes harder and harder as
    the rungs increase.
- Save and load game state.
  - Add stats to game state: number of fights won, locations visited, number and which
    cards defeated, which cards confronted with, ... -- could have an instance of each
    "thing" (card, location, etc.) and log the stats with these things (using a special
    Stats class that gets added to each such thing) -- or maybe just the entire run in
    some useful format? (Would replace log and maybe also the stateslogger)
- Smooth "state" changes such as map -> fight, fight won / fight -> map, game over, ...


# MVC Thoughts

(Not sure, how good the thoughts here are...)

- MVC: Could I have the basic FightVnC, which takes a Controller object, that does the
  playcard stuff etc. and an Animator object that makes all the animations available
  that are necessary?
  - QQ: How many of the controller-related functions in FightVnC are actually
    subclassed? How much subclassing is necessary there?
  - How many methods could really be moved to the Animator class? I.e., how many methods
    use information from the model?
  - Is the differentiation between methods that have r/o access to the model and ones
    that have r/w access?
- In `Card`: Should all the methods that need access to the vnc simply take a vnc object
  as a paramter? -- This could work. The methods in Card that should work with or w/o
  vnc could take vnc as an option and just not do the vnc part if no vnc was passed
  (e.g., `_die_silently`).


# Architectural considerations

- Rethink how the session module works. Maybe get rid of it? Maybe have a common way
  tests get set up in a central test module and a way sandbox.py sets up the game and
  get rid of session altogether? -- But would need some module that grants access to
  view to Card class.
  - Sometimes, we inject links to the model to an object (e.g., to grid) and sometimes
    we don't (e.g., humanagent and computeragent in FightVnC). -> Better make this
    consistent?
  - One approach could be: Always use the session. But no code whatsoever in the
    session. Everything gets set up outside of session and gets injected into the
    session module.
- Dependency chaos?
  - Draw all modules and their dependencies and think about them.
  - Should cards have a game attribute which they use to query the world (e.g., who the
    opposing agent is) and to update the world (instead of the view directly)?

# Todo

- Start the game w/ 0 skills.
- QQ: Spirits: keep them between fights (as it is now)? (Maybe have to sacrifice 1 life
  if you want to keep them?)
- In cursor-based views: Flash cursor red when an action is not possible.
- Check for right minimum resolution at the beginning.
- Can we add the new fire and spirits placement logic to the hypo-driven tests? Maybe
  using the placement mgr in the hypo test?
- Terminology: agent vs player everywhere? Which is the better term? Make it consistent.
- Look for all `grid.*=None` and use `remove_card` instead.
- Write tests for all card characteristics and skills.
- Edge case: What if the grid is empty or powerless at some point during a fight? Who
  will win?
- Reduce the number of places the session module gets imported to a sensible minimum.
- Add items? What kinds of items are there? (Can a number of items be derived from
  skills as one-time-skills?)
- Turn all the notes here and in DOMAIN into a Github wiki.
- Check TUI on linux / wsl.

# More animations

- When an agent loses a health bar.
- Animate overflow damage that turns into gems.
- More animations for certain skills?

# Ideas: All prios

- Add titles to locations.
- Location ideas:
  - Card shop: Buy cards for gems
  - Exchange: Change spirits to gems and vice versa
  - Card lottery: Give a card and get a random card in return
  - Card/skill game: Play some little game and the better you are the better the card
    you get (at random) in return. Or the better a skill you can chose? Or the more
    random skills or cards you can choose from. Or... -- Ideas for minigames:
    - Guess the number: The computer picks a number between 1 and 100 and you have to
      guess it. The computer tells you whether your guess is too high or too low.
    - Rock Paper Scissors for x times.
    - Perform calculations ever quicker.
    - Keep up with typing text that gets produced ever faster.
    - Press keys as they appear on screen as quickly as possible.
    - Snakes/Tron
    - Frogger
  - Card buyer: Buy certain cards for gems -- usually higher value cards
  - Card disposer: Allows you to get rid of cards (just 1 maybe) at a cost in gems
  - Card merger: Merge 2 identical cards for double attributes (or, if you don't have
    any pairs, duplicate a card)
  - Card cost mutator: Switch card costs from fire to (many more) spirits and vice
    versa.
  - Locations around items...? Item shop, ...?
  - Treasure location? ✘✘✘ -- Pick one of several digging locations and get a random
    item in return (or nothing).
- Maybe there can be inanimate cards that do not provide a fire? (So: Should cards have
  a `has_fire` attribute that can be 0, 1 or more? Or would this rather be subclasses?)
- Vast range of items: E.g., rucksack 🎒, bigger rucksack 🎒🎒, some item that allows me
  to keep my leftover spirits between fights but that I can also spend to get one-time
  somethingsomething.
- Could shorten the player's name according to its damage. Schnuzgi -> Schnuz -> Schn ->
  ...
- Use asciimatics' arrow as an avatar for the human player? (Or the computer?)
- Display some help output in the lower right corner? Current state of the app, allowed
  keys, unrecognized keys, ...?
- Check out performance of animations: Esp. when running on battery power. -> Add some
  setting that helps speed up / slow down the animations. Then do some self-timing e.g.
  on burning a card that will automatically adjust that setting if necessary (i.e.,
  animation takes too long or too short).
- could cards gain experience with fights and other things and evolve over time (stats
  would be permanent) but also die for real?
- Have a location that allows me to create new cards, combining health, power and
  skills, and give them a name and keep them. -- Or some other mechanism to create new
  cards?
- Terrain and weather conditions etc. that affect the cards?
- Maybe you can lose cards for good in a run -- in a fight? Or as a downside risk when
  going for a particularly strong upgrade? E.g., the stronger the upgrade the higher the
  likelihood to lose the card? -- Then, a save game and game progress score would
  somehow take into account a hash over the entire game to make sure the game has not
  been tampered with? Then only authoritative scores are allowed in leaderboards etc.
  Can the TSE be used somehow to that end? Or some authoritative docker images with the
  software? Of course one option is always to deploy on the web and run it centralized.
  (Yet another option might be to create logs of information with each run (including
  all user choices) that can be used to simulate and verify the run. That way, it can be
  verified if such a run relly exists. (Such a system would still be prone to cheating
  by creating a computer agent that brute force searches for the best run.)) (Maybe this
  could be combined with the code taking a hash over its entire code and game state to
  proof originality of code at a certain point in time? Maybe also combined with some
  proof of humanity (the minigames?) to prevent bots from playing the game?)
- Corveaux special ability/animal? Can consume ghosts/souls/spirits and release them as
  blood/energy/...?
- Have floor tiles with special effects? I.e., more strength if a create is on it?
- Can there be shops where you can buy stuff, including additional lives?
- Maybe spirits could be persistent and can be taken over to the next fight?
- Could cards have an icon that gets displayed, e.g., top right of the card? Then only
  pick animal (and plant?) types that have an emoji?
- Explain locations in the map view? Or have some keystroke that opens explanatory text
  in any view?

# Low Prio Ideas

- Maybe NoLocations can have minor "on the way" events? I.e., gain/lose some gems, ...?
- Hidden locations? I.e., locations that are not revealed until you visit them.
- Randomize player's start cards at the beginning of a run from a set of possible start
  cards.
- For convenience: Placement cursor could pick the first slot that makes sense for the
  current card, i.e., the first empty slot for cards with `costs_fire == 0`.
- Mark cards in a color other than blue.
- Turn marked positions from blue to green when the placement manager is ready to pick.
- Don't show costs in computer cards.
- Different tribes?
- If there are more and more cards, maybe they get some meta information around
  curation, likes, etc.?
- Achievements/badges for the player?
- Upgrading the game should invalidate all running/saved runs.

# Low Prio Todos

- Make fire effect work on WSL.

# Debugging hints

- Call `start_debug_mode` at spots in the code where you'd like to inspect variables
  during execution.
- Call `print(self.stateslogger.create_event())` when debugging the fight controller
  using pdb to show the current state of the game.

# Game related

- https://inscryption.fandom.com/wiki/Cards
- https://inscryption.fandom.com/wiki/Sigils
- "Cardio was massively inspyred by Inscryption. Buy yt and play yt!"

# Other TUI projects

- https://textual.textualize.io/
- http://urwid.org/index.html
- Curses
- https://inventwithpython.com/pygcurse/tutorial/


# UI Architecture options

- Grow my own I: Using asciimatics only for rendering.
- Grow my own II: Using https://github.com/Matthias1590/ConsoleDraw for output.
- Check interactive sample in asciimatics.
- Check https://github.com/a1usha/PyGol.
- Should animations be something like the RayCaster effect?
  - Could it have a reference to parameters that I could control from the outside? I.e.,
	attacker and target?
  - Cf https://stackoverflow.com/questions/68455609/how-to-run-an-asciimatics-animation-only-one-time-in-python


# Asciimatics

- Double buffering: Newly drawn stuff gets drawn to the buffer. A call to
  `screen.refresh()` will display the newly drawn stuff on screen. To clear the screen,
  use `clear_buffer` instead of the simple `clear` to prevent flickering.
- Simple rendering: https://github.com/peterbrittain/asciimatics/blob/master/samples/rendering.py
- How to cycle to different animation: https://github.com/peterbrittain/asciimatics/blob/master/samples/noise.py
- Use bars for scores or other stuff? https://github.com/peterbrittain/asciimatics/blob/master/samples/bars.py
- Use fireworks when won. 
  - Maybe small explosions when a player is hit? Or fireworks, bc they also show where the hit is coming from?
  - https://github.com/peterbrittain/asciimatics/blob/master/samples/particles.py
- Use speechbubbles and the arrow character. https://github.com/peterbrittain/asciimatics/blob/master/samples/basics.py
- Use widgets? https://github.com/peterbrittain/asciimatics/blob/master/samples/contact_list.py
- use the "fall away" effect at the end or the fire effect for cards that die? https://github.com/peterbrittain/asciimatics/blob/master/samples/credits.py
  - (Use figlet effect for new cards coming to the deck?)
- Super fire effect: https://github.com/peterbrittain/asciimatics/blob/master/samples/fire.py
- Use the mouse? https://github.com/peterbrittain/asciimatics/blob/master/samples/interactive.py
- Advanced widgets:
  - https://github.com/peterbrittain/asciimatics/blob/master/samples/forms.py
  - https://github.com/peterbrittain/asciimatics/blob/master/samples/experimental.py
- Use Kaleidoscope for start/welcome screen? or plasma? https://github.com/peterbrittain/asciimatics/blob/master/samples/plasma.py


# Fonts

- Hack NF works well.
- Is there a Consolas NF variant?