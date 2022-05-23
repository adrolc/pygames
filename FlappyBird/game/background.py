import pygame

from utilities.assets_path import AssetsPath

class Background:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        # Game background
        self.image_game = pygame.image.load(AssetsPath.background_day)
        self.image_game = pygame.transform.scale2x(self.image_game)
        self.rect_game = self.image_game.get_rect()
        self.rect_game.topleft = (0, 0)

        # Scoreboard background
        self.image_scoreboard = pygame.image.load(AssetsPath.background_scoreboard)
        self.image_scoreboard = pygame.transform.scale2x(self.image_scoreboard).convert_alpha()
        self.rect_scoreboard = self.image_scoreboard.get_rect()
        self.rect_scoreboard.center = self.screen.get_rect().center

    def draw_game_background(self):
        self.screen.blit(self.image_game, self.rect_game)

    def draw_scoreboard_background(self):
        self.screen.blit(self.image_scoreboard, self.rect_scoreboard)
