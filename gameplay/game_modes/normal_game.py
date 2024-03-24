from gameplay.game_modes.game import Game
from utils.constants import *


class NormalGame(Game):

    def __init__(self, map_level: Maps):
        super().__init__(map_level, GameMode.NORMAL)
        self.__rounds_amount = 20
        self.__money = 500
        self.__lives = 40

    def add_money(self, value: int):
        self.__money += value

    def lose_lives(self, value):
        self.__lives -= value

    def can_afford(self, price: int):
        return self.__money >= price

    def get_text_money(self):
        return str(self.__money)

    def get_text_lives(self):
        return str(self.__lives)

    def get_money(self):
        return self.__money

    def get_lives(self):
        return self.__lives
