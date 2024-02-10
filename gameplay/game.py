from utils.constants import *


class Game:

    def __init__(self, map_level: Maps, rounds_amount: int):
        self.__map_level = map_level
        self.__encoded_map_list = []
        self.make_encoded_map_list()
        self.__rounds_amount = rounds_amount
        self.__money = 0
        self.__lives = 40

    def get_map_level(self):
        return self.__map_level

    def get_encoded_map_list(self):
        return self.__encoded_map_list

    def add_money(self, value):
        self.__money += value

    def make_encoded_map_list(self):
        try:
            with open(MAP_TO_ENCODED_MAP[self.__map_level], 'r') as file:
                content = file.read()
        except Exception as e:
            print("Something went wrong", e)
        self.__encoded_map_list = [line.split() for line in content.split('\n')]
