# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:19:58 2020

@author: MOHANA D
"""

#Please write a program to generate all sentences where subject is in ["I", "You"] and 
#verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]. 
#Hints: Use list[index] notation to get a element from a list.

l1=["I", "You"]
l2=["Play", "Love"]
l3=["Hockey","Football"]
s1=l1[0]+" "+l2[0]+' '+l3[0]
s2=l1[1]+' '+l2[1]+' '+l3[1]
print(s1,end=',')
print(s2)

