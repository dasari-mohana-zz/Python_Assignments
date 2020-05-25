# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:16:58 2020

@author: MOHANA D
"""


#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
def printvalues():
    l1=list()
    for i in range(1,21):
        l1.append(i**2)
    print(l1[5:])
		
printvalues()


