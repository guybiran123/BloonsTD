from gameplay.shots.shot import Shot
from utils.point import Point
from utils.direction import Direction
from gameplay.game_map import GameMap


class Dart(Shot):

    def __init__(self, position: Point, direction: float, destination: Point, shot_range: int, damage: int, speed: int, game_map: GameMap):
        super().__init__(
            position,
            Direction(True, direction),
            destination,
            r'images/Shots/dart_image.png',
            shot_range,
            damage,
            speed,
            game_map)


