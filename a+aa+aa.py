# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:54:17 2020

@author: MOHANA D
"""


#write a program that computes the values of a+aa+aaa+aaaa with a given digit as value of a.
a = input("Enter value: ")

n1 = a * 1
n2 = a * 2
n3 = a * 3
n4 = a * 4

total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)


