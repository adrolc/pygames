import pygame
import sys

from components.button import Button

menu_options = [
    'Play',
    'Shop',
    'Settings',
    'Exit',
]

# Properties for the menu button
button_prop = {
    'width': 300,
    'height': 60,
    'button_color': (71, 71, 135),
    'active_button_color': (30, 30, 60),
    'text_color': (255, 255, 255),
    'font_size': 48,
    'font_family' : None
}

class Menu():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.scene = game.scene

        # Buttons group
        self.buttons = pygame.sprite.Group()

        # Creating buttons
        for option in menu_options:
            self.buttons.add(Button(
                self,
                option,
                button_prop['width'],
                button_prop['height'],
                button_prop['button_color'],
                button_prop['active_button_color'],
                button_prop['text_color'],
                button_prop['font_size'],
                button_prop['font_family'],
            ))

        # Center the buttons vertically
        self.space = len(self.buttons) * (self.settings.menu_button_height + self.settings.menu_button_margin)
        self.start = (self.settings.screen_height - self.space) / 2
        for i, button in enumerate(self.buttons.sprites()):
            button.rect.top = self.start + ((self.settings.menu_button_height + self.settings.menu_button_margin) * i)
            button.text_image_rect.center = button.rect.center

        self.active_button = 0

    def draw(self):
        for button_number, button in enumerate(self.buttons.sprites()):
            if button_number == self.active_button:
                self.screen.fill(button.active_button_color, button.rect)
            else:
                self.screen.fill(button.button_color, button.rect)
            self.screen.blit(button.text_image, button.text_image_rect)

    def next_option(self):
        self.active_button += 1
        if self.active_button >= len(self.buttons):
            self.active_button = 0

    def previous_option(self):
        self.active_button -= 1
        if self.active_button < 0:
            self.active_button = len(self.buttons) - 1

    def run_active_option(self):
        if self.active_button == menu_options.index('Play'):
            self.scene.activate_scene('game')
        elif self.active_button == menu_options.index('Exit'):
            sys.exit()

