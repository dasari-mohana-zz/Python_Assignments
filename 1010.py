# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:48:34 2020

@author: MOHANA D
"""


#The numbers that are divisible by 5 are to be printed in a comma separated sequence.1010
items = []
num = [x for x in input('give 4 digit intergers:').split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))
