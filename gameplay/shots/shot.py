import math
import pygame
from utils.drawable import Drawable
from utils.point import Point
from utils.direction import Direction
from gameplay.game_map import GameMap
from utils.constants import *


class Shot(Drawable):

    def __init__(
            self,
            position: Point,
            direction: Direction,
            destination: Point,
            image: str,
            shot_range: int,
            damage: int,
            speed: int,
            game_map: GameMap
    ):
        super().__init__(position, direction, image)
        self._start_point = Point(position.get_x(), position.get_y())
        self._destination = destination
        self._shot_range = shot_range
        self._damage = damage
        self._speed = speed
        self._last_moving_time = 0
        self._y_counter = 0.0
        self._y_progress = 0         # real y progress
        self._game_map = game_map

    def get_damage(self):
        return self._damage

    def activate(self):
        current_time = pygame.time.get_ticks()
        self.check_collisions()
        if current_time - self._last_moving_time > COOLDOWN_TIME:
            self.move()
            if self._position.get_distance(self._start_point) > self._shot_range:
                self._game_map.remove_shot(self)

    def check_collisions(self):
        hit_balloons = pygame.sprite.spritecollide(self, self._game_map.get_balloons(), False)
        if hit_balloons:
            balloon = hit_balloons[0]
            balloons_hp = balloon.get_hp()
            balloon.hit(self._damage)
            self._damage -= balloons_hp
            if self._damage <= 0:
                self._game_map.remove_shot(self)

    def move(self):
        delta_x = self._destination.get_x() - self._position.get_x()
        delta_y = self._destination.get_y() - self._position.get_y()
        for _ in range(self._speed):
            movement = self.single_move(delta_x, delta_y)
            if movement in (Movement.PLUS_X, Movement.MINUS_X):
                self.increase_x() if movement == Movement.PLUS_X else self.decrease_x()
            else:
                self.increase_y() if movement == Movement.PLUS_Y else self.decrease_y()
                self._y_progress += 1 if movement == Movement.PLUS_Y else -1

    def single_move(self, delta_x: int, delta_y: int) -> Movement:
        if delta_x != 0:
            y_extension = delta_y / delta_x
            if abs(self._y_progress) < abs(math.floor(self._y_counter)):
                return Movement.PLUS_Y if delta_y > 0 else Movement.MINUS_Y
            else:
                self._y_counter += y_extension
                return Movement.PLUS_X if delta_x > 0 else Movement.MINUS_X
        else:
            return Movement.PLUS_Y if delta_y > 0 else Movement.MINUS_Y
