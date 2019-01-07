import phue
import settings
import typing

bridge = phue.Bridge(settings.BRIDGE_IP)

scenes = {}

def findRoom(roomName: str) -> typing.Optional[int]:
  for room in bridge.groups:
    if roomName == room.name:
      return room.group_id
  return None

def getRoom(roomName: str):
  for room in bridge.groups:
    if roomName == room.name:
      return room
  return None

mainroom = findRoom(settings.MAIN_ROOM)

for sceneID, scene in bridge.get_api()["scenes"].items():
  if scene["recycle"] == False and scene.get("group") == str(mainroom):
    scenes[sceneID] = scene

def current_api() -> dict:
  return bridge.get_api()

class Light:
    def __init__(self, api: dict):
        self._name = api["name"]
        self._on = api["state"]["on"]
        self._brightness = api["state"]["bri"]
        self._saturation = api["state"]["sat"]
        self._hue = api["state"]["hue"]

    @property
    def on(self):
        return self._on

    @property
    def brightness(self) -> int:
        return self._brightness

    @property
    def hue(self) -> int:
        return self._hue

    @property
    def saturation(self) -> int:
        return self._saturation

    @property
    def name(self) -> str:
        return self._name

class Room:
    def __init__(self, group_id: typing.Any, name: str, lights: typing.List[Light]) -> None:
        self._id = int(group_id)
        self._name = str(name)
        self._lights = lights

    @property
    def group_id(self) -> int:
        return self._id

    @property 
    def name(self) -> str:
        return self._name

    @property 
    def lights(self) -> typing.List[Light]:
        return self._lights

def getRooms() -> typing.List[Room]:

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

def set_scene(scene_id: int) -> None:
  bridge.activate_scene(group_id=mainroom, scene_id=scene_id) 

def darken() -> None:
  """darken lights in room"""
  room = getRoom(settings.MAIN_ROOM)
  room.brightness = max(room.brightness - settings.BRIGHTNESS_STEP, 0)

def lighten() -> None:
  """brighten lights in room"""
  room = getRoom(settings.MAIN_ROOM)
  room.brightness = min(room.brightness + settings.BRIGHTNESS_STEP, 255)

def toggle() -> None:
  """toggle room on/off"""
  room = getRoom(settings.MAIN_ROOM)
  room.on = not room.on

