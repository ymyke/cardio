# %%
import logging
import cardio.session as session
import cardio.handlers as handlers

logging.basicConfig(level=logging.DEBUG)

session.bootstrap(prefill=True)
session.view.non_blocking = True
handlers.handle_turn()
handlers.handle_turn()
