import pygame
from gameplay.towers.tower import Tower
from utils.point import Point
from gameplay.game_map import GameMap
from utils.constants import *


class IceTower(Tower):

    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position,
                         ICE_TOWER_IMAGE,
                         ICE_TOWER_COST,
                         ICE_TOWER_SELL_COST,
                         ICE_TOWER_SHOT_SPEED,
                         ICE_TOWER_SHOT_DAMAGE,
                         ICE_TOWER_FREEZING_SPEED,
                         ICE_TOWER_RANGE_RADIUS,
                         game_map
                         )
        self.__freezing_duration = ICE_TOWER_FREEZING_DURATION

    def activate(self):
        if self._is_set:
            current_time = pygame.time.get_ticks()
            self.add_to_balloons_in_range()
            if self._balloons_in_range and current_time - self._last_shot_time > self._shooting_speed:
                self.freeze_balloons()

    def freeze_balloons(self):
        self._last_shot_time = pygame.time.get_ticks()
        for balloon in self._balloons_in_range:
            balloon.freeze(self.__freezing_duration)
