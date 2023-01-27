from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from cardio import Card

if TYPE_CHECKING:
    from . import FightVnC


def card2str(card: Optional[Card]) -> str:
    if card is None:
        return "-"
    symbols = "".join([s.value.symbol for s in card.skills])
    return f"{card.name[0]}p{card.power}h{card.health}{symbols}"


class StatesLogger:
    def __init__(self, vnc: FightVnC) -> None:
        self.vnc = vnc
        self.log = ""

    def log_current_state(self, final: bool = False) -> None:
        s = f"Starting round {self.vnc.round_num}:\n" if not final else "Final state:\n"
        for line in range(3):
            s += "|"
            for slot in range(self.vnc.grid.width):
                card = self.vnc.grid[line][slot]
                s += f" {card2str(card):12s}|"
            s += "\n"
        for deck, name in [
            (self.vnc.decks.handdeck, "Hand"),
            (self.vnc.decks.useddeck, "Used"),
            (self.vnc.decks.drawdeck, "Draw"),
            (self.vnc.decks.hamsterdeck, "Hamster"),
        ]:
            s += f"{name}: " + " ".join([card2str(c) for c in deck.cards]) + "\n"
        s += "\n"
        # FIXME Add human and computer damage, lives, maybe items, ...
        # FIXME Add damage and gems
        self.log += s
