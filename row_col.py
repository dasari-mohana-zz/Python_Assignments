# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:57:14 2020

@author: MOHANA D
"""

#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
#The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1.
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)