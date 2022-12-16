from . import session


def handle_turn() -> None:
    session.grid.playerline.activate()
    session.grid.opponentline.activate()
    session.grid.prepline.prepare()

    # FIXME Check if game over

    session.view.update()  # FIXME Should be done automatically somewhere?


# def add_card(cmd: commands.AddCard) -> None:
# # def add_card(self, linei: int, sloti: int, card: Card) -> None:
#     self.grid[linei][sloti] = card
#     self.gridview.update()
