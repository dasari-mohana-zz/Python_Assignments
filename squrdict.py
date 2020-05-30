# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:38:59 2020

@author: MOHANA D
"""
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 

num1=int(input("enter n value:"))
x={num1:num1*num1 for num1 in range(1,num1)}
print(x)