# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:56:47 2020

@author: MOHANA D
"""

#Define a class, which have a class parameter and have a same instance parameter.
class emp: 
    def __init__(self): 
        self.name = 'Dasari'
        self.salary = 40000
  
    def show(self): 
        print(self.name) 
        print(self.salary) 
  
e1 = emp() 
print("Dictionary form :", vars(e1)) 
print(dir(e1)) 