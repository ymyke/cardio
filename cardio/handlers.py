from . import session

# FIXME What exactly it the purpose of this module? Should the functions here be moved
# to session.py?


def handle_turn() -> None:
    session.grid.playerline.activate()
    session.grid.opponentline.activate()
    session.grid.prepline.prepare()
    session.view.update()


# def add_card(cmd: commands.AddCard) -> None:
# # def add_card(self, linei: int, sloti: int, card: Card) -> None:
#     self.grid[linei][sloti] = card
#     self.gridview.update()


def play_game() -> None:
    while True:
        handle_turn()
        if session.humanagent.has_lost_life():
            session.humanagent.update_lives_and_health_after_death()
            session.view.computer_wins_fight()
            break
        if session.computeragent.has_lost_life():
            overflow = session.computeragent.update_lives_and_health_after_death()
            session.view.human_wins_fight()
            # FIXME Do something w overflow damage here -- maybe just store it in the
            # object right in the update_lives_and_health_after_death function but also
            # pass it to the view for some animation?
            break
        if session.grid.is_empty():
            # QQ: Should this also break when the grid is "powerless", i.e., no cards
            # with >0 power?
            break
