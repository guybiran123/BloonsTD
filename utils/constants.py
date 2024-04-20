from enum import Enum
from utils.point import Point

# -----General_magic_numbers-------

COLOR_KEY = (20, 250, 250)
WHITE = (255, 255, 255)

X = 0
Y = 1
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 926
REFRESH_RATE = 60
INITIAL_ANGLE = 0
COOLDOWN_TIME = 30
NOT_FOUND = 0
MONEY_TEXT_BOX = 0
LIVES_TEXT_BOX = 1
ROUND_TEXT_BOX = 9
END_OF_TOWERS_BUTTONS = 6

# -----Encoded-map-decoding--------

UNPLACEABLE = '0'
ROUTE = '1'
PLACEABLE = '2'
ROUTE_START = '3'
ROUTE_END = '4'
ROADS_COLLISIONS = '5'
WATER = '6'
ROAD = '7'

# ------------Images---------------

# -------Shots-------
DART_IMAGE = r'images/Shots/dart_image.png'
TACK_IMAGE = r'images/Shots/tack_image.png'
BOMB_IMAGE = r'images/Shots/bomb_image.png'

# ------Towers-------
DART_MONKEY_IMAGE = r'images/Towers/dart_monkey_image.png'
TACK_TOWER_IMAGE = r'images/Towers/tack_tower_image.png'
BOMB_TOWER_IMAGE = r'images/Towers/bomb_tower_image.png'
ICE_TOWER_IMAGE = r'images/Towers/ice_tower_image.png'
SUPER_MONKEY_IMAGE = r'images/Towers/supermonkey_image.png'
BOAT_IMAGE = r'images/Towers/boat_image.png'

# -----Effects------
EXPLOSION_IMAGE = r'images/Effects/explosion_image.png'
POPPED_BALLOON_IMAGE = r'images/Effects/popped_balloon.png'

# ----Backgrounds----
HOME_SCREEN_IMAGE = r'images/Backgrounds/home_screen_image.png'
LEVEL_SELECTION_BACKGROUND_IMAGE = r'images/Backgrounds/level_selection_background.png'
SHOP_BACKGROUND_IMAGE = r'images/Backgrounds/shop_background.png'
MONEY_IMAGE = r'images/Backgrounds/money_image.png'
LIVES_IMAGE = r'images/Backgrounds/lives_image.png'
GAME_OVER_IMAGE = r'images/Backgrounds/game_over_image.png'
YOU_WIN_IMAGE = r'images/Backgrounds/you_win_image.png'


# ---------Towers-stats------------

# ---Dart-monkey-----
DART_MONKEY_COST = 250
DART_MONKEY_SELL_COST = 200
DART_MONKEY_SHOT_SPEED = 15
DART_MONKEY_SHOT_DAMAGE = 1
DART_MONKEY_SHOOTING_SPEED = 650
DART_MONKEY_RANGE_RADIUS = 100

# ---Tack-tower-----
TACK_TOWER_COST = 400
TACK_TOWER_SELL_COST = 320
TACK_TOWER_SHOT_SPEED = 12
TACK_TOWER_SHOT_DAMAGE = 1
TACK_TOWER_SHOOTING_SPEED = 1100
TACK_TOWER_RANGE_RADIUS = 70

# ---Bomb-tower-----
BOMB_TOWER_COST = 900
BOMB_TOWER_SELL_COST = 720
BOMB_TOWER_SHOT_SPEED = 4
BOMB_TOWER_SHOT_DAMAGE = 2
BOMB_TOWER_SHOOTING_SPEED = 1500
BOMB_TOWER_RANGE_RADIUS = 120

# ---Super-monkey---
SUPER_MONKEY_COST = 3000
SUPER_MONKEY_SELL_COST = 2400
SUPER_MONKEY_SHOT_SPEED = 20
SUPER_MONKEY_SHOT_DAMAGE = 1
SUPER_MONKEY_SHOOTING_SPEED = 120
SUPER_MONKEY_RANGE_RADIUS = 140

# -----Ice-tower-----
ICE_TOWER_COST = 850
ICE_TOWER_SELL_COST = 680
ICE_TOWER_SHOT_SPEED = 0
ICE_TOWER_SHOT_DAMAGE = 0
ICE_TOWER_FREEZING_SPEED = 3000
ICE_TOWER_RANGE_RADIUS = 80
ICE_TOWER_FREEZING_DURATION = 1500

# ------Boat-------
BOAT_COST = 1500
BOAT_SELL_COST = 1200
BOAT_SHOT_SPEED = 40
BOAT_SHOT_DAMAGE = 2
BOAT_SHOOTING_SPEED = 170
BOAT_RANGE_RADIUS = 180

# -------Effects_durations---------
EXPLOSION_DURATION = 250
POPPED_BALLOON_DURATION = 100


# --------Enumerations-------------

class Maps(Enum):
    MAP1 = 1
    MAP2 = 2
    MAP3 = 3


class Movement(Enum):
    PLUS_X = 1
    PLUS_Y = 2
    MINUS_X = 3
    MINUS_Y = 4


class BalloonColor(Enum):
    NO_BALLOON = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    BLACK = 5
    WHITE = 6


class State(Enum):
    HOME_SCREEN = 1
    HELP_SCREEN = 2
    LEVEL_SELECTION = 3
    IN_GAME = 4
    GAME_ENDED = 5


class ButtonName(Enum):
    HOME_SCREEN_BUTTON = 1
    HELP_BUTTON = 2
    CLOSE_BUTTON = 3
    SELECT_MAP1 = 4
    SELECT_MAP2 = 5
    SELECT_MAP3 = 6
    SELECT_NORMAL_MODE = 7
    SELECT_SANDBOX_MODE = 8
    START_GAME = 9
    BUY_DART_MONKEY = 10
    BUY_TACK_TOWER = 11
    BUY_BOMB_TOWER = 12
    BUY_ICE_TOWER = 13
    BUY_SUPER_MONKEY = 14
    BUY_BOAT = 15
    BUY_FIRST_UPGRADE = 16
    BUY_SECOND_UPGRADE = 17
    START_ROUND = 18
    LAUNCH_RED_BALLOON = 19
    LAUNCH_BLUE_BALLOON = 20
    LAUNCH_GREEN_BALLOON = 21
    LAUNCH_YELLOW_BALLOON = 22
    LAUNCH_BLACK_BALLOON = 23
    LAUNCH_WHITE_BALLOON = 24
    SELL_TOWER_BUTTON = 25
    BACK_TO_HOME_SCREEN = 26


class GameMode(Enum):
    NORMAL = 1
    SANDBOX = 2


class Ending(Enum):
    WIN = 1
    LOSE = 2
    NOT_OVER = 3


# --------Dictionaries-------------

BALLOON_HP_TO_IMAGE = {
    1: "images/Balloons/red_balloon.png",
    2: "images/Balloons/blue_balloon.png",
    3: "images/Balloons/green_balloon.png",
    4: "images/Balloons/yellow_balloon.png",
    5: "images/Balloons/black_balloon.png",
    6: "images/Balloons/white_balloon.png",
}

BALLOON_HP_TO_FROZEN_IMAGE = {
    1: "images/Balloons/Frozen_Balloons/frozen_red_balloon.png",
    2: "images/Balloons/Frozen_Balloons/frozen_blue_balloon.png",
    3: "images/Balloons/Frozen_Balloons/frozen_green_balloon.png",
    4: "images/Balloons/Frozen_Balloons/frozen_yellow_balloon.png",
    5: "images/Balloons/Frozen_Balloons/frozen_black_balloon.png",

}

BALLOON_HP_TO_SPEED = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
}

MAP_TO_ENCODED_MAP = {
    Maps.MAP1: r'gameplay/encoded_maps/encoded_map1.txt',
    Maps.MAP2: r'gameplay/encoded_maps/encoded_map2.txt',
    Maps.MAP3: r'gameplay/encoded_maps/encoded_map3.txt'
}

MAP_TO_IMAGE = {
    Maps.MAP1: r'images/Maps/Map1_image.png',
    Maps.MAP2: r'images/Maps/map2_image.png',
    Maps.MAP3: r'images/Maps/map3_image.png'
}

BUTTON_TO_IMAGE = {
    ButtonName.HOME_SCREEN_BUTTON: r'images/Buttons/Starting/home_screen_button_image.png',
    ButtonName.HELP_BUTTON: r'images/Buttons/Other/help_button_image.png',
    ButtonName.SELECT_MAP1: r'images/Buttons/LevelSelection/map1_button_image.png',
    ButtonName.SELECT_MAP2: r'images/Buttons/LevelSelection/map2_button_image.png',
    ButtonName.SELECT_MAP3: r'images/Buttons/LevelSelection/map3_button_image.png',
    ButtonName.SELECT_NORMAL_MODE: r'images/Buttons/LevelSelection/normal_mode_button_image.png',
    ButtonName.SELECT_SANDBOX_MODE: r'images/Buttons/LevelSelection/sandbox_mode_button_image.png',
    ButtonName.START_GAME: r'images/Buttons/Starting/start_game_button_image.png',
    ButtonName.CLOSE_BUTTON: r'images/Buttons/Other/close_button.png',
    ButtonName.BUY_DART_MONKEY: r'images/Buttons/BuyingTowers/affordable_dart_monkey_button_image.png',
    ButtonName.BUY_TACK_TOWER: r'images/Buttons/BuyingTowers/affordable_tack_tower_button_image.png',
    ButtonName.BUY_BOMB_TOWER: r'images/Buttons/BuyingTowers/affordable_bomb_tower_button_image.png',
    ButtonName.BUY_ICE_TOWER: r'images/Buttons/BuyingTowers/affordable_ice_tower_button_image.png',
    ButtonName.BUY_SUPER_MONKEY: r'images/Buttons/BuyingTowers/affordable_supermonkey_button_image.png',
    ButtonName.BUY_BOAT: r'images/Buttons/BuyingTowers/affordable_boat_button_image.png',
    ButtonName.LAUNCH_RED_BALLOON: r'images/Buttons/LaunchingBalloons/red_balloon_button.png',
    ButtonName.LAUNCH_BLUE_BALLOON: r'images/Buttons/LaunchingBalloons/blue_balloon_button.png',
    ButtonName.LAUNCH_GREEN_BALLOON: r'images/Buttons/LaunchingBalloons/green_balloon_button.png',
    ButtonName.LAUNCH_YELLOW_BALLOON: r'images/Buttons/LaunchingBalloons/yellow_balloon_button.png',
    ButtonName.LAUNCH_BLACK_BALLOON: r'images/Buttons/LaunchingBalloons/black_balloon_button.png',
    ButtonName.LAUNCH_WHITE_BALLOON: r'images/Buttons/LaunchingBalloons/white_balloon_button.png',
    ButtonName.START_ROUND: r'images/Buttons/Starting/start_round_button.png',
    ButtonName.SELL_TOWER_BUTTON: r'images/Buttons/Other/sell_button.png',
    ButtonName.BACK_TO_HOME_SCREEN: r'images/Buttons/Other/home_button.png'
}

TOWERS_BUTTONS_NAME_TO_UNAFFORDABLE_IMAGE = {
    ButtonName.BUY_DART_MONKEY: r'images/Buttons/BuyingTowers/unaffordable_dart_monkey_button_image.png',
    ButtonName.BUY_TACK_TOWER: r'images/Buttons/BuyingTowers/unaffordable_tack_tower_button_image.png',
    ButtonName.BUY_BOMB_TOWER: r'images/Buttons/BuyingTowers/unaffordable_bomb_tower_button_image.png',
    ButtonName.BUY_ICE_TOWER: r'images/Buttons/BuyingTowers/unaffordable_ice_tower_button_image.png',
    ButtonName.BUY_SUPER_MONKEY: r'images/Buttons/BuyingTowers/unaffordable_supermonkey_button_image.png',
    ButtonName.BUY_BOAT: r'images/Buttons/BuyingTowers/unaffordable_boat_button_image.png'
}

TOWER_BUTTON_NAME_TO_PRICE = {
    ButtonName.BUY_DART_MONKEY: DART_MONKEY_COST,
    ButtonName.BUY_TACK_TOWER: TACK_TOWER_COST,
    ButtonName.BUY_BOMB_TOWER: BOMB_TOWER_COST,
    ButtonName.BUY_ICE_TOWER: ICE_TOWER_COST,
    ButtonName.BUY_SUPER_MONKEY: SUPER_MONKEY_COST,
    ButtonName.BUY_BOAT: BOAT_COST
}

# -------Positions-------

BUTTON_TO_POSITION = {
    ButtonName.HOME_SCREEN_BUTTON: Point((WINDOW_WIDTH/2, 455)),
    ButtonName.HELP_BUTTON: Point((62, 35)),
    ButtonName.CLOSE_BUTTON: Point((730, 55)),
    ButtonName.SELECT_MAP1: Point((280, 145)),
    ButtonName.SELECT_MAP2: Point((472, 145)),
    ButtonName.SELECT_MAP3: Point((664, 145)),
    ButtonName.SELECT_NORMAL_MODE: Point((366, 300)),
    ButtonName.SELECT_SANDBOX_MODE: Point((580, 300)),
    ButtonName.START_GAME: Point((WINDOW_WIDTH/2, 417)),
    ButtonName.BUY_DART_MONKEY: Point((816, 114)),
    ButtonName.BUY_TACK_TOWER: Point((886, 114)),
    ButtonName.BUY_BOMB_TOWER: Point((816, 179)),
    ButtonName.BUY_ICE_TOWER: Point((886, 179)),
    ButtonName.BUY_SUPER_MONKEY: Point((816, 244)),
    ButtonName.BUY_BOAT: Point((886, 244)),
    ButtonName.LAUNCH_RED_BALLOON: Point((806, 305)),
    ButtonName.LAUNCH_BLUE_BALLOON: Point((851, 305)),
    ButtonName.LAUNCH_GREEN_BALLOON: Point((896, 305)),
    ButtonName.LAUNCH_YELLOW_BALLOON: Point((806, 350)),
    ButtonName.LAUNCH_BLACK_BALLOON: Point((851, 350)),
    ButtonName.LAUNCH_WHITE_BALLOON: Point((896, 350)),
    ButtonName.START_ROUND: Point((851, 447)),
    ButtonName.SELL_TOWER_BUTTON: Point((851, 360)),
    ButtonName.BACK_TO_HOME_SCREEN: Point((WINDOW_WIDTH/2 - 75, 400))
}

SHOP_BACKGROUND_POSITION = (776, 0)
MONEY_POSITION = (785, 6)
LIVES_POSITION = (785, 43)
GAME_OVER_POSITION = (190, 100)
YOU_WIN_POSITION = (185, 85)


# ------------Lists----------------

BLOCKS_SURROUNDINGS = [(-1, -1), (0, -1), (1, -1),
                       (-1, 0), (1, 0),
                       (-1, 1), (0, 1), (1, 1)]

TOWERS_BUTTONS_NAMES = [ButtonName.BUY_DART_MONKEY,
                        ButtonName.BUY_TACK_TOWER,
                        ButtonName.BUY_BOMB_TOWER,
                        ButtonName.BUY_ICE_TOWER,
                        ButtonName.BUY_SUPER_MONKEY,
                        ButtonName.BUY_BOAT]

# --------Audio--------
BALLOON_POP_SOUND = r'Audio/balloon_pop_sound.mp3'
BACKGROUND_MUSIC = r'Audio/background_music.mp3'


# --------Texts--------

HELP_TEXT_LINES = [
    "This is a simple game of Bloons TD.",
    "There are 2 modes: Normal and Sandbox",
    "Normal Mode:",
    "The goal is to survive through all 30 rounds without losing",
    "all of your lives.",
    "You lose lives when a balloon reaches the end of the route.",
    "You can prevent balloons from reaching the end by placing towers that will shoot",
    "them down and pop them.",
    "Every tower has its own unique way of attack.",
    "Sandbox Mode:",
    "There is no goal.",
    "Infinite money and infinite lives. You cannot lose nor win.",
    "Place as many towers as you want.",
    "Create balloons with the balloons buttons in the shop or with the keys 1-6 on the keyboard.",
    "Have fun!"
]


