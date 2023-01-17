from dataclasses import dataclass, field
from .deck import Deck


@dataclass
class HumanPlayer:
    name: str
    lives: int = 1
    gems: int = 0
    deck: Deck = field(default_factory=lambda: Deck())
    # FIXME Add score, stats, ...
    # FIXME Add items
    # FIXME Add card archive? -- all cards she has ever discovered
