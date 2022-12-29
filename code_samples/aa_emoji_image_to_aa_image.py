"""How to turn an image into an ascii image. In this case an emoji.

Could maybe be used for some effect when the player draws a new card. Or when he creates
a new card. 

At scale, could download this and index into it to get image files:
https://unicode.org/emoji/charts/full-emoji-list.html
"""

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import ImageFile


def demo(screen):
    scenes = []

    effects = [
        Print(screen, ImageFile("code_samples/hamster_1f439.png", height=20), 2, 2),
    ]
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


Screen.wrapper(demo)
