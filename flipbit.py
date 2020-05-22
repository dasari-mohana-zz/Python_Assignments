# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:23:23 2020

@author: MOHANA D
"""

#Write a program to flip bits of a binary number using bitwise operator.
import math 
  
def flipbits(num):  
    
    x = int(math.log2(num)) + 1
  
    # Inverting the bits one by one  
    for i in range(x):  
        num = (num ^ (1 << i))  
      
    print(num)  
  
num = 5
flipbits(num) 