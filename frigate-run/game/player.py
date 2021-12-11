import arcade
import game.constants as Constants
from game.health import Health
from datetime import datetime

class Player(arcade.Sprite):
    """ A code template for the person who plays the game. Determines the actions that happen 
    during gameplay.
    
        Attributes:
            _health: Health class
            _lastCollisionSprites: List to determine which enemies spirit is hit
            _lastHit: If player has hit a sprite object on the last hit then thay cannot be damaged again"""
    
    def __init__(self, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture: arcade.Texture = None, angle: float = 0):
        super().__init__(filename=Constants.FRIGATE_PATH, scale=Constants.FRIGATE_SCALE, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)
        self._health = Health(Constants.TOTAL_SHIELDS, Constants.TOTAL_HEALTH)
        self._lastCollisionSprites = []
        self._lastHit = 0
    
    def hitsObj(self, sprite):
        """ Determines if the player hit an object
        """
        if not sprite in self._lastCollisionSprites:
            self._health.takeDamage(Constants.HIT_POINTS)
            arcade.load_sound(Constants.CRASH_SOUND_PATH).play()
            self._lastCollisionSprites.append(sprite)
            self._didShieldRecharge = False
            self._lastHit = datetime.now()
            if len(self._lastCollisionSprites) >= 10:
                self._lastCollisionSprites.pop(0)
    
    def isDead(self):
        """ Determines if the player is dead
        """
        return self._health.isDead()
    
    def isShieldDown(self):
        """ Determines if the shield is down on player
        """
        return self._health.isShieldDown()
    
    def getTotalHealth(self):
        """ Determines the total health for the player
        """
        return self._health.getTotalHealth()
    
    def getActualHealth(self):
        """ Determines the health that the player has"""
        return self._health.getActualHealth()
    
    def getLastHitTime(self):
        """ Determines the last time the player was hit
        """
        return self._lastHit
    
    def isFullHealth(self):
        """ Determines if the players health is full or not"""
        if self._health.getActualHealth() == self._health.getTotalHealth():
            return True
        return False

    def recharge(self):
        """ Recharges player shield"""
        self._health.regenerateShield()
