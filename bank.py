# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:13:01 2020

@author: MOHANA D
"""

#	Write a program that computes the net amount of a bank account based a transaction 
#log from console input. The transaction log format is shown as following: 
#D 100 W 200 D means deposit while W means withdrawal

total = 0
while True:
    d_w_trans = input("Enter deposit and withdrawal amount:")
    if d_w_trans == "":
        break
    else:
        d_w_trans = d_w_trans.split(" ")
        if d_w_trans[0] == "D":
            total = total + int(d_w_trans[1])
        elif d_w_trans[0] == "W":
            total = total - int(d_w_trans[1])

print(total)