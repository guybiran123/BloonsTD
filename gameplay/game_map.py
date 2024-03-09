import pygame
from gameplay.game import Game
from utils.constants import *


class GameMap:
    def __init__(self, game: Game, screen: pygame.surface.Surface):
        self.__balloons = pygame.sprite.Group()
        self.__towers = pygame.sprite.Group()
        self.__shots = pygame.sprite.Group()
        self.__effects = pygame.sprite.Group()
        self.__game = game
        self.__route_positions = []
        self.make_route_positions()
        self.__screen = screen
        self.__roads_collisions_counter = 0

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

    def is_roads_collision_near(self, current_position, encoded_map_list):
        if encoded_map_list[current_position[Y]][current_position[X]] == ROUTE:
            for neigh in BLOCKS_SURROUNDINGS:
                if encoded_map_list[current_position[Y] + neigh[Y]][current_position[X] + neigh[X]] == ROADS_COLLISIONS:
                    return current_position[X] + neigh[X], current_position[Y] + neigh[Y]
        return NOT_FOUND

    def get_next_route_position(self, current_position, encoded_map_list):
        if encoded_map_list[current_position[Y]][current_position[X]] == ROUTE_START:
            for neigh in BLOCKS_SURROUNDINGS:
                if 0 <= current_position[Y] + neigh[Y] < len(encoded_map_list) and \
                        0 <= current_position[X] + neigh[X] < len(encoded_map_list[0]):
                    if encoded_map_list[current_position[Y] + neigh[Y]][current_position[X] + neigh[X]] == ROUTE:
                        return current_position[X] + neigh[X], current_position[Y] + neigh[Y]

        elif encoded_map_list[current_position[Y]][current_position[X]] == ROUTE:
            for neigh in BLOCKS_SURROUNDINGS:
                if encoded_map_list[current_position[Y] + neigh[Y]][current_position[X] + neigh[X]]\
                        in [ROUTE, ROUTE_END] and (current_position[X] + neigh[X], current_position[Y] + neigh[Y])\
                        != self.__route_positions[len(self.__route_positions) - 2]:
                    return current_position[X] + neigh[X], current_position[Y] + neigh[Y]

        elif encoded_map_list[current_position[Y]][current_position[X]] == ROADS_COLLISIONS:
            for neigh in BLOCKS_SURROUNDINGS:
                if encoded_map_list[current_position[Y] + neigh[Y]][current_position[X] + neigh[X]]\
                        == 10 + self.__roads_collisions_counter:
                    self.__roads_collisions_counter += 1
                    return current_position[X] + neigh[X], current_position[Y] + neigh[Y]

    def make_route_positions(self):
        self.add_route_starting_point_to_list()
        current_position = self.__route_positions[len(self.__route_positions) - 1]
        encoded_map_list = self.__game.get_encoded_map_list()
        while encoded_map_list[current_position[Y]][current_position[X]] != ROUTE_END:
            if MAP_HAS_ROADS_COLLISIONS[self.__game.get_map_level()]:
                collision_pos = self.is_roads_collision_near(current_position, encoded_map_list)
                if collision_pos != NOT_FOUND:
                    self.__route_positions.append(collision_pos)
                    continue
            self.__route_positions.append(self.get_next_route_position(current_position, encoded_map_list))
            current_position = self.__route_positions[len(self.__route_positions) - 1]

