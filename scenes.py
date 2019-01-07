import lights, settings, state

scenes = sorted(list(lights.scenes.items()), key=lambda s: s[1]["name"])
sceneNames = [scene.get("name") for sceneID, scene in scenes]
sceneIdx = 0
sceneFav = state.FAVE_SCENES

def is_fave(idx: int) -> bool:
  return sceneNames[idx] in sceneFav
 
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

