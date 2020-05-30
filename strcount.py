# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:02:59 2020

@author: MOHANA D
"""
#Please write a program which count and print the numbers of each character in a 
#string input by console.
string=input("Enter the string : ")
newstr=list(string)
newlist=[]
for j in newstr:
    if j not in newlist:
        newlist.append(j)
        count=0
        for i in range(len(newstr)):
            if j==newstr[i]:
                count+=1

        print("{},{}".format(j,count))