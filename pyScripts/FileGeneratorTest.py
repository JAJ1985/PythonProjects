Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\josjohn\\AppData\\Local\\Programs\\Python\\Python38'
>>> print (os.getcwd())
C:\Users\josjohn\AppData\Local\Programs\Python\Python38
>>> import shutil
import os
src = 'P:\WI\Teams\Programs\J&J CCC\Brand Champions\Verbatim Reports\Salesforce Reports\Ready For Import'
#dst = '\\Altaresources\shared\Apps\datamart\JNJ'
dst = 'P:\WI\Teams\Programs\J&J CCC\QMS\JOSJOHN\Python\Test'
filelist = []

files = os.listdir (src)
for filename in files:
    filelist.append(filename)
    fullpath = src + '/' + filename
shutil.move(fullpath,dst)
