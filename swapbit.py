# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:47:25 2020

@author: MOHANA D
"""
#Write a program to swap two numbers using bitwise operator.
x = 10 #(1010)
y = 5  #(0101)
#two numbers x & y returns a number which has all bits as 1 wherever bits of x & y differ.
# Code to swap 'x' and 'y' 
x = x ^ y; # x now becomes 15 (1111) 
y = x ^ y; # y becomes 10 (1010) 
x = x ^ y; # x becomes 5 (0101) 
  
print ("After Swapping: x = ", x, " y =", y)