#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/14 22:41
# @Author  : ZeQun
# @File    : Dictionaries, Oh Lovely Dictionaries

# create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Califonia': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# create a basic set of states and some cities in tem

cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the statethen cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

# no do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist') # dict.get(key, "if None: output")
print(f"The city for the state 'Tx' is {city}")
