# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:17:38 2020

@author: MOHANA D
"""


#Please write a program to print the running time of execution of "1+1" for 100 times.
import time
def func():
    for i in range(100):
        i='1+1'
        
start_time = time.process_time()
func()
print (time.process_time() - start_time, "seconds")
