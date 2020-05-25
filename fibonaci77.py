# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:08:59 2020

@author: MOHANA D
"""

#The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) 
#if n>1 Please write a program to compute the value of f(n) with a given n input by console. 

n= int(input("enter n: "))

a=0
b=1
print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
print(c)