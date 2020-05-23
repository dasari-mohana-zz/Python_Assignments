# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:33:29 2020

@author: MOHANA D
"""
#	Define a custom exception class which takes a string message as attribute
        
class MyError(Exception):
    def __init__(self, message, error):
        self.message = message
        self.error = error
    def __str__(self):
        return self.message


