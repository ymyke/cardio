import random
from typing import Optional
from .colorizer import Colorizer
from .registry import ColorizerRegistry
from .strategies import (
    RainbowColorizer,
    RandomColorizer,
    GradientColorizer,
    MonochromeColorizer,
    FireColorizer,
)


class ColorizerFactory:
    """Factory for creating colorizer instances."""
    
    _default_colorizers = [
        RainbowColorizer,
        RandomColorizer,
        GradientColorizer,
        FireColorizer,
    ]
    
    @classmethod
    def _ensure_registry_populated(cls) -> None:
        """Ensure default colorizers are registered."""
        registry = ColorizerRegistry()
        if not registry.list_names():
            for colorizer_class in cls._default_colorizers:
                registry.register(colorizer_class)
            registry.register(MonochromeColorizer)
    
    @classmethod
    def create(cls, name: str) -> Optional[Colorizer]:
        """Create a colorizer by name."""
        cls._ensure_registry_populated()
        registry = ColorizerRegistry()
        colorizer_class = registry.get(name)
        if colorizer_class:
            return colorizer_class()
        return None
    
    @classmethod
    def create_random(cls) -> Colorizer:
        """Create a random colorful colorizer (excludes monochrome)."""
        cls._ensure_registry_populated()
        colorizer_class = random.choice(cls._default_colorizers)
        return colorizer_class()
    
    @classmethod
    def create_default(cls) -> Colorizer:
        """Create the default colorizer for splash messages."""
        return cls.create_random()
