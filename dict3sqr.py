# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:35:50 2020

@author: MOHANA D
"""

#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

def squr2(x):
    x={num:num*num for num in range(1,4)}
    return x
print(squr2(x))