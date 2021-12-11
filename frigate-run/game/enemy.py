import arcade
import game.constants as Constants

class Enemy(arcade.Sprite):
    """ A code template for the enemies of the game. Each enemy is updated to determine movement 
    across the screen. 
    
        Attributes:
            velocity: velocity of the sprite across the screen"""

    def __init__(self, filepath, imgScale, velocity, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str = "Simple", hit_box_detail: float = 4.5, texture: arcade.Texture = None, angle: float = 0):
        """ Iniatialize the enemies"""
        super().__init__(filename=filepath, scale=imgScale, image_x=image_x, image_y=image_y, image_width=image_width, image_height=image_height, center_x=center_x, center_y=center_y, repeat_count_x=repeat_count_x, repeat_count_y=repeat_count_y, flipped_horizontally=flipped_horizontally, flipped_vertically=flipped_vertically, flipped_diagonally=flipped_diagonally, hit_box_algorithm=hit_box_algorithm, hit_box_detail=hit_box_detail, texture=texture, angle=angle)
        self.velocity = ((0 - abs(velocity)), 0)
    
    def update(self):
        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.right < 0:
            self.remove_from_sprite_lists()
    
    