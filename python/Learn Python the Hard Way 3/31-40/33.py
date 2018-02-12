#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 22:03
# @Author  : ZeQun
# @File    : While Loops

i = 0
numbers = []


while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now：", numbers)
    print(f"At the bottom is is {i}")

print("The numbers: ")
for num in numbers:
    print(num)



