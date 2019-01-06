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

def current_api():
  return bridge.get_api()

class Room:
  def __init__(self, id, name, lights):
    self._id = int(id)
    self._name = name
    self._lights = lights

  @property
  def group_id(self):
    return self._id
 
  @property 
  def name(self):
    return self._name
  
  @property 
  def lights(self):
    return self._lights

class Light:
  def __init__(self, api):
    self._name = api["name"]
    self._on = api["state"]["on"]
    self._brightness = api["state"]["bri"]
    self._saturation = api["state"]["sat"]
    self._hue = api["state"]["hue"]

  @property
  def on(self):
    return self._on

  @property
  def brightness(self):
    return self._brightness
  
  @property
  def hue(self):
    return self._hue
  
  @property
  def saturation(self):
    return self._saturation
  
  @property
  def name(self):
    return self._name


def getRooms():

  api = current_api()

  rooms = []
 
  groups = api["groups"]
  for groupID, group in groups.items():
     name = group["name"]
     lights = group["lights"]
     if "Entertainment area" not in name:
       roomlights = []
       for lightID in lights:
          light = api["lights"][lightID]
          roomlights.append(Light(light))

       rooms.append(Room(groupID, name, roomlights))

  rooms = sorted(rooms, key=lambda room: room.name)

  return rooms

def set_scene(scene_id):
  bridge.activate_scene(group_id=mainroom, scene_id=scene_id) 

def darken():
  """darken lights in room"""
  room = getRoom(settings.MAIN_ROOM)
  room.brightness = max(room.brightness - settings.BRIGHTNESS_STEP, 0)

def lighten():
  """brighten lights in room"""
  room = getRoom(settings.MAIN_ROOM)
  room.brightness = min(room.brightness + settings.BRIGHTNESS_STEP, 255)

def toggle():
  """toggle room on/off"""
  room = getRoom(settings.MAIN_ROOM)
  room.on = not room.on

