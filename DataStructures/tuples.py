#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:35:33 2021

@author: robertelias
"""

# Tuples
# A tuple is another useful container. It's a data type for immutable ordered 
# sequences of elements. They are often used to store related pieces of information. 
# Consider this example involving latitude and longitude:
    
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])


print("-----------------------------")


# dimensions = 52, 40, 100
# length, width, height = dimensions
# print("The dimensions are {} x {} x {}".format(length, width, height))


length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
print("-----------------------------")

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])