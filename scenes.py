import lights

scenes = sorted(list(lights.scenes.items()), key=lambda s: s[1]["name"])
sceneNames = [scene.get("name") for sceneID, scene in scenes]
sceneIdx = 0
      
def next_scene():
  global sceneIdx
  sceneIdx += 1
  sceneIdx %= len(scenes)  
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

