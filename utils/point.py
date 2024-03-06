import math


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_point(self):
        return self.__x, self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_point(self, x, y):
        self.__x = x
        self.__y = y

    def get_distance(self, point):
        return math.sqrt(((self.__x - point.__x) ** 2) + ((self.__y - point.__y) ** 2))

    def calc_angle_to_point(self, point):
        x1, y1 = self.__x, self.__y
        x2, y2 = point.__x, point.__y

        dx = x2 - x1
        dy = y2 - y1

        # Use atan2 to calculate the angle
        angle_rad = math.atan2(dy, dx)

        # Convert the angle to degrees
        angle_deg = math.degrees(angle_rad)
        # Ensure the angle is positive
        if angle_deg < 0:
            angle_deg += 360

        return -angle_deg - 90

    def find_point_with_distance_and_angle(self, angle: float, distance: int):    # function doesn't work
        angle = -angle - 90
        new_x = self.__x + math.cos(angle) * distance
        new_y = self.__y + math.sin(angle) * distance
        return Point(new_x, new_y)
