import pygame

from utilities.assets_path import AssetsPath

class Bird:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.movement = 0

        self.sound_wing = pygame.mixer.Sound(AssetsPath.sound_wing)
        self.sound_hit = pygame.mixer.Sound(AssetsPath.sound_hit)

        # Bird frames
        self.images = [pygame.transform.scale2x(pygame.image.load(bird)) for bird in AssetsPath.red_bird]

        self.frame_index = 0
        self.rect = self.images[self.frame_index].get_rect()

        # Set bird to the starting position
        self.center_bird()


        self.BIRD_ANIMATION = pygame.USEREVENT
        pygame.time.set_timer(self.BIRD_ANIMATION, self.settings.bird_animation_speed)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.movement += self.settings.gravity
        self.rect.y += self.movement
        self._bird_rotation()

    def center_bird(self):
        self.rect.midleft = (self.settings.bird_left_margin, self.settings.screen_height / 2)

    def jump(self):
        self.movement = self.settings.bird_jump_power
        self._play_sound_wing()

    def animation(self):
        self.frame_index += 1
        if self.frame_index >= len(self.images):
            self.frame_index = 0

    def _bird_rotation(self):
        self.image = pygame.transform.rotate(self.images[self.frame_index], self.movement * - 2.3)

    def _play_sound_wing(self):
        self.sound_wing.play()

    def play_sound_hit(self):
        self.sound_hit.play()

    def reset(self):
        self.center_bird()
        self.movement = 0
        self.frame_index = 0
