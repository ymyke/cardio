import curses
import random
import sys
from curses.textpad import Textbox, rectangle

def main(win):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    if curses.has_colors():
        curses.start_color()

    # win.immedok(True)
    win.nodelay(True)
    x, y = 0, 0
    while True:
        key = None
        try:
            key = win.getkey()
        except:
            pass
        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
        elif key == "q":
            sys.exit(0)
        win.clear()
        # win.addstr(y, x, random.choice("X"))
        win.addstr(y, x, random.choice("ABCDEF"))

def main2(win):
    rectangle(win, 2, 2, 10, 20)
    win.refresh()
    win.getch()


def main3(win):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    BLACK_ON_YELLOW = curses.color_pair(1)

    win.addstr(1,1, "opijflksjdu03234ioi20id3 NORMAL", curses.A_NORMAL)
    win.addstr(2,1, "opijflksjdu03234ioi20id3 STANDOUT", curses.A_STANDOUT)
    win.addstr(3,1, "opijflksjdu03234ioi20id3 UNDERLINE", curses.A_UNDERLINE)
    win.addstr(4,1, "opijflksjdu03234ioi20id3 REVERSE", curses.A_REVERSE)
    win.addstr(5,1, "opijflksjdu03234ioi20id3 BLINK", curses.A_BLINK)
    win.addstr(6,1, "opijflksjdu03234ioi20id3 DIM", curses.A_DIM)
    win.addstr(7,1, "opijflksjdu03234ioi20id3 BOLD", curses.A_BOLD)
    win.addstr(8,1, "opijflksjdu03234ioi20id3 PROTECT", curses.A_PROTECT)
    win.addstr(9,1, "opijflksjdu03234ioi20id3 INVIS", curses.A_INVIS)
    win.addstr(10,1, "opijflksjdu03234ioi20id3 ALTCHARSET", curses.A_ALTCHARSET)
    win.addstr(11,1, "opijflksjdu03234ioi20id3 BLACK ON YELLOW", BLACK_ON_YELLOW)
    win.addstr(12,1, "opijflksjdu03234ioi20id3 BLACK ON YELLOW REVERSE", BLACK_ON_YELLOW | curses.A_REVERSE)

    win.getch()


curses.wrapper(main3)



# stdscr = curses.initscr()
# # while True:
# #     print(curses.getmouse())
# stdscr.box()
# stdscr.addstr(0, 0, str(curses.getmouse()))
# stdscr.getch()
# print(curses.termattrs())
