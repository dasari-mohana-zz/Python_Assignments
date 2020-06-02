# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:25:59 2020

@author: MOHANA D
"""

#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
n= int(input("enter n : "))
 
f=0

if n>0:
    for i in range(1,n+1):
        f= f + (i/(i+1))
    print(round(f,2))   # upto 2 decimal points
else:
    print(" enter n value greater than 0")