import random
from typing import List
from .colorizer import Colorizer, ColorizedText, ColorizedLine, ColorizedChar
from ..constants import Color


class RainbowColorizer(Colorizer):
    """Colorizes text with rainbow colors cycling through each character."""
    
    RAINBOW_COLORS = [
        Color.RED,
        Color.YELLOW,
        Color.GREEN,
        Color.CYAN,
        Color.BLUE,
        Color.MAGENTA,
    ]
    
    @property
    def name(self) -> str:
        return "rainbow"
    
    def colorize(self, text: str) -> ColorizedText:
        result = ColorizedText()
        color_index = 0
        
        for line_text in text.split("\n"):
            line = ColorizedLine()
            for char in line_text:
                if char.strip():
                    color = self.RAINBOW_COLORS[color_index % len(self.RAINBOW_COLORS)]
                    color_index += 1
                else:
                    color = Color.WHITE
                line.append(ColorizedChar(char, color))
            result.append(line)
        
        return result


class RandomColorizer(Colorizer):
    """Colorizes each character with a random color."""
    
    COLORS = [
        Color.RED,
        Color.GREEN,
        Color.YELLOW,
        Color.BLUE,
        Color.MAGENTA,
        Color.CYAN,
    ]
    
    @property
    def name(self) -> str:
        return "random"
    
    def colorize(self, text: str) -> ColorizedText:
        result = ColorizedText()
        
        for line_text in text.split("\n"):
            line = ColorizedLine()
            for char in line_text:
                if char.strip():
                    color = random.choice(self.COLORS)
                else:
                    color = Color.WHITE
                line.append(ColorizedChar(char, color))
            result.append(line)
        
        return result


class GradientColorizer(Colorizer):
    """Colorizes text with a vertical gradient effect."""
    
    GRADIENT_COLORS = [
        Color.RED,
        Color.YELLOW,
        Color.GREEN,
        Color.CYAN,
        Color.BLUE,
        Color.MAGENTA,
    ]
    
    @property
    def name(self) -> str:
        return "gradient"
    
    def colorize(self, text: str) -> ColorizedText:
        result = ColorizedText()
        lines = text.split("\n")
        num_lines = len(lines)
        
        for i, line_text in enumerate(lines):
            line = ColorizedLine()
            color_index = int(i / max(1, num_lines) * len(self.GRADIENT_COLORS))
            color_index = min(color_index, len(self.GRADIENT_COLORS) - 1)
            color = self.GRADIENT_COLORS[color_index]
            
            for char in line_text:
                line.append(ColorizedChar(char, color if char.strip() else Color.WHITE))
            result.append(line)
        
        return result


class MonochromeColorizer(Colorizer):
    """Colorizes text with a single color (for backwards compatibility)."""
    
    def __init__(self, color: Color = Color.WHITE):
        self._color = color
    
    @property
    def name(self) -> str:
        return "monochrome"
    
    def colorize(self, text: str) -> ColorizedText:
        result = ColorizedText()
        
        for line_text in text.split("\n"):
            line = ColorizedLine()
            for char in line_text:
                line.append(ColorizedChar(char, self._color))
            result.append(line)
        
        return result


class FireColorizer(Colorizer):
    """Colorizes text with fire-like colors (red, yellow at top)."""
    
    @property
    def name(self) -> str:
        return "fire"
    
    def colorize(self, text: str) -> ColorizedText:
        result = ColorizedText()
        lines = text.split("\n")
        num_lines = len(lines)
        
        fire_colors = [Color.YELLOW, Color.YELLOW, Color.RED, Color.RED, Color.MAGENTA]
        
        for i, line_text in enumerate(lines):
            line = ColorizedLine()
            ratio = i / max(1, num_lines - 1)
            color_index = int(ratio * (len(fire_colors) - 1))
            color = fire_colors[color_index]
            
            for char in line_text:
                line.append(ColorizedChar(char, color if char.strip() else Color.WHITE))
            result.append(line)
        
        return result
