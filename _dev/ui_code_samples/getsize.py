import curses


def main(stdscr):
    # Get the dimensions of the terminal window
    rows, columns = stdscr.getmaxyx()

    # Print the dimensions to the terminal
    stdscr.addstr("The terminal window has %d rows and %d columns\n" % (rows, columns))

    # Wait for the user to press a key before exiting
    stdscr.getch()


# Initialize curses and run the main function
curses.wrapper(main)
