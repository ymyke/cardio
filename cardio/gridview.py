from .grid import Grid


class GridView:
    # FIXME Make this an ABC with init and update methods?
    def __init__(self, gridmodel: Grid) -> None:
        self.model = gridmodel

    def update(self) -> None:
        pass


class SimpleView(GridView):
    def update(self) -> None:
        repr = ""
        for i, line in enumerate(self.model):
            repr += f"{i}   "
            for slot in line.slots:
                slotstr = ""
                if slot is not None:
                    slotstr = f"{slot.name[0:6]}|{slot.power}|{slot.health}"
                repr += f"[{slotstr:13s}]"
            repr += "\n"
        print(repr)
