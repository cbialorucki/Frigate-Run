# Frigate Run
Escape a collapsing Halo™ ring. You have a Frigate at your disposal as you have to pass enemies, barriers, and more to ensure your safety and finish the fight.

## Game features
* Control the speed of your Frigate as you avoid obstacles.
* Escape the quickly deteriorating map before it's too late. 
* Players can fly; but there is no time to shoot.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- warthog-run         (source code for game)
  +-- game              (specific game classes)
    +-- collision.py    (base collision class that gets inherited by all objects with collision)
    +-- maingame.py     (directs game play and interprets map files)
    +-- warthog.py      (warthog vehicle object)
    +-- player.py       (represents the player)
    +-- enemy.py        (gets inherited by all enemy objects)
    +-- jackal.py       (a jackal enemy)
    +-- elite.py        (an elite enemy)
    +-- brute.py        (a brute enemy)
    +-- grunt.py        (a grunt enemy)
    +-- health.py       (base health class that gets inherited by all objects with health i.e. enemies and the player)
    +-- obstacle.py     (a scenic obstacle class)
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




