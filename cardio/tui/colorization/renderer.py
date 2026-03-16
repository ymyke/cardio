from abc import ABC, abstractmethod
from typing import Protocol
from asciimatics.screen import Screen
from .colorizer import ColorizedText
from ..constants import Color


class ScreenAdapter(Protocol):
    """Protocol for screen operations to allow testing."""
    
    @property
    def width(self) -> int: ...
    
    @property
    def height(self) -> int: ...
    
    def print_at(self, text: str, x: int, y: int, colour: int = 7, 
                 attr: int = 0, bg: int = 0, transparent: bool = False) -> None: ...
    
    def refresh(self) -> None: ...


class ColorizedTextRenderer(ABC):
    """Abstract base class for rendering colorized text."""
    
    @abstractmethod
    def render(self, colorized_text: ColorizedText) -> None:
        """Render colorized text to the output."""
        pass


class CenteredColorizedTextRenderer(ColorizedTextRenderer):
    """Renders colorized text centered on screen."""
    
    def __init__(self, screen: ScreenAdapter):
        self._screen = screen
    
    def render(self, colorized_text: ColorizedText) -> None:
        num_lines = len(colorized_text)
        start_y = self._screen.height // 2 - num_lines // 2
        
        for line_idx, line in enumerate(colorized_text):
            line_len = len(line)
            start_x = self._screen.width // 2 - line_len // 2
            y = start_y + line_idx
            
            for char_idx, colorized_char in enumerate(line):
                x = start_x + char_idx
                self._render_char(colorized_char.char, x, y, colorized_char.color)
        
        self._screen.refresh()
    
    def _render_char(self, char: str, x: int, y: int, color: Color) -> None:
        if color is Color.GRAY:
            self._screen.print_at(char, x, y, colour=Screen.COLOUR_BLACK, attr=Screen.A_BOLD)
        else:
            self._screen.print_at(char, x, y, colour=color.value)
