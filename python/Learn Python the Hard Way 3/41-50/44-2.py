#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 22:34
# @Author  : ZeQun
# @File    : Override explicitly

class Parent(object):

    def override(self):
        print("Parent override()")


class Child(Parent):

    def override(self):
        print("Child override()")


dad = Parent()
son = Child()

dad.override()
son.override()