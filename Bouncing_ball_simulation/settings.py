class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 800
        self.screen_height = 600

        # Env
        self.background = (255, 255, 255)
        self.gravity = (0, 0.0008) # vector

        # Balls
        self.ball_radius_range_a = 20
        self.ball_radius_range_b = 30
        self.elasticity = 0.75
        self.number_of_balls = 55


