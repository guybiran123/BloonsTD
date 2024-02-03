from utils.constants import *


class Game:

    def __init__(self, map_level: Maps, rounds_amount: int):
        self.__map_level = map_level
        self.__encoded_map = self.make_encoded_map_list()
        self.__rounds_amount = rounds_amount
        self.__money = 0
        self.__lives = 40

    def add_money(self, value):
        self.__money += value

    def make_encoded_map_list(self):
        try:
            with open('r', MAP_TO_ENCODED_MAP[self.__map_level]) as file:
                content = file.read()
        except Exception as e:
            print("Something went wrong")
        # function not finished
