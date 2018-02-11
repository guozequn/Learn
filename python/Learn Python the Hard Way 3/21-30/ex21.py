#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 17:03
# @Author  : ZeQun
# @File    : ex21.py

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def devide(a, b):
    print(f"DEVIDING {a} / {b}")
    return a / b


print("Let's do some math with just funcitons！")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)




print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("Here is a puzzle.")
what = add(age, substract(height, multiply(weight, devide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand ?")
