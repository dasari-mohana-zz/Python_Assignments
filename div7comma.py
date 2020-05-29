# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:03:58 2020

@author: MOHANA D
"""

#Write a program which will find all such numbers which are divisible by 7 
#but are not a multiple of 5,between 2000 and 3200 (both included). 

a=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        a.append(str(i))

print(",".join(a))