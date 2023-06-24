import curses
import sys


def main(argv):
    # BEGIN ncurses startup/initialization...
    # Initialize the curses object.
    stdscr = curses.initscr()

    # Do not echo keys back to the client.
    curses.noecho()

    # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
    curses.cbreak()

    # Turn off blinking cursor
    curses.curs_set(False)

    # Enable color if we can...
    if curses.has_colors():
        curses.start_color()

    # Optional - Enable the keypad. This also decodes multi-byte key sequences
    # stdscr.keypad(True)

    # END ncurses startup/initialization...

    caughtExceptions = ""
    try:
        # Coordinates start from top left, in the format of y, x.
        stdscr.addstr(0, 0, "Hello, world!")
        screenDetailText = (
            "This screen is ["
            + str(curses.LINES)
            + "] high and ["
            + str(curses.COLS)
            + "] across."
        )
        startingXPos = int((curses.COLS - len(screenDetailText)) / 2)
        stdscr.addstr(3, startingXPos, screenDetailText)
        stdscr.addstr(
            30, curses.COLS - len("Press a key to quit."), "Press a key to quit."
        )

        # Actually draws the text above to the positions specified.
        stdscr.refresh()

        # Grabs a value from the keyboard without Enter having to be pressed (see cbreak above)
        stdscr.getch()
    except Exception as err:
        # Just printing from here will not work, as the program is still set to
        # use ncurses.
        # print ("Some error [" + str(err) + "] occurred.")
        caughtExceptions = str(err)

    # BEGIN ncurses shutdown/deinitialization...
    # Turn off cbreak mode...
    curses.nocbreak()

    # Turn echo back on.
    curses.echo()

    # Restore cursor blinking.
    curses.curs_set(True)

    # Turn off the keypad...
    # stdscr.keypad(False)

    # Restore Terminal to original state.
    curses.endwin()

    # END ncurses shutdown/deinitialization...

    # Display Errors if any happened:
    if "" != caughtExceptions:
        print("Got error(s) [" + caughtExceptions + "]")


if __name__ == "__main__":
    main(sys.argv[1:])
