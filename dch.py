# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:53:52 2020

@author: MOHANA D
"""

#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. 
#H is 30. D is the variable whose values should be input to your program in a comma-separated sequence.


import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)

