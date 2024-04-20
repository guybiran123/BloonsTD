import pygame


class TextBox:

    def __init__(self, x, y, font_size, text_color, text, font=None, max_width=None):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.text_color = text_color
        self.text = text
        self.font = font or pygame.font.Font(None, self.font_size)

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_width, text_height = text_surface.get_size()
        screen.blit(text_surface, (self.x - text_width / 2, self.y - text_height / 2))

    def set_text(self, new_text):
        self.text = new_text
