# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:21:33 2020

@author: MOHANA D
"""

#Write a program which can map() to make a list whose elements are square of numbers between 1 and 20
def square(x):
        return x*x

numbers = range(1,21)
squares = map(square, numbers)
print(list(squares))

#or


numbers=range(1,21)
squares = map(lambda x:x*x,numbers)
print(list(squares))
