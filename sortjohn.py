# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:22:54 2020

@author: MOHANA D
"""


#If the following tuples are given as input to the program: 
#Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85
#Then, the output of the program should be:
#[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

a = ('Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85')

list1 = [tuple(x.split(',')) for x in a.split()]

print(sorted(list1))