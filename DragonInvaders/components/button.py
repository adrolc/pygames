import pygame.font
from pygame.sprite import Sprite

class Button(Sprite):
    def __init__(
        self,
        game,
        text,
        width,
        height,
        button_color,
        active_button_color,
        text_color,
        font_size,
        font_family
    ):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Button properties
        self.width, self.height = width, height
        self.button_color = button_color
        self.active_button_color = active_button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font_family, font_size)

        # Create a rect of button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Render text
        self._render_text(text)

    def _render_text(self, text):
        """Placing text on the button"""
        self.text_image = self.font.render(text, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self):
        """Display a button and text in it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
