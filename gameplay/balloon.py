from utils.drawable import Drawable
from utils.direction import Direction
from utils.point import Point
from utils.constants import *
from game_map import GameMap


class Balloon(Drawable):

    def __init__(self, position: Point, hp: int, game_map: GameMap):
        super().__init__(position, Direction(False, INITIAL_ANGLE), BALLOON_HP_TO_IMAGE[hp])
        self.__hp = hp
        self.__speed = BALLOON_HP_TO_SPEED[self.__hp]
        self.__route_progress = 0
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
            self._image = BALLOON_HP_TO_IMAGE[self.__hp]
        else:
            self.explode()

    def explode(self):
        self.__game_map.balloon_exploded(self)
