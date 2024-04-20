import pygame
from gameplay.game_modes.game import Game
from gameplay.round import Round
from gameplay.game_map import GameMap
from utils.constants import *


class NormalGame(Game):

    def __init__(self, map_level: Maps):
        super().__init__(map_level, GameMode.NORMAL)
        self.__rounds_amount = 30
        self.__money = 500
        self.__lives = 40
        self.__in_round = False
        self.__current_round = 1
        self.__round = None
        self.__last_balloon_time = pygame.time.get_ticks()

    def get_balloon_to_launch(self):
        if not self.__in_round:
            return BalloonColor.NO_BALLOON
        if self.__current_round > self.__rounds_amount:
            return BalloonColor.NO_BALLOON
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_balloon_time > self.__round.get_cooldown():
            balloon_to_return = self.__round.get_balloon()
            if self.__round.round_over():
                self.__round = None
                self.__in_round = False
                self.__current_round += 1
                self.__money += 200
            self.__last_balloon_time = current_time
            return balloon_to_return
        return BalloonColor.NO_BALLOON

    def is_game_over(self, all_balloons_popped: bool):
        if self.__current_round > self.__rounds_amount and all_balloons_popped:
            return Ending.WIN
        if self.__lives <= 0:
            return Ending.LOSE
        return Ending.NOT_OVER

    def start_round(self):
        if not self.__in_round:
            self.__in_round = True
            self.__round = Round(self.__current_round)

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

    def get_current_round(self):
        return self.__current_round
