import shelve, typing, settings

PRESETS = {1: "Dimmed", 2: "Bright"}

FAVE_SCENES = ["Dimmed", "Bright", "Nightlight"]

with shelve.open(".lucifer") as storage:
    PRESETS = storage.get("PRESETS", PRESETS)
    FAVE_SCENES = storage.get("FAVE_SCENES", FAVE_SCENES)

def save_state():
    with shelve.open(".lucifer") as storage:
        storage["PRESETS"] = PRESETS
        storage["FAVE_SCENES"] = FAVE_SCENES

def get_preset(preset: int) -> typing.Optional[str]:
    return PRESETS.get(preset, None)

def mark_preset(preset: int, scene: str):
    global PRESETS
    PRESETS[preset] = scene
    save_state()



