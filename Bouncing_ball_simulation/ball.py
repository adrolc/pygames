import pygame
import math

class Ball:
    def __init__(self, simulation, x, y, color, angle, speed, radius, width = 0):
        self.screen = simulation.screen
        self.settings = simulation.settings
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.width = width
        self.elasticity = simulation.settings.elasticity

    def _gravity(self):
        """Add the gravity vector to the ball vector"""
        gravity_angle, gravity_strength = self.settings.gravity
        dx = math.sin(self.angle) * self.speed + math.sin(gravity_angle) * gravity_strength
        dy = math.cos(self.angle) * self.speed + math.cos(gravity_angle) * gravity_strength
        speed = math.hypot(dx, dy)
        angle = math.pi / 2 - math.atan2(dy, dx)
        self.angle, self.speed = angle, speed

    def update(self):
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed
        self._gravity()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, self.width)
