import pygame
from utils.text_box import TextBox
from gameplay.buttons.button import Button
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
        self._next_screen_state = State.GAME_ENDED
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
        self.__did_win = True
        self.add_text_boxes()
        self._background = pygame.image.load(MAP_TO_IMAGE[map_level])
        self.__shop_background = pygame.image.load(SHOP_BACKGROUND_IMAGE)
        self.__money_image = pygame.image.load(MONEY_IMAGE)
        self.__money_image.set_colorkey(COLOR_KEY)
        self.__lives_image = pygame.image.load(LIVES_IMAGE)
        self.__lives_image.set_colorkey(COLOR_KEY)
        self.__sell_button = None
        self.create_sell_button()

    def draw(self):
        self._screen.blit(self._background, (0, 0))
        self.draw_range_circle()
        self.__game_map.draw_drawables()
        self.draw_shop_backgrounds()
        self._buttons.draw(self._screen)
        self.draw_text_boxes()

    def activate(self):
        self.__game_map.activate_drawables()
        if self.__is_tower_dragged:
            if self._screen.get_rect().collidepoint(pygame.mouse.get_pos()):
                self.__dragged_tower.set_position(Point(pygame.mouse.get_pos()))
        if self.__game.get_game_mode() != GameMode.SANDBOX:
            self.handle_text_changes()
            self.handle_button_changes()
            self.handle_round()

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.__is_tower_dragged:
                self.place_tower(mouse_pos)
                self.handle_tower_button_clicks()
            else:
                if self.__sell_button in self._buttons.sprites():
                    self.handle_sell_button_click()
                    self._buttons.remove(self.__sell_button)
                self.__is_tower_pressed = False
                self.__pressed_tower = None
                self.handle_towers_clicks()
                self.handle_button_clicks()
        elif event.type == pygame.KEYDOWN and self.__game.get_game_mode() == GameMode.SANDBOX:
            if event.key in self.__key_to_function:
                self.__key_to_function[event.key]()

    def handle_sell_button_click(self):
        if self.__sell_button.is_clicked(pygame.mouse.get_pos()):
            self.sell_tower()

    def handle_tower_button_clicks(self):
        for button in self._buttons.sprites()[:END_OF_TOWERS_BUTTONS]:
            if button.is_clicked(pygame.mouse.get_pos()):
                if button.get_name() in self._button_name_to_function:
                    self._button_name_to_function[button.get_name()]()
                    button.reset()
                else:
                    print("No function found for button " + button.get_name())

    def handle_text_changes(self):
        self._text_boxes[MONEY_TEXT_BOX].set_text(self.__game.get_text_money() + '$')
        self._text_boxes[LIVES_TEXT_BOX].set_text(self.__game.get_text_lives())
        self._text_boxes[ROUND_TEXT_BOX].set_text(str(self.__game.get_current_round()))

    def handle_button_changes(self):
        for button in self._buttons.sprites()[:END_OF_TOWERS_BUTTONS]:
            button.is_affordable(self.__game.get_money(), self.__game.get_map_level())

    def handle_round(self):
        balloon_to_launch = self.__game.get_balloon_to_launch()
        if balloon_to_launch != BalloonColor.NO_BALLOON:
            self.__game_map.add_balloon(Balloon(balloon_to_launch, self.__game_map))
        is_game_over = self.__game.is_game_over(self.__game_map.get_balloons().sprites() == [])
        if is_game_over != Ending.NOT_OVER:
            self._change_screen_state = True
            self.__did_win = (is_game_over == Ending.WIN)

    def draw_range_circle(self):
        if self.__is_tower_pressed:
            self.draw_circle(self.__pressed_tower.get_position().get_tuple(),
                             self.__pressed_tower.get_range_radius(),
                             True)
        elif self.__is_tower_dragged:
            placeable = self.can_place_tower(pygame.mouse.get_pos())
            self.draw_circle(self.__dragged_tower.get_position().get_tuple(),
                             self.__dragged_tower.get_range_radius(),
                             placeable)

    def draw_circle(self, position: tuple, radius: int, placeable: bool):
        transparency = 128
        if placeable:
            circle_color = (128, 128, 128, transparency)
        else:
            circle_color = (255, 0, 0, transparency)
        surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(surface, circle_color, position, radius)
        self._screen.blit(surface, (0, 0))

    def draw_shop_backgrounds(self):
        self._screen.blit(self.__shop_background, SHOP_BACKGROUND_POSITION)
        self._screen.blit(self.__money_image, MONEY_POSITION)
        self._screen.blit(self.__lives_image, LIVES_POSITION)

    def place_tower(self, mouse_pos: tuple):
        if self.can_place_tower(mouse_pos):
            self.__dragged_tower.set_is_set(True)
            self.__is_tower_dragged = False
            self.__dragged_tower = None

    def any_tower_touched(self, mouse_pos: tuple):
        for tower in self.__game_map.get_towers().sprites():
            if tower.is_clicked(mouse_pos) and tower is not self.__dragged_tower:
                return True
        return False

    def can_place_tower(self, mouse_pos: tuple):
        if not self.any_tower_touched(mouse_pos):
            if self._background.get_rect().collidepoint(mouse_pos):
                if isinstance(self.__dragged_tower, Boat):
                    if self.__game.get_encoded_map_list()[mouse_pos[Y]][mouse_pos[X]] == WATER:
                        return True
                else:
                    if self.__game.get_encoded_map_list()[mouse_pos[Y]][mouse_pos[X]] == PLACEABLE:
                        return True
        return False

    def handle_towers_clicks(self):
        for tower in self.__game_map.get_towers().sprites():
            if tower.is_clicked(pygame.mouse.get_pos()):
                self.__is_tower_pressed = True
                self.__pressed_tower = tower
                self._buttons.add(self.__sell_button)

    def add_text_boxes(self):
        self._text_boxes.append(TextBox(860, 21, 30, WHITE,
                                        (self.__game.get_text_money()
                                         + ('' if self.__game.get_game_mode() == GameMode.SANDBOX else '$'))))
        self._text_boxes.append(TextBox(860, 58, 30, WHITE, self.__game.get_text_lives()))
        self._text_boxes.append(TextBox(816, 134, 15, WHITE, (str(DART_MONKEY_COST) + '$')))
        self._text_boxes.append(TextBox(886, 134, 15, WHITE, (str(TACK_TOWER_COST) + '$')))
        self._text_boxes.append(TextBox(816, 199, 15, WHITE, (str(BOMB_TOWER_COST) + '$')))
        self._text_boxes.append(TextBox(886, 199, 15, WHITE, (str(ICE_TOWER_COST) + '$')))
        self._text_boxes.append(TextBox(816, 264, 15, WHITE, (str(SUPER_MONKEY_COST) + '$')))
        self._text_boxes.append(TextBox(886, 264, 15, WHITE, (str(BOAT_COST) + '$')))
        if self.__game.get_game_mode() != GameMode.SANDBOX:
            self._text_boxes.append(TextBox(710, 28, 34, WHITE, "Round: "))
            self._text_boxes.append(TextBox(760, 28, 34, WHITE, str(self.__game.get_current_round())))

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
            ButtonName.BUY_SECOND_UPGRADE: self.buy_second_upgrade,
            ButtonName.SELL_TOWER_BUTTON: self.sell_tower
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

    def return_tower_to_shop(self):
        price = 0
        if isinstance(self.__dragged_tower, DartMonkey):
            price = DART_MONKEY_COST
        elif isinstance(self.__dragged_tower, TackTower):
            price = TACK_TOWER_COST
        elif isinstance(self.__dragged_tower, BombTower):
            price = BOMB_TOWER_COST
        elif isinstance(self.__dragged_tower, IceTower):
            price = ICE_TOWER_COST
        elif isinstance(self.__dragged_tower, SuperMonkey):
            price = SUPER_MONKEY_COST
        elif isinstance(self.__dragged_tower, Boat):
            price = BOAT_COST
        self.__game_map.remove_tower(self.__dragged_tower)
        self.__dragged_tower = None
        self.__is_tower_dragged = False
        self.__game.add_money(price)

    def buy_dart_monkey(self):
        if self.__is_tower_dragged:
            self.return_tower_to_shop()
        elif self.__game.can_afford(DART_MONKEY_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = DartMonkey(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game_map.add_tower(self.__dragged_tower)
            self.__game.add_money(-DART_MONKEY_COST)

    def buy_tack_tower(self):
        if self.__is_tower_dragged:
            self.return_tower_to_shop()
        elif self.__game.can_afford(TACK_TOWER_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = TackTower(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game_map.add_tower(self.__dragged_tower)
            self.__game.add_money(-TACK_TOWER_COST)

    def buy_bomb_tower(self):
        if self.__is_tower_dragged:
            self.return_tower_to_shop()
        elif self.__game.can_afford(BOMB_TOWER_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = BombTower(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game_map.add_tower(self.__dragged_tower)
            self.__game.add_money(-BOMB_TOWER_COST)

    def buy_ice_tower(self):
        if self.__is_tower_dragged:
            self.return_tower_to_shop()
        elif self.__game.can_afford(ICE_TOWER_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = IceTower(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game_map.add_tower(self.__dragged_tower)
            self.__game.add_money(-ICE_TOWER_COST)

    def buy_super_monkey(self):
        if self.__is_tower_dragged:
            self.return_tower_to_shop()
        elif self.__game.can_afford(SUPER_MONKEY_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = SuperMonkey(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game_map.add_tower(self.__dragged_tower)
            self.__game.add_money(-SUPER_MONKEY_COST)

    def buy_boat(self):
        if self.__is_tower_dragged:
            self.return_tower_to_shop()
        elif self.__game.can_afford(BOAT_COST):
            self.__is_tower_dragged = True
            self.__dragged_tower = Boat(Point(pygame.mouse.get_pos()), self.__game_map)
            self.__game_map.add_tower(self.__dragged_tower)
            self.__game.add_money(-BOAT_COST)

    def start_round(self):
        self.__game.start_round()

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

    def sell_tower(self):
        price = 0
        if isinstance(self.__pressed_tower, DartMonkey):
            price = DART_MONKEY_SELL_COST
        elif isinstance(self.__pressed_tower, TackTower):
            price = TACK_TOWER_SELL_COST
        elif isinstance(self.__pressed_tower, BombTower):
            price = BOMB_TOWER_SELL_COST
        elif isinstance(self.__pressed_tower, IceTower):
            price = ICE_TOWER_SELL_COST
        elif isinstance(self.__pressed_tower, SuperMonkey):
            price = SUPER_MONKEY_SELL_COST
        elif isinstance(self.__pressed_tower, Boat):
            price = BOAT_SELL_COST
        self.__game_map.remove_tower(self.__pressed_tower)
        self.__pressed_tower = None
        self.__is_tower_pressed = False
        self.__game.add_money(price)

    def get_did_win(self):
        return self.__did_win

    def create_sell_button(self):
        Yposition = 410 if self.__game.get_game_mode() == GameMode.SANDBOX else 340
        self.__sell_button = Button(Point((851, Yposition),),
                                    BUTTON_TO_IMAGE[ButtonName.SELL_TOWER_BUTTON],
                                    ButtonName.SELL_TOWER_BUTTON)

