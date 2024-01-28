from point import Point

class Tower:
    def __init__(self, position: Point, direction, cost, sell_cost, shooting_speed, shooting_damage, range_radius, is_pressed, is_dragged, game_map):
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
