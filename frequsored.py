# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:18:24 2020

@author: MOHANA D
"""
#Write a program to compute the frequency of the words from the input.
#The output should output after sorting the key alphanumerically.
#Suppose the following input is supplied to the program:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#Then, the output should be: 2:2, 3.:1, 3?:1, New:1, Python:5, Read:1, and:1, between:1, choosing:1, or:2, to:1


    
# function for calculating the frequency     
def freq(str): 
  
    # break the string into list of words 
    str_list = str.split() 
  
    # gives set of unique words 
    unique_words = set(str_list) 
      
    for words in sorted(unique_words) : 
        print(words,':',str_list.count(words),end=',')

if __name__ == "__main__": 
      
    str ='New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
      
    # calling the freq function 
    freq(str)