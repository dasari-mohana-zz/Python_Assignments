# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:42:38 2020

@author: MOHANA D
"""

#Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
    if j%2==0:
  
        return res 
num = 5
start = 100
end = 200
print(Rand(start, end, num))
