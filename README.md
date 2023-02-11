# Next up

- Use redraw_view more extensively/elsewhere.

- MVC: Could I have the basic FightVnC, which takes a Controller object, that does the
  playcard stuff etc. and an Animator object that makes all the animations available
  that are necessary?
  - QQ: How many of the controller-related functions in FightVnC are actually
    subclassed? How much subclassing is necessary there?
  - How many methods could really be moved to the Animator class? I.e., how many methods use information from the model?
  - Is the differentiation between methods that have r/o access to the model and ones that have r/w access?
- In `Card`: Should all the methods that need access to the vnc simply take a vnc object
  as a paramter?

- Maybe try new ways of separating MVC? Play around w 2 screens...
- Can we more the business logic to fightvnc and invoke it via super?

- How can we test Skill.FERTILITY?

- Bug: When placing a card, it doesn't necessarily have to be placed on the last
  sacrifice. Can be placed somewhere else!

- Finish fight:
  - Start by creating some computer strategy
  - Finish when one party won
  - => Have a new starting point for this. g.py or so.
- Start thinking about the broader game, map, ...
- Implement some skills that have an influence on the decks (e.g., fertility, Ouroboros,
  unkillable, ...) and see if they work well with the current deck implementation.

# Architectural considerations

- Should I rethink the whole view after all? Simply redraw the entire model whenever
  necessary. But in the buffer and/or on a second screen so there is no flicker? (Is
  that possible w/ asciimatics?) -- Can I work with 2 asciimatics screens (and maybe
  some buffer to copy contents between the two) and simply do full screen refreshes
  whenever something happens and via that mechanism more properly separate the model
  from the view?
  - Should there be a plain view that does nothing other than display the current state
    of the model _and_ a collection of animations that can be called? -- But there's
    also all the controlling part with keyboard inputs etc. ...
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
- I think ComputerStrategy should be part of ComputerAgent and ComputerAgent should be
  part of the fightcontroller initiator, since it only has relevance in fights.
  (- Also, maybe there is no need for a ComputerAgent class in the end?)
- Add some draw_strategy param to the fight handler so the humanagent can be automated
  for tests? -- That way it would be warranted for both agents types to have
  strategties.
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

- Can we add the new fire and spirits placement logic to the hypo-driven tests? Maybe
  using the placement mgr in the hypo test?
- Terminology: agent vs player everywhere? Which is the better term? Make it consistent.
- Look for all `grid.*=None` and use `remove_card` instead.
- Write tests for all card characteristics and skills.
- Edge case: What if the grid is empty or powerless at some point during a fight? Who
  will win?
- Reduce the number of places the session module gets imported to a sensible minimum.
- Add items

# More animations

- When an agent loses a health bar.
- Animate overflow damage that turns into gems.
- More animations for certain skills?

# Ideas: All prios

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
  Can the TSM be used somehow to that end?
- Corveaux special ability/animal? Can consume ghosts/souls/spirits and release them as
  blood/energy/...?
- Have floor tiles with special effects? I.e., more strength if a create is on it?
- Can there be shops where you can buy stuff, including additional lives?
- Maybe spirits could be persistent and can be taken over to the next fight?
- Could cards have an icon that gets displayed, e.g., top right of the card? Then only
  pick animal (and plant?) types that have an emoji?

# Low Prio Ideas

- For convenience: Placement cursor could pick the first slot that makes sense for the
  current card, i.e., the first empty slot for cards with `costs_fire == 0`.
- Mark cards in a color other than blue.
- Don't show costs in computer cards.

# Low Prio Todos

- Make fire effect work on WSL.

# Game related

- https://inscryption.fandom.com/wiki/Cards
- https://inscryption.fandom.com/wiki/Sigils
- "Cardio was massively inspyred by Inscryption. Buy it and play it!"

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