from gameplay.towers.tower import Tower
from utils.point import Point
from gameplay.game_map import GameMap
from utils.constants import *

class DartMonkey(Tower):

    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position,
                         DART_MONKEY_IMAGE,
                         DART_MONKEY_COST,
                         DART_MONKEY_SELL_COST,
                         DART_MONKEY_SHOT_SPEED,
                         DART_MONKEY_SHOT_DAMAGE,
                         DART_MONKEY_SHOOTING_SPEED,
                         DART_MONKEY_RANGE_RADIUS,
                         game_map)
