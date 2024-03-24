import pygame
from gameplay.buttons.button import Button
from gameplay.buttons.tower_button import TowerButton
from utils.constants import *


class ScreenState:

    def __init__(self, screen: pygame.surface.Surface, buttons_names: list):
        self._screen = screen
        self._buttons = pygame.sprite.Group()
        self._background = pygame.image.load(HOME_SCREEN_IMAGE)
        self._change_screen_state = False  # tells if the screen state needs to be changed
        self._next_screen_state = State.HOME_SCREEN
        self._text_boxes = []
        self._button_name_to_function = {}
        self._buttons_names = buttons_names
        self.add_buttons(self._buttons_names)

    def draw(self):
        self._screen.blit(self._background, (0, 0))
        self._buttons.draw(self._screen)
        self.draw_text_boxes()

    def activate(self):
        pass

    def draw_text_boxes(self):
        for text_box in self._text_boxes:
            text_box.draw(self._screen)

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handle_button_clicks()

    def handle_button_clicks(self):
        for button in self._buttons.sprites():
            if button.is_clicked(pygame.mouse.get_pos()):
                if button.get_name() in self._button_name_to_function:
                    self._button_name_to_function[button.get_name()]()
                    button.reset()
                else:
                    print("No function found for button " + button.get_name())

    def add_buttons(self, buttons_names: list):
        for button_name in buttons_names:
            self._buttons.add(self.create_button_from_name(button_name))

    def create_button_from_name(self, button_name: ButtonName):
        if button_name in TOWERS_BUTTONS_NAMES:
            return TowerButton(BUTTON_TO_POSITION[button_name],
                               BUTTON_TO_IMAGE[button_name],
                               button_name)
        return Button(BUTTON_TO_POSITION[button_name],
                      BUTTON_TO_IMAGE[button_name],
                      button_name)

    def get_change_screen_state(self):
        return self._change_screen_state

    def get_next_screen_state(self):
        return self._next_screen_state
