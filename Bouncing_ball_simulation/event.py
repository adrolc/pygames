import pygame
import sys

class Event:
    def __init__(self, simulation):
        self.simulation = simulation

    def check_event(self, event):
        # Exit game
        if event.type == pygame.QUIT:
            sys.exit()
        # Take the ball
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.simulation.environment.check_selected_ball(mouse_pos)
        # Drop the ball
        elif event.type == pygame.MOUSEBUTTONUP:
            self.simulation.environment.selected_ball = None
