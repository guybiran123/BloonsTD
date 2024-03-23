import pygame
from utils.text_box import TextBox
from gameplay.screen_states.screen_state import ScreenState
from gameplay.game_modes.normal_game import NormalGame
from gameplay.game_modes.sandbox_game import SandboxGame
from gameplay.towers.dart_monkey import DartMonkey
from gameplay.towers.tack_tower import TackTower
from gameplay.towers.bomb_tower import BombTower
from gameplay.towers.ice_tower import IceTower
from gameplay.towers.supermonkey import SuperMonkey
from gameplay.towers.boat import Boat
from gameplay.balloon import Balloon
from gameplay.game_map import GameMap
from utils.constants import *


class InGameScreen(ScreenState):

    def __init__(self, screen: pygame.surface.Surface, map_level: Maps, game_mode: GameMode):
        self.__map_level = map_level
        self.__game_mode = game_mode
        self.__buttons_names = []
        self.create_buttons_names_list()
        super().__init__(screen, self.__buttons_names)
        self.create_button_name_to_function_dict()
        self.__key_to_function = {}
        self.create_key_to_function_dict()
        self.__game = None
        self.create_game()
        self.__game_map = GameMap(self.__game, self._screen)
        self.__is_tower_dragged = False
        self.__dragged_tower = None
        self.__is_tower_pressed = False
        self.__pressed_tower = None
        self._background = pygame.image.load(MAP_TO_IMAGE[map_level])

    def draw(self):
        super().draw()


    def activate(self):
        pass

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.__is_tower_dragged:
                self.place_tower(mouse_pos)
            else:
                self.__is_tower_pressed = False
                self.__pressed_tower = None
                self.handle_towers_clicks()
                self.handle_button_clicks()
        elif event.type == pygame.KEYDOWN:
            if event.key in self.__key_to_function:
                self.__key_to_function[event.key]()

    def place_tower(self, mouse_pos: tuple):
        if not self.any_tower_pressed(mouse_pos):
            if isinstance(self.__dragged_tower, Boat):
                if self.__game.get_encoded_map_list()[mouse_pos[Y]][mouse_pos[X]] == WATER:
                    self.__dragged_tower.set_is_set(True)
            else:
                if self.__game.get_encoded_map_list()[mouse_pos[Y]][mouse_pos[X]] == PLACEABLE:
                    self.__dragged_tower.set_is_set(True)

    def any_tower_pressed(self, mouse_pos: tuple):
        for tower in self.__game_map.get_towers().sprites():
            if tower.is_clicked(mouse_pos):
                return True
        return False

    def handle_towers_clicks(self):
        for tower in self.__game_map.get_towers().sprites():
            if tower.is_clicked(pygame.mouse.get_pos()):
                self.__is_tower_pressed = True
                self.__pressed_tower = tower

    def add_text_boxes(self):
        pass

    def create_buttons_names_list(self):
        self.__buttons_names = [ButtonName.BUY_DART_MONKEY,
                                ButtonName.BUY_TACK_TOWER,
                                ButtonName.BUY_BOMB_TOWER,
                                ButtonName.BUY_ICE_TOWER,
                                ButtonName.BUY_SUPER_MONKEY,
                                ButtonName.BUY_BOAT]
        if self.__game_mode == GameMode.SANDBOX:
            self.__buttons_names += [ButtonName.LAUNCH_RED_BALLOON,
                                     ButtonName.LAUNCH_BLUE_BALLOON,
                                     ButtonName.LAUNCH_GREEN_BALLOON,
                                     ButtonName.LAUNCH_YELLOW_BALLOON,
                                     ButtonName.LAUNCH_BLACK_BALLOON,
                                     ButtonName.LAUNCH_WHITE_BALLOON]
        else:
            self.__buttons_names.append(ButtonName.START_ROUND)

    def create_button_name_to_function_dict(self):
        self._button_name_to_function = {
            ButtonName.BUY_DART_MONKEY: self.buy_dart_monkey,
            ButtonName.BUY_TACK_TOWER: self.buy_tack_tower,
            ButtonName.BUY_BOMB_TOWER: self.buy_bomb_tower,
            ButtonName.BUY_ICE_TOWER: self.buy_ice_tower,
            ButtonName.BUY_SUPER_MONKEY: self.buy_super_monkey,
            ButtonName.BUY_BOAT: self.buy_boat,
            ButtonName.START_ROUND: self.start_round,
            ButtonName.LAUNCH_RED_BALLOON: self.launch_red_balloon,
            ButtonName.LAUNCH_BLUE_BALLOON: self.launch_blue_balloon,
            ButtonName.LAUNCH_GREEN_BALLOON: self.launch_green_balloon,
            ButtonName.LAUNCH_YELLOW_BALLOON: self.launch_yellow_balloon,
            ButtonName.LAUNCH_BLACK_BALLOON: self.launch_black_balloon,
            ButtonName.LAUNCH_WHITE_BALLOON: self.launch_white_balloon,
            ButtonName.BUY_FIRST_UPGRADE: self.buy_first_upgrade,
            ButtonName.BUY_SECOND_UPGRADE: self.buy_second_upgrade
        }

    def create_key_to_function_dict(self):
        self.__key_to_function = {
            pygame.K_1: self.launch_red_balloon,
            pygame.K_2: self.launch_blue_balloon,
            pygame.K_3: self.launch_green_balloon,
            pygame.K_4: self.launch_yellow_balloon,
            pygame.K_5: self.launch_black_balloon,
            pygame.K_6: self.launch_white_balloon,
        }

    def create_game(self):
        if self.__game_mode == GameMode.NORMAL:
            self.__game = NormalGame(self.__map_level)
        elif self.__game_mode == GameMode.SANDBOX:
            self.__game = SandboxGame(self.__map_level)

    def buy_dart_monkey(self):
        if self.__game.can_afford(DART_MONKEY_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = DartMonkey(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game.add_money(-DART_MONKEY_COST)

    def buy_tack_tower(self):
        if self.__game.can_afford(TACK_TOWER_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = TackTower(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game.add_money(-TACK_TOWER_COST)

    def buy_bomb_tower(self):
        if self.__game.can_afford(BOMB_TOWER_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = BombTower(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game.add_money(-BOMB_TOWER_COST)

    def buy_ice_tower(self):
        if self.__game.can_afford(ICE_TOWER_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = IceTower(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game.add_money(-ICE_TOWER_COST)

    def buy_super_monkey(self):
        if self.__game.can_afford(SUPER_MONKEY_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = SuperMonkey(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game.add_money(-SUPER_MONKEY_COST)

    def buy_boat(self):
        if self.__game.can_afford(BOAT_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = Boat(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game.add_money(-BOAT_COST)

    def start_round(self):
        pass

    def launch_red_balloon(self):
        self.__game_map.add_balloon(Balloon(1, self.__game_map))

    def launch_blue_balloon(self):
        self.__game_map.add_balloon(Balloon(2, self.__game_map))

    def launch_green_balloon(self):
        self.__game_map.add_balloon(Balloon(3, self.__game_map))

    def launch_yellow_balloon(self):
        self.__game_map.add_balloon(Balloon(4, self.__game_map))

    def launch_black_balloon(self):
        self.__game_map.add_balloon(Balloon(5, self.__game_map))

    def launch_white_balloon(self):
        self.__game_map.add_balloon(Balloon(6, self.__game_map))

    def buy_first_upgrade(self):
        pass

    def buy_second_upgrade(self):
        pass


