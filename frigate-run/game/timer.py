import arcade
from arcade.color import SHADOW
import game.constants as Constants

class Timer:
    """ A visible timer that keeps track of game time within the game.
    
        Attributes:
            total_time(int): The total time the player has to finish the game"""

    def __init__(self):
        """ Initialize the timer
        """
        self.total_time = 135
        
    def timer(self):
        """ Determines the time has passed in the game
        """
        mins, secs = divmod(self.total_time, 60)
  
        timer = f'{int(mins):02d}:{int(secs):02d}'
        arcade.draw_text(timer, Constants.TIMER_X_OFFSET, Constants.TIMER_Y_OFFSET, arcade.color.SKY_BLUE, Constants.TIMER_SIZE, font_name=Constants.TIMER_FONT, bold=True)
            
            
            
        