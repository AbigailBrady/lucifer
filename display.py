import lights, scenes, curses, bindings, presets, settings, typing, keynames

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

def xy(value: tuple) -> str:
    return "[{0:.2f}, {1:.2f}]".format(value[0], value[1])

def describe_light(light: lights.Light) -> str:
    if light.on:
        return pad(light.name, 20) + " b: " + bright(light.brightness) + " " + xy(light.xy)

      # hue and saturation don't seem to update quickly enough ?
      # + " h: " + pad(light.hue, 5) + " s: " + pad(light.saturation, 3)
    return pad(light.name, 20) + " [off]"

def key_for(scene_name: str) -> str:
    for key, binding in bindings.BINDINGS.items():
        if isinstance(binding, presets.RecallPreset):
            if binding.scene == scene_name:
                return keynames.keyname(key)
    return ""

def paint() -> None:
    if stdscr is None:
        return
    global lastKey

    rooms = lights.get_rooms()

    guess = scenes.guess_activated_scene(rooms)
    if guess is not None:
        scenes.sceneIdx = guess
    
    stdscr.clear()
    stdscr.addstr(0, 0, str(lastKey))
    row = 2
    for room in rooms:
        stdscr.addstr(row, 2, room.name, curses.A_REVERSE if room.group_id == lights.mainroom else 0)
        row += 1
        for light in room.lights: 
            stdscr.addstr(row, 4, describe_light(light))
            row += 1

    row += 1
    first_scene_row = row

    for idx, sceneName in enumerate(scenes.sceneNames):
        stdscr.addstr(row, 0, "*" if scenes.is_fave(idx) else "")
        stdscr.addstr(row, 2, sceneName, curses.A_REVERSE if idx == scenes.sceneIdx else 0)
        stdscr.addstr(row, 25, key_for(sceneName))
        row += 1

    row = first_scene_row

    for key, binding in bindings.BINDINGS.items():
        if not isinstance(binding, (str, presets.RecallPreset)):
            stdscr.addstr(row, 40, keynames.keyname(key))
            stdscr.addstr(row, 62, binding.__doc__ or "")
            row += 1

    stdscr.refresh()


