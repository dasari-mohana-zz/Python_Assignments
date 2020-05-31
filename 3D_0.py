# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:30:00 2020

@author: MOHANA D
"""
#By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
array = [[ ['0' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)