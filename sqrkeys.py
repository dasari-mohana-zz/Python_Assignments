# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:05:18 2020

@author: MOHANA D
"""

#Define a function which can generate a dictionary where the keys are numbers
#between 1 and 20 (both included) and the values are square of keys.
#The function should print all key/value combinations.

sqr_dict={num:num*num for num in range(1,21)}
print(sqr_dict)

