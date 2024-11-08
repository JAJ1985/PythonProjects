# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:48:05 2021

@author: JOSJOHN
"""

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basci timedelta and print it
print (timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print ("Today is: " + str(now))

# print today's date one year from now
print ("One year from now it will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print ("In two weeks and 3 days it will be: " + str(now + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago formatted as a string
t = datetime.now() - timedelta(weeks=1)
s= t.strftime("%A %B %d, %Y")
print ("One week ago it was " + s)