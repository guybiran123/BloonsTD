from enum import Enum

# -----General_magic_numbers-------

COLOR_KEY = (20, 250, 250)

X = 0
Y = 1
WINDOW_HEIGHT = 475
WINDOW_WIDTH = 639
REFRESH_RATE = 60
INITIAL_ANGLE = 0
COOLDOWN_TIME = 30
NOT_FOUND = 0

# -----Encoded-map-decoding--------

UNPLACEABLE = '0'
ROUTE = '1'
PLACEABLE = '2'
ROUTE_START = '3'
ROUTE_END = '4'
ROADS_COLLISIONS = '5'
WATER = '6'

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
BOMB_TOWER_SHOT_DAMAGE = 3
BOMB_TOWER_SHOOTING_SPEED = 1500
BOMB_TOWER_RANGE_RADIUS = 120

# ---Super-monkey---
SUPER_MONKEY_COST = 4000
SUPER_MONKEY_SELL_COST = 3200
SUPER_MONKEY_SHOT_SPEED = 15
SUPER_MONKEY_SHOT_DAMAGE = 1
SUPER_MONKEY_SHOOTING_SPEED = 120
SUPER_MONKEY_RANGE_RADIUS = 140


# -------Effects_durations---------
EXPLOSION_DURATION = 250
POPPED_BALLOON_DURATION = 100


# ------------Lists----------------

BLOCKS_SURROUNDINGS = [(-1, -1), (0, -1), (1, -1),
                       (-1, 0), (1, 0),
                       (-1, 1), (0, 1), (1, 1)]


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


# --------Dictionaries-------------

BALLOON_HP_TO_IMAGE = {
    1: "images/Balloons/red_balloon.png",
    2: "images/Balloons/blue_balloon.png",
    3: "images/Balloons/green_balloon.png",
    4: "images/Balloons/yellow_balloon.png",
    5: "images/Balloons/black_balloon.png",
    6: "images/Balloons/white_balloon.png",
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
    Maps.MAP1: r'gameplay/encoded_maps/encoded_map1.txt'
}

MAP_TO_IMAGE = {
    Maps.MAP1: r'images/Maps/Map1_image.png'
}

MAP_HAS_ROADS_COLLISIONS = {
    Maps.MAP1: False,
    Maps.MAP2: True,
    Maps.MAP3: False,
}
