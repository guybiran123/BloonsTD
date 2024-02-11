import pygame
from utils.point import Point
from gameplay.game_map import GameMap
from utils.drawable import Drawable
from utils.direction import Direction
from utils.constants import *
from gameplay.balloon import Balloon
from gameplay.shots.dart import Dart


class Tower(Drawable):
    """
    A parent class that represents a tower in the game.
    """

    def __init__(
            self,
            position: Point,
            image: str,
            cost: int,
            sell_cost: int,
            shot_speed: int,
            shot_damage: int,
            shooting_speed: int,
            range_radius: int,
            game_map: GameMap
    ):
        super().__init__(position, Direction(True, INITIAL_ANGLE), image)
        self._cost = cost
        self._sell_cost = sell_cost
        self._shot_speed = shot_speed
        self._shot_damage = shot_damage
        self._shooting_speed = shooting_speed  # The smaller, the faster
        self._range_radius = range_radius
        self._is_pressed = False
        self._is_set = False
        self.last_shot_time = 0
        self._game_map = game_map
        self._balloons_in_range = []

    def get_cost(self) -> int:
        return self._cost

    def get_sell_cost(self) -> int:
        return self._sell_cost

    def get_shot_speed(self):
        return self._shot_speed

    def get_shot_damage(self):
        return self._shot_damage

    def get_shooting_speed(self):
        return self._shooting_speed

    def get_range_radius(self):
        return self._range_radius

    def get_is_pressed(self):
        return self._is_pressed

    def set_is_pressed(self, is_pressed: bool) -> None:
        self._is_pressed = is_pressed

    def get_is_set(self):
        return self._is_set

    def set_is_set(self, is_set) -> None:
        self._is_set = is_set

    def is_balloon_in_range(self, balloon: Balloon) -> bool:
        return self._range_radius >= self._position.get_distance(balloon.get_position())

    def activate(self):
        current_time = pygame.time.get_ticks()
        self.add_to_balloons_in_range()
        if self._balloons_in_range and current_time - self.last_shot_time > self._shooting_speed:
            first_balloon = self.get_first_balloon()
            self.shoot_balloon(first_balloon)

    def add_to_balloons_in_range(self):
        for balloon in self._game_map.get_balloons().sprites():
            if self.is_balloon_in_range(balloon):
                self._balloons_in_range.append(balloon)

    def get_first_balloon(self):
        return max(self._balloons_in_range, key=lambda balloon: balloon.get_route_progress())

    def shoot_balloon(self, balloon: Balloon):
        """
        The function takes a balloon and shoots a dart towards that balloon
        :param balloon:
        :return:
        """
        self.last_shot_time = pygame.time.get_ticks()
        direction = self._position.calc_angle_to_point(balloon.get_position())
        dart = Dart(
            self._position,
            direction,
            balloon.get_position(),
            self._range_radius,
            self._shot_damage,
            self._shot_speed,
            self._game_map)
        self.set_direction_value(direction)
        self._game_map.add_shot(dart)


