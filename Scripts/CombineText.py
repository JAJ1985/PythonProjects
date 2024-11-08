# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:34:30 2020

@author: josjohn
"""

import shutil 
from pathlib import Path 
   
firstfile = Path(r'\\altaresources\dfs\Apps\Client\DMC\Idiomatic_Extract\Archive\DMC_ChatDetail_20180225-20180303.txt') 
secondfile = Path(r'\\altaresources\dfs\Apps\Client\DMC\Idiomatic_Extract\Archive\DMC_ChatDetail_20180304-20180310.txt') 
  
newfile = input("Enter the name of the new file: ") 
print() 
print("The merged content of the 2 files will be in", newfile) 
  
with open(newfile, "wb") as wfd: 
  
    for f in [firstfile, secondfile]: 
        with open(f, "rb") as fd: 
            shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10) 
  
print("\nThe content is merged successfully!") 
print("Do you want to view it ? (y / n): ") 
  
check = input() 
if check == 'n': 
    exit() 
else: 
    print() 
    c = open(newfile, "r") 
    print(c.read()) 
    c.close() 
