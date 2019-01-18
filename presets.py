import state, scenes

class RecallPreset:
    def __init__(self, preset: int) -> None:
        self._preset = preset

    @property
    def scene(self) -> str:
        return state.get_preset(self._preset)

    def __call__(self) -> None:
        newScene = self.scene
        if newScene is not None:
            scenes.set_scene(newScene)

class MarkPreset:
    def __init__(self, preset: int) -> None:
        self._preset = preset

    def __call__(self) -> None:
        state.mark_preset(self._preset, scenes.current_scene())

    @property
    def __doc__(self) -> str:
        return "mark last set scene as preset " + str(self._preset)


