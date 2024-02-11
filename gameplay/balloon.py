import pygame
from utils.drawable import Drawable
from utils.direction import Direction
from utils.point import Point
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
            self.image = BALLOON_HP_TO_IMAGE[self.__hp]
        else:
            self.explode()

    def explode(self):
        self.__game_map.balloon_exploded(self)

    def activate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_moving_time > COOLDOWN_TIME:
            self.move()

    def move(self):
        route_positions = self.__game_map.get_route_positions()
        self.__route_progress += self.__speed
        if self.__route_progress >= len(route_positions):
            self.finish_route()
        else:
            self.set_position(Point(route_positions[self.__route_progress][X], route_positions[self.__route_progress][Y]))

    def finish_route(self):
        self.__game_map.balloon_finished(self)
