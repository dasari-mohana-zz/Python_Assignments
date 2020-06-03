# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:12:02 2020

@author: MOHANA D
"""

#Please write a program to randomly generate a list with 5 numbers, 
#which are divisible by 5 and 7 , between 1 and 1000 inclusive


import random
l1 = [i for i in range(1,1001) if i%5 == 0 and i%7==0]
l2 = random.sample(l1,5)
print("Random numbers:",l2)