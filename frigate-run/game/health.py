import arcade
import game.constants as Constants

class Health():
    """ A class to determine the health that a player has when taking damage or regenerating health.
    
        Attributes:
            _totalShields: The total amount of shield health
            _currentHealth: The current health of the player
            _isDead: Determines if the player out of health
            _totalHealth: Total health of the player"""
    def __init__(self, totalShields, totalHealth):
        """ Iniatialize the health"""
        self._totalShields = totalShields
        self._currentHealth = self._totalShields
        self._isDead = False
        self._totalHealth = totalHealth
    
    def takeDamage(self, hitPoints):
        """ Dertermines if the player """
        self._currentHealth -= hitPoints
        if(self._currentHealth < (0 - self._totalHealth)):
            self._isDead = True
    
    def isDead(self):
        return self._isDead
    
    def isShieldDown(self):
        if self._currentHealth <= 0:
            return True
        else:
            return False
    
    def regenerateShield(self):
        self._currentHealth = self._totalShields
    
    def getTotalHealth(self):
        return self._totalShields
    
    def getActualHealth(self):
        return self._currentHealth
