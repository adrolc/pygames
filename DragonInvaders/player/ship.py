import pygame

from utilities.asset_path import AssetPath
from .bullet import Bullet
from .life import Lifes

class Ship:
    """Player class"""
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(AssetPath.ship)
        self.image = pygame.transform.scale(self.image, self.settings.ship_size)
        self.rect = self.image.get_rect()

        self.center_ship()
        self.rect.y -= self.settings.ship_bottom_margin

        self.moving_right = False
        self.moving_left = False

        self.bullets = pygame.sprite.Group()

        self.lifes = Lifes(self.game)

        # Automatic fire event
        self.FIRE = pygame.USEREVENT + 5

    def fire_on(self):
        """Set the time interval to fire the bullet"""
        pygame.time.set_timer(self.FIRE, self.settings.ship_fire_speed)

    def fire_off(self):
        """Set timer to 0 - Turning off automatic fire"""
        pygame.time.set_timer(self.FIRE, 0)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

        self._update_bullets()

    def draw(self):
        self.screen.blit(self.image, self.rect)

        self._draw_bullets()

        self.lifes.draw()

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        # Set the x coordinate to float type for better precision
        self.x = float(self.rect.x)

    def fire_bullet(self):
        new_bullet = Bullet(self.game, self.settings.bullet_type)
        self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update all bullets in the group"""
        self.bullets.update()

        # remove bullet from group if its position moves beyond the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _draw_bullets(self):
        """Draw all bullets in the group"""
        for bullet in self.bullets.sprites():
            bullet.draw()

