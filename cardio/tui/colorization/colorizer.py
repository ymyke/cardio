from abc import ABC, abstractmethod
from typing import List, Tuple
from ..constants import Color


class ColorizedChar:
    """Represents a character with its associated color."""
    
    def __init__(self, char: str, color: Color):
        self.char = char
        self.color = color


class ColorizedLine:
    """Represents a line of colorized characters."""
    
    def __init__(self, chars: List[ColorizedChar] = None):
        self.chars = chars or []
    
    def append(self, char: ColorizedChar) -> None:
        self.chars.append(char)
    
    def __iter__(self):
        return iter(self.chars)
    
    def __len__(self):
        return len(self.chars)


class ColorizedText:
    """Represents multi-line colorized text."""
    
    def __init__(self, lines: List[ColorizedLine] = None):
        self.lines = lines or []
    
    def append(self, line: ColorizedLine) -> None:
        self.lines.append(line)
    
    def __iter__(self):
        return iter(self.lines)
    
    def __len__(self):
        return len(self.lines)


class Colorizer(ABC):
    """Abstract base class for text colorization strategies."""
    
    @abstractmethod
    def colorize(self, text: str) -> ColorizedText:
        """Transform plain text into colorized text."""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of this colorization strategy."""
        pass
