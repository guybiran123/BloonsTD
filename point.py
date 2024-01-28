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
