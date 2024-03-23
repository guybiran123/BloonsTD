from gameplay.game_modes.game import Game
from utils.constants import *


class SandboxGame(Game):

    def __init__(self, map_level: Maps):
        super().__init__(map_level, GameMode.SANDBOX)
