from enum import Enum


# ---General_magic_numbers---------

X = 0
Y = 1
WINDOW_HEIGHT = 475
WINDOW_WIDTH = 639
INITIAL_ANGLE = 0
COOLDOWN_TIME = 100
NOT_FOUND = 0


# -----Encoded-map-decoding--------

UNPLACEABLE = '0'
ROUTE = '1'
PLACEABLE = '2'
ROUTE_START = '3'
ROUTE_END = '4'
ROADS_COLLISIONS = '5'
WATER = '6'


# --------Lists--------------------

BLOCKS_SURROUNDINGS = [(-1, -1), (0, -1), (1, -1),
                       (-1, 0),           (1, 0),
                       (-1, 1),  (0, 1),  (1, 1)]


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
    1: "images/Balloons/Red_balloon_image.png",
    2: "images/Balloons/Blue_balloon_image.png",
    3: "images/Balloons/Green_balloon_image.png",
    4: "images/Balloons/Yellow_balloon_image.png",
    5: "images/Balloons/Black_balloon_image.png",
    6: "images/Balloons/White_balloon_image.png",
}

BALLOON_HP_TO_SPEED = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
}

MAP_TO_ENCODED_MAP = {
    Maps.MAP1: r"gameplay/encoded_maps/encoded_map1.txt"
}

MAP_HAS_ROADS_COLLISIONS = {
    Maps.MAP1: False,
    Maps.MAP2: True,
    Maps.MAP3: False,
}
