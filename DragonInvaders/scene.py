class Scene:
    def __init__(self):
        self.scene = {
            'game': False,
            'menu': False,
        }

        # Default scene
        self.activate_scene('menu')

    def activate_scene(self, scene):
        """Set the scene"""
        for key in self.scene.keys():
            if key == scene:
                self.scene[key] = True
            else:
                self.scene[key] = False

