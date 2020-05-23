# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:24:26 2020

@author: MOHANA D
"""

#write is program to find maximum between three numbers using conditional operator.
a=float(input("enter 'a' number:"))
b=float(input("enter 'b' number:"))
c=float(input("enter 'c' number:"))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")