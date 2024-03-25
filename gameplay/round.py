import random
from gameplay.game_map import GameMap

from utils.constants import *


class Round:

    def __init__(self, level: int):
        self.__level = level
        self.__cooldown = self.get_cooldown_from_level()
        self.__balloons = self.get_balloons_dict_from_level()

    def get_cooldown_from_level(self):
        level_to_cooldown = {
            1: 1000, 2: 900, 3: 800, 4: 700, 5: 600,
            6: 550, 7: 500, 8: 450, 9: 400, 10: 350,
            11: 300, 12: 275, 13: 250, 14: 225, 15: 200,
            16: 175, 17: 150, 18: 125, 19: 100, 20: 75,
            21: 50, 22: 50, 23: 50, 24: 50, 25: 50,
            26: 50, 27: 50, 28: 50, 29: 50, 30: 50, 31: 30
        }
        return level_to_cooldown[self.__level]

    def get_cooldown(self):
        return self.__cooldown

    def get_balloons_dict_from_level(self):
        level_to_balloons_dict = {
            1: {  # Start very easy
                1: 5,  # Red
                2: 0,  # Blue
                3: 0,  # Green
                4: 0,  # Yellow
                5: 0,  # Black
                6: 0,  # White
            },
            2: {  # Slightly more difficult
                1: 8,
                2: 1,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
            },
            3: {  # Introduce Green Bloons, increase slightly
                1: 10,
                2: 2,
                3: 2,
                4: 0,
                5: 0,
                6: 0,
            },
            4: {  # Gradual increase
                1: 12,
                2: 3,
                3: 3,
                4: 1,
                5: 0,
                6: 0,
            },
            5: {  # Slight increase
                1: 14,
                2: 4,
                3: 4,
                4: 2,
                5: 0,
                6: 0,
            },
            6: {  # Introduce Yellow Bloons
                1: 16,
                2: 5,
                3: 5,
                4: 3,
                5: 0,
                6: 0,
            },
            7: {  # Increase all basic bloons
                1: 18,
                2: 6,
                3: 6,
                4: 4,
                5: 1,  # Introduce a single Black Bloon
                6: 0,
            },
            8: {  # Balanced mix of basic bloons
                1: 20,
                2: 7,
                3: 7,
                4: 5,
                5: 2,
                6: 0,
            },
            9: {  # Start decreasing Red Bloons, introduce White Bloons
                1: 18,
                2: 8,
                3: 8,
                4: 6,
                5: 3,
                6: 1,
            },
            10: {  # Higher count of all basic bloons
                1: 16,
                2: 9,
                3: 9,
                4: 7,
                5: 4,
                6: 2,
            },
            11: {  # Increase difficulty with more bloons
                1: 20,
                2: 10,
                3: 10,
                4: 8,
                5: 5,
                6: 3,
            },
            12: {
                1: 22,
                2: 11,
                3: 11,
                4: 9,
                5: 6,
                6: 4,
            },
            13: {
                1: 24,
                2: 12,
                3: 12,
                4: 10,
                5: 7,
                6: 5,
            },
            14: {
                1: 26,
                2: 13,
                3: 13,
                4: 11,
                5: 8,
                6: 6,
            },
            15: {
                1: 28,
                2: 14,
                3: 14,
                4: 12,
                5: 9,
                6: 7,
            },
            16: {  # Introduce more Black and White Bloons
                1: 25,
                2: 12,
                3: 12,
                4: 10,
                5: 10,
                6: 8,
            },
            17: {
                1: 23,
                2: 11,
                3: 11,
                4: 8,
                5: 12,
                6: 9,
            },
            18: {
                1: 21,
                2: 10,
                3: 10,
                4: 7,
                5: 14,
                6: 10,
            },
            19: {
                1: 20,
                2: 9,
                3: 9,
                4: 6,
                5: 16,
                6: 11,
            },
            20: {  # Final round, very challenging
                1: 18,
                2: 8,
                3: 8,
                4: 5,
                5: 18,
                6: 12,
            },
            21: {  # Higher counts and mixed bloons
                1: 30,
                2: 15,
                3: 13,
                4: 11,
                5: 12,
                6: 9,
            },
            22: {  # Introduce more Yellow and Black Bloons
                1: 28,
                2: 14,
                3: 12,
                4: 14,
                5: 14,
                6: 10,
            },
            23: {  # Emphasis on Blue and Green Bloons
                1: 26,
                2: 16,
                3: 14,
                4: 12,
                5: 10,
                6: 8,
            },
            24: {  # Balanced mix with higher totals
                1: 24,
                2: 15,
                3: 13,
                4: 11,
                5: 13,
                6: 11,
            },
            25: {  # Focus on Red and White Bloons
                1: 32,
                2: 12,
                3: 10,
                4: 8,
                5: 8,
                6: 14,
            },
            26: {  # Increasing all bloon types
                1: 30,
                2: 14,
                3: 12,
                4: 10,
                5: 12,
                6: 12,
            },
            27: {  # More Black and White Bloons, fewer Red
                1: 28,
                2: 13,
                3: 11,
                4: 9,
                5: 14,
                6: 15,
            },
            28: {  # Balanced mix with a twist (more Green)
                1: 26,
                2: 12,
                3: 16,
                4: 8,
                5: 10,
                6: 14,
            },
            29: {  # Focus on Yellow Bloons, some stronger types
                1: 24,
                2: 10,
                3: 8,
                4: 16,
                5: 12,
                6: 10,
            },
            30: {  # Final round (extremely challenging)
                1: 22,
                2: 8,
                3: 6,
                4: 18,
                5: 16,
                6: 16,
            },
            31: {1: 30,
                 2: 30,
                 3: 30,
                 4: 30,
                 5: 30,
                 6: 30
                }
        }
        return level_to_balloons_dict[self.__level]

    def get_balloon(self):
        rand = random.randint(1, 6)
        while self.__balloons[rand] == 0:
            rand = random.randint(1, 6)
        self.__balloons[rand] -= 1
        return rand

    def round_over(self):
        for value in self.__balloons.values():
            if value > 0:
                return False
        return True
