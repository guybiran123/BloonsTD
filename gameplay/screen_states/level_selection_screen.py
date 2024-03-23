import pygame
from gameplay.screen_states.screen_state import ScreenState
from utils.text_box import TextBox
from utils.constants import *


class LevelSelectionScreen(ScreenState):

    def __init__(self, screen: pygame.surface.Surface):
        self.__buttons_names = [ButtonName.SELECT_MAP1,
                                ButtonName.SELECT_MAP2,
                                ButtonName.SELECT_MAP3,
                                ButtonName.SELECT_NORMAL_MODE,
                                ButtonName.SELECT_SANDBOX_MODE,
                                ButtonName.START_GAME]
        super().__init__(screen, self.__buttons_names)
        self.__selected_map = Maps.MAP1
        self.__selected_mode = GameMode.NORMAL
        self.add_text_boxes()
        self._button_name_to_function = {
            ButtonName.SELECT_MAP1: self.select_map1,
            ButtonName.SELECT_MAP2: self.select_map2,
            ButtonName.SELECT_MAP3: self.select_map3,
            ButtonName.SELECT_NORMAL_MODE: self.select_normal_mode,
            ButtonName.SELECT_SANDBOX_MODE: self.select_sandbox_mode,
            ButtonName.START_GAME: self.start_game
        }

    def draw(self):
        self._screen.blit(self._background, (0, 0))
        level_selection_background_image = pygame.image.load(LEVEL_SELECTION_BACKGROUND_IMAGE)
        level_selection_background_image.set_colorkey(COLOR_KEY)
        self._screen.blit(level_selection_background_image,
                          ((WINDOW_WIDTH - level_selection_background_image.get_rect().width) / 2,
                           (WINDOW_HEIGHT - level_selection_background_image.get_rect().height) / 2
                           ))
        self._buttons.draw(self._screen)
        self.draw_text_boxes()

    def select_map1(self):
        self.__selected_map = Maps.MAP1

    def select_map2(self):
        self.__selected_map = Maps.MAP2

    def select_map3(self):
        self.__selected_map = Maps.MAP3

    def select_normal_mode(self):
        self.__selected_mode = GameMode.NORMAL

    def select_sandbox_mode(self):
        self.__selected_mode = GameMode.SANDBOX

    def start_game(self):
        self._change_screen_state = True

    def get_selected_map(self):
        return self.__selected_map

    def get_selected_mode(self):
        return self.__selected_mode

    def add_text_boxes(self):
        self._text_boxes.append(TextBox(366, 370, 30, (255, 255, 255), "Normal"))
        self._text_boxes.append(TextBox(580, 370, 30, (255, 255, 255), "Sandbox"))
