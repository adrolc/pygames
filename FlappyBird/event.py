import pygame
import sys

class Event:
    def __init__(self, game):
        self.game = game

    def check_event(self, event):
        # Exit game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Exit game
            if event.key == pygame.K_q:
                sys.exit()
            # Jump
            elif event.key == pygame.K_SPACE and not self.game.lost:
                self.game.bird.jump()
            # New game
            elif event.key == pygame.K_SPACE and self.game.lost:
                self.game.scoreboard.reset()
                self.game.bird.reset()
                self.game.pipe.generate_pipe()
                self.game.lost = False
        # Wing flapping animation
        elif event.type == self.game.bird.BIRD_ANIMATION:
            self.game.bird.animation()
