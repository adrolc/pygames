class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800

        # Item drop
        self.gold_drop_speed = 0.4
        self.gold_img_size = (35,35)
        self.gold_rotate_animation_speed = 80 # ms

        self.item_drop_speed = 0.4
        self.item_drop_luck = 20 # percentage of chance for drop item
        # 2000 = 2 sec -> every two seconds there is a chance to drop an item
        self.item_drop_lottery_speed = 2000

        # Ship
        self.ship_size = (100, 100)
        self.ship_bottom_margin = 40
        self.heart_icon_size = (35, 35)
        self.ship_speed = 1
        self.ship_lives = 3
        self.ship_fire_speed = 250

        # Bullets
        self.ship_bullet_speed = 1
        self.bullet_size = [
            (20, 50),
            (40, 50),
            (60, 50),
            (80, 50),
        ]
        # default - single bullet
        self.bullet_type = 0

        # Dragons
        self.dragon_movement_animation_speed = 260 # ms
        self.dragon_explosion_animation_speed = 0.05
        self.dragon_speed = 0.1 # level 1
        self.dragons_number = 20 # level 1 -> number of dragons to kill
        self.dragon_spawn_speed = 1000 # (ms)  # level 1

        # scale of progress
        self.dragon_speed_scale = 1.1
        self.increase_dragons_scale = 1.15
        # self.dragon_spawn_speed_scale = 0.95

        # button
        self.menu_button_width = 300
        self.menu_button_height = 60
        self.menu_button_margin = 20
