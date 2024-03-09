import pygame
from utils.point import Point
from gameplay.game_map import GameMap
from gameplay.effects.effect import Effect
from utils.constants import *


class Explosion(Effect):

    def __init__(self, position: Point, damage: int, game_map: GameMap):
        super().__init__(position, EXPLOSION_DURATION, EXPLOSION_IMAGE, game_map)
        self.__damage = damage
        self.damage_balloons()

    def damage_balloons(self):
        hit_balloons = pygame.sprite.spritecollide(self, self._game_map.get_balloons(), False)
        for balloon in hit_balloons:
            balloon.hit(self.__damage)

