import arcade
from game import constants

class Enemies(arcade.Sprite):
    
    def update(self):
        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()
    
    