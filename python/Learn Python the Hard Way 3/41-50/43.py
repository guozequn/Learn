#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/21 22:13
# @Author  : ZeQun
# @File    : 43.py


# 1. Write or draw about the problem

# 2. Extract key concepts from 1 and research them

# 3. Create a class hierarchy and object map for the concepts.

# 4. Code the classes and a test to run them.

# 5. Repeat and refine

import sys
from sys import exit
from random import randint
from textwrap import dedent

"""
I'm going to write a little paragraph for the game:
    
    "Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can
    be escape into an escape pod to hte planet below. The game will be more like a Zork or Adventure type game with 
    text outputs and funny way to die. The game will involve  an engine that runs a map full of rooms or scenes.
    Each room will print its own description when the player enters it and then tell the engine what room to run next 
    out of the map."
    
At this point I have a good idea for the game and how it would run, so now I want to describe each scene:

Death               This is when the player dies and should be something funny.

Central Corridor    THis is the starting point and has a Gothon already standing there that the players have to defeat
                    with a joke before continuing.

Laser Weapon Armory This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod.
                    It has a keypad the hero has to guess the number for.
                    
The Bridge          Another battle scene with a Gothon where the hero places the bomb. 

Escape Pod          Where the hero escapes but only after guessing the right escape pod


"""


class Scence(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene.
        current_scene.enter()


class Death(Scence):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
       ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scence):

    def enter(self):
        pass


class LaserWeaponArmory(Scence):
    def enter(self):
        pass


class EscapePod(Scence):
    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scence):
        pass



    def next_scene(self):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
