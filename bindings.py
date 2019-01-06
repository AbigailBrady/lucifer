import curses, lights, scenes, sys, settings

def set_dark():
  """set current scene as dark scene"""
  settings.set_dark(scenes.current_scene())

def set_bright():
  """set current scene as bright scene"""
  settings.set_bright(scenes.current_scene())

class SceneSetter:
  def __init__(self, getter):
    self._getter = getter

  @property
  def scene(self):
    return self._getter()

  def __call__(self):
    scenes.set_scene(self._getter())

BINDINGS = { 27: lambda: sys.exit(0),

             curses.KEY_HOME : SceneSetter(settings.get_dark),
             ord('i') : SceneSetter(settings.get_bright),

	     curses.KEY_DOWN: scenes.next_scene,
             curses.KEY_UP: scenes.prev_scene,

             curses.KEY_PPAGE: scenes.reset_scene, 
             ord('*'): scenes.toggle_fav,

             49: set_dark,
             50: set_bright,
             ord('-'): lights.darken,
             ord('='): lights.lighten,
             curses.KEY_LEFT: scenes.prev_fav,
             curses.KEY_RIGHT: scenes.next_fav,
             10: lights.toggle,

}


