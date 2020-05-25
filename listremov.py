# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:44:30 2020

@author: MOHANA D
"""

#By using list comprehension, please write a program to print the list after removing 
#the 0th,4th,5th numbers in [12,24,35,70,88,120,155]. Hints: Use list comprehension to
#delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

l1=[12,24,35,70,88,120,155]
print(l1)

l2= [ enum for x, enum in enumerate(l1) if x not in [0,4,5]]  # method 1
print(l2)

l3=[x for x in l1 if x not in [12, 88, 120]]  # method 2
print(l3)