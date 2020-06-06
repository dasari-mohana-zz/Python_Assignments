# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:35:26 2020

@author: MOHANA D
"""
# Write a recursive function to calculate X power Y. X and Y inputs should be read from input. 
#Negative values, zero's need to be checked and error should be thrown in TRY/Except block.

def recursion_func():
    try:
        x=int(input("Enter x (base) value: "))
        y=int(input("Enter y (power) value: "))
        if (x>0 and y>0) or (x<0 and y>0):
            #Here only y (power) value is consider to be only positive intergers
            z=x**y
        print("the result is:",z)
    except:
        print("you can't enter negative integer or zero please enter positive values")
recursion_func()
        
#################################################################################
# or

def frecursion_func():
    try:
        x=int(input("Enter x value: "))
        y=int(input("Enter y value: "))
        if x>0 and y>0:
            #Here both x and y values are consider to be only positive intergers
            z=x**y
        print("the result is:",z)
    except:
        print("you can't enter negative integer or zero please enter positive values") 
recursion_func()