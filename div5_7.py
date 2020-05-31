# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:48:17 2020

@author: MOHANA D
"""
#By using list comprehension, please write a program to print the list after removing
#delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
l1=[12,24,35,70,88,120,155]
print(l1)

l2= [ x for x in l1 if x%5==0 and x%7==0]
print(l2)

l3=[ k for k in l1 if k not in l2]
print(l3)