# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:41:16 2020

@author: MOHANA D
"""

#Use a list comprehension to square each odd number in a list. 
#The list is input by a sequence of comma-separated numbers
num=input("Enter numbers:")

b=[i for i in num.split(',') if (int(i)%2!=0)]
print((",").join(b))

