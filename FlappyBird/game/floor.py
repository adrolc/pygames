import pygame

from utilities.assets_path import AssetsPath

class Floor:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen

        self.image = pygame.image.load(AssetsPath.floor)
        self.image = pygame.transform.scale2x(self.image)

        self.rect = self.image.get_rect()

        self._floor_initial_position()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.settings.floor_speed
        if self.rect.right <= self.settings.screen_width:
            self._floor_initial_position()

    def _floor_initial_position(self):
        self.rect.bottomleft = (0, self.settings.screen_height + self.settings.floor_hight)


