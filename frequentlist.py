# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:50:13 2020

@author: MOHANA D
"""

#	write a program to find the 2nd most frequently occurring number in a given list. Read list from input

def most_frequent(List): 
    return max(set(List), key = List.count) 
  
List = [2, 1, 2, 2, 1, 3] 
print(most_frequent(List))