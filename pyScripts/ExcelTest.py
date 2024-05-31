# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:00:06 2019

@author: josjohn
"""

import os
import shutil

#move a file from on directory to another
shutil.move('\\altaresources\dfs\shares\WI\Teams\Programs\J&J CCC\Brand Champions\Verbatim Reports\Salesforce Reports\Ready For Import\VerbatimReport.csv.foo', '\\Altaresources\shared\Apps\datamart\JNJ.foo')

pip install xlrd
import xlrd
loc = ("P:\WI\Teams\Programs\J&J CCC\Brand Champions\Verbatim Reports\Salesforce Reports\Ready For Import")
wb  = xlrd.open_Workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

import pandas as pd
import numpy as np

pd.read_csv('\\altaresources\dfs\shares\WI\Teams\Programs\J&J CCC\Brand Champions\Verbatim Reports\Salesforce Reports\Ready For Import\VerbatimReport.csv')
