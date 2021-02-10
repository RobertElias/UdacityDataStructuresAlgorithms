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


VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']

print(VINIX[0])


print(VINIX[12])

print('GE' in VINIX)
print('GOOGL' in VINIX)
print("------------------------------------------")

# List Methods 

# print("scores:" + str(scores))
# print("grades: " + str(grades))

# Useful Functions for Lists I
# len() returns how many elements are in a list.
# max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
# min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
# sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.


# Useful Functions for Lists II
# join method
# Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
print("------------------------------------------")

name = "-".join(["Garcia", "O'Kelly"])
print(name)

print("------------------------------------------")


letters = ['a','b','c', 'd']
letters.append('z')
print(letters)


print("----------------")

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

print("---------------------")
#sorted join
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


#append list
print("--------------------------------")

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
print("----------------")

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


print(arr[2:6])
print(arr[:3])
print(arr[4:])
# print(arr[4:6])

