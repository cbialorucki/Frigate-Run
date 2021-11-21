import arcade
from game.maingame import Maingame
from game import constants

if __name__ == "__main__":
    app = Maingame(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    app.setup()
    arcade.run()