#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 15:45
# @Author  : ZeQun
# @File    : Printing, Priting

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one","two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try Your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

