import pygame
from gameplay.game import Game
from utils.constants import *


class GameMap:
    def __init__(self, game: Game, screen: pygame.surface.Surface):
        self.__balloons = pygame.sprite.Group()
        self.__towers = pygame.sprite.Group()
        self.__shots = pygame.sprite.Group()
        self.__effects = pygame.sprite.Group()
        self.__roads_collisions_counter = 0
        self.__game = game
        self.__route_positions = []
        self.make_route_positions()
        self.__screen = screen

    def get_balloons(self):
        return self.__balloons

    def add_balloon(self, balloon):
        self.__balloons.add(balloon)

    def get_towers(self):
        return self.__towers

    def add_tower(self, tower):
        self.__towers.add(tower)

    def get_shots(self):
        return self.__shots

    def add_shot(self, shot):
        self.__shots.add(shot)

    def get_effects(self):
        return self.__effects

    def add_effect(self, effect):
        self.__effects.add(effect)

    def remove_effect(self, effect):
        self.__effects.remove(effect)

    def get_game(self):
        return self.__game

    def get_route_positions(self):
        return self.__route_positions

    def add_money(self, value: int):
        self.__game.add_money(value)

    def balloon_exploded(self, balloon):
        self.__balloons.remove(balloon)

    def balloon_finished(self, balloon):
        self.__game.lose_lives(balloon.get_hp())
        self.__balloons.remove(balloon)

    def remove_shot(self, shot):
        self.__shots.remove(shot)

    def add_route_starting_point_to_list(self):
        encoded_map_list = self.__game.get_encoded_map_list()
        for row in range(len(encoded_map_list)):
            for col in range(len(encoded_map_list[row])):
                if encoded_map_list[row][col] == ROUTE_START:
                    self.__route_positions.append((col, row))
                    return

    def get_next_route_position(self, current_position):
        encoded_map_list = self.__game.get_encoded_map_list()
        current_encoded_pixel = encoded_map_list[current_position[Y]][current_position[X]]
        neighbors = self.get_neighbors(current_position)

        if current_encoded_pixel == ROUTE_START:
            for neighbor in neighbors:
                if 0 <= neighbor[Y] < len(encoded_map_list) and \
                        0 <= neighbor[X] < len(encoded_map_list[0]):
                    if self.get_encoded_pixel_from_position(neighbor) == ROUTE:
                        return neighbor

        elif current_encoded_pixel == ROUTE:
            for neighbor in neighbors:
                if (self.get_encoded_pixel_from_position(neighbor) in [ROUTE, ROUTE_END] and
                    neighbor != self.__route_positions[len(self.__route_positions) - 2]) or \
                        self.get_encoded_pixel_from_position(neighbor).isupper():
                    return neighbor

        elif current_encoded_pixel.islower():
            for neighbor in neighbors:
                if self.get_encoded_pixel_from_position(neighbor) == ROUTE:
                    return neighbor

        elif current_encoded_pixel == ROADS_COLLISIONS:
            for neighbor in neighbors:
                if self.get_encoded_pixel_from_position(neighbor) ==\
                        self.get_encoded_pixel_from_position(
                            self.__route_positions[len(self.__route_positions) - 2]
                        ).lower():
                    return neighbor

        elif current_encoded_pixel.isupper():
            for neighbor in neighbors:
                if self.get_encoded_pixel_from_position(neighbor) == ROADS_COLLISIONS:
                    return neighbor

    def make_route_positions(self):
        self.add_route_starting_point_to_list()
        current_position = self.__route_positions[len(self.__route_positions) - 1]
        while self.get_encoded_pixel_from_position(current_position) != ROUTE_END:
            self.__route_positions.append(self.get_next_route_position(current_position))
            current_position = self.__route_positions[len(self.__route_positions) - 1]

    def get_encoded_pixel_from_position(self, position: tuple):
        return self.__game.get_encoded_map_list()[position[Y]][position[X]]

    def get_neighbors(self, position: tuple):
        return [
            (position[X] + neighbor[X], position[Y] + neighbor[Y])
            for neighbor in BLOCKS_SURROUNDINGS
        ]
