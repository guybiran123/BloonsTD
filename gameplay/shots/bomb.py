import pygame
from gameplay.shots.shot import Shot
from utils.point import Point
from utils.direction import Direction
from gameplay.game_map import GameMap
from gameplay.effects.explosion import Explosion
from utils.constants import *


class Bomb(Shot):
    def __init__(self, position: Point, destination: Point, shot_range: int, damage: int, speed: int, game_map: GameMap):
        super().__init__(
            position,
            Direction(False, 0),
            destination,
            BOMB_IMAGE,
            shot_range,
            damage,
            speed,
            game_map)

    def activate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._last_moving_time > COOLDOWN_TIME:
            self.move()
            if self._position.get_distance(self._start_point) >= self._shot_range or\
                    pygame.sprite.spritecollide(self, self._game_map.get_balloons(), False):
                self.explode()

    def explode(self):
        self._game_map.add_effect(
            Explosion(Point(self._position.get_x(), self._position.get_y()), self._damage, self._game_map)
        )
        self._game_map.remove_shot(self)
