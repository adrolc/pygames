
import pygame
from pygame.sprite import Sprite

from utilities.asset_path import AssetPath

class Gold(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.images = []
        for frame in AssetPath.gold_frames:
            image = pygame.image.load(frame)
            image = pygame.transform.scale(image, self.settings.gold_img_size)
            self.images.append(image)

        self.animation_index = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.gold_drop_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def animate(self):
        """Animation of gold rotation"""
        self.animation_index += 1
        if self.animation_index == len(self.images):
            self.animation_index = 0
        self.image = self.images[self.animation_index]

class Golds:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.golds = pygame.sprite.Group()

        self.GOLD_ROTATE_ANIMATION = pygame.USEREVENT + 2
        pygame.time.set_timer(self.GOLD_ROTATE_ANIMATION, self.settings.gold_rotate_animation_speed)

    def drop_gold(self, dragon_rect):
        gold = Gold(self.screen, self.settings)
        gold.rect.center = dragon_rect.center
        gold.y = gold.rect.y
        self.golds.add(gold)

    def update(self):
        self.golds.update()

        # remove gold from group if its position moves beyond the bottom of the screen
        for gold in self.golds.copy():
            if gold.rect.top >= self.settings.screen_height:
                self.golds.remove(gold)

    def draw(self):
        self.golds.draw(self.screen)

    def animate(self):
        """Animate all gold in the group"""
        for gold in self.golds.sprites():
            gold.animate()
