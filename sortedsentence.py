# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:02:06 2020

@author: MOHANA D
"""

#Write a program that accepts a sequence of whitespace separated words as input and prints
#the words after removing all duplicate words and sorting them alphanumerically. 
#Suppose the following input is supplied to the program

words= input("enter words : ").split(' ')
print(words)
print(' '.join(sorted(set(words))))