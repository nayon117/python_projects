import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello world")
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)

wrapper(main)
