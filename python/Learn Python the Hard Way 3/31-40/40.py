#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 19:18
# @Author  : ZeQun
# @File    : Modules, Classes, and Objects

mystuff = {'apple': "I AM Apples!"}
print(mystuff['apple'])


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And Now a thousand years between."

    def apple(self):
        print("I am an apple.")




thing = MyStuff()
thing.apple()
print(thing.tangerine)


# 1. Python looks for MyStuff() and sees that it is a class you've defined.
# 2. Python crafts an empty object with all the functions you've specified in the class using def.
# 3. Pthon then looks to see if you made a "magic" __init__ function, and if you have it calls that function
#    to initialize your newly created empty object
# 4. In the MyStuff function __init__ I then get this extra variable self, which is that empty object Python made for
#    me, and I can set variables on it just like you would with a module, dictionary, or other object.
# 5. In this case, I set self.tangerine to a song lyric and then I've initialized this object.
# 6. Now Python can take tis newly minted object and assign it to the thing variable for me to work with.



class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_day = Song(["Happy Birthday to you",
                  "I don't want to get sued.",
                  "So I'll stop right here "])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells."])

happy_day.sing_me_a_song()
bulls_on_parade.sing_me_a_song()