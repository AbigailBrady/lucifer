import lights, settings

scenes = sorted(list(lights.scenes.items()), key=lambda s: s[1]["name"])
sceneNames = [scene.get("name") for sceneID, scene in scenes]
sceneIdx = 0
sceneFav = settings.FAVE_SCENES

def is_fave(idx):
  return sceneNames[idx] in sceneFav
 
def next_scene():
  global sceneIdx
  sceneIdx += 1
  sceneIdx %= len(scenes)  
  lights.set_scene(scenes[sceneIdx][0])

def toggle_fav():
  name = sceneNames[sceneIdx]
  if name in sceneFav:
    sceneFav.remove(name)
  else:
    sceneFav.append(name)  

def prev_fav():
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

def next_fav():
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

def prev_scene():
  global sceneIdx
  sceneIdx -= 1
  sceneIdx %= len(scenes)  
  lights.set_scene(scenes[sceneIdx][0])

def reset_scene():
  global sceneIdx
  lights.set_scene(scenes[sceneIdx][0])

def set_scene(sceneName):
  global sceneIdx
  idx = sceneNames.index(sceneName)
  sceneIdx = idx
  lights.set_scene(scenes[sceneIdx][0])

def set_starting(first_char):
  for name in sceneNames[sceneIdx+1:] + sceneNames[0:sceneIdx]:
    ch = ord(name.lower()[0])
    if ch == first_char:
      set_scene(name)
      return

