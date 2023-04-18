from typing import Protocol


class BaseLocationView(Protocol):
    def close(self) -> None:
        ...
