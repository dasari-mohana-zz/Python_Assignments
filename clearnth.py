# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:08:00 2020

@author: MOHANA D
"""

#Write a program to clear nth bit of a number.
def clear(n, k): 
    return (n &(~(1 << (k-1))))
      
# Driver code 
n = 7
k = 2
print(clear(n , k)) 