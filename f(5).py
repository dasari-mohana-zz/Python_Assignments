# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:39:06 2020

@author: MOHANA D
"""

#Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0)
def fun(n):
    if n==0:
        return 0
    elif n>0:
        return fun(n-1) +100
    else:
        pass
fun(5)