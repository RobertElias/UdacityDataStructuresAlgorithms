#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:58:55 2021

@author: robertelias

Data Structures: Lists
"""

#

greeting = "Hello There"
print(greeting.replace("H", "M"))


month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month - 1]

#[1:8]
print(num_days)



#Quiz: Slicing Lists
#Select the three most recent dates from this list using list slicing notation.
# Hint: negative indexes work in slices!
#####
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])



#
#
#


cubes = [x**3 for x in range(1,6)]
print(cubes)