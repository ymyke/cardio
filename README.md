
# Next up

- Review TODOs and FIXMEs.
- Add more skills.
- Scoring and difficulty progress: Refine FightLocation and Computerstrategy so the game
  becomes harder and harder as the rungs increase. (Refine what is there already.)
  - In FightLocation: Use some new computer strategy that brings more cards into play in
    later rounds of a fight. And that brings overall more and more cards into play as
    the rung increases.
- Add more locations? -- esp. some where you can get new cards as a human.
- Revamp Underdog


# Todo

- Check for right minimum resolution at the beginning.
- Terminology: agent vs player everywhere? Which is the better term? Make it consistent.
  -- Or: Terminology: Player 1 or H and Player C?
- Turn all the notes here and in DOMAIN into a Github wiki.
- Write a proper README here that introduces the project, plugs Inscryption, and
  explains the different parts of the project: code, issues, discussions, wiki, ...
- Remove and regenerate Openai key.

# Architectural considerations

- MVC: Could I have the basic FightVnC, which takes a Controller object, that does the
  playcard stuff etc. and an Animator object that makes all the animations available
  that are necessary?
  - QQ: How many of the controller-related functions in FightVnC are actually
    subclassed? How much subclassing is necessary there?
  - How many methods could really be moved to the Animator class? I.e., how many methods
    use information from the model?
  - Is the differentiation between methods that have r/o access to the model and ones
    that have r/w access?


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