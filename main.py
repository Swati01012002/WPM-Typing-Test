import curses
from curses import wrapper

def main(stdscr):
    stdscr.addstr("Hello")

wrapper(main)