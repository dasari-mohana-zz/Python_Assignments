# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:56:33 2020

@author: MOHANA D
"""


#Write a program to count trailing zeros in a binary number.
def trailingzero(x): 
    count = 0
    while ((x & 1) == 0): 
        x = x >> 1
        count += 1
      
    return count 
print(trailingzero(18))