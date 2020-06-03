# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:49:25 2020

@author: MOHANA D
"""

#Write a program which accepts a string as input to print "Yes" if the string is "yes" 
#or "YES" or "Yes", otherwise print "No".


x=str(input("Enter charecterrs: "))
if x=="yes":
    print("Yes")
elif x=="Yes":
    print("Yes")
elif x=="YES":
    print("Yes")    

else:
    print("No")