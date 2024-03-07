from gameplay.towers.tower import Tower
from utils.point import Point
from gameplay.game_map import GameMap
from utils.constants import *


class SuperMonkey(Tower):

    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position,
                         SUPER_MONKEY_IMAGE,
                         SUPER_MONKEY_COST,
                         SUPER_MONKEY_SELL_COST,
                         SUPER_MONKEY_SHOT_SPEED,
                         SUPER_MONKEY_SHOT_DAMAGE,
                         SUPER_MONKEY_SHOOTING_SPEED,
                         SUPER_MONKEY_RANGE_RADIUS,
                         game_map)
