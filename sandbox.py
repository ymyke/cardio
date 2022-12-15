# %%
import logging
import cardio.session as session
import cardio.commands as commands
import cardio.handlers as handlers

logging.basicConfig(level=logging.DEBUG)

session.bootstrap(prefill=True)

handlers.handle_turn(commands.HandleTurn())
