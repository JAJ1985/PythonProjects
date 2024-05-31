# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:54:05 2020

@author: JOSJOHN
"""

import string
import random

#Function
def generate(num):
    password = ''
    #Generating the password
    for n in range (num):
        x = random.randint(0,60)
        password += string.printable[x]
        
    return password
#Change the number for the length
print(generate(60))
