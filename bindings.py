import curses, lights, scenes

BINDINGS = { curses.KEY_HOME : lambda: scenes.set_scene("Evening reading"),
             ord('i') : lambda: scenes.set_scene("Daylight"),

	     curses.KEY_DOWN: scenes.next_scene,
             curses.KEY_UP: scenes.prev_scene,

             0: scenes.reset_scene, 
             
             curses.KEY_LEFT: lights.darken,
             curses.KEY_RIGHT: lights.lighten,
             10: lights.toggle,

}


