# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:21:49 2020

@author: MOHANA D
"""

#Please write a program to output a random number, which is divisible by 5 and 7, 
#between 0 and 10 inclusive using random module and list comprehension.

import random
num=list(i for i in range(0,11) if i%5==0 & i%7==0)
print(num)
print(random.choice(num))

