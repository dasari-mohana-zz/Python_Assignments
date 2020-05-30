# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:56:07 2020

@author: MOHANA D
"""

word = input("Input a word to reverse: ")

for x in range(len(word) - 1, -1, -1):
  print(word[x], end="")
