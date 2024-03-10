from gameplay.effects.effect import Effect
from utils.point import Point
from gameplay.game_map import GameMap
from utils.constants import *


class PoppedBalloon(Effect):

    def __init__(self, position: Point, game_map: GameMap):
        super().__init__(position, POPPED_BALLOON_DURATION, POPPED_BALLOON_IMAGE, game_map)
