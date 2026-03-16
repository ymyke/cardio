from typing import Dict, Type, Optional
from .colorizer import Colorizer


class ColorizerRegistry:
    """Registry for colorizer implementations. Allows dynamic registration and lookup."""
    
    _instance: Optional["ColorizerRegistry"] = None
    
    def __new__(cls) -> "ColorizerRegistry":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._colorizers: Dict[str, Type[Colorizer]] = {}
        return cls._instance
    
    def register(self, colorizer_class: Type[Colorizer]) -> Type[Colorizer]:
        """Register a colorizer class. Can be used as a decorator."""
        instance = colorizer_class()
        self._colorizers[instance.name] = colorizer_class
        return colorizer_class
    
    def get(self, name: str) -> Optional[Type[Colorizer]]:
        """Get a colorizer class by name."""
        return self._colorizers.get(name)
    
    def list_names(self) -> list:
        """List all registered colorizer names."""
        return list(self._colorizers.keys())
    
    @classmethod
    def reset(cls) -> None:
        """Reset the registry (mainly for testing)."""
        cls._instance = None
