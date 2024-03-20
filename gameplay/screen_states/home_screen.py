import pygame
from gameplay.screen_states.screen_state import ScreenState
from gameplay.buttons.button import Button
from utils.constants import *


class HomeScreen(ScreenState):

    def __init__(self, screen: pygame.surface.Surface):
        super().__init__(screen)
        self._button_name_to_function = {ButtonName.HOME_SCREEN_BUTTON: self.home_screen_button_clicked}

    def add_buttons(self):
        buttons = []
        home_screen_button = Button(BUTTON_TO_POSITION[ButtonName.HOME_SCREEN_BUTTON],
                                    BUTTON_TO_IMAGE[ButtonName.HOME_SCREEN_BUTTON],
                                    ButtonName.HOME_SCREEN_BUTTON)
        buttons.append(home_screen_button)
        self.add_buttons_to_group(buttons)

    def add_buttons_to_group(self, buttons):
        for button in buttons:
            self._buttons.add(button)

    def home_screen_button_clicked(self):
        self._change_screen_state = True

