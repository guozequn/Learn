#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/18 20:22
# @Author  : ZeQun
# @File    : Learning to Speak Object-Oriented

# I'm going to give you a large set of exercises that you have
# to complete to make these sentences solid in you vocabulary.


# class     Tell Python to make a new type of thing.

# object    Two meanings: the most basic type of thing, and any instance of something

# instance  What you get when you tell Python to create a class

# def       How you define a function inside a class

# self      Inside the functions in a class, self is a variable ofr the instance/object being accessed.

# inheritance   The concept that a class can inherit trait from another class, much like you and your parents.

# composition   The concept that a class can be composed of other classes as parts, much like how a car has wheels.

# attribute     A property classes have that are from composition and are usually variables.

# is-a      A phrase to say that something inherits from another, as in a "salmon" is a "fish".


"""
Phrase Drills
"""
# class X(Y)    "Make a class named X that is-a Y."

# class X(object): def __init__(self,J) "class X has-a __init__ that takes self and J parameters."

# class X(object): def M(self, J) " class X has-a function named M that takes self and J parameters."

# foo = X() "Set foo to an instance of class X"

# foo.M(j) " from foo, get M function, and call it with parameters self, J"

# foo.K = Q "from foo ,get K attribute, and set it to Q "

"""
In each of these, where you see X, Y, M, J, K, Q, and foo, you can treat those like blank spots.


"""

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%."
}

