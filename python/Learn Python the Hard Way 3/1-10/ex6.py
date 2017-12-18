#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 11:28
# @Author  : ZeQun
# @File    : Exercise 6: Strings and Text

types_of_people = 10
x = f"There are {types_of_people} types of people."


binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."


print(x)
print(y)


hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"


print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

# Extension with .format()

joke_1 = "ZeQun"
joke_2 = "Zejones"


statement = "{}'s English name is {}."
print(statement.format(joke_1, joke_2))
