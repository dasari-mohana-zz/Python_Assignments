# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:27:48 2020

@author: MOHANA D
"""

#Assuming that we have some email addresses in the "username@companyname.com" format, 
#please write program to print the company name of a given email address. 
#Both user names and company names are composed of letters only.

email=input("enter the email address:")
user_name=email[:email.index('@')]
print("the username is:",user_name)