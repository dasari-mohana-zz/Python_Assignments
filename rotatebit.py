# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:14:07 2020

@author: MOHANA D
"""

#Write a program to rotate bits of a given number.
INT_BITS = 32 
# Function to left 
def leftRotate(n, d): 
    return (n << d)|(n >> (INT_BITS - d)) 
  
# Function to right 
def rightRotate(n, d): 
    return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF
  
n = 23
d = 2

print('left rotate:',leftRotate(n, d)) 

print('right rotate:',rightRotate(n, d)) 