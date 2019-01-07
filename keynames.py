import curses

KEYNAMES = { 27: "Escape",

             curses.KEY_HOME : "Home",
	     curses.KEY_DOWN: "Down",
             curses.KEY_UP: "Up",

             curses.KEY_PPAGE: "Page up",
             curses.KEY_NPAGE: "Page down",

             curses.KEY_LEFT: "Left",
             curses.KEY_RIGHT: "Right",
             10: "Return",
}


def keyname(key):
   return KEYNAMES.get(key, curses.keyname(key))
