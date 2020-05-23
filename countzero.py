# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:09:04 2020

@author: MOHANA D
"""


#Write a program to count leading zeros in a binary number.
def countzeros(x): 
      
    # Keep shifting x by one until  
    # leftmost bit does not become 1. 
    total_bits = 32
    res = 0
    while ((x & (1 << (total_bits - 1))) == 0): 
        x = (x << 1) 
        res += 1
    return res 

x =30
print(countzeros(x)) 