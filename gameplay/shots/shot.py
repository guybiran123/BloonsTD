from utils.drawable import Drawable
from utils.point import Point
from utils.direction import Direction
from gameplay.game_map import GameMap


class Shot(Drawable):

    def __init__(
            self,
            position: Point,
            direction: Direction,
            image: str,
            shot_range: int,
            damage: int,
            speed: int,
            game_map: GameMap
    ):
        super().__init__(position, direction, image)
        self._shot_range = shot_range
        self._damage = damage
        self._speed = speed
        self._game_map = game_map
