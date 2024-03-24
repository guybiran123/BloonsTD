import pygame
from gameplay.screen_states.screen_state import ScreenState
from gameplay.buttons.button import Button
from utils.constants import *


class HomeScreen(ScreenState):

    def __init__(self, screen: pygame.surface.Surface):
        self._buttons_names = [ButtonName.HOME_SCREEN_BUTTON]
        super().__init__(screen, self._buttons_names)
        self._next_screen_state = State.LEVEL_SELECTION
        self._button_name_to_function = {ButtonName.HOME_SCREEN_BUTTON: self.home_screen_button_clicked}

    def home_screen_button_clicked(self):
        self._change_screen_state = True

