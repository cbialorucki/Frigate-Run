# Frigate Run
Fly through a Covenant armada. You have a Frigate at your disposal as you have to pass Phantoms, Banshees, Seraphs, and more to ensure your safety and finish the fight.

## Game features
* Control the speed of your Frigate as you avoid obstacles.
* Escape the quickly multiplying Covenant before it's too late. 
* Players can fly; but there is no time to shoot.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- frigate-run         (source code for game)
  +-- resources         (contains images and sounds for the game)
  +-- game              (specific game classes)
    +-- constants.py    (constants used by the game)
    +-- enemy.py        (base class for all enemy objects)
    +-- health.py       (health class that is used for the player)
    +-- hud.py          (draws the "Heads Up Display" (HUD))
    +-- maingame.py     (directs game play)
    +-- player.py       (represents the player)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Legal
This game is not affiliated with Microsoft, Xbox, Bungie, or 343 Industries. This is a fan made game.

## Required Technologies
* Python 3.8.0
* Arcade

## Authors
* Carl Bialorucki carl.bialorucki@byui.edu
* Karla Sommerfeldt  kryn5796@yahoo.ca
* Jake Corn corn614@gmail.com




