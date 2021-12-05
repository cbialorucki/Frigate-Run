import arcade
from game.health import Health
from game.player import Player
import game.constants as Constants
from datetime import datetime

class HUD():
    def __init__(self, player):
        self._player = player
        self._shieldDownSound = arcade.load_sound(Constants.SHIELD_DOWN_SOUND_PATH)
        self._shieldDownPlayer = arcade.play_sound(self._shieldDownSound, looping=True, volume=1)
        self._shieldDownPlayer.pause()
        self._isHealthRed = False
        self._shieldRechargeSound = arcade.load_sound(Constants.SHIELD_RECHARGE_SOUND_PATH)
    
    def playRechargeSound(self):
        arcade.play_sound(self._shieldRechargeSound, volume=1)

    def updateBar(self):
        arcade.draw_rectangle_filled(center_x=Constants.SCREEN_WIDTH/2,
                                         center_y=Constants.SCREEN_HEIGHT + Constants.HEALTH_BAR_OFFSET_Y,
                                         width=Constants.HEALTH_BAR_WIDTH,
                                         height=Constants.HEALTH_BAR_HEIGHT,
                                         color=arcade.color.RED if self._isHealthRed else arcade.color.GRAY)
        
        self._health_width = Constants.HEALTH_BAR_WIDTH * (self._player.getActualHealth() / self._player.getTotalHealth())

        arcade.draw_rectangle_filled(center_x=Constants.SCREEN_WIDTH/2 - 0.5 * (Constants.HEALTH_BAR_WIDTH - self._health_width),
                                     center_y=Constants.SCREEN_HEIGHT + Constants.HEALTH_BAR_OFFSET_Y,
                                     width=self._health_width,
                                     height=Constants.HEALTH_BAR_HEIGHT,
                                     color=arcade.color.SKY_BLUE)
        
        if self._player.isShieldDown():
            self._shieldDownPlayer.play()
            
            if round(datetime.now().microsecond / 180000) % 2 == 0:
                self._isHealthRed = True
            else:
                self._isHealthRed = False
        
        else:
            self._shieldDownPlayer.pause()
            self._isHealthRed = False
        

        

    
