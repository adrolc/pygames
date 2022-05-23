import pygame
from pygame.sprite import Sprite

from utilities.asset_path import AssetPath

class Life(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load(AssetPath.heart)
        self.image = pygame.transform.scale(self.image, self.settings.heart_icon_size)
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Lifes():
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.number_of_lives = self.settings.ship_lives

        self.lifes = pygame.sprite.Group()
        self.start()

    def start(self):
        self.lifes.empty()
        for i in range(self.number_of_lives):
            life = Life(self.screen, self.settings)
            life.rect.y = self.settings.screen_height - life.rect.height - 10
            life.rect.x = 10 + (life.rect.width + 5) * i
            self.lifes.add(life)

    def decrease(self):
        self.lifes.remove(self.lifes.sprites()[-1])

    def increase(self):
        if len(self.lifes) < 3:
            life = Life(self.screen, self.settings)
            life.rect.y = self.settings.screen_height - life.rect.height - 10
            life.rect.x = 10 + (life.rect.width + 5) * len(self.lifes)
            self.lifes.add(life)

    def dead(self):
        if not len(self.lifes):
            return True
        return False

    def draw(self):
        self.lifes.draw(self.screen)


