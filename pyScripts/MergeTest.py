# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:53:40 2020

@author: josjohn
"""
import fileinput
import glob

file_list = glob.glob("DMC_ChatDetail_*.txt")

with open('DMC_ChatDetail_Results.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)
        