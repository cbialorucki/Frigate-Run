import arcade

class Health:

    def __init__(self, health, bar):

        self.health = health
        self.bar = bar

    def healthbar(self, bar):

        self.bar = bar

    def player_health(self, health):

        self.health = health
  
  
    
       