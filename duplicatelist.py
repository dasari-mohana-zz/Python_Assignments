# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:14:22 2020

@author: MOHANA D
"""


#With a given list [12,24,35,24,88,120,155,88,120,155], 
#write a program to print this list after removing all duplicate values with original order reserved.

list1 = [12,24,35,24,88,120,155,88,120,155]
org=[]
for i in list1:
    if i not in org:
        org.append(i)
print(list(org))

#or

list1 = [12,24,35,24,88,120,155,88,120,155]
print(list(set(list1))) 