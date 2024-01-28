from point import Point


class Drawable:
    def __init__(self, position: Point, direction: float, image: str):
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

    def set_direction(self, direction):
        self.__direction = direction
