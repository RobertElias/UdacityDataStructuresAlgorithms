#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:49:11 2021

@author: robertelias
"""

# Dictionaries
# A dictionary is a mutable data type that stores mappings of unique keys to values. 
# Here's a dictionary that stores elements and their atomic numbers.

# A dictionary is a mutable, unordered data structure that contains mappings of keys to values. 
# Because these keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as 
# the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"])
elements["lithium"] = 3

print("carbon" in elements)
print(elements.get("dilithium"))


n = elements.get("dilithium")
print(n is None)
print(n is not None)



population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

header = "key"

print(header.center(15,' ') + '|   ' + 'Value')

for x in population:
    print(x.center(15, ' ') + '|   ' + str(population[x]) )
    


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)


animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals[3])


room_numbers = {
    'Freddie', 'Jen': [403],
    'Ned', 'Keith': [391],
    'Kristin', 'Jazzmyne': [411],
    'Eugene', 'Zach': [395]
}

print(room_numbers)