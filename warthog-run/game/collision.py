import arcade

class Collision:
    
    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing

        Arguments:
            delta_time {float} -- Time since the last update
        """

        # Did you hit anything? If so, end the game
        if self.player.collides_with_list(self.enemies_list):
            arcade.close_window()

       