# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:27:09 2020

@author: MOHANA D
"""


#Write a program to check whether a number is even or odd using bitwise operator.
num=int(input("Enter a number:"))
if((num&1)==0):
    print("{} is Even".format(num))
else:
    print("{} is Odd".format(num))