# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:03:07 2020

@author: MOHANA D
"""

#Please write a program using generator to print the even numbers between 0 and n in 
#comma separated form while n is input by console.

n=int(input("Enter n value:"))
for i in range(n):
    if i%2==0:
         print(i,end=",")
