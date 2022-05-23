import pygame
from pygame.sprite import Sprite

from utilities.asset_path import AssetPath

class Bullet(Sprite):
    def __init__(self, game, type):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(AssetPath.bullets[type])
        self.image = pygame.transform.scale(self.image, self.settings.bullet_size[type])
        self.rect = self.image.get_rect()

        # Set initial position
        self.rect.midtop = game.ship.rect.midtop

        # Set the y coordinate to float type for better precision
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.ship_bullet_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

