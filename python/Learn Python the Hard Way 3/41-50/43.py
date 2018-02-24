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

    Text_begining = """
    The Gothons of Planet Percal #25 have invaded destroyed your entire crew.
    You are the last survive member and your last mission is to get the neutron 
    bomb from the Weapons Armory. put it in the bridge blow the ship up after getting ]
    into an escape pod.
    
    You're running down the central corridor to the Armory when a Gothon jumps out, red scaly
    skin and teeth, and evil clown costume flowing around highly filled body. He's blocking the
    door to the Armory about to pull a weapon to blast you.
    """

    Text_shoot = """
    Quick on the draw you yank out your blaster it at the Gothon. His clown costume is flow moving 
    around his body, which throws off you. Your laser hits his costume but misses him.
    This completely ruins his brand niw costum bought him, which makes him fly into an indeed and 
    blast you repeatly in the face until dead. then he eats you.
    """

    Text_dodge = """
    Like a world class boxer you dodge, weave, slide right as the Gothon's blaster cranks past your head.
    In the middle of your artfully past your head on wall and pass out. You wake up shortly after 
    die as the Gothon stomps on your head and Leg.
    """

    Text_joke = """
    Lucky for you they made you learn Gothon i n the academy. You tell the one Gothon joke 
    Lbhe zbgure vf fb sbg, jura fur fvgf nebgh fvgf nebgaq . The Gothon stop  not to laugh, 
    then busts out laughing and While he's laughing you run up and shoot his head putting him down,
    then jump through Weapon Armory door.
    """


    def enter(self):
        print(dedent(self.Text_begining))

    action = input("> ")

    if action == "shoot!":
        print(dedent(Text_shoot))
        return 'death'
    elif action == "dodge!":
        print(dedent(Text_dodge))
        return 'death'
    elif action == "tell a joke!":
        print(dedent(Text_joke))
        return 'laser_weapon_armory'
    else:
        print("DOES NOT COMPLETE!")
        return 'central_corridor'


class LaserWeaponArmory(Scence):

    Text_enter = """
    You do a dive roll into the Weapon Armory, critical
    the room for the more Gothons that might be hiding quiet,
    too quiet. You stand up and run to the room and find the neutron
    bomb in its constant There's a keypad lock on the box and you need the lock closes 
    forever and you can't get the code is 3 digits 
    """
    Text_bingo = """
    The container clicks open and the seal bridge and blown the gas out.
    You grab the neutron bomb and run as fast as you can to the bridge where
    you must place right spot.
    """
    Text_death = """
    The lock buzzes one last time and then you sickening melting sound as the mechanism together
    You decide to sit there, and fight the Gothons blow up the ship from their ship.
    """
    def enter(self):
        print(dedent(self.Text_enter))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print(f"BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent(self.Text_bingo))
            return 'the_bridge'

        else:
            print(dedent(self.Text_death))
            return 'death'


class TheBridge(Scence):

    Text_enter = """
    You burst onto the bridge with the neutron des under your arm and surprise 5 Gothons who are 
    take control of the ship. Each of them has an clown costume than the ship. Each of them has an 
    clown costume than the last. They haven't pull weapons out yet, as they see the active bomb 
    arm and don't want to set if off.
    """
    Text_throw = """
    In a panic you throw the bomb at the groud and make a leap for the door. Right as you Gothon shoots
    you right in the back killing you die you see another Gothon frantically disarm the bomb. You die knowing
    they will blow up when it goes off.
    """
    Text_place = """
    You point your blaster at the bomb under the Gothons put their hands up and start You inch backward to the door 
    open it a carefully place the bomb on the floor, post blaster at it . You then jump back through and punch 
    the close button and blast the lock Gothons can't get out. Now that the bomb will explode after you run 
    to the escape pod to get off this.
    """

    def enter(self):
        print(dedent(self.Text_enter))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent(self.Text_throw))
        elif action == "slowly place the bomb":
            print(dedent(self.Text_place))
        else:
            print('DOES NOT COMPUTE!')
            return "the_bridge"



class EscapePod(Scence):

    good_pod = randint(1,5)
    Text_enter = """
    You rush through the ship desperately trying the escape pod before the whole ship explodes
    like hardly any Gothons are on the ship, so you clear of interference. You get to the chamber
    escape pods, and now need to pick one to take them cold be damaged but you don't have time 
    There's 5 pods witch one do you take ?
    """

    def enter(self):
        guess = input("[pod]> ")
        Text_wrong = f"""
        You jump into pod {guess} and hit the eject button. The pod escapes out into the void of space implodes
        as the hull reptures, crushing yet jam jelly .
        """
        Text_right = f"""
        You jump into pod {guess} and hit the eject button. The pod easily slides out into the space head to the
        planet blow. As it files to the planet, back and see your ship implode then explore bright star, taking out 
        the Gothon ship at the same time. You Win!
        """
        if guess != self.good_pod:
            print(dedent(Text_wrong))
            return 'death'
        else:
            print(dedent(Text_right))
            return 'finished'


class Finished(Scence):

    def enter(self):
        print("You won! Good job!")
        return 'finished'




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
