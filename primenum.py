# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:20:11 2020

@author: MOHANA D
"""

#print all the prime numbers between input1(say 100) and input2(say 200)

prime_nums=[]

for i in range(100,200):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime_nums.append(i)
        
print(prime_nums)