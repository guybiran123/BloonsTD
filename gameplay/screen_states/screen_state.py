import pygame
from utils.constants import *


class ScreenState:

    def __init__(self, screen: pygame.surface.Surface):
        self._screen = screen
        self._buttons = pygame.sprite.Group()
        self.add_buttons()
        self._background = pygame.image.load(HOME_SCREEN_IMAGE)
        self._change_screen_state = False  # tells if the screen state needs to be changed
        self._button_name_to_function = {}

    def draw(self):
        self._screen.blit(self._background, (0, 0))
        self._buttons.draw(self._screen)

    def handle_events(self, event: pygame.event.Event):
        self.handle_button_clicks(event)

    def handle_button_clicks(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self._buttons.sprites():
                if button.is_clicked(pygame.mouse.get_pos()):
                    if button.get_name() in self._button_name_to_function:
                        self._button_name_to_function[button.get_name()]()
                        button.reset()
                    else:
                        print("No function found for button " + button.get_name())

    def add_buttons(self):
        pass
