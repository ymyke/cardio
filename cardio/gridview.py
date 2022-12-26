import os
from .card import Card
from .grid import Grid
from . import session

# FIXME This is not nice: On one hand, the view has a link to the model as an attribute.
# On the other, it accesses the session directly. Use only one of these mechanisms!


class GridView:
    # FIXME Make this an ABC with init and update methods?
    def __init__(self, gridmodel: Grid) -> None:
        self.model = gridmodel

    def update(self) -> None:
        pass

    # FIXME Need to add more blueprint methods here.


# QQ: Would it make things easier / more decoupled if the model would send certain view
# events to the view which then get handled appropriately? E.g., AttackAnimation or
# OverflowAnimation or OverwhelmingAttackAnimation or LethalAttackAnimation or ...


class SimpleView(GridView):
    frames: dict = {}
    msg: str = ""
    non_blocking: bool = False

    def update(self) -> None:
        repr = ""
        for i, line in enumerate(self.model):
            repr += f"{i}   "
            for sloti, slot in enumerate(line.slots):
                frame = self.frames.get(f"{i}:{sloti}", "[]")
                slotstr = ""
                if slot is not None:
                    slotstr = f"{slot.name[0:6]}|{slot.power}|{slot.health}"
                    skillstr = "".join(s.value.symbol for s in slot.skills)
                    slotstr = slotstr + skillstr
                repr += f"{frame[0]}{slotstr:13s}{frame[1]}"
            repr += "\n"
        print(repr)

        print(
            f"\nYour health: {session.humanagent.health} | His health: {session.computeragent.health}"
        )

        print(
            f"\nYour lives: {session.humanagent.lives} | His lives: {session.computeragent.lives}"
        )

        if self.msg != "":
            print(f"\n{self.msg}")

        print()
        if not self.non_blocking:
            input()
        os.system("cls")

        self.frames = {}
        self.msg = ""

    def activate_card(self, card: Card) -> None:
        linei, sloti = self.model.find_card_position(card)
        self.frames[f"{linei}:{sloti}"] = "**"
        self.update()

    def get_attacked(self, target: Card, attacker: Card) -> None:
        linei, sloti = self.model.find_card_position(target)
        self.frames[f"{linei}:{sloti}"] = "><"
        self.update()

    def human_wins_fight(self) -> None:
        self.msg = "You won!"

    def computer_wins_fight(self) -> None:
        # QQ: Boss fights will work differently.
        self.msg = "You lost!"
