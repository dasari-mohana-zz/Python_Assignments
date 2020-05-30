# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:31:43 2020

@author: MOHANA D
"""
#Write a program that accepts a sentence and calculate the number of letters and digits.
txt= input("enter a sentence: ")
print(txt)
  
letters=0
digits=0

for i in txt:
    if i.isalpha() == True:
        letters+=1
    elif i.isdigit() == True: 
        digits+=1
    else:
        pass

print("letters ", letters)
print("digits ", digits)