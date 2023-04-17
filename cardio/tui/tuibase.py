import atexit
from asciimatics.screen import Screen


class TUIBaseMixin:
    def __init__(self, debug: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.debug = debug
        self.screen = Screen.open(unicode_aware=True)
        atexit.register(self.close)

    def close(self) -> None:
        self.screen.close()
