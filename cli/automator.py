import curses
import time

def startCurses():
    curses.wrapper(Automator.run)

class Automator:

    @staticmethod
    def run(stdscr) -> None:
        # Initialize curses

        curses.curs_set(0)  # Hide cursor

        self="Hi, I'm an automator!"

        # Clear the screen
        stdscr.clear()

        # Display a message in the center of the screen
        height, width = stdscr.getmaxyx()
        text_x = width // 2 - len(self) // 2
        text_y = height // 2
        stdscr.addstr(text_y, text_x, self)

        # Refresh the screen
        stdscr.refresh()

        # Wait for user input
        while True:
            key = stdscr.getch()
            if key == ord('q'):
                break

        # Clear the screen before exiting
        stdscr.clear()
        stdscr.refresh()