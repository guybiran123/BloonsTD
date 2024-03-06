import pygame
from gameplay.towers.tower import Tower
from utils.point import Point
from utils.direction import Direction
from gameplay.game_map import GameMap
from gameplay.shots.tack import Tack
from gameplay.balloon import Balloon
from utils.constants import *


class TackTower(Tower):
    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position,
                         TACK_TOWER_IMAGE,
                         TACK_TOWER_COST,
                         TACK_TOWER_SELL_COST,
                         TACK_TOWER_SHOT_SPEED,
                         TACK_TOWER_SHOT_DAMAGE,
                         TACK_TOWER_SHOOTING_SPEED,
                         TACK_TOWER_RANGE_RADIUS,
                         game_map)

    def shoot_balloon(self, balloon: Balloon):  # function doesn't work
        self._last_shot_time = pygame.time.get_ticks()
        for direction in range(0, 360, 45):
            tack = Tack(
                Point(self._position.get_x(), self._position.get_y()),
                direction,
                self._position.find_point_with_distance_and_angle(direction, self._range_radius),
                self._range_radius,
                self._shot_damage,
                self._shot_speed,
                self._game_map)
            self._game_map.add_shot(tack)


"""
    def activate(self):
        current_time = pygame.time.get_ticks()
        self.add_to_balloons_in_range()
        if self._balloons_in_range and current_time - self._last_shot_time > self._shooting_speed:
            self.shoot_balloon()
"""
