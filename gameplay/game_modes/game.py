from utils.constants import *


class Game:

    def __init__(self, map_level: Maps, game_mode: GameMode):
        self.__map_level = map_level
        self.__encoded_map_list = []
        self.make_encoded_map_list()
        self._game_mode = game_mode

    def get_map_level(self):
        return self.__map_level

    def get_encoded_map_list(self):
        return self.__encoded_map_list

    def make_encoded_map_list(self):
        try:
            with open(MAP_TO_ENCODED_MAP[self.__map_level], 'r') as file:
                content = file.read()
        except Exception as e:
            print("Something went wrong", e)
        self.__encoded_map_list = [line.split() for line in content.split('\n')]

    def add_money(self, value):
        pass

    def lose_lives(self, value):
        pass

    def get_game_mode(self):
        return self._game_mode

    def can_afford(self, price: int):
        return True

    def get_text_money(self):
        pass

    def get_text_lives(self):
        pass
