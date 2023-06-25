import atexit
from typing import Optional
import time
from asciimatics.screen import Screen
from asciimatics.renderers import FigletText
from .utils import splash_message, wait_for_any_key


class TUIBaseMixin:
    def __init__(
        self, description: Optional[str] = None, debug: bool = False, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.debug = debug
        self.screen = Screen.open(unicode_aware=True)
        if self.screen.height < 52 or self.screen.width < 160:
            self.close()
            raise RuntimeError(
                "Screen resolution must be at least 160x52 (WxH). "
                f"Yours is {self.screen.width}x{self.screen.height}."
            )
        atexit.register(self.close)
        if description:
            self.message(description)

    def close(self) -> None:
        self.screen.close()

    def message(self, msg: str) -> None:
        """Display a message for the user and wait for any key."""
        self.screen.clear_buffer(0, 0, 0)
        if len(msg) > 10:
            # Long messages are displayed normally:
            splash_message(self.screen, msg)
            wait_for_any_key(self.screen)
        else:
            # Short messages are displayed in big letters and without waiting for a key:
            # (This is mostly a gimmick for the fight location.)
            figlet = str(FigletText(msg, "doh"))
            splash_message(self.screen, figlet)
            time.sleep(0.1)

    def error(self, msg: str) -> None:
        """Display a message and then close the view also. `error` is expected to be
        used as the final interaction with this view.
        """
        self.message(msg)
        self.close()
