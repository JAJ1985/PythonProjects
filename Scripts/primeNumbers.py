# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:02:28 2023

@author: JOSJOHN
"""

from IPython.display import Image
import math
import matplotlib.pyplot as plt
import numpy as np
#from shapely.geometry import LineString
from numpy import loadtxt
from pylab import imshow, show, jet, gray, hsv, bone, hot


def prime_num(n):
    
    '''
    This function takes a positive integer 'n' as an input & performs following steps to determine whether it's prime or non-prime. 
    If it's a prime number then it append it to the list.
 
    Step 1: Check whether the number is divisible by any of the primes in the list up to and including √n. 
    Step 2: Stop checking with rest of the prime numbers in the list if it find a single prime factor.
    Step 3: If it finds no prime factors √n or less then it determines 'n' is a prime & append it to the list. 

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # check if number is divisible by other primes
    for x in primelist:
        if x <= math.sqrt(n):
            if n%x == 0:
                break #stop if other prime  ≤ √n & n is divisible by the prime
                
        else:
         # If other prime > √n & no prime factors found before,
         # it's a prime number! Hurray! Add it to the list!
         primelist.append(n) 
         #print("Prime nos = ", primelist,"\n")
         break # stop the loop once we determine it
         
# Intialize the list of primes with firt prime = 2
primelist = [2]

# Input intial & final numbers of the range check
print('\n***This program will find out the primes over the input range starting from 3.\n')         
b = input('Enter the final number for the range: ')
b = int(b)

# for loop input range to call funtion over
for i in range(3,b):
    prime_num(i)
    
# Print the final list of prime numbers
print(f"\n\nPrime numbers found in the range from 3 to {b} = \n", primelist,"\n")