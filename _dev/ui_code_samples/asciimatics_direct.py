"""Using asciimatics and getting and drawing one frame after the next manually."""

from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Box
from asciimatics.scene import Scene
from asciimatics.screen import Screen
import time


def update_screen(end_time, loop, screen):
    screen.draw_next_frame()
    if loop.time() < end_time:
        loop.call_later(0.05, update_screen, end_time, loop, screen)
    else:
        loop.stop()


# Define the scene that you'd like to play.
screen = Screen.open()
effects = [
    # Cycle(
    #     screen,
    #     FigletText("ASCIIMATICS", font='big'),
    #     screen.height // 2 - 8),
    # Cycle(
    #     screen,
    #     FigletText("ROCKS!", font='big'),
    #     screen.height // 2 + 3),
    # Stars(screen, (screen.width + screen.height) // 2),
    Print(screen, Box(10, 10), 10, 10, delete_count=2),
]
screen.set_scenes([Scene(effects)])

# Can I just paint effects to the screen directly w/o a scene?

for i in range(20):
    screen.draw_next_frame()
    time.sleep(0.5)

# Schedule the first call to display_date()
# loop = asyncio.new_event_loop()
# end_time = loop.time() + 5.0
# loop.call_soon(update_screen, end_time, loop, screen)

# Blocking call interrupted by loop.stop()
# loop.run_forever()
# loop.close()
screen.close()
