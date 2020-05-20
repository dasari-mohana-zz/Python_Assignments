# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:59:07 2020

@author: MOHANA D
"""

#Take input as student marks (0,100) and return if the student is distinction
# or first class or second class or third class or fail (Marks>70 distinction,
# 70>marks>60 first class, 60>marks>50 second class, 50>marks>40 third class, marks<40 fail.


marks=int(input("Enter marks="))

if marks>70:
    print("Distinction")
elif 70>=marks>60:
    print("First class")
elif 60>=marks>50:
    print("second class")
elif 50>=marks>=40:
    print("third class")
elif marks<40:
    print("Fail")