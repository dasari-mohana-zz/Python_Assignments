# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:27:25 2020

@author: MOHANA D
"""

#A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password: 1. At least 1 letter between [a-z] 2. At least 1 number between [0-9] 1. At least 1 letter between [A-Z] 3. At least 1 character from [$#@] 4. Minimum length of transaction password: 6 5. Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
#Passwords that match the criteria are to be printed, each separated by a comma. 
import re
p= input("Enter your password : ")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password, Please try again")