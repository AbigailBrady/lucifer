import curses, lights, scenes, sys

BINDINGS = { 27: sys.exit,

             curses.KEY_HOME : lambda: scenes.set_scene("Evening reading"),
             ord('i') : lambda: scenes.set_scene("Daylight"),

	     curses.KEY_DOWN: scenes.next_scene,
             curses.KEY_UP: scenes.prev_scene,

             curses.KEY_PPAGE: scenes.reset_scene, 
             ord('*'): scenes.toggle_fav,
             
             ord('-'): lights.darken,
             ord('='): lights.lighten,
             curses.KEY_LEFT: scenes.prev_fav,
             curses.KEY_RIGHT: scenes.next_fav,
             10: lights.toggle,

}


