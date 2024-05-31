# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:22:06 2019

@author: josjohn
"""

import shutil
import os
src = r'M:\Teams\JnJ_CCC\Brand Champions\Verbatim Reports\Salesforce Reports\Ready For Import'
dst = r'\\Altaresources\shared\Apps\datamart\JNJ'
#dst = '\\pvfs2010\shared01$\Apps\Datamart'
#dst = r'P:\WI\Teams\Programs\J&J CCC\QMS\JOSJOHN\Python\Test'
filelist = []

files = os.listdir (src)
for filename in files:
    filelist.append(filename)
    fullpath = src + '/' + filename
shutil.move(fullpath,dst)