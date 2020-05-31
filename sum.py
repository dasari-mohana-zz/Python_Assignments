# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:26:58 2020

@author: MOHANA D
"""

#Define a function that can receive two integral numbers in string form and 
#compute their sum and then print it in console.
def Sum (a,b):
	s = int(a) + int(b)
	return s 

num1 = "10"
num2 = "20"

# calculate sum
sum = Sum (num1, num2)

print ("Sum = ", sum)

