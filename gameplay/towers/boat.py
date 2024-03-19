import pygame
from gameplay.shots.dart import Dart
from gameplay.towers.tower import Tower
from utils.point import Point
from gameplay.game_map import GameMap
from gameplay.balloon import Balloon
from utils.constants import *


class Boat(Tower):

    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position,
                         BOAT_IMAGE,
                         BOAT_COST,
                         BOAT_SELL_COST,
                         BOAT_SHOT_SPEED,
                         BOAT_SHOT_DAMAGE,
                         BOAT_SHOOTING_SPEED,
                         BOAT_RANGE_RADIUS,
                         game_map)

    def shoot_balloon(self, balloon: Balloon):
        """
        The function takes a balloon and shoots a dart towards that balloon
        :param balloon:
        :return:
        """
        self._last_shot_time = pygame.time.get_ticks()
        direction = self._position.calc_angle_to_point(balloon.get_position())
        dart = Dart(
            Point(self._position.get_x(), self._position.get_y()),
            direction,
            balloon.get_position(),
            self._range_radius,
            self._shot_damage,
            self._shot_speed,
            self._game_map)
        self.set_direction_value(direction + 90)
        self._game_map.add_shot(dart)
