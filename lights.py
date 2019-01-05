import phue
import settings

bridge = phue.Bridge(settings.BRIDGE_IP)

scenes = {}

def findRoom(roomName):
  for room in bridge.groups:
    if roomName == room.name:
      return room.group_id

def getRoom(roomName):
  for room in bridge.groups:
    if roomName == room.name:
      return room

mainroom = findRoom(settings.MAIN_ROOM)

for sceneID, scene in bridge.get_api()["scenes"].items():
  if scene["recycle"] == False and scene.get("group") == str(mainroom):
    scenes[sceneID] = scene

def getRooms():
  rooms = []
  for room in bridge.groups:
    if "Entertainment area" not in room.name:
       rooms.append(room)
  return sorted(rooms, key=lambda room: room.name)

def set_scene(scene_id):
  bridge.activate_scene(group_id=mainroom, scene_id=scene_id) 

def darken():
  room = getRoom(settings.MAIN_ROOM)
  room.brightness = max(room.brightness - settings.BRIGHTNESS_STEP, 0)

def lighten():
  room = getRoom(settings.MAIN_ROOM)
  room.brightness = min(room.brightness + settings.BRIGHTNESS_STEP, 255)

def toggle():
  room = getRoom(settings.MAIN_ROOM)
  room.on = not room.on

