import copy
from asciimatics.screen import Screen


class BufferCopy:
    def __init__(self, screen: Screen) -> None:
        self.screen = screen
        self.update()

    def update(self) -> None:
        self.buffer = copy.deepcopy(self.screen._buffer._double_buffer)

    def copyback(self) -> None:
        self.screen._buffer._double_buffer = copy.deepcopy(self.buffer)


# TODO Remove BufferCopy??
