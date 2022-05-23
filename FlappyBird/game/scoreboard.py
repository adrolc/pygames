import pygame

from utilities.assets_path import AssetsPath

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.pipe_rect = game.pipe.rect[0]
        self.settings = game.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(AssetsPath.font, 55)

        self.__score = 0
        self.__highest_score = 0

        self.render_score()
        self.render_highest_score()

    def render_score(self, lost = False):
        self.score = str(self.__score)
        score_text = f"Score: {self.score}" if lost else self.score
        self.score_image = self.font.render(score_text, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = (self.settings.screen_width / 2, 100)

    def render_highest_score(self):
        self.highest_score = str(self.__highest_score)
        self.highest_score_image = self.font.render(f"High score: {self.highest_score}", True, self.text_color)

        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.center = (self.settings.screen_width / 2, self.settings.screen_height - 100)

    def _add_point(self):
        self.__score += 1
        self.render_score()

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def draw_score_summary(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)

    def update_score(self):
        if self.pipe_rect.right <= 4:
            self._add_point()

    def check_new_record(self):
        if self.__score > self.__highest_score:
            self.__highest_score = self.__score
            self.render_highest_score()

    def reset(self):
        self.__score = 0
        self.render_score()

