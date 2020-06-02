# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:16:26 2020

@author: MOHANA D
"""
#Please write a program to compress and decompress the string 
#"hello world!hello world!hello world!hello world!".
import zlib
text=str("hello world!hello world!hello world!hello world!")
comp=zlib.compress(text)
print("Compressed: ", comp)
decomp=zlib.decompress(text)
print("Decompressed: ", decomp)


