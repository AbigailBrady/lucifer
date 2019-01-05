import curses

import lights, scenes

import bindings


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
    return pad(light.name, 20) + " b: " + bright(light.brightness) + " h: " + pad(light.hue, 5) + " s: " + pad(light.saturation, 3)
  return pad(light.name, 20) + " [off]"

def main(stdscr):

  lastKey = ""

  while True:

    stdscr.clear()

    stdscr.addstr(0, 0, repr(lastKey))

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

    stdscr.timeout(1000)

    key = stdscr.getch()

    lastKey = key

    if key == 27:
      return

    binding = bindings.BINDINGS.get(key)
    if binding is not None:
      binding()
      continue

    if key >= ord('a') and key <= ord('z'):
      scenes.set_starting(key)
 

curses.wrapper(main)
