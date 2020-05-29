# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:11:54 2020

@author: MOHANA D
"""

#Write a program which can filter even numbers in a list by using filter function. 
#The list is: [1,2,3,4,5,6,7,8,9,10].


list1=[1,2,3,4,5,6,7,8,9,10]
a=lambda x:x%2==0
print(list(filter(a,list1)))