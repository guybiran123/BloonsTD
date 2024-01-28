from utils.point import Point
from gameplay.game_map import GameMap


class Tower:
    """
    A father class that represents a tower in the game.
    """
    def __init__(
        self,
        position: Point,
        direction: float,
        cost: int,
        sell_cost: int,
        shooting_speed: float,
        shooting_damage: int,
        range_radius: int,
        is_pressed: bool,
        is_dragged: bool,
        game_map: GameMap
    ):
        self.__position = position
        self.__direction = direction
        self.__cost = cost
        self.__sell_cost = sell_cost
        self.__shooting_speed = shooting_speed
        self.__shooting_damage = shooting_damage
        self.__range_radius = range_radius
        self.__is_pressed = is_pressed
        self.__is_dragged = is_dragged
        self.__game_map = game_map

    def get_cost(self) -> int:
        return self.__cost

    def get_sell_cost(self) -> int:
        return self.__sell_cost

    def get_shooting_speed(self):
        return self.__shooting_speed

    def get_shooting_damage(self):
        return self.__shooting_damage

    def get_range_radius(self):
        return self.__range_radius

    def get_is_pressed(self):
        return self.__is_pressed

    def set_is_pressed(self, is_pressed: bool) -> None:
        self.__is_pressed = is_pressed

    def get_is_dragged(self):
        return self.__is_dragged

    def set_is_dragged(self, is_dragged) -> None:
        self.__is_dragged = is_dragged

