# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:08:34 2020

@author: Edwin
"""


suman= lambda x: 0 if x==0 else x+suman(x-1) 
print(suman(6))