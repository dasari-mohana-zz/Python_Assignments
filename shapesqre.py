# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:19:30 2020

@author: MOHANA D
"""

#Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        pass



class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        a = (self.length * self.length)
        print('The area of a sqre with  side length of %f is %f' % (self.length, a))


s = Square(4)
s.area()