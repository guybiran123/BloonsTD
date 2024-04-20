import pygame
import sys
from gameplay.screen_states.screen_state import ScreenState
from gameplay.screen_states.home_screen import HomeScreen
from gameplay.screen_states.help_screen import HelpScreen
from gameplay.screen_states.level_selection_screen import LevelSelectionScreen
from gameplay.screen_states.in_game_screen import InGameScreen
from gameplay.screen_states.game_ended_screen import GameEndedScreen
from utils.constants import *


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Bloons TD")
    running = True
    clock = pygame.time.Clock()
    screen_state = HomeScreen(screen)
    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1, 0.0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                screen_state.handle_events(event)
        screen_state.activate()
        screen_state.draw()
        pygame.display.flip()

        if screen_state.get_change_screen_state():
            if screen_state.get_next_screen_state() == State.HOME_SCREEN:
                screen_state = HomeScreen(screen)
            elif screen_state.get_next_screen_state() == State.HELP_SCREEN:
                screen_state = HelpScreen(screen)
            elif screen_state.get_next_screen_state() == State.LEVEL_SELECTION:
                screen_state = LevelSelectionScreen(screen)
            elif screen_state.get_next_screen_state() == State.IN_GAME:
                screen_state = InGameScreen(screen,
                                            screen_state.get_selected_map(),
                                            screen_state.get_selected_mode())
            elif screen_state.get_next_screen_state() == State.GAME_ENDED:
                screen_state = GameEndedScreen(screen, screen_state.get_did_win())

        clock.tick(REFRESH_RATE)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
