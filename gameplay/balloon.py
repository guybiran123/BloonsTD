import pygame
from utils.drawable import Drawable
from utils.direction import Direction
from utils.point import Point
from gameplay.effects.Popped_balloon import PoppedBalloon
from utils.constants import *
from gameplay.game_map import GameMap


class Balloon(Drawable):

    def __init__(self, hp: int, game_map: GameMap):
        route_positions = game_map.get_route_positions()
        super().__init__(Point(route_positions[0][X], route_positions[0][Y]),
                         Direction(False, INITIAL_ANGLE),
                         BALLOON_HP_TO_IMAGE[hp])
        self.__hp = hp
        self.__speed = BALLOON_HP_TO_SPEED[self.__hp]
        self.__route_progress = 0
        self.__last_moving_time = 0
        self.__is_frozen = False
        self.__freezing_time = 0
        self.__freezing_duration = 0
        self.__game_map = game_map

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp: int):
        self.__hp = hp

    def get_route_progress(self):
        return self.__route_progress

    def hit(self, damage: int):
        self.__game_map.add_money(min(damage, self.__hp))
        self.__hp -= damage
        if self.__hp > 0:
            self.change_image(BALLOON_HP_TO_IMAGE[self.__hp])
        else:
            self.explode()

    def explode(self):
        self.__game_map.add_effect(PoppedBalloon(self._position, self.__game_map))
        self.__game_map.balloon_exploded(self)

    def activate(self):
        current_time = pygame.time.get_ticks()
        self.check_to_unfreeze()
        if current_time - self.__last_moving_time > COOLDOWN_TIME:
            self.move()

    def move(self):
        self.__last_moving_time = pygame.time.get_ticks()
        route_positions = self.__game_map.get_route_positions()
        self.__route_progress += self.__speed
        if self.__route_progress >= len(route_positions):
            self.finish_route()
        else:
            self.set_position(Point(route_positions[self.__route_progress][X], route_positions[self.__route_progress][Y]))

    def finish_route(self):
        self.__game_map.balloon_finished(self)

    def freeze(self, freezing_duration: int):
        if self.__hp != 6:
            self.__is_frozen = True
            self.__freezing_time = pygame.time.get_ticks()
            self.__freezing_duration = freezing_duration
            self.change_image(BALLOON_HP_TO_FROZEN_IMAGE[self.__hp])
            self.__speed = 1

    def unfreeze(self):
        self.__is_frozen = False
        self.change_image(BALLOON_HP_TO_IMAGE[self.__hp])
        self.__speed = BALLOON_HP_TO_SPEED[self.__hp]

    def check_to_unfreeze(self):
        current_time = pygame.time.get_ticks()
        if self.__is_frozen:
            if current_time - self.__freezing_time > self.__freezing_duration:
                self.unfreeze()
