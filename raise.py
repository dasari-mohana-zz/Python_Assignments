# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:02:27 2020

@author: MOHANA D
"""

#Please raise a RuntimeError exception. Hints: Use raise() to raise an exception.
x=float(input("Enter x value:"))
if x < 0:
  raise Exception("Sorry, no numbers below zero")
else:
    print(x+2)