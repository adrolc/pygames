import pygame

from settings import Settings
from event import Event
from environment import Environment

class Simulation:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Bouncing ball simulation")

        self.event = Event(self)
        self.environment = Environment(self)

        self.environment.generate_balls(self.settings.number_of_balls)

    def run(self):
        while True:
            self._check_events()
            self._update()
            self._draw()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            self.event.check_event(event)

    def _update(self):
        self.environment.update_balls()
        if self.environment.selected_ball:
            self.environment.move_ball(pygame.mouse.get_pos())

    def _draw(self):
        self.screen.fill(self.settings.background)
        self.environment.draw_balls()


if __name__ == '__main__':
    simulation = Simulation()
    simulation.run()
