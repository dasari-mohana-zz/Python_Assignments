# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:35:47 2020

@author: MOHANA D
"""

#Write a program that accepts a comma separated sequence of words as input 
#and prints the words in a comma-separated sequence after sorting them alphabetically.
items = input("Input comma separated sequence of words:")
words = [word for word in items.split(",")]
print((sorted(list(set(words)))))