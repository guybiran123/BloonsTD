import pygame
import sys
from gameplay.game import Game
from gameplay.game_map import GameMap
from gameplay.towers.dart_monkey import DartMonkey
from gameplay.balloon import Balloon
from utils.point import Point
from utils.constants import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Bloons TD")

    running = True
    game = Game(Maps.MAP1, 20)
    game_map = GameMap(game, screen)
    image = pygame.image.load(MAP_TO_IMAGE[Maps.MAP1])
    clock = pygame.time.Clock()
    counter = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos_point = Point(mouse_pos[X], mouse_pos[Y])
                monkey = DartMonkey(mouse_pos_point, game_map)
                game_map.add_tower(monkey)
                counter = counter + 1 if counter < 6 else 1
                game_map.add_balloon(Balloon(1, game_map))

        screen.blit(image, (0, 0))
        activate_drawables(game_map)
        draw_drawables(game_map, screen)
        pygame.display.flip()

        clock.tick(REFRESH_RATE)

    pygame.quit()
    sys.exit()


def draw_drawables(game_map: GameMap, screen: pygame.surface.Surface):
    game_map.get_balloons().draw(screen)
    game_map.get_towers().draw(screen)
    game_map.get_shots().draw(screen)


def activate_drawables(game_map: GameMap):
    for balloon in game_map.get_balloons().sprites():
        balloon.activate()
    for tower in game_map.get_towers().sprites():
        tower.activate()
    for shot in game_map.get_shots().sprites():
        shot.activate()


if __name__ == '__main__':
    main()
