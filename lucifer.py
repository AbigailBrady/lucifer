import curses, phue

import lights, scenes

import bindings, display

import sys

def iteration(stdscr):

    display.paint()

    stdscr.timeout(500)

    key = stdscr.getch()

    display.lastKey = key

    binding = bindings.BINDINGS.get(key)
    if binding is not None:
      if isinstance(binding, str):
        scenes.set_scene(binding)
      else:
        binding()
      return

    if key >= ord('a') and key <= ord('z'):

      scenes.set_starting(key)
      return

def main(stdscr):
  display.stdscr = stdscr
  while True:
    try:
      iteration(stdscr)
    except OSError as e:
      pass
    except phue.PhueRequestTimeout as e:
      pass
 
curses.wrapper(main)
	
