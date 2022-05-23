class Level:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen

        # Scale of progress
        self.dragon_speed_scale = self.settings.dragon_speed_scale
        self.increase_dragons_scale = self.settings.increase_dragons_scale
        # self.dragon_spawn_speed_scale = self.settings.dragon_spawn_speed_scale

        self.start()


    def start(self):
        """Level 1 - initial parameters"""
        self.dragon_speed = self.settings.dragon_speed
        self.dragons_number = self.settings.dragons_number
        self.dragon_spawn_speed = self.settings.dragon_spawn_speed # ms

    def levelup(self):
        self.dragon_speed *= self.dragon_speed_scale
        self.dragons_number = int(self.dragons_number * self.increase_dragons_scale)
        # self.dragon_spawn_speed = int(self.dragon_spawn_speed * self.dragon_spawn_speed_scale)


