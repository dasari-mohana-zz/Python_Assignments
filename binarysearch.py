# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:56:15 2020

@author: MOHANA D
"""
#Please write a binary search function which searches an item in a sorted list. 
#The function should return the index of element to be searched in the list.
from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
  
a  = [1, 2, 4, 4, 8] 
x = int(2) 
res = BinarySearch(a, x) 
if res == -1: 
    print(x, "is absent") 
else: 
    print("First occurrence of", x, "is present at", res) 