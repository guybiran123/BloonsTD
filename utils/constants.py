from enum import Enum


WINDOW_HEIGHT = 475
WINDOW_WIDTH = 639

# --------Dictionaries-------------

BALLOON_HP_TO_IMAGE = {
    1: "images/Balloons/Red_balloon_image.png",
    2: "images/Balloons/Blue_balloon_image.png",
    3: "images/Balloons/Green_balloon_image.png",
    4: "images/Balloons/Yellow_balloon_image.png",
    5: "images/Balloons/Black_balloon_image.png",
    6: "images/Balloons/White_balloon_image.png",
}


# --------Enumerations-------------
class Maps(Enum):
    MAP1 = 1
    MAP2 = 2
    MAP3 = 3
