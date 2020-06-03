# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:12:13 2020

@author: MOHANA D
"""

#Please write a program using generator to print the numbers which can be divisible by 5 
#and 7 between 0 and n in comma separated form while n is input by console.


n=int(input("enter n number: "))
ll=[]
for x in range(0,n):
    if (x%7==0) and (x%5==0):
        ll.append(str(x))
print (','.join(ll))
