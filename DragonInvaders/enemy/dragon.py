import pygame
from pygame.sprite import Sprite
from random import randint

from utilities.asset_path import AssetPath
from .explosion import Explosions


class Dragon(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        # Load dragon frames
        self.images = [
            pygame.image.load(AssetPath.dragon_frame_1),
            pygame.image.load(AssetPath.dragon_frame_2),
        ]
        self.animation_index = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # Set the y coordinate to float type for better precision
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.game.level.dragon_speed
        self.rect.y = self.y

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def animation(self):
        self.animation_index += 1
        if self.animation_index > 1:
            self.animation_index = 0
        self.image = self.images[self.animation_index]

class Dragons:
    def __init__(self, game):
        """Initialize group"""
        self.game = game
        self.dragons = pygame.sprite.Group()

        # Animation event
        self.DRAGON_MOVEMENT = pygame.USEREVENT
        pygame.time.set_timer(self.DRAGON_MOVEMENT, self.game.settings.dragon_movement_animation_speed)

        # Auto spawn dragon event
        self.SPAWN_DRAGON = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_DRAGON, self.game.settings.dragon_spawn_speed)

        self.explode_animation = Explosions(game)

        self.dragons_left = self.game.level.dragons_number

    def start_auto_spawn(self):
        pygame.time.set_timer(self.SPAWN_DRAGON, self.game.level.dragon_spawn_speed)

    def stop_auto_spawn(self):
        pygame.time.set_timer(self.SPAWN_DRAGON, 0)

    def spawn_dragon(self):
        """Add new dragon to group"""
        if self.dragons_left > 0:
            dragon = Dragon(self.game)
            dragon.rect.x = randint(0, self.game.settings.screen_width - dragon.rect.width)
            dragon.rect.bottom = 0
            self.dragons.add(dragon)


    def update(self):
        self.dragons.update()
        self.explode_animation.update()

    def draw(self):
        self.dragons.draw(self.game.screen)
        self.explode_animation.draw()

    def animation(self):
        """Show the next frame on each dragon object
        Method called by DRAGON_MOVEMENT event"""
        for dragon in self.dragons.sprites():
            dragon.animation()
