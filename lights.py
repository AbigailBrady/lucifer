import phue
import settings
import typing

from pprint import pprint

bridge = phue.Bridge(settings.BRIDGE_IP)

scenes = {}

def find_room_id(roomName: str) -> typing.Optional[int]:
  for room in bridge.groups:
    if roomName == room.name:
      return room.group_id
  return None

def get_room_object(roomName: str):
  for room in bridge.groups:
    if roomName == room.name:
      return room
  return None

mainroom = find_room_id(settings.MAIN_ROOM)

for sceneID, scene in bridge.get_api()["scenes"].items():
  if scene["recycle"] == False and scene.get("group") == str(mainroom):
    scenes[sceneID] = scene

def current_api() -> dict:
  return bridge.get_api()

class Light:
    def __init__(self, lightID: str, api: dict):
        self._id = lightID
        self._name = api["name"]
        self._on = api["state"]["on"]
        self._brightness = api["state"]["bri"]
        self._xy = api["state"].get("xy")
        self._ct = api["state"].get("ct")

    @property
    def id(self):
        return self._id
    
    @property
    def on(self):
        return self._on

    @property
    def brightness(self) -> int:
        return self._brightness

    @property
    def ct(self) -> float:
        return self._ct
    
    @property
    def xy(self) -> list:
        return self._xy

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

class Rooms:
    def __init__(self, rooms: list) -> None:
        self.rooms = sorted(rooms, key=lambda room: room.name)

    @property
    def main(self) -> Room:
        for room in self.rooms:
            if room.group_id == mainroom:
                return room
        return None

    def __iter__(self):
        yield from self.rooms

def get_rooms() -> Rooms:

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
                roomlights.append(Light(lightID, light))

            rooms.append(Room(groupID, name, roomlights))

    return Rooms(rooms)


def set_scene(scene_id: int) -> None:
  bridge.activate_scene(group_id=mainroom, scene_id=scene_id) 

def darken() -> None:
  """darken lights in room"""
  room = get_room_object(settings.MAIN_ROOM)
  room.brightness = max(room.brightness - settings.BRIGHTNESS_STEP, 0)

def lighten() -> None:
  """brighten lights in room"""
  room = get_room_object(settings.MAIN_ROOM)
  room.brightness = min(room.brightness + settings.BRIGHTNESS_STEP, 255)

def dimmest() -> None:
  """put lights as dark as they will go (while still On)"""
  room = get_room_object(settings.MAIN_ROOM)
  room.brightness = 0

def brightest() -> None:
  """put lights as bright as they will go"""
  room = get_room_object(settings.MAIN_ROOM)
  room.brightness = 255

def toggle() -> None:
  """toggle room on/off"""
  room = get_room_object(settings.MAIN_ROOM)
  room.on = not room.on

