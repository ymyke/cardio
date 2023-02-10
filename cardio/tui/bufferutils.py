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


# LIXME Use BufferedScreen instead of BufferCopy everywhere?


class BufferedScreen:
    """Adds buffering to the asciimatics screen. Supports 2 use cases:

    - `copy_to`/`restore_from`: Copy current screen content to buffer screen or restore
      from it when needed. Much more performant than redrawing the entire view; can be
      useful when redrawing needs to happen often (e.g., when moving cursors).
    - `buffer_on`/`buffer_off`: To draw to a second "off-screen" screen and copy those
      contents back to the main screen when done drawing. To prevent flickering when
      drawing the view.

    Note that all write accesses write to the same variables, which can lead to desired
    or undesired outcomes. But it is something to keep in mind esp. where the same
    `BufferedScreen` object is accessed in a nested fashion (e.g., in
    `handle_human_plays_card` and `_handle_card_placement_interaction`). For the same
    reason, the call to `copy_to` might sometimes not be necessary because a view update
    might already have updated the buffer on the buffer screen.
    """

    def __init__(self) -> None:
        self._bufferscreen = Screen.open(unicode_aware=True)
        self._screen = Screen.open(unicode_aware=True)
        self._buffer_active = False

    def __call__(self) -> Screen:
        """Convenience method so the object can be called directly, saving some clutter
        in the code.
        """
        return self._bufferscreen if self._buffer_active else self._screen

    def copy_to(self) -> None:
        self._bufferscreen._buffer._double_buffer = copy.deepcopy(
            self._screen._buffer._double_buffer
        )

    def restore_from(self) -> None:
        # TODO Could sometimes be used instead of redraw_view
        self._screen._buffer._double_buffer = copy.deepcopy(
            self._bufferscreen._buffer._double_buffer
        )

    def buffer_on(self) -> None:
        self._buffer_active = True

    def buffer_off(self) -> None:
        self._buffer_active = False
        self.restore_from()

    def close(self) -> None:
        self._bufferscreen.close()
        self._screen.close()
