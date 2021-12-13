import arcade
from game.health import Health
from game.player import Player
import game.constants as Constants
from datetime import datetime

class HUD():
    """ A code template for handling the display of the healthbar and sounds for player health.
    
        Attributes:
            _player: The player class
            _shieldDownSound: Sound for low health
            _shieldDownPlayer: Sound for being hit
            _isHealthRed: Is player almost dead
            _shieldRechargeSound: Sound for recharging shield"""
    
    def __init__(self, player):
        """ Initialize the HUD
        """
        self._player = player
        self._shieldDownSound = arcade.load_sound(Constants.SHIELD_DOWN_SOUND_PATH)
        self._shieldDownPlayer = arcade.play_sound(self._shieldDownSound, looping=True, volume=1)
        self._shieldDownPlayer.pause()
        self._isHealthRed = False
        self._shieldRechargeSound = arcade.load_sound(Constants.SHIELD_RECHARGE_SOUND_PATH)
    
    def playRechargeSound(self):
        """ Recharging sound for regenerating health"""

        arcade.play_sound(self._shieldRechargeSound, volume=1)

    def updateBar(self):
        """ Updates the health bar each time the player is hit or recharging health"""

        arcade.draw_rectangle_filled(center_x=Constants.SCREEN_WIDTH/2,
                                         center_y=Constants.SCREEN_HEIGHT + Constants.HEALTH_BAR_OFFSET_Y,
                                         width=Constants.HEALTH_BAR_WIDTH,
                                         height=Constants.HEALTH_BAR_HEIGHT,
                                         color=arcade.color.RED if self._isHealthRed else arcade.color.GRAY)
        
        if self._player.getActualHealth() > 0:
            """ Function to determine the health that the player has at each moment"""

            self._health_width = Constants.HEALTH_BAR_WIDTH * (self._player.getActualHealth() / self._player.getTotalHealth())

            arcade.draw_rectangle_filled(center_x=Constants.SCREEN_WIDTH/2 - 0.5 * (Constants.HEALTH_BAR_WIDTH - self._health_width),
                                        center_y=Constants.SCREEN_HEIGHT + Constants.HEALTH_BAR_OFFSET_Y,
                                        width=self._health_width,
                                        height=Constants.HEALTH_BAR_HEIGHT,
                                        color=arcade.color.SKY_BLUE)
            
        if self._player.isShieldDown():
            """ Determines if the player shield is down 
            """
            self._shieldDownPlayer.play()
            
            if round(datetime.now().microsecond / 180000) % 2 == 0:
                self._isHealthRed = True
            else:
                self._isHealthRed = False
        
        else:
            self._shieldDownPlayer.pause()
            self._isHealthRed = False
        

        

    
