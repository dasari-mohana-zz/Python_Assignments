# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:03:56 2020

@author: MOHANA D
"""

#Define a function which can generate and print a tuple where the value are 
#square of numbers between 1 and 20 (both included)


def squr():
    sqr=list()
    for i in range(1,21):
        sqr.append(i**2)
    print(tuple(sqr))
squr()
        