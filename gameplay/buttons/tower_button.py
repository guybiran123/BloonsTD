from gameplay.buttons.button import Button
from utils.drawable import Drawable
from utils.direction import Direction
from utils.constants import *


class TowerButton(Button):

    def __init__(self, position: Point, image: str, name: ButtonName):
        super().__init__(position, image, name)
        self.__price = TOWER_BUTTON_NAME_TO_PRICE[name]
        self.__affordable = True

    def is_affordable(self, money: int, map_level: Maps):
        if self.__affordable and self.__price > money:
            self.change_image(TOWERS_BUTTONS_NAME_TO_UNAFFORDABLE_IMAGE[self._name])
            self.__affordable = False
        elif not self.__affordable and money >= self.__price:
            self.change_image(BUTTON_TO_IMAGE[self._name])
            self.__affordable = True

    def get_affordable(self):
        return self.__affordable
