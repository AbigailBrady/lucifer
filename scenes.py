import lights, settings, state

scenes = sorted(list(lights.scenes.items()), key=lambda s: s[1]["name"])
sceneNames = [scene.get("name") for sceneID, scene in scenes]
sceneIdx = 0
sceneFav = state.FAVE_SCENES

def is_fave(idx: int) -> bool:
  return sceneNames[idx] in sceneFav
 
def is_similar(a, b):
    for a_v, b_v in zip(a, b):
        if abs(a_v - b_v) > settings.XY_MATCH_THRESHOLD:
            return False
    return True

cached_scene_descs = {}

def get_scene_desc(scene_id):
    if scene_id in cached_scene_descs:
        return cached_scene_descs[scene_id]
    desc = lights.bridge.request('GET', '/api/' + lights.bridge.username + '/scenes/' + scene_id)
    cached_scene_descs[scene_id] = desc
    return desc

def guess_activated_scene(rooms: list = None, take_a_stab: bool = False):
    
    if rooms is None:
        rooms = lights.get_rooms()

    sceneIDs = [scene[0] for scene in scenes]

    cands = []

    for idx, sceneid in enumerate(sceneIDs):

        desc = get_scene_desc(sceneid)
        
        match = True

        for light in rooms.main.lights:
            
            scene_bright = desc["lightstates"][light.id]["bri"]
            light_bright = light.brightness
            
            if scene_bright != light_bright:
                break
            
            scene_temp = desc["lightstates"][light.id].get("ct")
            light_temp = light.ct
            
            if scene_temp is not None and scene_temp != light_temp:
                break
            
            scene_xy = desc["lightstates"][light.id].get("xy")
            light_xy = light.xy
            
            if scene_xy is not None and not is_similar(scene_xy, light_xy):
                break
            

        else:

            if take_a_stab:
                if idx == sceneIdx:
                    return idx

            cands.append(idx)

    if take_a_stab:
        for idx, cand in enumerate(cands):
            if is_fave(idx):
                return idx

    if cands != [] and take_a_stab:
        return cands[0]

    if len(cands) == 1:
        return cands[0]

    return None
    
def current_scene() -> str:
  return sceneNames[sceneIdx]

def prev_scene() -> None:
  """select the previous scene"""

  global sceneIdx
  sceneIdx -= 1
  sceneIdx %= len(scenes)  
  lights.set_scene(scenes[sceneIdx][0])

def next_scene() -> None:
  """select the next scene"""

  global sceneIdx
  sceneIdx += 1
  sceneIdx %= len(scenes)  
  lights.set_scene(scenes[sceneIdx][0])

def toggle_fav() -> None:
  """toggle last selected scene as favorite"""
  
  name = sceneNames[sceneIdx]
  if name in sceneFav:
    sceneFav.remove(name)
  else:
    sceneFav.append(name)
  state.save_state()

def prev_fav() -> None:
  """go to the previous favorite scene"""
  
  global sceneIdx
  origIdx = sceneIdx
  while True: 
    sceneIdx -= 1
    sceneIdx %= len(scenes)  
    if sceneNames[sceneIdx] in sceneFav:
      break
    if sceneIdx == origIdx:
      return
  lights.set_scene(scenes[sceneIdx][0])

def next_fav() -> None:
  """go to the next favorite scene"""
  
  global sceneIdx
  origIdx = sceneIdx
  while True:
    sceneIdx += 1
    sceneIdx %= len(scenes)  
    if sceneNames[sceneIdx] in sceneFav:
      break
    if sceneIdx == origIdx:
      return
  lights.set_scene(scenes[sceneIdx][0])


def reset_scene() -> None:
  """reset scene to last selected"""

  global sceneIdx
  lights.set_scene(scenes[sceneIdx][0])

def set_scene(sceneName: str) -> None:
  global sceneIdx
  try:
    idx = sceneNames.index(sceneName)
    sceneIdx = idx
    lights.set_scene(scenes[sceneIdx][0])
  except ValueError as e:
    pass

def set_starting(first_char: int) -> None:
  for name in sceneNames[sceneIdx+1:] + sceneNames[0:sceneIdx]:
    ch = ord(name.lower()[0])
    if ch == first_char:
      set_scene(name)
      return

sceneIdx = guess_activated_scene(take_a_stab = True) or 0

