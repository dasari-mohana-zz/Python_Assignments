# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:10:09 2020

@author: MOHANA D
"""

#write a program to check whether year is leap year or not using conditional operator.
y=int(input("enter year :"))
if (y%4==0 or y%100==0 or y%400==0):
    print("{} is leap year".format(y))
else:
    print("{} is not leap year".format(y))
