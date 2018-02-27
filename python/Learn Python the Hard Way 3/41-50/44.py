#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 21:00
# @Author  : ZeQun
# @File    : inheritance versus composition
from sys import  exit
"""
in the fairy tale about heroes defeating evil villains there's always a dark forest of somke kind
Of course, shortly after the villain is introduced you find out
you rarely read fairy tales about the heros who are smart enough to just avoid the whole situation entirely 
you never hear a hero say, 
wait a minute, if i leave to make my fortunes ont the high seas, leaving buttercup behind, 
I could die and then she'd have to marry some ugly prince named humperdink。 Humperdink！ 
I think i'll stay here and start a Farm Boy for rent bussiness."
If he did that there'd be no fire swamp ,dying ,reanimation, sword fight ,giants,
or any kind of story really Because of this , 
the forest in these stories seems to exist like a black hole that drags the hero in no matter what they do.
"""

"""
What is Inheritance?

Inheritance is used to indicate that one class will get most or all of its features from a parent class.
This happens implicitly whenever you write class Foo(Bar), which says "Make a class Foo that inherits from Bar."
When you do this,  the language makes any action that you do on instances of Foo also work as if they were done to an 
instance of Bar . Doing this lets you put common functionality in the Bar class, then specialize that functionality in 
the Foo class as needed.

When you  are doing this kind of specialization, there are three ways that the parent and child classes can interact:
1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.
I will now demonstrate each of these in order and show you code for them.

"""
'Implicit Inheritance'
class Parent