# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:32:43 2020

@author: MOHANA D
"""

#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
#write a program to make a list whose elements are intersection of the above given lists

def intersect(a,b):
    c=[i for i in a if i in b]
    print(c)
a=[1,3,6,78,35,55] 
b=[12,24,35,24,88,120,155]
intersect(a,b)

#or


def Intersect(a,b): 
    return set(a).intersection(b)
a=[1,3,6,78,35,55] 
b=[12,24,35,24,88,120,155]
list(Intersect(a,b))