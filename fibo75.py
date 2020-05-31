# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:48:25 2020

@author: MOHANA D
"""

#The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0 f(n)
#=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1 Please write a program using list comprehension 
#to print the Fibonacci Sequence in comma separated form with a given n input by console

def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for i in fib():
    if i>100:
        break
    print(i)
    
