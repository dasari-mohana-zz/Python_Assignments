# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:14:13 2020

@author: MOHANA D
"""

fact=1
n=int(input("enter n :"))

for i in range(1,n+1):
    fact=fact*i
print("factorial of {} is: ".format(n),fact)