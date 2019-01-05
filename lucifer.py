import curses

import lights

scenes = list(lights.scenes.items())
sceneNames = [scene.get("name") for sceneID, scene in scenes]
sceneIdx = 0
      
def nextScene():
  global sceneIdx
  sceneIdx += 1
  sceneIdx %= len(scenes)  
  lights.set_scene(scenes[sceneIdx][0])

def prevScene():
  global sceneIdx
  sceneIdx -= 1
  sceneIdx %= len(scenes)  
  lights.set_scene(scenes[sceneIdx][0])

def resetScene():
  global sceneIdx
  lights.set_scene(scenes[sceneIdx][0])

def setScene(sceneName):
  global sceneIdx
  idx = sceneNames.index(sceneName)
  sceneIdx = idx
  lights.set_scene(scenes[sceneIdx][0])

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
        stdscr.addstr(row, 2, room.name)
        row += 1
        for light in room.lights:
           stdscr.addstr(row, 4, describeLight(light))
           row += 1

    row += 2

    for idx, sceneName in enumerate(sceneNames):
    	stdscr.addstr(row + idx, 0, sceneName, curses.A_REVERSE if idx == sceneIdx else 0)

    stdscr.refresh()

    stdscr.timeout(1000)

    key = stdscr.getch()

    lastKey = key

    if key == ord('q'):
      return

    if key == curses.KEY_DOWN:
      nextScene()

    if key == curses.KEY_UP:
      prevScene()

    if key == curses.KEY_LEFT:
      lights.darken()
   
    if key == curses.KEY_RIGHT:
      lights.lighten()
    
    if key == curses.KEY_HOME:
      setScene("Evening reading")
    
    if key == ord('i'):
      setScene("Daylight")
   
    if key == 0:
      resetScene()
 
    if key == 10:
      lights.toggle()

curses.wrapper(main)
