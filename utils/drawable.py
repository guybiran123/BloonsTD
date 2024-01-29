from point import Point
from direction import Direction


class Drawable:
    def __init__(self, position: Point, direction: Direction, image: str):
        self.__position = position
        self.__direction = direction
        self.__image = image

    def get_position(self):
        return self.__position

    def set_position(self, position: Point):
        self.__position = position

    def set_x(self, x: int):
        self.__position.set_x(x)

    def set_y(self, y: int):
        self.__position.set_y(y)

    def add_to_x(self, value: int):
        self.__position.set_x(self.__position.get_x() + value)

    def add_to_y(self, value: int):
        self.__position.set_y(self.__position.get_y() + value)

    def increase_x(self):
        self.add_to_x(1)

    def increase_y(self):
        self.add_to_y(1)

    def decrease_x(self):
        self.add_to_x(-1)

    def decrease_y(self):
        self.add_to_y(-1)

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction: Direction):
        self.__direction = direction

    def get_direction_value(self):
        return self.__direction.value

    def set_direction_value(self, value):
        self.__direction.value = value

    def get_does_direction_matter(self):
        return self.__direction.does_matter

    def set_does_direction_matter(self, does_matter: bool):
        self.__direction.does_matter = does_matter









