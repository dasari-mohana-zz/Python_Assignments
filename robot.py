# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:42:02 2020

@author: MOHANA D
"""
#A robot moves in a plane starting from the original point (0,0). 
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
#The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 
#if The numbers after the direction are steps. Please write a program to compute the 
#distance from current position after a sequence of movement and original point. 
#If the distance is a float, then just print the nearest integer

import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if not step:
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)

