import pygame

from utilities.asset_path import AssetPath

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.render_level()
        self.render_dragons_left()
        self.render_gold()

        # Event showing the new level for 3 seconds
        self.HIDE_LEVELUP = pygame.USEREVENT + 3
        self.levelup_is_shown = False


    def render_level(self):
        self.level = str(self.game.game_stats.level)
        self.level_image = self.font.render(f"Level: {self.level}", True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.midtop = self.screen_rect.midtop
        self.level_rect.y += 10

    def render_dragons_left(self):
        dragons_left = str(self.game.dragons.dragons_left)
        self.dragons_left_image = self.font.render(f"Left: {dragons_left}", True, self.text_color)

        self.dragons_left_rect = self.dragons_left_image.get_rect()
        self.dragons_left_rect.x = 10
        self.dragons_left_rect.y = 10

    def render_gold(self):
        # Gold icon
        self.gold_icon_image = pygame.image.load(AssetPath.gold)
        self.gold_icon_image = pygame.transform.scale(self.gold_icon_image, self.game.settings.gold_img_size)
        self.gold_icon_rect = self.gold_icon_image.get_rect()
        self.gold_icon_rect.topright = (self.game.settings.screen_width - 10, 10)

        # Gold value
        gold = str(self.game.game_stats.gold)
        self.gold_image = self.font.render(gold, True, self.text_color)

        self.gold_rect = self.gold_image.get_rect()
        self.gold_rect.center = self.gold_icon_rect.center
        self.gold_rect.right = self.gold_icon_rect.left - 15

    def draw(self):
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.dragons_left_image, self.dragons_left_rect)
        self.screen.blit(self.gold_icon_image, self.gold_icon_rect)
        self.screen.blit(self.gold_image, self.gold_rect)


    def _render_levelup(self):
        self.levelup_image = self.font.render(f"Level: {self.level}", True, self.text_color)

        self.levelup_rect = self.levelup_image.get_rect()
        self.levelup_rect.center = self.screen_rect.center

    def draw_levelup(self):
        if self.levelup_is_shown:
            self.screen.blit(self.levelup_image, self.levelup_rect)

    def show_levelup(self):
        """Render and show a new level, then run an event to turn it off"""
        self._render_levelup()
        self.levelup_is_shown = True
        # this event will disable the display of the new level after 3 seconds
        pygame.time.set_timer(self.HIDE_LEVELUP, 3000)

    def hide_levelup(self):
        """Method called by the event. Disables the event and stops displaying the new level"""
        pygame.time.set_timer(self.HIDE_LEVELUP, 0)
        self.levelup_is_shown = False




