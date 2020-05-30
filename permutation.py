# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:25:17 2020

@author: MOHANA D
"""

#	Please write a program which prints all permutations of [1,2,3]
from itertools import permutations

permtn= permutations([1,2,3])

for i in permtn:
    print(i)