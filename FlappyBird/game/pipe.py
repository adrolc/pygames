import pygame
import random

from utilities.assets_path import AssetsPath

class Pipe:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen

        top_pipe = pygame.image.load(AssetsPath.pipe_green)
        top_pipe = pygame.transform.flip(top_pipe, False, True)
        top_pipe =  pygame.transform.scale2x(top_pipe)

        bottom_pipe = pygame.image.load(AssetsPath.pipe_green)
        bottom_pipe = pygame.transform.scale2x(bottom_pipe)

        self.images = [top_pipe, bottom_pipe]

        self.rect = [
            self.images[0].get_rect(),
            self.images[1].get_rect()
        ]

        self.gap_height = [100, 150, 200, 250, 300, 350]

        self.generate_pipe()

    def draw(self):
        self.screen.blit(self.images[0], self.rect[0]) # top pipe
        self.screen.blit(self.images[1], self.rect[1]) # bottom pipe

    def update(self):
        for pipe in self.rect:
            pipe.x -= self.settings.pipe_movement_speed
        if self.rect[0].right <= 0:
            self.generate_pipe()

    def generate_pipe(self):
        gap_height = random.choice(self.gap_height)
        self.rect[0].bottomleft = (self.settings.screen_width, gap_height)
        self.rect[1].topleft = (self.settings.screen_width, gap_height + self.settings.pipe_gap_size)


