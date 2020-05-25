# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:26:08 2020

@author: MOHANA D
"""

#find the LCM of any number

a=int(input("enter first number:"))
b=int(input("enter second number:"))
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        lcm= i*(a/i)*(b/i)
    
    i+=1
    
print(lcm)