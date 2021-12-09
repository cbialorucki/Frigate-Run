import arcade
import game.constants as Constants

class Health():
    def __init__(self, totalShields, totalHealth):
        self._totalShields = totalShields
        self._currentHealth = self._totalShields
        self._isDead = False
        self._totalHealth = totalHealth
    
    def takeDamage(self, hitPoints):
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
