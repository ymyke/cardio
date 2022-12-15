from .grid import Grid

class GridView:
    # FIXME Make this an ABC with init and update methods?
    def __init__(self, gridmodel: Grid) -> None:
        self.model = gridmodel

    def update(self) -> None:
        pass


class SimpleView(GridView):
    def update(self) -> None:
        print(str(self.model))
