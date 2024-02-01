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
        self._destination = destination
        self._shot_range = shot_range
        self._damage = damage
        self._speed = speed
        self._progress = 0
        self.last_moving_time = 0
        self.last_move = Axis.X
        self._game_map = game_map

    def get_damage(self):
        return self._damage

    def activate(self):
        current_time = pygame.time.get_ticks()
        self.check_collisions()
        if current_time - self.last_moving_time > COOLDOWN_TIME:
            self.move()
            if self._progress > self._shot_range:
                self._game_map.remove_shot(self)

    def check_collisions(self):
        hit_balloons = pygame.sprite.spritecollide(self, self._game_map.get_balloons(), False)
        for balloon in hit_balloons:
            balloons_hp = balloon.get_hp()
            balloon.hit(self._damage)
            self._damage -= balloons_hp
            if self._damage <= 0:
                self._game_map.remove_shot(self)

    def move(self):
        count_x = 0
        count_y = 0
        final_x = self._destination.get_x() - self._position.get_x()
        final_y = self._destination.get_y() - self._position.get_y()
        for i in range(self._speed):
            if count_x == final_x and count_y == final_y:
                count_x = 0
                count_y = 0
            if self.last_move == Axis.X:
                if self.check_y_increasement(count_y, final_y):
                    continue
                self.check_x_increasement(count_x, final_x)
            else:
                if self.check_x_increasement(count_x, final_x):
                    continue
                self.check_y_increasement(count_y, final_y)

    def check_x_increasement(self, count_x: int, final_x: int):
        if abs(count_x) < abs(final_x):
            if final_x > 0:
                self.increase_x()
                count_x += 1
            else:
                self.decrease_x()
                count_x -= 1
            self.last_move = Axis.X
            self._progress += 1
            return True
        return False

    def check_y_increasement(self, count_y: int, final_y: int):
        if abs(count_y) < abs(final_y):
            if final_y > 0:
                self.increase_y()
                count_y += 1
            else:
                self.decrease_y()
                count_y -= 1
            self.last_move = Axis.Y
            self._progress += 1
            return True
        return False
