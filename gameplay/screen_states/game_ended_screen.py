import pygame
from gameplay.screen_states.screen_state import ScreenState
from utils.text_box import TextBox
from utils.constants import *


class GameEndedScreen(ScreenState):

    def __init__(self, screen: pygame.surface.Surface, did_win: bool):
        self.__did_win = did_win
        self.__buttons_names = [ButtonName.BACK_TO_HOME_SCREEN]
        super().__init__(screen, self.__buttons_names)
        self._next_screen_state = State.HOME_SCREEN
        self._button_name_to_function = {
            ButtonName.BACK_TO_HOME_SCREEN: self.back_to_home_screen
        }

    def draw(self):
        level_selection_background_image = pygame.image.load(LEVEL_SELECTION_BACKGROUND_IMAGE)
        level_selection_background_image.set_colorkey(COLOR_KEY)
        self._screen.blit(level_selection_background_image,
                          ((WINDOW_WIDTH - level_selection_background_image.get_rect().width) / 2 - 75,
                           (WINDOW_HEIGHT - level_selection_background_image.get_rect().height) / 2
                           ))
        self._buttons.draw(self._screen)
        if self.__did_win:
            you_win_image = pygame.image.load(YOU_WIN_IMAGE)
            you_win_image.set_colorkey(COLOR_KEY)
            self._screen.blit(you_win_image, YOU_WIN_POSITION)
        else:
            game_over_image = pygame.image.load(GAME_OVER_IMAGE)
            game_over_image.set_colorkey(COLOR_KEY)
            self._screen.blit(game_over_image, GAME_OVER_POSITION)

    def back_to_home_screen(self):
        self._change_screen_state = True
