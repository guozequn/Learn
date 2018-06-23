#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 22:21
# @Author  : ZeQun
# @File    : Implicit Inheritance

class Parent(object):

    def implicit(self):
        print("Parent implicit")

class Child(Parent):

    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()


