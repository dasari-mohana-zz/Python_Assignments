# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:40:22 2020

@author: MOHANA D
"""

#Define a class with a generator which can iterate the numbers,
#which are divisible by 7, between a given range 0 and n

def func():
    n = int(input("enter n value:"))
    divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
    yield(divBy7)
for x in func():
    print(x)
func()


