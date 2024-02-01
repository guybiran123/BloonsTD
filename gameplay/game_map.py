import pygame
from gameplay.balloon import Balloon
from gameplay.game import Game
from towers.tower import Tower
from shots.shot import Shot

class GameMap:
    def __init__(self, game: Game, screen: pygame.surface.Surface):
        self.__balloons = pygame.sprite.Group()
        self.__towers = pygame.sprite.Group()
        self.__shots = pygame.sprite.Group()
        self.__game = game
        self.__screen = screen

    def get_balloons(self):
        return self.__balloons

    def add_balloon(self, balloon):
        self.__balloons.add(balloon)

    def get_towers(self):
        return self.__towers

    def add_tower(self, tower):
        self.__towers.add(tower)

    def get_shots(self):
        return self.__shots

    def add_shot(self, shot):
        self.__shots.add(shot)

    def get_game(self):
        return self.__game

    def add_money(self, value: int):
        self.__game.add_money(value)

    def balloon_exploded(self, balloon):
        self.__balloons.remove(balloon)

    def remove_shot(self, shot):
        self.__shots.remove(shot)
