# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:03:16 2020

@author: MOHANA D
"""
#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
words= input("enter words : ").split(' ')

for i in words:
    if i.isdigit()==True :
        print(i, end= ', ')