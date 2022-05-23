import pygame

class GameOver:
    def __init__(self, game):
        self.game = game

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.render_gameover()

        self.HIDE_GAMEOVER = pygame.USEREVENT + 6
        self.gameover_is_shown = False

    def render_gameover(self):
        self.gameover = 'Game over'
        self.gameover_image = self.font.render(self.gameover, True, self.text_color)

        self.gameover_rect = self.gameover_image.get_rect()
        self.gameover_rect.center = self.screen_rect.center

    def draw(self):
        if self.gameover_is_shown:
            self.screen.blit(self.gameover_image, self.gameover_rect)

    def show_gameover(self):
        self.gameover_is_shown = True
        self.game.dragons.stop_auto_spawn()
        self.game.drop.stop_auto_drop()
        pygame.time.set_timer(self.HIDE_GAMEOVER, 3000)

    def hide_gameover(self):
        pygame.time.set_timer(self.HIDE_GAMEOVER, 0)
        self.gameover_is_shown = False

    def reset_game(self):
        self.hide_gameover()
        self.game.dragons.start_auto_spawn()
        self.game.game_stats.reset()
        self.game.dragons.dragons_left = self.game.settings.dragons_number
        self.game.scoreboard.render_dragons_left()
        self.game.scoreboard.render_level()
        self.game.scoreboard.render_gold()
        self.game.drop.start_auto_drop()
        self.game.settings.bullet_type = 0
