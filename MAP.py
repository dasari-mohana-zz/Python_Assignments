# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:24:15 2020

@author: MOHANA D
"""

#write a program to enter marks of five subjects and calculate total,average and percentage
a=float(input("enter english marks:"))
b=float(input("enter physics marks:"))
c=float(input("enter biology marks:"))
d=float(input("enter maths marks:"))
e=float(input("enter social marks:"))
t=a+b+c+d+e
avg=t/5
per=(t/500)*100
print("total:",t,"average",avg,"percentage%:",per)