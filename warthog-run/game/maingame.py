import arcade
import random
from game import constants
from game.enemy import Enemies
from game.collision import Collision


class Maingame(arcade.Window):
    
    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        self.paused = None


        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
    
    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set up the player
        self.player = arcade.Sprite("Warthog-Run\warthog-run\game\images\warthog.jpg", constants.SCALING)
        self.player.center_y = self.height - 799
        self.player.left = 10
        self.all_sprites.append(self.player)

        arcade.schedule(self.add_enemy, 1.0)
        arcade.schedule(self.add_wall, 2.0)

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new enemy sprite
        enemy = Enemies("Warthog-Run\warthog-run\game\images\idle.png", constants.SCALING)

        # Set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-10, -5), 0)

        # Add it to the enemies list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

        if enemy.right < 0:
            enemy.remove_from_sprite_lists()

        for enemy in self.enemies_list:
            enemy.update()

    def add_wall(self, delta_time: float):
        """Adds a new cloud to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new cloud sprite
        wall = Enemies("Warthog-Run\warthog-run\game\images/wall.jpg", constants.SCALING)

        # Set its position to a random height and off screen right
        wall.left = random.randint(self.width, self.width + 20)
        wall.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        wall.velocity = (random.randint(-5, -2), 0)

        # Add it to the enemies list
        self.enemies_list.append(wall)
        self.all_sprites.append(wall)

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.change_y = 5

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player.change_y = -5

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -5

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing

        Arguments:
            delta_time {float} -- Time since the last update
        """

        # If paused, don't update anything
        if self.paused:
            return

        # Update everything
        self.all_sprites.update()

        # Did you hit anything? If so, end the game
        if self.player.collides_with_list(self.enemies_list):
            arcade.close_window()

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0


    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        self.all_sprites.draw()