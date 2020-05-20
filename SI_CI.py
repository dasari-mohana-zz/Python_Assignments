# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:23:04 2020

@author: MOHANA D
"""

#write a program to P,T,R and calculate simple interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
SI=(p*t*r)/100 #simple interest=(P*T*R)/100
print("simple interest:",SI)

#write a program to P,T,R and calculate compound interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
CI=p*(1+r/100)**t #compound interest=P(1+1/r)^t
print("compound interest:",CI)