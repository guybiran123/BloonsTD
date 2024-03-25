import pygame
from gameplay.screen_states.screen_state import ScreenState
from utils.text_box import TextBox
from utils.constants import *


class HelpScreen(ScreenState):
    
    def __init__(self, screen: pygame.surface.Surface):
        self.__buttons_names = [ButtonName.CLOSE_BUTTON]
        super().__init__(screen, self.__buttons_names)
        self.add_text_boxes()
        self._button_name_to_function = {ButtonName.CLOSE_BUTTON: self.close_help}

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

    def add_text_boxes(self):
        for line in HELP_TEXT_LINES:
            self._text_boxes.append(TextBox(WINDOW_HEIGHT/2+205, 45 + 30*HELP_TEXT_LINES.index(line), 23, WHITE, line))

    def close_help(self):
        self._next_screen_state = State.HOME_SCREEN
        self._change_screen_state = True


        