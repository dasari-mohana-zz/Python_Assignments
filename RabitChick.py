# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:55:50 2020

@author: MOHANA D
"""

#Write a program to solve a classic ancient Chinese puzzle
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have?
def solve(numheads,numlegs):

    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if (2*i)+(4*j)==numlegs:
            return i,j
    return ns,ns


numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)

#or

heads = 35
legs = 94
if legs % 2 !=0 or heads ==0 or heads > legs:
    print('No solution')
else:
    r = int((legs + (-2*heads))/2)   #r = (legs - 2heads)/2
    c = int(heads - r)
    print('rabbits -{},chikhens-{}'.format(c,r))