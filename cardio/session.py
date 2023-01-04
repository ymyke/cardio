from __future__ import annotations
import os
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    # Functional imports will happen later to prevent circular dependencies.
    from . import Grid, GridView, Agent


grid: Grid
view: GridView
humanagent: Agent
computeragent: Agent

# QQ: Should this rather be Game instead of session? Or should there be a Game class?


def get_starterdeck_names() -> List[str]:
    # QQ: Should the starter deck be generated at some point? Based on what?
    return ["Koala", "Weasel", "Lynx", "Porcupine"]


def setup() -> None:
    from . import Grid, SimpleView, Agent, Deck
    from cardio.card_blueprints import create_cards_from_blueprints

    global grid, view, humanagent, computeragent
    grid = Grid(4)  # QQ: What if the grid size changes in the game?
    # FIXME ^ Grid needs to be setup in a fight. No grid outside of fights.
    view = SimpleView(grid)

    humanagent = Agent(name="Schnuzgi", health=5, initial_health=5, lives=1)
    humanagent.deck = Deck(create_cards_from_blueprints(get_starterdeck_names()))
    computeragent = Agent(name="Yshl", health=5, initial_health=5, lives=1)
