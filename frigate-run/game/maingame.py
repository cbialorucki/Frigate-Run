import arcade
import random

from arcade.window_commands import schedule
import game.constants as Constants
from game.enemy import Enemy
from game.player import Player
from game.hud import HUD
from datetime import datetime
from game.timer import Timer

class Maingame(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is display the screen and inputs for .
    
    Stereotype:
        Controller

    Attributes:
        enemies_list (dictionary): The game enemies
        all_sprites (dictionary): All sprites to be used in game
    """
    
    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)
        
        # Play Menu Music, Show Splash Screen
        self.paused = True
        self.isSetup = False
        self.bgImg = arcade.load_texture(Constants.SPLASH_PATH)
        self.bgMusic = arcade.load_sound(Constants.MENU_MUSIC_PATH).play()
        self.bgMusic.loop = True
        
        

        # Set up the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
    
    def setup(self):
        """Get the game ready to play
        """
        # Unload Splash Screen
        self.bgImg = arcade.load_texture(Constants.BACKGROUND_PATH)
        

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.bgMusic.pause()
        self.bgMusic = arcade.load_sound(Constants.GAME_MUSIC_PATH).play()
        self.bgMusic.loop = True

        # Set up the player
        self.player = Player(hit_box_algorithm='Detailed')
        self.player.center_y = self.height - 799
        self.player.left = 10
        self.all_sprites.append(self.player)

        self.schedule_enemies()
        arcade.schedule(self.schedule_enemies, Constants.DOUBLE_ENEMIES)

        self._hud = HUD(self.player)
        self._timer = Timer()
        self.paused = False
        
    def schedule_enemies(self, delta_time: float=0.0): 
        arcade.schedule(self.add_seraph, Constants.SERAPH_FREQUENCY)
        arcade.schedule(self.add_banshee, Constants.BANSHEE_FREQUENCY)
        arcade.schedule(self.add_cruiser, Constants.CRUISER_FREQUENCY)
        arcade.schedule(self.add_phantom, Constants.PHANTOM_FREQUENCY)
        arcade.schedule(self.add_spirit, Constants.SPIRIT_FREQUENCY)

    def add_seraph(self, delta_time: float):
        self.add_enemy(Enemy(Constants.SERAPH_PATH, Constants.SERAPH_SCALE, Constants.SERAPH_VELOCITY))
    
    def add_banshee(self, delta_time: float):
        self.add_enemy(Enemy(Constants.BANSHEE_PATH, Constants.BANSHEE_SCALE, Constants.BANSHEE_VELOCITY))
    
    def add_cruiser(self, delta_time: float):
        self.add_enemy(Enemy(Constants.CRUISER_PATH, Constants.CRUISER_SCALE, Constants.CRUISER_VELOCITY))
        
    def add_phantom(self, delta_time: float):
        self.add_enemy(Enemy(Constants.PHANTOM_PATH, Constants.PHANTOM_SCALE, Constants.PHANTOM_VELOCITY)) 
    
    def add_spirit(self, delta_time: float):
        self.add_enemy(Enemy(Constants.SPIRIT_PATH, Constants.SPIRIT_SCALE, Constants.SPIRIT_VELOCITY))

    def add_enemy(self, enemy):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """
        # Set its position to a random height and off screen right
        enemy.left = random.SystemRandom().randint(self.width, self.width + 80)
        enemy.top = random.SystemRandom().randint(10, self.height - 10)

        # Add it to the enemies list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

        if enemy.right < 0:
            enemy.remove_from_sprite_lists()

        for enemy in self.enemies_list:
            enemy.update()

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

        if not self.isSetup:
            return

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
        # If the game hasn't progressed past the Splash Screen yet, load the game.
        if not self.isSetup:
            self.setup()
            self.isSetup = True

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

        
        #self._timer.begin_time += delta_time
        self._timer.total_time -= delta_time
        if self._timer.total_time < 0.0:
            arcade.close_window()
            arcade.draw_text("Cogratulations you made it through the game", Constants.SCREEN_WIDTH/2, Constants.SCREEN_HEIGHT/2, arcade.color.AERO_BLUE, 25)
        
            

        # Did you hit anything? If so, deduct health
        if self.player.collides_with_list(self.enemies_list):
            for x in self.enemies_list:
                if self.player.collides_with_sprite(x):
                    self.player.hitsObj(x)
            
            if self.player.isDead():
                arcade.close_window()
            
            
        
        if not self.player.isFullHealth() and (datetime.now() - self.player._lastHit).total_seconds() >= Constants.SHIELD_RECHARGE_TIME:
            #Recharge shields
            self.player.recharge()
            self._hud.playRechargeSound()

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
        arcade.draw_texture_rectangle(Constants.SCREEN_WIDTH/2, Constants.SCREEN_HEIGHT/2, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, self.bgImg)
        self.all_sprites.draw()
        
        if self.isSetup:
            self._hud.updateBar()
            self._timer.timer()
       