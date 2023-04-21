from typing import Protocol


class BaseLocationView(Protocol):
    def close(self) -> None:
        ...

    def message(self, msg: str) -> None:
        ...

    def error(self, msg: str) -> None:
        ...
