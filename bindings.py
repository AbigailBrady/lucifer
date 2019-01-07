import curses, lights, scenes, sys, settings, presets

BINDINGS = { 27: lambda: sys.exit(0),

             curses.KEY_HOME : presets.RecallPreset(1),
             ord('i') : presets.RecallPreset(2),

	     curses.KEY_DOWN: scenes.next_scene,
             curses.KEY_UP: scenes.prev_scene,

             curses.KEY_PPAGE: scenes.reset_scene, 
             ord('*'): scenes.toggle_fav,

             49: presets.MarkPreset(1),
             50: presets.MarkPreset(2),
             ord('-'): lights.darken,
             ord('='): lights.lighten,
             curses.KEY_LEFT: scenes.prev_fav,
             curses.KEY_RIGHT: scenes.next_fav,
             10: lights.toggle,

}



