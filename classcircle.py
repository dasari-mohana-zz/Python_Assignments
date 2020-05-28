# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:44:44 2020

@author: MOHANA D
"""

#Define a class named Circle which can be constructed by a radius. 
#The Circle class has a method which can compute the area.

class circle:
    pi=3.14
    def __init__(self,radius):  #no need to mention area
        self.radius=radius
        
    def area(self):
        return(self.pi*(self.radius)**2)
c1=circle(5)
c1.radius
c1.area()

#or

class circle:
    pi=3.14
    def __init__(self,radius):  #no need to mention area
        self.radius=radius
        self.area=self.pi*(self.radius)**2
c1=circle(5)
c1.radius
c1.area