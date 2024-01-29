from balloon import Balloon
from game import Game


class GameMap:
    def __init__(self, game: Game):
        self.__balloons = []
        self.__towers = []
        self.__shots = []
        self.__game = game

    def get_game(self):
        return self.__game

    def add_money(self, value: int):
        self.__game.add_money(value)

    def balloon_exploded(self, balloon: Balloon):
        self.__balloons.remove(balloon)
