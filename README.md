# Next up

- Fight:
  - Finish fight, e.g. cards that die, ...
  - Add other elements:
    - Switch agent health to agent damage where the difference between the two must be
      visualized and indicates loss/win if it exceeds 5.
    - score/health between human and computer
    - agent state
  - More animations needed for Spine and maybe other skills?
- Interactive UI
  - All fixmes is fightvnc and tuivnc
- Blood costs (Or some other concept? Rations? Energy? Karma? ...?)
- Bones (other name? Spirits? Essence? Soul? ...?)

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
- Check out performance of animations: Esp. when running on battery power. -> Add some
  setting that helps speed up / slow down the animations. Then do some self-timing e.g.
  on burning a card that will automatically adjust that setting if necessary (i.e.,
  animation takes too long or too short).

# Todo

- Look for all `grid.*=None` and use `remove_card` instead.
- Implement some skills that have an influence on the decks (e.g., fertility, Ouroboros,
  unkillable, ...) and see if they work well with the current deck implementation.
- Write tests for all existing classes and all card characteristics and sigils.
- Edge case: What if the grid is empty or powerless at some point during a fight? Who
  will win?
- Display some help output in the lower right corner? Current state of the app, allowed keys, unrecognized keys, ...?

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