# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:38:22 2021

@author: JOSJOHN
"""

import calendar
#enter in format - 2018, 1997, 2003 etc.
year = int(input("Enter Year: ") )
#enter in format - 01, 06, 15 etc.
month = int(input("Enter Month: "))
#print Calendar
print(calendar.month(year, month))
