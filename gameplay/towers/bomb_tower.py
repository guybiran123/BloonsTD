import pygame
from gameplay.towers.tower import Tower
from utils.point import Point
from gameplay.game_map import GameMap
from gameplay.balloon import Balloon
from gameplay.shots.bomb import Bomb
from utils.constants import *


class BombTower(Tower):
    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position,
                         BOMB_TOWER_IMAGE,
                         BOMB_TOWER_COST,
                         BOMB_TOWER_SELL_COST,
                         BOMB_TOWER_SHOT_SPEED,
                         BOMB_TOWER_SHOT_DAMAGE,
                         BOMB_TOWER_SHOOTING_SPEED,
                         BOMB_TOWER_RANGE_RADIUS,
                         game_map)

    def shoot_balloon(self, balloon: Balloon):
        self._last_shot_time = pygame.time.get_ticks()
        direction = self._position.calc_angle_to_point(balloon.get_position())
        dart = Bomb(
            Point(self._position.get_x(), self._position.get_y()),
            balloon.get_position(),
            self._range_radius,
            self._shot_damage,
            self._shot_speed,
            self._game_map)
        self.set_direction_value(direction)
        self._game_map.add_shot(dart)


