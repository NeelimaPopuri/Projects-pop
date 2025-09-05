import curses
from curses import wrapper
import queue
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)
    stdscr.clear()
    stdscr.addstr(5, 10, "hello world!", blue_and_black)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
