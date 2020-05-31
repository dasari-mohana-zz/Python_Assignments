# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:35:54 2020

@author: MOHANA D
"""

#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
#Then the function needs to print the first 5 elements in the list.
def squr():
    l1=list()
    for i in range(1,21):
        l1.append(i**2)
    print(l1)
    print(l1[:5])
squr()

