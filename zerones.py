# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:28:28 2020

@author: MOHANA D
"""


#Write a program to count total zeros and ones in a binary number.


def countones(num): 
     binary = bin(num) 
     setBits = [ones for ones in binary[2:] if ones=='1'] 
       
     print (len(setBits))
     
def countzeros(num): 
     binary = bin(num) 
     setBits = [zeros for zeros in binary[2:] if zeros=='0'] 
       
     print (len(setBits))


num = 18
countones(num)
countzeros(num)
    
    