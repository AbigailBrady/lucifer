import curses, lights, scenes, sys, settings

class RecallPreset:
    def __init__(self, preset: int) -> None:
        self._preset = preset

    @property
    def scene(self) -> str:
        return settings.get_preset(self._preset)

    def __call__(self) -> None:
        newScene = self.scene
        if newScene is not None:
            scenes.set_scene(newScene)

class MarkPreset:
    def __init__(self, preset: int) -> None:
        self._preset = preset

    def __call__(self) -> None:
        settings.mark_preset(self._preset, scenes.current_scene())

BINDINGS = { 27: lambda: sys.exit(0),

             curses.KEY_HOME : RecallPreset(1),
             ord('i') : RecallPreset(2),

	     curses.KEY_DOWN: scenes.next_scene,
             curses.KEY_UP: scenes.prev_scene,

             curses.KEY_PPAGE: scenes.reset_scene, 
             ord('*'): scenes.toggle_fav,

             49: MarkPreset(1),
             50: MarkPreset(2),
             ord('-'): lights.darken,
             ord('='): lights.lighten,
             curses.KEY_LEFT: scenes.prev_fav,
             curses.KEY_RIGHT: scenes.next_fav,
             10: lights.toggle,

}


