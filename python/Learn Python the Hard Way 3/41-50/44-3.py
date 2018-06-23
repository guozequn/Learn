#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 22:37
# @Author  : ZeQun
# @File    : Alter Before or After

class Parent(object):

    def altered(self):
        print("Parent altered()")


class Child(Parent):

    def altered(self):
        print("Child, Before Parent altered()")
        super(Child,self).altered()
        print("Child, After Parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
dad.altered()