import random
import math

from ball import Ball

class Environment:
    def __init__(self, simulation):
        self.simulation = simulation
        self.settings = self.simulation.settings

        self.balls = []
        self.selected_ball = None

    def generate_balls(self, n):
        for _ in range(n):
            radius = random.randint(
                self.settings.ball_radius_range_a,
                self.settings.ball_radius_range_b
            )
            x = random.randint(radius, self.settings.screen_width - radius)
            y = random.randint(radius, self.settings.screen_height - radius)
            angle = random.uniform(0, math.pi * 2)
            color = (
                random.randint(0,220),
                random.randint(0,220),
                random.randint(0,220)
            )
            speed = random.random()
            ball = Ball(self.simulation, x, y, color, angle, speed, radius)
            self.balls.append(ball)

    def bounce(self, ball):
        # Left wall
        if ball.x < ball.radius:
            ball.x = ball.radius + (ball.radius - ball.x)
            ball.angle = -ball.angle
            ball.speed *= ball.elasticity
        # Right wall
        elif ball.x > self.settings.screen_width - ball.radius:
            ball.x = (self.settings.screen_width - ball.radius) - (ball.x - (self.settings.screen_width - ball.radius))
            ball.angle = -ball.angle
            ball.speed *= ball.elasticity
        # Top wall
        if ball.y < ball.radius:
            ball.y = ball.radius + (ball.radius - ball.y)
            ball.angle = math.pi - ball.angle
            ball.speed *= ball.elasticity
        # Bottom wall
        elif ball.y > self.settings.screen_height - ball.radius:
            ball.y = (self.settings.screen_height - ball.radius) - (ball.y - (self.settings.screen_height - ball.radius))
            ball.angle = math.pi - ball.angle
            ball.speed *= ball.elasticity

    def check_selected_ball(self, mouse_pos):
        """Calculates the distance between the cursor position
        and the center of the circle. If the distance is less or equal
         to the radius, it will set the selected ball"""
        mouse_x, mouse_y = mouse_pos
        for ball in self.balls:
            dx = ball.x - mouse_x
            dy = ball.y - mouse_y
            distance = math.hypot(dx, dy)
            if distance <= ball.radius:
                self.selected_ball = ball

    def move_ball(self, mouse_pos):
        """The selected ball follows the cursor
         with a slight delay to enable the throw"""
        mouse_x, mouse_y = mouse_pos
        dx = mouse_x - self.selected_ball.x
        dy = mouse_y - self.selected_ball.y
        delay = 0.15
        self.selected_ball.speed = math.hypot(dx, dy) * delay
        self.selected_ball.angle = math.pi/2 - math.atan2(dy, dx)


    def update_balls(self):
        for ball in self.balls:
            ball.update()
            self.bounce(ball)

    def draw_balls(self):
        for ball in self.balls:
            ball.draw()

