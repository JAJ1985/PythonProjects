# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:47:58 2019

@author: JOSJOHN
"""

 import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
19
pageObj = pdfReader.getPage(0)
 pageObj.extractText()