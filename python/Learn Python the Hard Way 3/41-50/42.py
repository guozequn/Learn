#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/20 21:50
# @Author  : ZeQun
# @File    : Is-A, Has-A, Objects, and Classes


## Animal is-a object (yes, sort of confusing) look at te e

class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None


## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm wat is this strange magic?
        super(Employee, self).__init__(name):
        ## ??
        self.salary = salary


## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank",120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()


"""
What does super(Employee, self).__init__(name) do ?

That's how you can run the __init__ method of a parent class reliably . 
Search for "python3.6 super" and read the various advice on it being evil and good for you 

可靠的运行父类的方法。
"""