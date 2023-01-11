import os
from .card import Card
from .grid import Grid, GridPos
from . import session

# FIXME This is not nice: On one hand, the view has a link to the model as an attribute.
# On the other, it accesses the session directly. Use only one of these mechanisms!


class GridView:
    """
    - All the `card_` methods should be able to rely on the precondition that the `card`
      is still in the grid when the method is called.
    """

    def __init__(self, grid: Grid) -> None:
        self.grid = grid

    def card_about_to_die(self, card: Card) -> None:
        pass

    def card_lost_health(self, card: Card) -> None:
        pass

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pass

    def card_activate(self, card: Card) -> None:
        pass

    def card_prepare(self, card: Card) -> None:
        pass

    def pos_card_deactivate(self, pos: GridPos) -> None:
        pass

    def update(self) -> None:
        # FIXME Is this still necessary? Still used anywhere?
        pass


class SimpleView(GridView):
    frames: dict = {}
    msg: str = ""
    non_blocking: bool = False

    def update(self) -> None:
        repr = ""
        for i, line in enumerate(self.grid):
            repr += f"{i}   "
            for sloti, slot in enumerate(line):
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

    def card_activate(self, card: Card) -> None:
        pos = self.grid.find_card(card)
        assert pos is not None, (
            f"{card.name} gets gets activated and "
            "needs a view update but has no position on the grid"
        )
        self.frames[f"{pos.line}:{pos.slot}"] = "**"
        self.update()

    def card_getting_attacked(self, target: Card, attacker: Card) -> None:
        pos = self.grid.find_card(target)
        assert pos is not None, (
            f"{target.name} gets attacked by {attacker.name} and "
            "needs a view update but has no position on the grid"
        )
        self.frames[f"{pos.line}:{pos.slot}"] = "><"
        self.update()

    def human_wins_fight(self) -> None:
        # FIXME Still necessary?
        self.msg = "You won!"

    def computer_wins_fight(self) -> None:
        # FIXME Still necessary?
        # QQ: Boss fights will work differently.
        self.msg = "You lost!"
