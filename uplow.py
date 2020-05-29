# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:20:11 2020

@author: MOHANA D
"""

#Write a program that accepts a sentence and calculate the number of upper case 
#letters and lower case letters

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for x in s:
        if x.isupper():
           d["UPPER_CASE"]+=1
        elif x.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('Dasari Mohan Krishna')