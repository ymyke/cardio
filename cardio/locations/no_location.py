from .location import Location


class NoLocation(Location):
    marker = "···"

    def generate(self) -> None:
        super().generate()

    def handle(self) -> bool:
        return True
