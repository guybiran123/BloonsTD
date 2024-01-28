from point import Point


class Tower:
    """
    A class that represents a tower in the game.
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
        game_map
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

    def get_position(self) -> Point:
        return self.__position

    def set_position(self, position: Point) -> None:
        self.__position = position

    def get_direction(self) -> float:
        return self.__direction

    def set_direction(self, direction: float) -> None:
        self.__direction = direction
