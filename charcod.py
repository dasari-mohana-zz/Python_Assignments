# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:05:15 2020

@author: MOHANA D
"""


#Write a program to check whether character is an alphabet or not using conditional operator.
ch = input("Please Enter Your Own Character : ")
# isalpha() is built in function to check a character
if(ch.isalpha()):
    print("Given Character ", ch, "is an Alphabet")
else:
    print("Given Character ", ch, "is not an Alphabet")