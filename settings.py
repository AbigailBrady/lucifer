BRIDGE_IP = "192.168.0.23"

MAIN_ROOM = "Bedroom"

BRIGHTNESS_STEP = 64

DARK_SCENE = "Dimmed"
BRIGHT_SCENE = "Bright"

def get_dark():
  return DARK_SCENE

def get_bright():
  return BRIGHT_SCENE

def set_dark(scene):
  global DARK_SCENE
  DARK_SCENE = scene

def set_bright(scene):
  global BRIGHT_SCENE
  BRIGHT_SCENE = scene

FAVE_SCENES = ["Dimmed", "Bright", "Nightlight"]

# FAVE_SCENES= ["Evening reading", "Evening", "Rainbow", "Daylight", "Purple"]
