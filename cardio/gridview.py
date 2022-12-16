import os
from .card import Card
from .grid import Grid


class GridView:
    # FIXME Make this an ABC with init and update methods?
    def __init__(self, gridmodel: Grid) -> None:
        self.model = gridmodel

    def update(self) -> None:
        pass


# QQ: Would it make things easier / more decoupled if the model would send certain view
# events to the view which then get handled appropriately? E.g., AttackAnimation or
# OverflowAnimation or OverwhelmingAttackAnimation or LethalAttackAnimation or ...


class SimpleView(GridView):
    frames: dict = {}

    def update(self) -> None:
        input()
        os.system("cls")
        repr = ""
        for i, line in enumerate(self.model):
            repr += f"{i}   "
            for sloti, slot in enumerate(line.slots):
                frame = self.frames.get(f"{i}:{sloti}", "[]")
                slotstr = ""
                if slot is not None:
                    slotstr = f"{slot.name[0:6]}|{slot.power}|{slot.health}"
                repr += f"{frame[0]}{slotstr:13s}{frame[1]}"
            repr += "\n"
        print(repr)
        self.frames = {}

    def activate_card(self, card: Card) -> None:
        rowi, sloti = self.model.find_card_position(card)
        self.frames[f"{rowi}:{sloti}"] = "**"
        self.update()

    def get_attacked(self, target: Card, attacker: Card) -> None:
        rowi, sloti = self.model.find_card_position(target)
        self.frames[f"{rowi}:{sloti}"] = "><"
        self.update()
