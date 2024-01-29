from utils.constants import *

class Game:

    def __init__(self, map_level: Maps, rounds_amount: int):
        self.__map_level = map_level
        self.__rounds_amount = rounds_amount
        self.__money = 0
        self.__lives = 40

    def add_money(self, value):
        self.__money += value
