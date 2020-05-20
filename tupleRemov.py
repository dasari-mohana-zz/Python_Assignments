# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:39:41 2020

@author: MOHANA D
"""

#Create a tuple (1,2,3,4,5,6), then remove element 5 from it.
a=(1,2,3,4,5,6)
b=list(a) #convert tuple to list
b.remove(5)
#del b[4]
b
c=tuple(b)
c