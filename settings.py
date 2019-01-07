import typing

BRIDGE_IP = "192.168.0.23"

MAIN_ROOM = "Bedroom"

BRIGHTNESS_STEP = 64

PRESETS = {1: "Dimmed", 2: "Bright"}

def get_preset(preset: int) -> typing.Optional[str]:
    return PRESETS.get(preset, None)

def mark_preset(preset: int, scene: str):
    global PRESETS
    PRESETS[preset] = scene
    
FAVE_SCENES = ["Dimmed", "Bright", "Nightlight"]

# FAVE_SCENES= ["Evening reading", "Evening", "Rainbow", "Daylight", "Purple"]
