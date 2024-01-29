from utils.point import Point
from gameplay.game_map import GameMap
from utils.drawable import Drawable
from utils.direction import Direction
from utils.constants import *


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
        self._shooting_speed = shooting_speed
        self._range_radius = range_radius
        self._is_pressed = False
        self._is_set = False
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

    def get_is_dragged(self):
        return self._is_set

    def set_is_dragged(self, is_set) -> None:
        self._is_set = is_set

