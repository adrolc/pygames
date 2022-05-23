import pygame

from settings import Settings
from event import Event
from game.background import Background
from game.floor import Floor
from game.bird import Bird
from game.pipe import Pipe
from game.scoreboard import Scoreboard

class FlappyBird:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("FlappyBird")

        self.lost = False

        self.event = Event(self)
        self.background = Background(self)
        self.floor = Floor(self)
        self.bird = Bird(self)
        self.pipe = Pipe(self)
        self.scoreboard = Scoreboard(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update()
            self._draw()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            self.event.check_event(event)

    def _update(self):
        if not self.lost:
            self.floor.update()
            self.bird.update()
            self.pipe.update()
            self.scoreboard.update_score()
            self._check_collisions()

    def _draw(self):
        self.background.draw_game_background()
        if not self.lost:
            self.pipe.draw()
            self.floor.draw()
            self.bird.draw()
            self.scoreboard.draw_score()
        else:
            self.background.draw_scoreboard_background()
            self.scoreboard.draw_score_summary()

    def _check_collisions(self):
        self._check_bird_collision()

    def _check_bird_collision(self):
        if self.bird.rect.collidelist([
            self.pipe.rect[0],
            self.pipe.rect[1],
            self.floor.rect
        ]) != -1 or self.bird.rect.top <= 0:
            self.bird.play_sound_hit()
            self.lost = True
            self.scoreboard.render_score(lost=True) # Add prefix 'Score'
            self.scoreboard.check_new_record()


if __name__ == '__main__':
    game = FlappyBird()
    game.run_game()
