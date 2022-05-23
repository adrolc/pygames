import pygame

from utilities.asset_path import AssetPath

class Explosion(pygame.sprite.Sprite):
    """Animation of the explosion after shooting down the dragon"""
    def __init__(self, screen, settings, dragon_rect):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load explosion frames
        self.frames = []
        for frame_path in AssetPath.explosion_frames:
            self.frames.append(pygame.image.load(frame_path))

        # Set starting params of animation
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = dragon_rect.center

        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_frame += self.settings.dragon_explosion_animation_speed

            if self.current_frame >= len(self.frames):
                self.is_animating = False
            else:
                self.image = self.frames[int(self.current_frame)]

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Explosions:
    """Group of explosion animation"""
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.explosions = pygame.sprite.Group()

    def explode(self, dragon_rect):
        """run the explosion animation"""
        explosion = Explosion(self.screen, self.settings, dragon_rect)
        self.explosions.add(explosion)

    def update(self):
        self.explosions.update()
        self.delete_finished_animations()

    def draw(self):
        self.explosions.draw(self.screen)

    def delete_finished_animations(self):
        """Remove animation from group when finished"""
        for explosion in self.explosions.copy():
            if not explosion.is_animating:
                self.explosions.remove(explosion)
