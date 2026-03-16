import unittest
from .factory import ColorizerFactory
from .strategies import RainbowColorizer
from ..constants import Color


class TestColorization(unittest.TestCase):
    def test_rainbow_colorizer_produces_output(self):
        colorizer = RainbowColorizer()
        result = colorizer.colorize("FIGHT!")
        self.assertGreater(len(result), 0)
        
    def test_factory_creates_colorizer(self):
        colorizer = ColorizerFactory.create_random()
        self.assertIsNotNone(colorizer)


if __name__ == "__main__":
    unittest.main()
