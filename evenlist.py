# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:47:05 2020

@author: MOHANA D
"""

#Write code create a list of even numbers (2 to 20) with list comprehension

list1=list(range(2,20))
x=[i for i in list1 if i%2==0]
print(x)