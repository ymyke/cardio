from .location import Location
from cardio import HumanPlayer


class NoLocation(Location):
    marker = "···"

    def generate(self) -> None:
        super().generate()

    def handle(self, view_class: type, humanplayer: HumanPlayer) -> bool:
        return True
