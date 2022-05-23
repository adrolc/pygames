class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 576
        self.screen_height = 1024

        # Game
        self.gravity = 0.25

        # Floor
        self.floor_speed = 4
        self.floor_hight = 75

        # Bird
        self.bird_left_margin = 25
        self.bird_jump_power = -10
        self.bird_animation_speed = 200

        # Pipe
        self.pipe_gap_size = 300
        self.pipe_movement_speed = 4
