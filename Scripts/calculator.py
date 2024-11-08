# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:30:27 2023

@author: JOSJOHN
"""

def calculator():
    #two numbers separated by a space
    a,b = map(str,input('Enter numbers to calculate: ').split())
    x = input('Enter your operator: ')
    answer = eval(a + x + b)
    print('The answer is: ', answer)


run = 'y'
while run == 'y':
    calculator()
    run = input('Do you want to continue(Y/N): ')