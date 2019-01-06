import lights, scenes, curses

stdscr = None
lastKey = 0

def pad(name, width):
  name = str(name)
  while len(name) < width:
    name += " "
  return name

def bright(value):
  value = round(value * 100 / 255)
  return pad(str(value) + "%", 4)

def describeLight(light):
  if light.on:
    return pad(light.name, 20) + " b: " + bright(light.brightness)

  # hue and saturation don't seem to update quickly enough ?
  # + " h: " + pad(light.hue, 5) + " s: " + pad(light.saturation, 3)
  return pad(light.name, 20) + " [off]"

def realpaint():
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

    row += 2

    for idx, sceneName in enumerate(scenes.sceneNames):
    	stdscr.addstr(row + idx, 0, sceneName, curses.A_REVERSE if idx == scenes.sceneIdx else 0)

    stdscr.refresh()

def paint():
   import timeit
   print(timeit.timeit(realpaint, number=1))


