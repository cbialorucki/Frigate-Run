import arcade
from game.maingame import Maingame
import game.constants as Constants

if __name__ == "__main__":
    app = Maingame(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.SCREEN_TITLE)
    arcade.run()