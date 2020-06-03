# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:53:19 2020

@author: MOHANA D
"""

#Please write a program to generate a list with 5 random numbers between 100 & 200 inclusive.

import random
l1=[]
n=5
for i in range(5):
    l1.append(random.randint(100,201))
print("Random numbers are : ",l1)