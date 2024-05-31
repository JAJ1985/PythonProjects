# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:22:42 2020

@author: JOSJOHN
"""

from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello_world():
    return "Hello, World!"
