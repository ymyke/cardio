from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cardio import Card


class Potency:
    """Potency of a card.
    
    - net: W/o fire/spirits (i.e., w/o costs_* and has_*), this is typically used to
      determine what the computer player works with, since it doesn't need to care about
      fire/spirits.
    - gross: All in, typically used to determine what the human player works with.
    - raw: The raw numbers.
    - normd: Normalized to a 0-100 scale, based on a theoretical min and max card.
    """

    def __init__(self, card: Card) -> None:
        self._card = card

    @property
    def net_raw(self) -> int:
        return (
            self._card.power * 2
            + self._card.health * 2
            + sum(s.potency for s in self._card.skills)
        )

    @property
    def net_normd(self) -> int:
        from cardio import Card

        mincard, maxcard = Card.get_min_max()
        return int(
            (self.net_raw - mincard.pot.net_raw)
            / (maxcard.pot.net_raw - mincard.pot.net_raw)
            * 100
        )
    
    @property
    def net_normd2gross(self) -> int:
        from cardio import Card

        mincard, maxcard = Card.get_min_max()

        slope = (maxcard.pot.gross_raw - mincard.pot.gross_raw) / (maxcard.pot.net_raw - mincard.pot.net_raw)
        output = mincard.pot.gross_raw + slope * (self.net_raw - mincard.pot.net_raw)

        return int(output)

    @property
    def gross_raw(self) -> int:
        strengths = self.net_raw + self._card.has_fire + self._card.has_spirits
        costs = self._card.costs_fire + self._card.costs_spirits
        costs_bonus = 10 if costs == 0 else 0  # Cards with 0 costs are strong
        return strengths - costs + costs_bonus

    @property
    def gross_normd(self) -> int:
        from cardio import Card

        mincard, maxcard = Card.get_min_max()
        return int(
            (self.gross_raw - mincard.pot.gross_raw)
            / (maxcard.pot.gross_raw - mincard.pot.gross_raw)
            * 100
        )
    


    # TODO Maybe have gross and net for conveneince, both meaning normd?
