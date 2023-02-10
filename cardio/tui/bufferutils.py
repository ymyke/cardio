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


class BufferedScreen:
    def __init__(self) -> None:
        self._bufferscreen = Screen.open(unicode_aware=True)
        self._screen = Screen.open(unicode_aware=True)
        self._buffer_active = False

    def __call__(self) -> Screen:
        """Convenience method so the object can be called directly, saving some clutter
        in the code.
        """
        return self._bufferscreen if self._buffer_active else self._screen

    def buffer_on(self) -> None:
        self._buffer_active = True

    def buffer_off(self) -> None:
        self._buffer_active = False
        self._screen._buffer._double_buffer = copy.deepcopy(
            self._bufferscreen._buffer._double_buffer
        )
        self._screen.refresh()

    def close(self) -> None:
        self._bufferscreen.close()
        self._screen.close()
