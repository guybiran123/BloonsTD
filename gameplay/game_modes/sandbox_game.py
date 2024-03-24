from gameplay.game_modes.game import Game
from utils.constants import *


class SandboxGame(Game):

    def __init__(self, map_level: Maps):
        super().__init__(map_level, GameMode.SANDBOX)

    def get_text_money(self):
        return "Infinity"

    def get_text_lives(self):
        return "Infinity"
