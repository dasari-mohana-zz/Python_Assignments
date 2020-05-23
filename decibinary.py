# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:16:22 2020

@author: MOHANA D
"""

#Write a program to convert decimal to binary number system using bitwise operator.
def decToBinary(n): 
    # Size of an integer is assumed to be 32 bits 
    for i in range(31, -1, -1):  
        k = n >> i
        if (k & 1): 
            print("1", end = "")
        else: 
            print("0", end = "")

n = 32
decToBinary(n)

