import pygame
from utils.point import Point
from utils.direction import Direction
from utils.constants import *


class Drawable(pygame.sprite.Sprite):
    def __init__(self, position: Point, direction: Direction, image: str):
        super().__init__()
        self._position = position
        self._direction = direction
        self._original_image = pygame.image.load(image).convert()
        self._original_image.set_colorkey(COLOR_KEY)
        self.image = self._original_image.copy()
        self.rect = self.image.get_rect()
        self.original_center = self.rect.center
        self.rotate_image()
        self.align_rect_to_pos()

    def align_rect_to_pos(self):
        self.rect.center = self._position.get_x(), self._position.get_y()
        rotated_rect = self.image.get_rect()
        offset = (self.original_center[0] - rotated_rect.centerx,
                  self.original_center[1] - rotated_rect.centery)
        self.rect.x += offset[0]
        self.rect.y += offset[1]

    def rotate_image(self):
        if self._direction.does_matter:
            self.image = pygame.transform.rotate(self._original_image, self._direction.value)
            rotated_rect = self.image.get_rect()
            offset = (self.original_center[0] - rotated_rect.centerx,
                      self.original_center[1] - rotated_rect.centery)
            self.rect.x += offset[0]
            self.rect.y += offset[1]
            self.align_rect_to_pos()

    def change_image(self, image: str):
        self._original_image = pygame.image.load(image).convert()
        self._original_image.set_colorkey(COLOR_KEY)
        self.image = self._original_image.copy()

    def get_position(self):
        return self._position

    def set_position(self, position: Point):
        self._position = position
        self.align_rect_to_pos()

    def set_x(self, x: int):
        self._position.set_x(x)
        self.align_rect_to_pos()

    def set_y(self, y: int):
        self._position.set_y(y)
        self.align_rect_to_pos()

    def add_to_x(self, value: int):
        self._position.set_x(self._position.get_x() + value)
        self.align_rect_to_pos()

    def add_to_y(self, value: int):
        self._position.set_y(self._position.get_y() + value)
        self.align_rect_to_pos()

    def increase_x(self):
        self.add_to_x(1)
        self.align_rect_to_pos()

    def increase_y(self):
        self.add_to_y(1)
        self.align_rect_to_pos()

    def decrease_x(self):
        self.add_to_x(-1)
        self.align_rect_to_pos()

    def decrease_y(self):
        self.add_to_y(-1)
        self.align_rect_to_pos()

    def get_direction(self):
        return self._direction

    def set_direction(self, direction: Direction):
        self._direction = direction
        self.rotate_image()

    def get_direction_value(self):
        return self._direction.value

    def set_direction_value(self, value):
        self._direction.value = value
        self.rotate_image()

    def get_does_direction_matter(self):
        return self._direction.does_matter

    def set_does_direction_matter(self, does_matter: bool):
        self._direction.does_matter = does_matter
