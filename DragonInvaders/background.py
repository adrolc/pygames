import pygame
from utilities.asset_path import AssetPath

class Background:
    def __init__(self, game):
        self.screen = game.screen

        self.image = pygame.image.load(AssetPath.background)
        self.image = pygame.transform.scale(self.image, (game.settings.screen_width, game.settings.screen_width))

    def draw(self):
        self.screen.blit(self.image, (0, 0))
