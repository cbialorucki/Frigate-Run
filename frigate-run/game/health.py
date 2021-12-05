import arcade

class Health():
    def __init__(self, totalPoints):
        self._initHealth = totalPoints
        self._actualHealth = self._initHealth
        self._isDead = False
    
    def takeDamage(self, hitPoints):
        self._actualHealth -= hitPoints
        if(self._actualHealth < 0):
            self._isDead = True
    
    def isDead(self):
        return self._isDead
    
    def isShieldDown(self):
        if self.actualHealth == 0:
            return True
        else:
            return False
    
    def regenerateShield(self):
        self._actualHealth = self._initHealth
    
    def getTotalHealth(self):
        return self._initHealth
