# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:49:44 2020

@author: MOHANA D
"""

#Write a function to compute 5/0 and use try/except to catch the exceptions.
try:
    a=5
    b=0
    print(a/b)
except:
    print("you cannot divide with zero")