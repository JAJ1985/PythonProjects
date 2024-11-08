# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:18:19 2019

@author: JOSJOHN
"""

# If errors are found, do this
# clear contents of C:\Users\<username>\AppData\Local\Temp\gen_py
# that should fix it, to test it type
import win32com.client
app = win32com.client.gencache.EnsureDispatch('Word.Application')
app.Visible = True