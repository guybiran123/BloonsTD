from utils.drawable import Drawable
from utils.direction import Direction
from utils.constants import *


class Button(Drawable):

    def __init__(self, position: Point, image: str, name: ButtonName):
        super().__init__(position, Direction(False, 0), image)
        self._name = name
        self._clicked = False

    def is_clicked(self, mouse_position: tuple):
        if self.rect.collidepoint(mouse_position):
            self._clicked = True
            return True
        self._clicked = False
        return False

    def reset(self):
        self._clicked = False

    def get_name(self):
        return self._name

