# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:21:13 2020

@author: MOHANA D
"""

#Write a program which accepts a sequence of comma-separated numbers from console 
#and generate a list and a tuple which contains every number. 

x=input("enter values: ")
l1=x.split(',')
print(list(l1))
print(tuple(l1))