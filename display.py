import lights, scenes, curses, bindings, settings, typing

stdscr = None
lastKey = 0

def pad(name: typing.Any, width: int) -> str:
    name = str(name)
    while len(name) < width:
        name += " "
    return name

def bright(value: int) -> str:
    value = round(value * 100 / 255)
    return pad(str(value) + "%", 4)

def describeLight(light: lights.Light) -> str:
    if light.on:
        return pad(light.name, 20) + " b: " + bright(light.brightness)

      # hue and saturation don't seem to update quickly enough ?
      # + " h: " + pad(light.hue, 5) + " s: " + pad(light.saturation, 3)
    return pad(light.name, 20) + " [off]"

def keyFor(scene_name: str) -> str:
    for key, binding in bindings.BINDINGS.items():
        if isinstance(binding, bindings.RecallPreset):
            if binding.scene == scene_name:
                return curses.keyname(key)
    return ""

def paint() -> None:
    if stdscr is None:
        return
    global lastKey
    
    stdscr.clear()
    stdscr.addstr(0, 0, str(lastKey))
    row = 2
    for room in lights.getRooms():
        stdscr.addstr(row, 2, room.name, curses.A_REVERSE if room.group_id == lights.mainroom else 0)
        row += 1
        for light in room.lights: 
            stdscr.addstr(row, 4, describeLight(light))
            row += 1

    row += 1

    for idx, sceneName in enumerate(scenes.sceneNames):
        stdscr.addstr(row, 0, "*" if scenes.is_fave(idx) else "")
        stdscr.addstr(row, 2, sceneName, curses.A_REVERSE if idx == scenes.sceneIdx else 0)
        stdscr.addstr(row, 25, keyFor(sceneName))
        row += 1

    row = 5

    for key, binding in bindings.BINDINGS.items():
        if not isinstance(binding, (str, bindings.RecallPreset)):
            stdscr.addstr(row, 40, curses.keyname(key))
            stdscr.addstr(row, 62, binding.__doc__ or "")
            row += 1

    stdscr.refresh()


