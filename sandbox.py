# %%
import logging
import cardio.session as session
import cardio.handlers as handlers

logging.basicConfig(level=logging.DEBUG)

session.setup(prefill=True)
# session.view.non_blocking = True

handlers.play_game()
