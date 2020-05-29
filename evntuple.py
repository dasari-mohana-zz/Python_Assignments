# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:53:46 2020

@author: MOHANA D
"""

#	Write a program to generate and print another tuple whose values are 
#even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)


        
a=(1,2,3,4,5,6,7,8,9,10)
b=tuple([i for i in a if i%2==0])
b