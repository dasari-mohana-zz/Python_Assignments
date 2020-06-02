# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:45:11 2020

@author: MOHANA D
"""

#Write a program which can map() and filter() to make a list whose elements are square of even number in 
l1=[1,2,3,4,5,6,7,8,9,10]
evn=list(map(lambda x:x**2,filter(lambda x:x%2==0,l1)))
evn