# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:13:41 2020

@author: MOHANA D
"""

#Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

a=[5,6,77,45,22,12,24]
for i in list(a):
    if i%2==0:
        a.remove(i)
print(a)
        