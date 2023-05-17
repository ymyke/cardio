from cardio import Card, CardList
from . import all_cards

# TODO:
# - should this be called blueprints? also the all_cards.py file?
# - incorporate blueprints here
# - need to make sure that this only ever creates copies but never gives out originals.


class CardCatalog:
    def __init__(self) -> None:
        self.cards = [c["card"] for c in all_cards.cards]

    def get_card(self, name: str) -> Card:
        for card in self.cards:
            if card.name == name:
                return card
        raise ValueError(f"Card with name '{name}' not found in catalog.")

    def find_by_potency(self, wanted_potency: int, exactly: bool = False) -> CardList:
        """Find all cards with potency `potency` (normalized, i.e., [0, 100])."""
        assert 0 <= wanted_potency <= 100
        return [c for c in self.cards if c.has_potency(wanted_potency, exactly)]

    def find_gameplay_equals(self, other: Card) -> CardList:
        """Return all cards that are gameplay-equal to `other`."""
        return [c for c in self.cards if c.is_gameplay_equal(other)]

    # TODO: Save to file and load from file.
