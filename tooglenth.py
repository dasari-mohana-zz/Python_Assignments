# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:35:10 2020

@author: MOHANA D
"""
#Write a program to toggle nth bit of a number.
def toggle(n, k): 
    return (n ^ (1 << (k-1))) 
      
# Driver code 
n = 7
k = 2
print( toggle(n , k)) 