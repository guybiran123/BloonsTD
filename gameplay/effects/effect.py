import pygame
from utils.drawable import Drawable
from utils.point import Point
from gameplay.game_map import GameMap
from utils.direction import Direction
from utils.constants import *


class Effect(Drawable):

    def __init__(self, position: Point, duration: int, image: str, game_map: GameMap):
        super().__init__(position, Direction(False, 0), image)
        self._creation_time = pygame.time.get_ticks()
        self._duration = duration
        self._game_map = game_map

    def activate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._creation_time > self._duration:
            self._game_map.remove_effect(self)



