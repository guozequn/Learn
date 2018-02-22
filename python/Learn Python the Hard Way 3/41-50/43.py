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
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass


    def play(self):
        pass


class